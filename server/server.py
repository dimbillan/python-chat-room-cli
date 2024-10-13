#import os
import socket
import time
import threading
from client_handler import handle_client
from helpers import *

def start_server(host, port):
   
    clear()
  
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((host, port))
        server_socket.listen()
  
        print(f"Server is on. Listening {host}:{port} ...")

    except:
        print("Error creating socket. Exiting...")
        time.sleep(2)
        exit(1)

    while True:

        client_socket, client_address = server_socket.accept()
        print(f"Client connected: {client_address}")

        threading.Thread(target=handle_client, args=(client_socket,)).start()



if __name__ == "__main__":
    clear()
    host = "127.0.0.1"
    port = 65432
    start_server(host, port)