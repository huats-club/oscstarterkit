# Huats 2023 oscstarterkit
import RPi.GPIO as GPIO
import time
from send_basic_print import send_message

# FOR INFO: IP address and port of the receiving Raspberry Pi
PI_A_ADDR = "192.168.1.100"
PORT = 2000

addr = "/print"
init_msg = "salutations from pi_B"
deinit_msg = "byebye from b"

# Set the GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Set up the button pin
button_pin = 27
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

push_flag = 0

while True:
    if GPIO.input(button_pin) == GPIO.LOW:
        if push_flag == 0:
            ## write in this block what happens upon 1st press
            send_message(PI_A_ADDR, PORT, addr, init_msg)

            ## block end
            push_flag = 1
        else:
            ## write in this block what happens upon 2nd press
            send_message(PI_A_ADDR, PORT, addr, deinit_msg)

            ## block end
            push_flag = 0
        time.sleep(1)
