#!/bin/bash

echo "[+] Installing IAMGROOT Toolkit..."

sudo apt update
sudo apt install -y python3 python3-venv python3-pip nmap net-tools

sudo mkdir -p /usr/local/bin/iamgroot-toolkit
sudo cp -r * /usr/local/bin/iamgroot-toolkit/

sudo python3 -m venv /usr/local/bin/iamgroot-toolkit/venv

sudo /usr/local/bin/iamgroot-toolkit/venv/bin/pip install python-nmap colorama requests

echo '#!/bin/bash
/usr/local/bin/iamgroot-toolkit/venv/bin/python /usr/local/bin/iamgroot-toolkit/main.py' | sudo tee /usr/local/bin/iamgroot > /dev/null

sudo chmod +x /usr/local/bin/iamgroot

echo "[+] Installation Complete!"
echo "[+] Run using: iamgroot"
