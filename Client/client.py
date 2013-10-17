'''
Created on Oct 16, 2013

@author: christopherhuang
'''
import sys
from socket import *

if __name__ == '__main__':
    serverHost = 'localhost'
    serverPort = 50007
    
    message = [b'Hello Network World']
    
    if len(sys.argv) > 1:
        serverHost = sys.argv[1]
        if len(sys.argv) > 2:
            message = (x.encode() for x in sys.argv[2:])
    
    sockObj = socket(AF_INET, SOCK_STREAM)
    sockObj.connect(serverHost, serverPort)
    
    for line in message:
        sockObj.send(line)
        data = sockObj.recv(1024)
        print('Client received:', data)
        
    sockObj.close()