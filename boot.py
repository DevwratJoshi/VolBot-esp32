# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)

import network 
import wifi_init as wi

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

b = [code[0] for code in wlan.scan()]

if wi.bunri_wifi["ssid"] in b :
	print("Found lab network")
	wlan.connect(wi.bunri_wifi["ssid"], wi.bunri_wifi["pass"]) 

import main



