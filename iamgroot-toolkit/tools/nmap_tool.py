import nmap

target = input("Enter target IP: ")

nm = nmap.PortScanner()
nm.scan(target, arguments='-sV')

for host in nm.all_hosts():
    print("\nHost:", host)
    for proto in nm[host].all_protocols():
        print("Protocol:", proto)
        for port in nm[host][proto]:
            print(f"Port: {port} | {nm[host][proto][port]['state']}")
