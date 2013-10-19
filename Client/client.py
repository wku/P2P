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
    
    if len(sys.argv) > 1:
        myHost = 'localhost'        #client host name
        myPort = int(sys.argv[1])        #client port number
    else:               
        print "no host name and port number"
        sys.exit()
        
    client = Client(myHost, myPort)
    
    client.main()                   #run the client
    


    