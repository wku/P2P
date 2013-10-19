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
    if len(peerList) == 0:
        peerList.append(address)
        return "success"
    else:
        if address not in peerList:
            peerList.append(list(address))
            peer = peerList[random.randint(0,len(peerList) - 2)]
            peer = str(peer[0]) + ' ' + str(peer[1])
            return peer
        else:
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
        print type(address)
        while True:
            data = connection.recv(1024)
            if not data: 
                break
            if data == 'join':
                outcome = register(address, peerList)                
                connection.send(outcome)
                print peerList
                
        connection.close()
            