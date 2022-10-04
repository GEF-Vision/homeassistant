"""Config flow for GEF Vision integration."""
from __future__ import annotations

import logging
from typing import Any
from httpx import ConnectError, ConnectTimeout
import voluptuous as vol

from homeassistant import config_entries
from homeassistant.core import HomeAssistant
from homeassistant.components.sensor import PLATFORM_SCHEMA
from homeassistant.const import CONF_USERNAME, CONF_PASSWORD, CONF_SCAN_INTERVAL
from homeassistant.data_entry_flow import FlowResult
from homeassistant.exceptions import (
    PlatformNotReady,
    ConfigEntryAuthFailed,
    HomeAssistantError,
)
from .api_client.client import Client, AuthenticatedClient
from .api_client.api.authentication import (
    api_v2_auth_token_create,
)
from .api_client.models import AuthToken

from .const import DOMAIN, DEFAULT_SCAN_INTERVAL, VISION_BASE_URL

_LOGGER = logging.getLogger(__name__)

GEF_VISION_DATA_SCHEMA = {
    vol.Required(CONF_USERNAME, description="User name"): str,
    vol.Required(CONF_PASSWORD, description="Password"): str,
    vol.Required(
        CONF_SCAN_INTERVAL,
        description="Poll interval in seconds (min. 10)",
        default=DEFAULT_SCAN_INTERVAL,
    ): int,
}
GEF_VISION_USER_SCHEMA = vol.Schema(GEF_VISION_DATA_SCHEMA)

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(GEF_VISION_DATA_SCHEMA)


class CannotConnect(HomeAssistantError):
    """Error to indicate we cannot connect."""


class InvalidAuth(HomeAssistantError):
    """Error to indicate there is invalid auth."""


class InvalidParameter(HomeAssistantError):
    """Error to indicate an invalid parameter."""


async def validate_input(hass: HomeAssistant, data: dict[str, Any]) -> dict[str, Any]:
    """Attempts to connect to GEF Vision using the provided credentials"""
    client = Client(VISION_BASE_URL)
    auth = AuthToken(
        username=data[CONF_USERNAME], password=data[CONF_PASSWORD], token=""
    )

    if data[CONF_SCAN_INTERVAL] < 10:
        raise InvalidParameter

    try:
        token = await api_v2_auth_token_create.asyncio(client=client, json_body=auth)
        if not token:
            raise InvalidAuth
    except (ConnectError, ConnectTimeout) as exc:
        raise CannotConnect from exc

    return data[CONF_USERNAME].lower()


class ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for GEF Vision."""

    VERSION = 1

    async def async_step_user(self, info: dict[str, Any]) -> FlowResult:
        errors = {}
        if info is not None:
            errors = {}
            await self.async_set_unique_id(info[CONF_USERNAME].lower())
            self._abort_if_unique_id_configured()
            try:
                title = await validate_input(self.hass, info)
                return self.async_create_entry(title=title, data=info)
            except CannotConnect:
                errors["base"] = "cannot_connect"
                raise PlatformNotReady("Connection to GEF Vision failed")
            except InvalidAuth:
                errors["base"] = "invalid_auth"
                raise ConfigEntryAuthFailed(
                    "Invalid authentication data for GEF Vision"
                )
            except InvalidParameter:
                errors["base"] = "invalid_parameter"
                raise PlatformNotReady("Invalid parameter was provided")
        return self.async_show_form(
            step_id="user", data_schema=GEF_VISION_USER_SCHEMA, errors=errors
        )

    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> FlowResult:
        """Perform reauth upon an API authentication error."""
        self._reauth_config_entry = self.hass.config_entries.async_get_entry(
            self.context["entry_id"]
        )
        return await self.async_step_reauth_confirm()

    async def async_step_reauth_confirm(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Confirm reauth dialog."""
        errors = {}
        if not user_input:
            return self.async_show_form(
                step_id="user", data_schema=GEF_VISION_USER_SCHEMA, errors=errors
            )
        try:
            title = await validate_input(self.hass, user_input)
        except CannotConnect:
            errors["base"] = "cannot_connect"
            raise PlatformNotReady("Connection to GEF Vision failed")
        except InvalidAuth:
            errors["base"] = "invalid_auth"
            raise ConfigEntryAuthFailed("Invalid authentication data for GEF Vision")
        except InvalidParameter:
            errors["base"] = "invalid_parameter"
            raise PlatformNotReady("Invalid parameter was provided")
