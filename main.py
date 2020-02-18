import time
import config
#import motorcontrol as mc
#import APDS9960 as cs

maxTime = 120000 # Execute the script for this long in ms
start_time = time.ticks_ms()
last_zone = 3
sensor = cs.APDS9960()
servo = mc.Servo()
time.sleep(2)

#while time.ticks_diff(time.ticks_ms(), start_time) < maxTime:

#    if not sensor.getZone() == last_zone: #This means a size change is required
 #       if(sensor.getZone() == config.returns["white_zone_return"]):
  #          servo.changeSize('small')
   #         print("time to become small")
    #    elif(sensor.getZone() == config.returns["black_zone_return"]):
     #       servo.changeSize('big')
      #      print("time to become big")
       # time.sleep(2)
        #last_zone = sensor.getZone()


    #time.sleep(1)
    #print("Executing the function")


#print("Done with the program")
