from helpers import *
import threading

onlineUsers = {}

lock = threading.Lock()


def user_handler(client_socket, username):
    with lock:
        onlineUsers[username] = client_socket

    send(client_socket, f"Welcome to chat room {username}!\n")
    broadcast(f"{username} has joined the room.")

    while True:
        try:
            received_message = recv(client_socket)

            if not received_message:  # If recv returns empty, client disconnected
                raise ConnectionResetError(f"Client {username} disconnected unexpectedly.")

            if received_message == "!exit":
                broadcast(f"Client {username} disconnected.")
                break

            elif received_message == "!onlines":
                online_user_list = ", ".join(onlineUsers.keys())  # Create a string of online usernames
                send(client_socket, f"Online users: {online_user_list}")

            elif received_message.startswith("!msg"):
                # Handle private messages
                parts = received_message.split(" ", 2)  # Split the command into parts
                if len(parts) < 3:
                    send(client_socket, "Usage: !msg <username> <message>")
                    continue
                
                target_username = parts[1]
                private_message = parts[2]

                # Check if the target user is online
                if target_username in onlineUsers:
                    target_socket = onlineUsers[target_username]
                    send(target_socket, f"Private message from {username}: {private_message}")  # Send private message
                    send(client_socket, f"Message sent to {target_username}: {private_message}")
                else:
                    send(client_socket, f"User {target_username} is not online.")

            else:
                broadcast(f"{username}: {received_message}")

        except ConnectionResetError:
            break

        except Exception as e:
            break

    with lock:
        if username in onlineUsers:
            del onlineUsers[username]

    client_socket.close()
    broadcast(f"Client {username} disconnected unexpectedly.")

def broadcast(broadcast_message):
    for client_socket in onlineUsers.values():
        send(client_socket, broadcast_message)
    print(broadcast_message)
