import socket

domain = input("Enter domain: ")

try:
    ip = socket.gethostbyname(domain)
    print(f"IP Address: {ip}")
except:
    print("Unable to resolve domain")
