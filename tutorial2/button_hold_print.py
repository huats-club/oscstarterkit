from gpiozero import Button
import time
from send_basic_print import send_message

# FOR INFO: IP address and port of the receiving Raspberry Pi
PI_A_ADDR = "192.168.1.100"
PORT = 2000

addr = "/print"
init_msg = "salutations from pi_B"
deinit_msg = "byebye from b"


button = Button(17)
press_flag = 0

while True:
	if button.is_pressed and press_flag == 0:
		## write in this block what happens upon press
		send_message(PI_A_ADDR, PORT, addr, init_msg)
		
		## block end
		press_flag = 1
		time.sleep(0.5)
	elif (not button.is_pressed) and press_flag == 1:
		## write in this block what upon 2nd press
		send_message(PI_A_ADDR, PORT, addr, deinit_msg)
		
		## block end
		press_flag = 0 
		time.sleep(0.5)
