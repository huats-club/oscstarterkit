# Huats 2023 oscstarterkit
import socket

def send_message(receiver_ip, receiver_port, msg):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        MESSAGE = bytes(msg, 'UTF-8')
        sock.sendto(MESSAGE, (receiver_ip, receiver_port))
        sock.close()
        print('messsage sent')

    except:
        print("Message not sent")

if __name__ == "__main__":
    ip = "192.168.1.100" # Widget Designer IP Address
    port = 8888 # Widget Deisgner (IN Port)
    message = "Python to Widget Designer"
    send_message(ip, port, message)
