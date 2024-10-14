from helpers import *
import socket
import time
onlineUsers = {}

def user_handler(client_socket, username):
    onlineUsers[username] = client_socket
    while True:
        x = recv(client_socket)
        broadcast(f"dsadad:{x}")

def broadcast(broadcast_message):
    for username, client_socket in onlineUsers.items():
        send(client_socket, broadcast_message)
    print(broadcast_message)

