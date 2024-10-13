import sqlite3
import hashlib
import threading
import time
import traceback
import os
from helpers import *

db_path = os.path.join(os.getcwd(), "server/data/userdata.db")

conn = sqlite3.connect(db_path, check_same_thread=False)
cur = conn.cursor()

onlineUsers = {}

def handle_client(client_socket):
    #time.sleep(3)
    send(client_socket,
        "Welcome.\n"
        "Please choose an option:\n"
        "1 - Login\n"
        "2 - Register\n")
    
    while True:
        try:
            logorreg = recv(client_socket)

            if logorreg == "1":
                send(client_socket, "Enter your username:")
                username = recv(client_socket)

                send(client_socket, "Enter your password:")
                password = recv(client_socket)

                password = password.encode("utf-8")

                password = hashlib.sha256(password).hexdigest()

                cur.execute("SELECT username, password, status FROM userdata WHERE username = ? AND password = ?", (username, password))
                result = cur.fetchone()    
                
                if not result:
                    send(client_socket, "Failed to authorize")
                    client_socket.close()
                    return
                
                username, password, status = result
                
                if username in onlineUsers:
                    send(client_socket, "You have already logged in")
                    client_socket.close()
                    return
                
                if status == 1:
                    send(client_socket, "You have been kicked")
                    client_socket.close()

                elif status == 0 or status == 2:
                    send(client_socket, "success")
                    #threading.Thread(target=user_handler, args=(client_socket,username))

                else:
                    send(client_socket, "Failed: Unvalid status")
                    client_socket.close()
                    
            elif logorreg == "register":

                username = client_socket.recv(1024).decode("utf-8")
                password = client_socket.recv(1024)
                password = hashlib.sha256(password).hexdigest()

                cur.execute("SELECT username FROM userdata WHERE username = ?", (username,))

                result = cur.fetchone()

                if not result:
                    cur.execute("INSERT INTO userdata (username, password, status) VALUES (?, ?, ?)",(username, password, 0))
                    conn.commit()

                    send(client_socket, "success")

                    threading.Thread(target=handle_client, args=(client_socket, username)).start()

                    onlineUsers[username] = client_socket                

                else:
                    send(client_socket, "Username has already been taken")
                    client_socket.close()
                    onlineUsers[username] = client_socket           

        except Exception as e:
            print(f"error: {e}")
            traceback.print_exc()
            break