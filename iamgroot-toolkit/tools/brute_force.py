target_password = "admin123"

wordlist = ["1234", "admin", "password", "admin123", "root"]

print("Starting brute force...\n")

for password in wordlist:
    print(f"Trying: {password}")

    if password == target_password:
        print(f"\n[+] Password Found: {password}")
        break
