from machine import Timer 

#Making this a class so that the main function can choose when to start the timer

counter = 0

class timers:
    
    period = 60000
    tim = Timer(counter)
    
    def __init__(self):
        global counter
        tim.init(
        
        
