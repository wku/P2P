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
        self.myAddress = (host, port)
        self.serverHost = 'localhost'
        self.serverPort = 50007
        self.neighbour = []
        
    def isConfirmed(self, address, sockObj):  

        message = 'join'
        
        try:
            sockObj.connect(address)   #connect to the neighbor
        except error:
            print "fail to connect peer"   
        
        sockObj.send(message)    
        
        while True:
            response = sockObj.recv(1024)
            
            if response == 'success':
                sockObj.close()
                return True
            else:
                return False
        
    def join(self):

        '''
        join the P2P system
        '''
        request = 'join'                                    #join request
        sockObj = socket(AF_INET, SOCK_STREAM)
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
        sockObj = socket(AF_INET, SOCK_STREAM)              #initialize the socket object
        
        if self.join():
            sockObj.bind(self.myAddress)                        #bind it to client's address
            sockObj.listen(5)                               #start to listen the coming message
            print "join the P2P system successfully"
            
        while True:
            connection, address = sockObj.accept()
            print "Client connected " , address
            
            while True:
                data = connection.recv(1024)
                
                if not data: break
                else:
                    if data == 'join':
                        self.neighbour.append(address)                        
                        connection.send('success') 
            
    def parseCommandLine(self):
        pass

        