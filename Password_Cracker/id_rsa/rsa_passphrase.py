#!/usr/bin/env python3
import subprocess

with open("/usr/share/wordlists/rockyou.txt", "r", encoding="latin-1", errors="ignore") as file:
    for password in file:
        password = password.strip()
        result = subprocess.run(
            ["ssh-keygen", "-y", "-f", "id_rsa", "-P", password],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        if result.returncode == 0:
            print(f"[+] FOUND PASSPHRASE: {password}")
            break
        else:
            print(f"[-] Tried: {password}")
