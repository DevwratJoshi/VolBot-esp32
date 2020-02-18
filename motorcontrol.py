from machine import Pin, PWM
import config
    
frequency = 50
smallDuty = 103
bigDuty = 50
class Servo:
    

    # This class holds the methods to control the servo motor 
    # A single instance of this class will be insantized during the lifetime of the main program

    def __init__(self):
        self.servo = PWM(Pin(config.pins["servo_pin"]))
        self.servo.freq(frequency) #This has to do with the servo expecting a pulse every 20ms
        self.servo.duty(smallDuty) 

    def changeSize(self, size):
        
        if size == 'big':
            self.servo.duty(bigDuty)

        elif size == 'small':
            self.servo.duty(smallDuty)
    
    #The following function will toggle between the sizes of the servo
    def toggleSize(self):

        if(self.servo.duty() == smallDuty):
            self.servo.duty(bigDuty)

        else:
            self.servo.duty(smallDuty)

