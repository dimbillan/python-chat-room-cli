import socket
import threading
import sys
import os
import time
import traceback
from message_handler import *
from helpers import *

def recv(sock):
    while True:
        try:
            received_message = sock.recv(1024).decode('utf-8')
            if not received_message:
                print("Connection closed by the server.")
                print("Restarting...")

                clear()

                time.sleep(1)

                python = sys.executable
                os.execl(python, python, *sys.argv)

            print("mh runs")
            message_handler(received_message)

        except Exception as e:
            print(f"Error receiving data: {e}")
            print(traceback.format_exc())
            break

def run_client(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((host, port))
        print(f"Connected to server at {host}:{port}")

        threading.Thread(target=recv, args=(sock,), daemon=True).start()

        while True:
            message = input("")
            if message.lower() == 'exit':
                print("Exiting...")
                break
            try:
                sock.sendall(message.encode('utf-8'))
            except Exception as e:
                print(f"Error sending message: {e}")
                break

if __name__ == '__main__':
    server_address = input("Enter a server address in the format ip:port: ")

    try:
        host, port = server_address.split(":")
        port = int(port)

        clear()
    
    except ValueError:
        print("Invalid format. Please enter in 'ip:port' format.")
        exit(1)

    run_client(host, port)
