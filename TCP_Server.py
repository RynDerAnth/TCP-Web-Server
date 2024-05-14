# from socket import *
# serverPort = 1080
# serverSocket = socket(AF_INET,SOCK_STREAM)
# serverSocket.bind(('',serverPort))
# serverSocket.listen(1)
# print ('Server siap')
# while True:
#     connectionSocket, addr = serverSocket.accept()

#     sentence = connectionSocket.recv(1024).decode()
#     connectionSocket.send(sentence.encode())
#     connectionSocket.close()

#import socket module 
from socket import * 
import sys # In order to terminate the program 
serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
serverName = '123.456.789' 
serverPort = 1080 
serverSocket.bind((serverName,serverPort))
serverSocket.listen(1) 
while True: 
    #Establish the connection 
    print('Ready to serve...') 
    connectionSocket, addr = serverSocket.accept()
    try: 
        message = connectionSocket.recv(1024).decode()
        filename = message.split()[1] 
        f = open(filename[1:]) 
        outputdata = f.read()
        #Send one HTTP header line into socket 
        response = f"HTTP/1.1 200 OK\r\nContent-Length: {len(outputdata)}\r\n\r\n".encode(
            'utf-8')
        response += outputdata 
        #Send the content of the requested file to the client 
        for i in range(0, len(outputdata)): 
            connectionSocket.send(outputdata[i].encode()) 
        connectionSocket.send("\r\n".encode()) 
        connectionSocket.close() 
    except IOError: 
        #Send response message forfile not found 
        response = "HTTP/1.1 404 Not Found\r\nContent-Type: text/html; charset=utf-8\r\n\r\n".encode(
            'utf-8')
        response += "<h1>404 Not Found</h1>".encode('utf-8') 
        #Close client socket 
        connectionSocket.sendall(response)
        connectionSocket.close() 
    serverSocket.close() 
    sys.exit()#Terminate the program after sending the corresponding data