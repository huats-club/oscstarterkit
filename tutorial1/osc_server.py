# Huats 2023 oscstarterkit
from pythonosc import osc_server, dispatcher

# change the receiver_ip value to your RPi's IP address
receiver_ip = "192.168.1.100"
receiver_port = 2000

# this function prints the arguments in received OSC messages 
def print_args(addr, *args):
  if addr == "/print":
    print(args[0])
  
#catches osc messgaes
dispatcher = dispatcher.Dispatcher()
dispatcher.map("/print", print_args) ## if OSC message with addr "/print" is received, message_handler function will run

server = osc_server.ThreadingOSCUDPServer((receiver_ip, receiver_port), dispatcher)
print("serving on{}".format(server.server_address))
server.serve_forever()
  

