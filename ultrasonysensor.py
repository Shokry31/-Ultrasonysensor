from machine import Pin                                                     # import pin functionalty
import utime                                                                # import utime to sleep/pause

led = Pin(25, Pin.OUT)                                                      # set ligt to pin 25                                                
trigger = Pin(3, Pin.OUT)                                                   # set pulsing to pin 3                                             
echo = Pin(2, Pin.IN)                                                       # set pulsing to pin 2

def ultra():                                                                # create function callled ultra                                                           
   trigger.low()                                                            # set trigger to low
   utime.sleep_us(2)                                                        # sleep for 2 micro seconds
   trigger.high()                                                           # start the trigger/pulsing
   utime.sleep_us(5)                                                        # sleep for 5 micro seconds
   trigger.low()                                                            # stop pulsing
   while echo.value() == 0:                                                 # check of the echo value is equal low
       signaloff = utime.ticks_us()                                         # turn the signal off
   while echo.value() == 1:                                                 # check of the echo value is high
       signalon = utime.ticks_us()                                          # turn the signal on
   timepassed = signalon - signaloff                                        # calculate the on signal and the off signal
   distance = (timepassed * 0.0343) / 2                                     # caluculate the distance
   print("The distance from object is ",distance,"cm")                      # print to the shell the distance
   
   if distance < 10:                                                        # distance less than 10 cm 
       led.high()                                                           # lamp lights up
   else:
       led.low()                                                            # set lamp to low
       
   if distance < 10:
    print ("Vehicle is too close")
   
   
while True:                                                                 # create infinite while loop
   ultra()                                                                  # call the function created
   utime.sleep(1)                                                           # sleep/wait/pause for 1 second
