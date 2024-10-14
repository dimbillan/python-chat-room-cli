import socket

def get_all_local_ips():
    hostname = socket.gethostname()  # Geçerli makinenin adını al
    local_ip = socket.gethostbyname(hostname)  # Makinenin yerel IP'sini al
    return local_ip

if __name__ == "__main__":
    ip_address = get_all_local_ips()
    print(f"Yerel IP Adresi: {ip_address}")

from colorama import Fore, Back, Style, init

# Renklerin düzgün çalışması için init()
init()

# Farklı renklerde yazı yazma
print(Fore.RED + "Bu kırmızı bir yazıdır.")
print(Fore.GREEN + "Bu yeşil bir yazıdır.")
print(Fore.BLUE + "Bu mavi bir yazıdır.")
print(Fore.YELLOW + "Bu sarı bir yazıdır.")

# Arka plan renkleri
print(Back.CYAN + "Bu arka planı mavi olan bir yazıdır." + Style.RESET_ALL)

# Yazı stilleri
print(Style.DIM + "Bu soluk bir yazıdır.")
print(Style.BRIGHT + "Bu parlak bir yazıdır." + Style.RESET_ALL)























"""
    user_input = input(""
To start the server, please choose one of the following options:
1. Press "1" to start a local server (localhost).
2. Enter an external server address in the format "ip:port".

Examples:
- For a local server: 1
- For an external server: 192.168.1.10:65432

Please make your selection: "")

    if user_input == "1":
        host = '127.0.0.1'
        port = 65432
    else:
        try:
            host, port = user_input.split(":")
            port = int(port)
        except ValueError:
            print("Invalid format. Please enter in 'ip:port' format.")
            exit(1)
    """