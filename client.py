import socket
import threading 
import os


ip_address = "0.0.0.0"
def_port = 5000
clients = {} 

def connection(): 
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client: 
        client.connect(("localhost", def_port))