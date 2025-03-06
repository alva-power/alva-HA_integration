from homeassistant import config_entries
import voluptuous as vol
import homeassistant.helpers.config_validation as cv

from .const import DOMAIN, CONF_DEVICE_ID

class AlvaIntegrationConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle the config flow for Alva Integration."""

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        errors = {}

        if user_input is not None:
            return self.async_create_entry(title=f"Alva Device {user_input[CONF_DEVICE_ID]}", data=user_input)

        schema = vol.Schema({
            vol.Required(CONF_DEVICE_ID): cv.string,
        })

        return self.async_show_form(step_id="user", data_schema=schema, errors=errors)
