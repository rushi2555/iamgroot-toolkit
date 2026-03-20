import requests

ip = input("Enter IP: ")
url = f"http://ip-api.com/json/{ip}"

data = requests.get(url).json()

for key, value in data.items():
    print(f"{key}: {value}")
