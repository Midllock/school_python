import socket
import sys
from time import sleep
import random as r

class Client:

    def init(self, *kwargs):

        self.host = kwargs['host'] if 'host' in kwargs else socket.gethostname()
        self.port = kwargs['port'] if 'port' in kwargs else 5000

        self.client_socket = socket.socket()
        self.client_socket.connect((self.host, self.port))

    def go(self):

        r.seed()
        self.message = input(" $ ") 

        while self.message.lower().strip() != 'bye':
            self.client_socket.send(self.message.encode())
            self.data = self.client_socket.recv(1024).decode()
            print('-> ', end ="")
            for char in self.__data:
                sleep(r.random() 0.05)
                sys.stdout.write(char)
                sys.stdout.flush()
            print("")
            self.message = input(" $ ")

        self.clientsocket.close()

if __name__ == '_main':
    client = Client()
    client.go()