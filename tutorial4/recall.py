# Credits to Yamaha Professional Audio
# This script sends a scene recall command to a Yamaha mixing console.
# Please execute this scrupt like this:
# "python recall.py 1"
# It will recall scene #001 of the target console

import sys
import socket

# Host is console's IP
host ="192.168.0.128"
# Port must be 49280
port =49280

args = sys.argv
no = int(args[1])

# connect socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)
s.connect((host,port))

# Recalls a scene
command = ("ssrecall_ex MIXER:Lib/Scene " + str(no) + "\n").encode()
s.sendall(command)

# receive a message before closing socket
s.recv(1500)

# Closes socket
s.close ()
