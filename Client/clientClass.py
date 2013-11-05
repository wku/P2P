'''
Created on Oct 17, 2013

@author: christopherhuang
'''
import random, thread, sys
from socket import *
from subprocess import call

class Client:
    '''
    class for client. It contains client's attributes and methods
    '''
    def __init__(self, arg):
        '''
        constructor to initialize the client
        '''
        print arg
        self.filePath = arg[1]
        self.myAddress = (gethostname(), 50008)
        self.serverHost = arg[2]
        self.serverPort = int(arg[3])
        self.neighbour = []                     #neighbour list
        self.signal = False
        
    def isConfirmed(self, address):  
        sockObj = socket(AF_INET, SOCK_STREAM)
        message = 'join' + ' ' + str(self.myAddress[1])     #send the listening port number
        
        try:
            print address
            sockObj.connect((address[0], int(address[1])))   #connect to the neighbor
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
        request = 'join' + ' ' + str(self.myAddress[1])               #join request
        sockObj = socket(AF_INET, SOCK_STREAM)
        
        try:
            sockObj.connect((self.serverHost, self.serverPort)) #connect to the server
        except error:
            print error                        #if the connection fails
            return False                                    #return false
        
        sockObj.send(request)                               #send join request
        print "send request to server", self.serverHost, self.serverPort
        
        while True:
            response = sockObj.recv(1024)                       #response from server
            
            if response == 'success':
                sockObj.close()
                return True                                 #join successfully
            else:
                address = response.split(' ')               #retrieve the host name and port number
                sockObj.close()                             #close the connection to the server 
                       
                if self.isConfirmed(address):      #connect the peer
                    self.neighbour.append(address)
                    return True                             #join successfully
                else:
                    return False
    def listFile(self):
        '''
        list files in the shared directory
        '''
        call(["ls", self.filePath])
        
    def quit(self):
        '''
        quit the system
        '''
        request = "quit"
        inform = self.neighbour
        inform.append(object)
        socketObj = socket(AF_INET, SOCK_STREAM)
        
    def handleService(self):
        '''
        Handle the service request such as share and get from console
        '''
        while True:
            prompt = "p2p system"
                     
            request = raw_input(prompt)
            
            if request == 'quit':
                self.quit()
                break
            elif request == 'list':
                self.listFile()
                
    def main(self):

        '''
        main function
        '''
        sockObj = socket(AF_INET, SOCK_STREAM)              #initialize the socket object
        if self.join():                                     #request to join the system
            sockObj.bind(self.myAddress)                    #bind it to client's address
            sockObj.listen(5)                               #start to listen the coming message            
            print "join the P2P system successfully"
            print "waiting"
            print self.neighbour
            
            thread.start_new_thread(self.handleService, ())
        while True:
            connection, address = sockObj.accept()
            print "Client connected " , address
            
            while True:
                data = connection.recv(1024)
                data = data.split(' ')
                if not data: break
                else:
                    if data[0] == 'join':
                        self.neighbour.append([address[0], data[1]])                        
                        connection.send('success') 
            
        sockObj.close()
        