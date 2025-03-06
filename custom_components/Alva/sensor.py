import requests
import logging

from homeassistant.components.sensor import SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.const import UnitOfElectricPotential

from .const import DOMAIN, CONF_DEVICE_ID, BASE_URL

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities):
    """Set up the ESP32 RSSI sensor from a config entry."""
    device_id = entry.data[CONF_DEVICE_ID]
    resource = BASE_URL.format(device_id)
    async_add_entities([ESP32RssiSensor(resource)], True)

class ESP32RssiSensor(SensorEntity):
    """Representation of an ESP32 RSSI sensor."""

    def __init__(self, resource):
        """Initialize the sensor."""
        self._name = "ESP32 RSSI"
        self._resource = resource
        self._state = None
        self._attr_native_unit_of_measurement = UnitOfElectricPotential.VOLT

    @property
    def name(self):
        """Return the name of the sensor."""
        return self._name

    @property
    def state(self):
        """Return the current state."""
        return self._state

    def update(self):
        """Fetch new state data from the REST API."""
        try:
            response = requests.get(self._resource, timeout=5)
            response.raise_for_status()
            data = response.json()
            self._state = data.get("rssi", None)
        except Exception as e:
            _LOGGER.error("Error fetching data from %s: %s", self._resource, e)
            self._state = None
