'''
Created on Oct 17, 2013

@author: christopherhuang
'''
import random, thread, sys, time
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
        self.filePath = arg[1]
        self.myAddress = ('127.0.0.1', int(arg[3]))
        self.serverHost = arg[2]
        self.serverPort = 50007
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
        request = "quit" + ' ' + str(self.myAddress[1])
        inform = self.neighbour
        inform.append([self.serverHost, self.serverPort])       #list of neighbors and a server to be informed later
        
        for address in inform:
            socketObj = socket(AF_INET, SOCK_STREAM)
            socketObj.connect((address[0], int(address[1])))                               #connect to the remote host
            socketObj.send(request)                                  #send quit request
            response = socketObj.recv(1024)                          #get response
            print "disconnected with %s %s successfully" % (address[0], address[1])
            socketObj.close()                                        #close the connection
        print "quit P2P system successfully"
        sys.exit()
        
    def handleService(self):
        '''
        Handle the service request such as share and get from console
        '''
        print "main thread"
        while True:
            prompt = "p2p system\n"
                     
            request = raw_input(prompt)
            
            if request == 'quit':
                self.quit()
                break
            elif request == 'list':
                self.listFile()
                
    def handleRequest(self):
        '''
        handle the request from neighbors 
        '''
        print "child thread"
        time.sleep(1)
        sockObj = socket(AF_INET, SOCK_STREAM)              #initialize the socket object
        sockObj.bind(self.myAddress)                    #bind it to client's address
        sockObj.listen(5)                               #start to listen the coming message            
        
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
                        break
                    elif data[0] == 'quit':
                        self.neighbour.remove([address[0], data[1]])    #remove the record of the peer
                        print "peer:[%s,%s] quit" % (address[0], data[1])
                        break
            connection.close()
        sockObj.close()           
    def main(self):
        '''
        main function
        '''
        if self.join():                                     #request to join the system
            print "join successfully"
            thread.start_new_thread(self.handleRequest(), ())
            self.handleService()                            #handle the user request
        else:
            print "cann't connect the server"

        