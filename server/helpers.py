import socket
import os
def send(client_socket, message):
    client_socket.send(message.encode("utf-8"))
    print(f"Sended:{message}")

def recv(client_socket):
    received_message = client_socket.recv(1024).decode("utf-8")
    print(f"Recieved:{received_message}")
    return received_message

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
        
def log():
    print()