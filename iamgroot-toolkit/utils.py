import time
import sys
from colorama import Fore, Style

def typing(text, delay=0.02):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def loading():
    messages = ["Initializing system...", "Loading modules...", "Access granted ✔"]
    for msg in messages:
        print(Fore.GREEN + "[+] " + msg + Style.RESET_ALL)
        time.sleep(0.5)

def banner():
    print(Fore.GREEN + r"""
╔══════════════════════════════════════════════╗
║        ███ IAMGROOT TOOLKIT v1.0 ███         ║
╚══════════════════════════════════════════════╝
""" + Style.RESET_ALL)

def menu():
    print(Fore.CYAN + """
[1] Nmap Scanner      → Scan open ports & services
[2] Network Scanner   → Discover devices on network
[3] IP Info Tool      → Get IP address details
[4] Port Checker      → Check specific port status
[5] WiFi Scanner      → Show nearby WiFi networks
[6] DNS Lookup        → Resolve domain to IP
[7] Brute Force Tool  → Test password list
[0] Exit              → Terminate program
""" + Style.RESET_ALL)
