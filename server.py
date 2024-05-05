import socket
import threading 
import os

ip_address = "0.0.0.0"
def_port = 5000
clients = {} 

def server_setup(ip_address, port = 5000):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server: 
        server.bind((ip_address, port))
        while True:
            (client,address) = server.accept()
            clients[clients] = ""
            client.send("You have connected".encode("utf-8"))
            
        

def connection_handling(server): 
    server




def main():
    if len(os.args) == 1:  
        server_setup(ip_address, def_port)
    elif len(os.args) == 2:
        server_setup(ip_address, os.args[1])
    threading.Thread()



