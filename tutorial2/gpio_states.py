# Huats 2023 oscstarterkit
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIOs = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
         12, 13, 16, 17, 18, 19, 20, 21,
         22, 23, 24, 25, 26, 27]

# Setup all GPIOs to input
for gpio in GPIOs:
    GPIO.setup(gpio, GPIO.IN)
    
# Read state for each GPIO
for gpio in GPIOs:
    print("GPIO no " + str(gpio) + ": " + str(GPIO.input(gpio)))
    
# Cleanup all GPIOs - state will be different after that!
GPIO.cleanup()