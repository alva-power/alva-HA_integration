## ALVA integration for Home Assistant

This is an Alva integration for home assistant.

# Setup

## Prerequisites 

1. Have the Home Assistant Server already setup
2. Have the HACS (Home Assistant Community Store) integrated. 

You need to have the home assistant server setup. If you don't have their device, you can setup a containerized server as well. [Follow this link](https://www.home-assistant.io/installation/linux#install-home-assistant-container) for home assistant server in a docker container.


## Alva Integartion Steps

1. Go to the HACS tab in the left side bar.
2. On the top right corner press the 3 dots `:` for the drop down menu. 
3. Select the `Custom repositories` option in the menu.
4. Enter the link `https://github.com/alva-power/alva-HA_integration` And select the type as `Integration`. 
5. At this point if you search for Alva in the HACS search bar, it should appear. Click on it.  
6. You should see a Download button after opening the Alva in the HACS at the bottom right corner. Download it.
7. A restart is now required after download. So go to the settings tab, and Select the `Restart required` option. For the restart.
7. Now to setup Alva integartion go to Settings tab > Devices & services > Add integration > Search Alva and select it > Enter the device_id. 



## Add the Alva to your dashboard

Now you can add Alva to your own dashboard. 






