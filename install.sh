#!/bin/bash
echo -e "[96m[*] Installing Device Lookup...[0m"
pip install requests --break-system-packages 2>/dev/null || pip install requests
chmod +x device-lookup.py
ln -sf $(pwd)/device-lookup.py /usr/local/bin/device-lookup 2>/dev/null
echo -e "[92m[+] Done! Run: device-lookup[0m"
