import os
from utils import banner, loading, menu

def main():
    os.system("clear")
    banner()
    loading()

    while True:
        menu()
        choice = input("root@iamgroot:~# Select option > ")

        if choice == "1":
            os.system("python3 tools/nmap_tool.py")
        elif choice == "2":
            os.system("python3 tools/network_scan.py")
        elif choice == "3":
            os.system("python3 tools/ip_info.py")
        elif choice == "4":
            os.system("python3 tools/port_checker.py")
        elif choice == "5":
            os.system("python3 tools/wifi_scan.py")
        elif choice == "6":
            os.system("python3 tools/dns_lookup.py")
        elif choice == "7":
            os.system("python3 tools/brute_force.py")
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
