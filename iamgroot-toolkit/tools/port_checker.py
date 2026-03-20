import socket

ip = input("Enter IP: ")
port = int(input("Enter port: "))

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
result = sock.connect_ex((ip, port))

if result == 0:
    print("Port is OPEN")
else:
    print("Port is CLOSED")

sock.close()
