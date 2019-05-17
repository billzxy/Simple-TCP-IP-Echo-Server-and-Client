import socket, sys, time

#TODO: server process monitor, timeout auto disconnect, TLS/SSL
#TODO: multi-threading, timer for switch, console
#TODO: socket conn accept() interruption, OOP design



#Echo server setup
INET = ''
PORT = 13337

class Server:
    def __init__(self,inet,port):
        self.__inet = inet
        self.__port = port
        self.__server_address=(self.__inet,self.__port)
        self.__sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__sock.bind(self.__server_address)
        print('Starting up socket server on %s:%s' % self.__server_address)
        self.__sock.listen(1)
        self.__connection = None
        self.__client_address = None
        self.__main_switch = 1 #Server connection switch: 1 on, 0 off
        self.run()


    def run(self):
        while(self.__main_switch):
            self.handleConnection()
        self.closeConn()
        self.serverShutdown()
    
    def handleConnection(self):
        print('Waiting for a connection...')
        self.__connection, self.__client_address = self.__sock.accept()
        try:
            print('Connection from', self.__client_address)
            while True:
                data = self.__connection.recv(16)
                localtime = time.localtime(time.time())
                print('On %i/%i/%i, at %i:%i:%i, %s: '
                      %(localtime.tm_mon,localtime.tm_mday,localtime.tm_year,
                        localtime.tm_hour,localtime.tm_min,
                        localtime.tm_sec,self.__client_address[0]), data)
                if data:
                    #print('sending data back to the client')
                    self.__connection.sendall(data)
                else:
                    print('no more data from', self.__client_address)
                    break
                
        finally:
            self.closeConn()

    def serverSwitch(self,signal): #1 for on, 0 for off
        if(not self.__connection==None and signal==0):#needs testing
            ans = input('Warning! Connection still ongoing, sure to disconnect?(y/n):')
            while(not type(ans)==str or not ans in ('y','n')):
                ans = input('Only type "y" or "n" plz: ')
            if(ans=='y'):
                self.__main_switch = signal
        else:
            self.__main_switch = signal

    def closeConn(self):
        self.__connection.close()
        print('Connection with %s Closed.' %self.__client_address[0])
    
    def saveProgress(self):
        pass

    def serverShutdown(self):
        self.saveProgress()
        print("Socket Server shutting down...")
        sys.exit(1)

if(__name__=="__main__"):
    svr = Server(INET,PORT)




