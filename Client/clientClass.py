'''
Created on Oct 17, 2013

@author: christopherhuang
'''
import socket
class Client:
    '''
    class for client. It contains client's attributes and methods
    '''
    def createSocket(self, family, protocol):
        '''
        make a socket object
        '''
        self.socketObj = socket(family, protocol)
    
    def connect(self, server, port):
        '''
        connect to server machine 
        '''
        self.serverHost = server
        self.serverPort = port
        self.socketObj.connect((self.serverHost, self.serverPort))
    
    def close(self):
        '''
        close the socket to send eof to server
        '''
        self.socketObj.close()