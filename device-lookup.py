#!/usr/bin/env python3
import requests, socket, subprocess, os
C="\033[96m";G="\033[92m";Y="\033[93m";R="\033[91m";W="\033[97m";D="\033[90m";B="\033[1m";X="\033[0m"
def banner():
    os.system('clear')
    print(f"{C}{B}\n ╔╦╗╔═╗╦  ╦╦╔═╗╔═╗  ╦  ╔═╗╔═╗╦╔═╦ ╦╔═╗\n  ║║║╣ ╚╗╔╝║║  ║╣   ║  ║ ║║ ║╠╩╗║ ║╠═╝\n ═╩╝╚═╝ ╚╝ ╩╚═╝╚═╝  ╩═╝╚═╝╚═╝╩ ╩╚═╝╩ \n{X}{W}              Device Lookup v3.0{X}\n{D}       github.com/denzil6067-stack{X}\n{G}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{X}\n")
def lookup_mac(mac):
    mac=mac.strip().lower()
    print(f"\n{Y}{B}[ MAC ]{X} {W}{mac}{X}\n")
    try:
        r=requests.get(f"https://api.maclookup.app/v2/macs/{mac}",timeout=10).json()
        vendor=r.get('company') or requests.get(f"https://api.macvendors.com/{mac}",timeout=8).text
        print(f"  {C}Vendor  :{X} {W}{vendor}{X}")
        if r.get('company'):
            print(f"  {C}Country :{X} {r.get('country','-')} {r.get('countryCode','')}")
            print(f"  {C}Address :{X} {r.get('address','-')}")
            print(f"  {C}Block   :{X} {r.get('blockStart')} -> {r.get('blockEnd')}")
    except Exception as e:
        print(f"  {R}Error:{X} {e}")
def lookup_ip(ip):
    print(f"\n{Y}{B}[ IP ]{X} {W}{ip}{X}\n")
    try:
        print(f"  {C}Hostname:{X} {socket.gethostbyaddr(ip)[0]}")
    except:
        print(f"  {C}Hostname:{X} {D}No reverse DNS{X}")
    out=subprocess.getoutput(f"ping -c 1 -W 1 {ip} 2>&1")
    print(f"  {C}Status  :{X} {G}Alive{X}" if "ttl=" in out.lower() else f"  {C}Status  :{X} {R}Down / Filtered{X}")
banner()
print(f"  {W}[1]{X} MAC Lookup\n  {W}[2]{X} IP Lookup\n  {W}[3]{X} Both\n")
c=input(f"{G}└──╼ $ {X}").strip()
if c=="1":
    lookup_mac(input(f"{C}MAC > {X}"))
elif c=="2":
    lookup_ip(input(f"{C}IP > {X}"))
elif c=="3":
    lookup_mac(input(f"{C}MAC > {X}"))
    lookup_ip(input(f"{C}IP > {X}"))
print(f"\n{G}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{X}\n")
