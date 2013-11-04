'''
Created on Oct 16, 2013

@author: christopherhuang
'''
import sys
from socket import *
from clientClass import *

    
if __name__ == '__main__':
    serverHost = 'localhost'
    serverPort = 50007
    
    if len(sys.argv) == 4:
        client = Client(sys.argv)
    else:               
        print "no host name and port number"
        sys.exit()
         
    client.main()                   #run the client
    


    