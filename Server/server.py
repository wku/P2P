'''
Created on Oct 16, 2013

@author: christopherhuang
'''
from socket import *

if __name__ == '__main__':
    myHost = ''
    myPort = 50007
    
    sockObj = socket(AF_INET, SOCK_STREAM)
    sockObj.bind((myHost, myPort))
    sockObj.listen(5)
    
    while True:
        connection, address = sockObj.accept()
        print('Server connected by', address)
        while True:
            data = connection.recv(1024)
            if not data: 
                break
            if data == 'join':
                connection.send('xxxxx xxxxx')
        connection.close()
            