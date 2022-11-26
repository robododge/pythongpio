
from signal import pause
from time import sleep
from gpiozero import Buzzer, Button


print("Program Button Buzz started!!")
bz_count = 0
print("Start count: %d\n" % bz_count)


def increment_buzz():
    '''
    Called to increment the global buzzer counter and print
    '''
    global bz_count
    bz_count = bz_count + 1
    print("BUZZ COUNT: %d\n" % bz_count)

def go_count():
    '''
    Callback function, called when button is held longer than default 1 second
    '''
    increment_buzz()

def go_buzz():
    '''
    Callback function, called when button is actiated
    '''

    #only increment if button hasn't been held too long (default 1 sec)
    #if not button.is_held:
        #print("incremting, button not held")
    #    increment_buzz()
    buzz.on()


def off_buzz():
    '''
    Callback function, called when button is released
    '''
    buzz.off()

button = Button(21, hold_time=0.05)
buzz = Buzzer(20)

try:
    button.when_pressed = go_buzz
    button.when_held = go_count
    button.when_released = off_buzz
    pause()

finally:
    pass

