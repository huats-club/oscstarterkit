from pythonosc import udp_client, osc_message_builder
import time

def send_message(receiver_ip, receiver_port, address, message):
	try:
		# Create an OSC client to send messages
		client = udp_client.SimpleUDPClient(receiver_ip, receiver_port)

		# Send an OSC message to the receiver
		client.send_message(address, message)

		print("Message sent successfully.")
	except:
		print("Message not sent")

#change the below values
if __name__ == "__main__":
    LAPTOP_IP = "192.168.0.100"		# send to laptop w grandMA3
    PORT = 8000                     # laptop w grandMA3 port number
    addr = "/gma3/cmd"

    send_message(LAPTOP_IP, PORT, addr, "Go Sequence 1")