'''
Created on Oct 16, 2013

@author: christopherhuang
'''
from socket import *
import random

def register(address, peerList):
    '''
    register a new peer into the system
    '''
    if len(peerList) == 0:                  #there is no peer in the system
        peerList.append(address)
        return "success"
    else:
        print "at regester\n"               #store newly coming peer
        if address not in peerList:
            peerList.append(address)
            peer = peerList[random.randint(0,len(peerList) - 2)]        #randomly choose peer from the list
            peer = str(peer[0]) + ' ' + str(peer[1])
            return peer
        else:                                                           #duplicated address
            return 'already registered'
    
if __name__ == '__main__':
    myHost = ''
    myPort = 50007
    peerList = []
    
    sockObj = socket(AF_INET, SOCK_STREAM)
    sockObj.bind((myHost, myPort))
    sockObj.listen(5)
    
    while True:
        connection, address = sockObj.accept()
        print('Server connected by', address)
        while True:
            data = connection.recv(1024)
            data = data.split(' ')
            print data
            if not data: 
                break
            if data[0] == 'join':                       #one peer wants to join the system
                address = list(address)                     
                address[1] = data[1]                     #switch listening port over the connection port number
                outcome = register(address, peerList)                
                connection.send(outcome)                #respond the peer
                print peerList                          #print the peer already in the system
                break                                   #finish the response this time
        connection.close()
            