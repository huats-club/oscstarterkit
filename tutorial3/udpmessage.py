# Huats 2023 oscstarterkit
import socket

# UDP_IP is target IP address
UDP_IP = "192.168.0.100"
UDP_PORT = 10066

# set up UDP transmission
try:
  sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  MESSAGE= "Hello There!+"
  MESSAGE = bytes(MESSAGE, 'UTF-8')
  sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
  sock.close()
  print('messsage sent')
except:
  print('message not sent')
