# Huats 2023 oscstarterkit
from pythonosc import osc_server, dispatcher, udp_client

#server for this RPi (Pi_A)
server_ip = "192.168.1.100"
server_port = 2000

#sending to the following device (Pi_B)
receiver_ip = '192.168.1.101'
receiver_port = 2000

# this function will send a message back to Pi_B upon receiving an OSC message
def message_handler_ack(addr, *args):
  if addr == "/print":
    print(args[0])

    ##feel free to change the message below
    address = '/print'
    message = 'Acknowledgement of message from Pi_A'
    client.send_message(address, message)
   
#create a client to send osc messages
client = udp_client.SimpleUDPClient(receiver_ip, receiver_port)

#catches osc messgaes and executes function that corresponds to address of message
dispatcher = dispatcher.Dispatcher()
dispatcher.map('/print', message_handler_ack)

#create a threading server that will listen to multiple incoming messages when running
server = osc_server.ThreadingOSCUDPServer((server_ip, server_port), dispatcher)
print("serving on{}".format(server.server_address))
server.serve_forever()
  

