'''
Created on Oct 16, 2013

@author: christopherhuang
'''
import sys
from socket import *

def parseCommandLine():
    
if __name__ == '__main__':
    serverHost = 'localhost'
    serverPort = 50007
    
    message = [b'Hello Network World']
    
    if len(sys.argv) > 1:
        filePath = sys.argv[1]
        if len(sys.argv) > 2:
            message = (x.encode() for x in sys.argv[2:])
    
    socketObj = socket(AF_INET, SOCK_STREAM)
    socketObj.connect((serverHost, serverPort))
    
    while True:
        for line in message:
            socketObj.send(line)
            data = socketObj.recv(1024)
            print 'Client received:', data
        
    socketObj.close()