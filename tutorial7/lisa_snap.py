# Huats 2023 oscstarterkit
# This python script demonstrate OSC control on Raspberry Pi to L-ISA
# Controller triggering "next" snapshot
from pythonosc import udp_client

def send_message(receiver_ip, receiver_port, address, message):
	try:
		# Create an OSC client to send messages
		client = udp_client.SimpleUDPClient(receiver_ip, receiver_port)

		# Send an OSC message to the receiver
		client.send_message(address, message)

		print("Message sent successfully.")
	except:
		print("Message not sent")

# FOR INFO: IP address and port of the receiving Raspberry Pi
PI_A_ADDR = "10.10.10.10"		# wlan ip
PORT = 8880

addr = "/ext/snap/n/f"
msg = ""

send_message(PI_A_ADDR, PORT, addr, msg)
