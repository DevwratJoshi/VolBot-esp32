from machine import I2C, Pin
import config


APDS9960_I2C_ADDR = 0x39
id_addr = 0x92 
ERROR =  0xFF
enable_addr = 0x80
i2c = I2C(scl=Pin(config.pins["I2C_SCL_pin"]), sda= Pin(config.pins["I2C_SDA_pin"]), freq = 100000)


# The following are the addresses for the 2 bytes holding the data for clear light, red, green and blue colour.
c_low = 0x94
c_high = 0x95
r_low = 0x96
r_high = 0x97
g_low = 0x98
g_high = 0x99
b_low = 0x9A
b_high = 0x9B
#Acceptable device IDs 
APDS9960_ID_1 = 0xAB
APDS9960_ID_2 = 0x9C

#General definitions
ON = 1
OFF = 0
#clearThresh is the value of the clear threshold below which the robot will think it is 
# in the black zone and above which it will think it in the white zone
clearThresh = 10 
#modes
POWER = 0
AMB_LIGHT = 1
PROXIMITY = 2
ALL = 7
class APDS9960():

    def __init__(self):
        self.id = ord(i2c.readfrom_mem(APDS9960_I2C_ADDR,id_addr, 1))
        self.setMode(POWER, ON)
        self.enableLightSensor()

    def setMode(self, mode, enable):
        #Make sure to convert reg_val to int with ord()
        reg_val = self.getMode()
        if reg_val == ERROR:
            return False
        #Change bit(s) in ENABLE register 
        enable = enable & 0x01
        if mode >= 0 and mode <= 6:
            if enable:
                reg_val |= (1 << mode)
            else:
                reg_val &= ~(1 << mode)
           
        elif mode == ALL:
            if enable:
                reg_val = 0x7F
            else:
                reg_val = 0x00
                # Write value back to ENABLE register 
        i2c.writeto_mem(APDS9960_I2C_ADDR, enable_addr, reg_val.to_bytes(1, 'big'))
    
    #Getting the un-normalized red light intensity 
    def getRed(self):
        
        val_low = ord(i2c.readfrom_mem(APDS9960_I2C_ADDR, r_low, 1)) 
        val_high = ord(i2c.readfrom_mem(APDS9960_I2C_ADDR, r_high, 1))
        print(str(val_high) + " " + str(val_low))
        val_high = val_high << 8
        val = val_high + val_low

        return val
   
    def getGreen(self):
        
        val = ord(i2c.readfrom_mem(APDS9960_I2C_ADDR, g_low, 1))
        val = (ord(i2c.readfrom_mem(APDS9960_I2C_ADDR, g_high, 1)) << 8) + val

        return val

      
    def getBlue(self):
        
        val = ord(i2c.readfrom_mem(APDS9960_I2C_ADDR, b_low, 1))
        val = (ord(i2c.readfrom_mem(APDS9960_I2C_ADDR, b_high, 1)) << 8) + val

        return val

    def getClear(self):
        
        val = ord(i2c.readfrom_mem(APDS9960_I2C_ADDR, c_low, 1))
        val = (ord(i2c.readfrom_mem(APDS9960_I2C_ADDR, c_high, 1)) << 8) + val

        return val

    # For now, the inturrputs will be had coded to be disabled. This is the default positon
    # If they should be necessary, change the following function
    # Refer to the example code from Sparkfun ColorSensor.io as needed
    def enableLightSensor(self):
        self.setMode(AMB_LIGHT, ON)

    def disableLightSensor(self):
        global i2c
        self.setMode(AMB_LIGHT, OFF)

    def getMode(self):
        global i2c
        mode = i2c.readfrom_mem(APDS9960_I2C_ADDR, enable_addr, 1)
        return ord(mode)
    
    # The following function will return values as per the config file
    def getZone(self):
        val = self.getClear()
        global clearThresh
        if val > clearThresh:
            return config.returns["white_zone_return"]
        else:
            return config.returns["black_zone_return"]


