# Import socket module
from socket import *
import sys

def create_client(server_host, server_port, filename):
    # Create a TCP/IP socket
    clientSocket = socket(AF_INET, SOCK_STREAM)

    # Connect to the server
    clientSocket.connect((server_host, server_port))

    # Create a GET HTTP request message
    request = f'GET /{filename} HTTP/1.1\r\nHost: {server_host}\r\n\r\n'

    # Send the request to the server
    clientSocket.send(request.encode())

    # Receive the response from the server
    response = clientSocket.recv(4096).decode()

    # Print the response
    print(response)

    # Close the socket
    clientSocket.close()

server_host = 'localhost'
server_port = 1080
filename = sys.argv[3]

create_client(server_host, server_port, filename)