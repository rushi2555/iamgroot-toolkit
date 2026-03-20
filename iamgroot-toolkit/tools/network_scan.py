import os

target = input("Enter network (e.g. 192.168.1.0/24): ")
os.system(f"nmap -sn {target}")
