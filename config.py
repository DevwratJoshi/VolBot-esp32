pins = {
            "I2C_SCL_pin": 25,
            "I2C_SDA_pin": 26,
            "servo_pin": 32
        }


modes = {
            "set_timer" : True, 
            "check_for_update_time": 60000, 
            
        }
bunri_wifi= {
                "ssid": b'HosodaLab712-24G',
                "pass": 'verycuteroboy'
            }

# The follwing are the standard return values for functions from different modules
# white and black zone returns are the values returned by the getZone function from the 
# APDS9960 sensor control module

returns={
            "white_zone_return": 0,
            "black_zone_return": 1
        }
