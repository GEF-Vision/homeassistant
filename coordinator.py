from abc import ABC
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed
from homeassistant.core import HomeAssistant
from homeassistant.const import CONF_USERNAME, CONF_PASSWORD
from homeassistant.exceptions import ConfigEntryAuthFailed
from httpx import ConnectError
from .api_client.api.authentication import (
    api_v2_auth_token_create,
)
from .api_client.client import Client, AuthenticatedClient
from .api_client.models import AuthToken
from .api_client.api.plant import api_v2_plant_retrieve
from .const import VISION_BASE_URL
from datetime import timedelta
import logging


_LOGGER = logging.getLogger(__name__)


class VisionPlantCoordinator(DataUpdateCoordinator):
    def __init__(
        self,
        hass: HomeAssistant,
        client: AuthenticatedClient,
        uuid: str,
        name: str,
        scan_interval: int,
        has_energymeter: bool,
        has_production: bool,
    ) -> None:
        self.client = None
        self.hass = hass
        self.client = client
        self.uuid = uuid
        self.capabilities = {"has_energymeter": False, "has_production": False}
        self.current_values = None
        self.scan_interval = scan_interval
        self.has_energymeter = has_energymeter
        self.has_production = has_production
        super().__init__(
            hass,
            _LOGGER,
            name=f"GEF Vision {self.uuid}",
            update_interval=timedelta(seconds=self.scan_interval),
        )

    @staticmethod
    async def authenticate_user(username, password):
        auth = AuthToken(
            username=username,
            password=password,
            token="",
        )
        client = Client(VISION_BASE_URL)
        token = await api_v2_auth_token_create.asyncio_detailed(
            client=client, json_body=auth
        )
        if token.status_code != 200:
            return False
        return AuthenticatedClient(
            base_url=VISION_BASE_URL, token=token.parsed.token, prefix="Token"
        )

    async def _async_update_data(self):
        try:
            data = await api_v2_plant_retrieve.asyncio_detailed(
                client=self.client, uuid=self.uuid
            )
            if data.status_code == 200:
                self.current_values = data.parsed
            elif data.status_code == 403:
                # Attempt re-authentication
                try:
                    client = self.authenticate_user(
                        self.config.data[CONF_USERNAME], self.config.data[CONF_PASSWORD]
                    )
                    if not client:
                        raise ConfigEntryAuthFailed(
                            f"Authentication failed for {self.uuid}"
                        )
                    else:
                        self.client = client
                except ConnectError as err:
                    raise UpdateFailed(err) from err
            else:
                _LOGGER.error(f"Failed to fetch data: {data}")
                self.current_values = None
        except Exception as err:
            _LOGGER.exception(f"Update failed for plant {self.uuid}")
            self.current_values = None
            raise UpdateFailed(err) from err
