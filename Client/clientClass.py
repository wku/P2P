'''
Created on Oct 17, 2013

@author: christopherhuang
'''
from socket import *

class Client:
    '''
    class for client. It contains client's attributes and methods
    '''
    def __init__(self, host, port):
        '''
        constructor to initialize the client
        '''
        self.serverHost = host
        self.serverPort = port
        self.neighbour = []
        
    def isConfirmed(self, address, sockObj):  
        try:
            sockObj.connect(address)   #connect to the neighbor
        except error:
            print "fail to connect peer"   
    
        
    def join(self):
        '''
        join the P2P system
        '''
        request = 'join'                                    #join request
        sockObj = socket(AF_INET, SOCK_STREAM)              #initialize the socket object
        
        try:
            sockObj.connect((self.serverHost, self.serverPort)) #connect to the server
        except error:
            print 'connection error'                        #if the connection fails
        
        sockObj.send(request)                               #send join request
        
        while True:
            response = sockObj.recv(1024)                       #response from server
            
            if response == 'success':
                sockObj.close()
                return True                                 #join successfully
            else:
                address = tuple(response.split(' '))               #retrieve the host name and port number
                sockObj.close()                             #close the connection to the server 
                       
                if self.isConfirmed(address, sockObj):      #connect the peer
                    self.neighbour.append(address)
                    return True                             #join successfully
                else:
                    return False
    
                   
    def main(self):
        '''
        main function
        '''
        self.sockObj = socket(AF_INET, SOCK_STREAM)              #initialize the socket object
        self.sockObj.connect((self.serverHost, self.serverPort)) #connect to the server
    def parseCommandLine(self):
        pass

        