"""Config flow for ESP32 RSSI integration."""
import voluptuous as vol

from homeassistant import config_entries
import homeassistant.helpers.config_validation as cv

from .const import DOMAIN, CONF_DEVICE_ID

class ESP32RSSIConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for ESP32 RSSI."""

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        errors = {}

        if user_input is not None:
            return self.async_create_entry(title=f"ESP32 {user_input[CONF_DEVICE_ID]}", data=user_input)

        schema = vol.Schema({
            vol.Required(CONF_DEVICE_ID): cv.string,
        })

        return self.async_show_form(step_id="user", data_schema=schema, errors=errors)
