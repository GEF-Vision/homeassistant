"""Config flow for GEF Vision integration."""
from __future__ import annotations

import logging
from typing import Any

import voluptuous as vol

from homeassistant import config_entries
from homeassistant.core import HomeAssistant
from homeassistant.data_entry_flow import FlowResult
from homeassistant.exceptions import HomeAssistantError
from .client import VisionClient, VisionAuthenticationError, VisionConnectionError

from .const import (
    DOMAIN,
    PRODUCTION_ENTITY_DESCRIPTIONS,
    GRID_INTERFACE_ENTITY_DESCRIPTIONS,
    CONSUMPTION_ENTITY_DESCRIPTIONS,
    POLL_INTERVAL,
)

_LOGGER = logging.getLogger(__name__)

# TODO adjust the data schema to the data that you need
STEP_USER_DATA_SCHEMA = vol.Schema(
    {
        vol.Required("username", description="User name"): str,
        vol.Required("password", description="Password"): str,
        vol.Required("plant_uuid", description="Plant UUID"): str,
        vol.Required(
            "poll_interval_s",
            description="Poll interval in seconds (min. 10)",
            default=POLL_INTERVAL,
        ): int,
    }
)


class CannotConnect(HomeAssistantError):
    """Error to indicate we cannot connect."""


class InvalidAuth(HomeAssistantError):
    """Error to indicate there is invalid auth."""


class InvalidParameter(HomeAssistantError):
    """Error to indicate an invalid parameter."""


async def validate_input(hass: HomeAssistant, data: dict[str, Any]) -> dict[str, Any]:
    """Validate the user input allows us to connect.

    Data has the keys from STEP_USER_DATA_SCHEMA with values provided by the user.
    """
    client = VisionClient(data["username"], data["password"], data["plant_uuid"])

    if data["poll_interval_s"] < 10:
        raise InvalidParameter
    try:
        await client.authenticate()
    except VisionConnectionError as exc:
        raise CannotConnect from exc
    except VisionAuthenticationError as exc:
        raise InvalidAuth from exc

    return data["plant_uuid"]


class ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for GEF Vision."""

    VERSION = 1

    async def async_step_user(self, info: dict[str, Any]) -> FlowResult:
        errors = {}
        if info is not None:
            errors = {}
            await self.async_set_unique_id(info["plant_uuid"])
            self._abort_if_unique_id_configured()
            try:
                title = await validate_input(self.hass, info)
                return self.async_create_entry(title=title, data=info)
            except CannotConnect:
                errors["base"] = "cannot_connect"
            except InvalidAuth:
                errors["base"] = "invalid_auth"
            except InvalidParameter:
                errors["base"] = "invalid_parameter"
            except Exception:  # pylint: disable=broad-except
                _LOGGER.exception("Unexpected exception")
                errors["base"] = "unknown"
        return self.async_show_form(
            step_id="user", data_schema=STEP_USER_DATA_SCHEMA, errors=errors
        )
