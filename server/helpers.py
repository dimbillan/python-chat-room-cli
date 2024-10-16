import socket
import os
import datetime

def send(client_socket, message):
    client_socket.sendall(message.encode("utf-8"))

def recv(client_socket):
    received_message = client_socket.recv(1024).decode("utf-8")
    print(f"Recieved:{received_message}")
    return received_message

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def timestamp():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def log():
    print()