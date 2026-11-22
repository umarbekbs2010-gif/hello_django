#!/usr/bin/env python3
"""
Wi-Fi Tarmoq Skaneri (Termux / Android uchun — Root talab qilmaydi)
Uyingizdagi Wi-Fi tarmog'iga ulangan barcha qurilmalarni 5-10 soniyada aniqlaydi.
"""

import concurrent.futures
import ipaddress
import re
import socket
import subprocess
import sys


def get_gateway_and_subnet():
    """Asosiy router IP manzili va lokal tarmoq diapazonini aniqlaydi."""
    try:
        out = subprocess.check_output(["ip", "route"], text=True, stderr=subprocess.DEVNULL)
        gw_match = re.search(r"default via (\d+\.\d+\.\d+\.\d+)", out)
        src_match = re.search(r"src (\d+\.\d+\.\d+\.\d+)", out)
        gateway = gw_match.group(1) if gw_match else "192.168.1.1"
        local_ip = src_match.group(1) if src_match else gateway
        network = ipaddress.IPv4Network(f"{local_ip}/24", strict=False)
        return gateway, local_ip, network
    except Exception:
        return "192.168.1.1", "192.168.1.2", ipaddress.IPv4Network("192.168.1.0/24")


def ping_ip(ip_str):
    """Bitta IP manzilga tezkor ping yuborib ARP/neigh jadvalini yangilaydi."""
    subprocess.run(
        ["ping", "-c", "1", "-W", "1", ip_str],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )


def get_neighbors():
    """'ip neigh show' orqali faol qurilmalar ro'yxatini o'qiydi."""
    devices = {}
    try:
        out = subprocess.check_output(["ip", "neigh", "show"], text=True, stderr=subprocess.DEVNULL)
        for line in out.splitlines():
            m = re.match(r"^(\d+\.\d+\.\d+\.\d+)\s+dev\s+\S+\s+lladdr\s+([0-9a-fA-F:]+)\s+(\S+)", line)
            if m:
                ip, mac, state = m.groups()
                if state.upper() not in ("FAILED", "INCOMPLETE"):
                    devices[ip] = {"mac": mac.upper(), "state": state}
    except Exception:
        pass
    return devices


def resolve_name(ip):
    """Qurilma nomini (hostname) aniqlashga harakat qiladi."""
    try:
        return socket.gethostbyaddr(ip)[0]
    except Exception:
        return "Noma'lum qurilma"


def main():
    print("\n" + "=" * 54)
    print("   WI-FI O'G'RILARINI FOSH QILISH SKANERI (TERMUX)")
    print("=" * 54)

    gateway, local_ip, network = get_gateway_and_subnet()
    print(f"[*] Router (Gateway) : {gateway}")
    print(f"[*] Sizning IP       : {local_ip}")
    print(f"[*] Skanerlanmoqda   : {network} (5-10 soniya kuting...)\n")

    hosts = [str(ip) for ip in network.hosts()]
    with concurrent.futures.ThreadPoolExecutor(max_workers=64) as executor:
        executor.map(ping_ip, hosts)

    devices = get_neighbors()
    if not devices:
        print("[!] Faol qurilmalar topilmadi. Wi-Fi yoqilganini tekshiring.")
        sys.exit(1)

    print(f"{'№':<3} {'IP MANZIL':<16} {'MAC MANZIL':<19} {'QURILMA / HOLAT'}")
    print("-" * 54)

    sorted_ips = sorted(devices.keys(), key=lambda x: tuple(int(p) for p in x.split(".")))
    for idx, ip in enumerate(sorted_ips, start=1):
        mac = devices[ip]["mac"]
        if ip == gateway:
            label = "ROUTER (Asosiy)"
        elif ip == local_ip:
            label = "SIZNING TELEFONINGIZ"
        else:
            label = resolve_name(ip)
        print(f"{idx:<3} {ip:<16} {mac:<19} {label}")

    print("-" * 54)
    print(f"[+] Jami topilgan qurilmalar: {len(sorted_ips)} ta")
    print(f"[!] Notanish MAC manzil ko'rsangiz, brauzerda http://{gateway} ga kirib")
    print("    'MAC Filtering' yoki 'Connected Devices' bo'limidan darhol bloklang!\n")


if name == "main":
    main()