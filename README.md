# esp32-servo
A collection of micropython code used to program a VolBot prototype

The Volbot prototype was produced to verify the simulations from the VolBotSims repository, found here: 
https://github.com/DevwratJoshi/VolBotSims

The VolBot prototype is made by sandwiching a PQ12 linear actuator between two 18-gon Hoberman planar linkages. The linear actuator is used to change the dimeter of the robot. The robot also has on board an APDS9960 color sensor from Sparkfun. 
An ESp32 board with micropython firmware is used for control. The code for the board is included in this repository.

Using picocom for repl and ampy to transfer files to the board.

Note: Before transferring config.py to the board, remember to change the ssid and password under 'bunri_wifi' to the appropriate values. The board will look for the given ssid, and will connect to it with the appropriate password if found.
