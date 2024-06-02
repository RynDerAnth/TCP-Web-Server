#import socket module 
from socket import * 
import sys # In order to terminate the program 
serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
serverName = 'localhost' 
serverPort = 1080 
serverSocket.bind((serverName,serverPort))
serverSocket.listen(1) 
while True: 
    #Establish the connection 
    print('Ready for incoming connection(s)') 
    connectionSocket, addr = serverSocket.accept()
    try: 
        message = connectionSocket.recv(1024).decode()
        filename = message.split()[1] 
        f = open(filename[1:], 'rb') 
        outputdata = f.read()
        #Send one HTTP header line into socket 
        response = "HTTP/1.1 200 OK\r\nContent-Length: {len(outputdata)}\r\n\r\n".encode() 
        #Send the content of the requested file to the client 
        # for i in range(0, len(outputdata)): 
        #     connectionSocket.send(outputdata[i].encode())
        connectionSocket.send(response + outputdata) 
        connectionSocket.send("\r\n".encode()) 
        connectionSocket.close() 
    except IOError: 
        #Send response message forfile not found 
        response = "HTTP/1.1 404 Not Found\r\nContent-Type: text/html; charset=utf-8\r\n\r\n".encode() 
        #Close client socket 
        connectionSocket.send(response)
        connectionSocket.close()      
serverSocket.close() 
sys.exit()#Terminate the program after sending the corresponding data