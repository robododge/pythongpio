
from signal import pause
from time import sleep
from gpiozero import LED, Button

def go_blink():
    led1.blink(0.5, 0.5)
    sleep(0.5)
    led2.blink(0.5, 0.5)

def off_blink():
    led1.off()
    led2.off()

button = Button(21)

led1 = LED(9)
led2 = LED(10)

try:
    button.when_pressed = go_blink
    button.when_released = off_blink
    pause()

finally:
    pass

