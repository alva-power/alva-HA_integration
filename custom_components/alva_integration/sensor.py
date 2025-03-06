"""Sensor platform for Alva Integration."""
from __future__ import annotations

from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntity,
    SensorStateClass,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN


async def async_setup_entry(
    hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback
) -> None:
    """Set up the Alva sensor platform."""
    coordinator = hass.data[DOMAIN][entry.entry_id]
    async_add_entities([AlvaSensor(coordinator, entry)])


class AlvaSensor(CoordinatorEntity, SensorEntity):
    """Representation of an Alva sensor."""

    _attr_has_entity_name = True
    _attr_name = "RSSI"
    _attr_native_unit_of_measurement = "V"
    _attr_device_class = SensorDeviceClass.VOLTAGE
    _attr_state_class = SensorStateClass.MEASUREMENT

    def __init__(self, coordinator, entry):
        """Initialize the sensor."""
        super().__init__(coordinator)
        self._entry = entry
        self._attr_unique_id = f"{entry.data['device_id']}_rssi"

    @property
    def device_info(self):
        """Return device information."""
        return {
            "identifiers": {(DOMAIN, self._entry.data["device_id"])},
            "name": f"Alva Device {self._entry.data['device_id']}",
            "manufacturer": "Alva",
            "model": "Alva Sensor",
        }

    @property
    def native_value(self):
        """Return the state of the sensor."""
        if self.coordinator.data is None:
            return None
        
        return self.coordinator.data.get("rssi")