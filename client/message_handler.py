from helpers import *
from colorama import Fore, Back, Style, init

init(autoreset=True)

def message_handler(message):
    if message.startswith(":-server:-"):
        if message == ':-server:-success':
            #clear()
            printc("green", "You have successfully logged in.")

        elif message == ":-server:-fail":
            #clear()
            printc("red", "Invalid username or password.")

        elif message == ":-server:-alrdylogin":
            #clear()
            printc("red","You are already logged in.")

        elif message == ":-server:-kicked":
            #clear()
            printc("red","You have been kicked from the server.")

        elif message == ":-server:-invalid":
            #clear()
            printc("red","Invalid command.")

        else:
            print(Fore.YELLOW + "Server: " + Style.BRIGHT + message + Style.RESET_ALL)

    elif message.startswith(":-") and message.endswith(":-"):
            print(message[2:-2])
        
    else:
        print(message)

def printc(color,message):
    """
    Print with given color and message
    """
    match color:
        case "red":
            print(Fore.RED + message + Style.RESET_ALL)

        case "green":
            print(Fore.GREEN + message + Style.RESET_ALL)

        case "blue":
            print(Fore.BLUE + message + Style.RESET_ALL)

        case "yellow":
            print(Fore.YELLOW + message + Style.RESET_ALL)

        case "magenta":
            print(Fore.MAGENTA + message + Style.RESET_ALL)

        case "cyan":
            print(Fore.CYAN + message + Style.RESET_ALL)

        case "white":
            print(Fore.WHITE + message + Style.RESET_ALL)

        case "bright":
            print(Style.BRIGHT + message + Style.RESET_ALL)