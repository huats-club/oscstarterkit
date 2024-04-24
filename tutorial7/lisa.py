# Huats 2023 oscstarterkit
import socket

# UDP_IP is target IP address
UDP_IP = "192.168.254.201" #IP Address of L-ISA Controller (e.g. Laptop)
UDP_PORT = 10096

# set up UDP transmission
try:
  sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  MESSAGE= "/ext/src/4/p 0.3" # Adjust pan of source 4 by a value of 0.3
  MESSAGE = bytes(MESSAGE, 'UTF-8')
  sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
  sock.close()
  print('messsage sent')
except:
  print('message not sent')