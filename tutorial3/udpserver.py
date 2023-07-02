# Huats 2023 oscstarterkit
import socket

# Configure server address and port
server_ip = '0.0.0.0'  # Set to '0.0.0.0' to listen on all available interfaces
server_port = 10096

# Create a UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the server address and port
server_socket.bind((server_ip, server_port))

print('UDP server is listening...')

# Listen for incoming messages indefinitely
while True:
    # Receive message and address from the client
    message, client_address = server_socket.recvfrom(1024)

    # Decode the received message
    message = message.decode('utf-8')

    # Print the received message and client address
    print(f'Received message: {message} from {client_address[0]}:{client_address[1]}')

    # Send a response back to the client (optional)
    response = 'Message received successfully!'
    server_socket.sendto(response.encode('utf-8'), client_address)
