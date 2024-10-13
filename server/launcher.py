import subprocess
import sys
import os

def check_library(library_name):
    try:
        __import__(library_name)
        print(f"{library_name} is already installed.")

    except ImportError:
        answer = input(f"{library_name} is not installed. Would you like to install it? (yes/y or no/n): ").lower()

        if answer in ["yes", "y"]:
            print(f"Installing {library_name}...")

            subprocess.check_call([sys.executable, "-m", "pip", "install", library_name])

        elif answer in ["no", "n"]:
            print(f"{library_name} was not installed. Continuing to the next one.")

        else:
            print("Invalid response! Please enter 'yes/y' or 'no/n'.")
            sys.exit()

def check_libraries(library_list):
    print("Checking libraries")

    for library in library_list:
        check_library(library)

library_list = ["hashlib", "socket", "sqlite3", "threading", "datetime", "time"]

if __name__ == "__main__":
    check_libraries(library_list)
    
    subprocess.run(['python', os.path.join(os.getcwd(), "server/server.py")])
