import requests
import time
from datetime import datetime
from colorama import init, Fore, Style
import os

init(autoreset=True)

print(f"{Fore.CYAN}Discord Username Claimer{Style.RESET_ALL}")
print(f"{Fore.CYAN}The Program will try to claim your desired username every 4 minutes.{Style.RESET_ALL}")
print(f"{Fore.CYAN}Github: https://github.com/LightCyan01/discord-username-claimer{Style.RESET_ALL}")

if os.path.isfile('cfg.txt'):
    with open('cfg.txt', 'r') as cfg:
        lines = cfg.readlines()
        username = lines[0].strip().split(': ')[1]
        token = lines[1].strip().split(': ')[1]
        os.system('cls' if os.name == 'nt' else 'clear')
else:
    username = input('Enter the username: ')
    token = input('Enter your auth token: ')

    with open('cfg.txt', 'w') as cfg:
        cfg.write(f"username: {username}\nauthorization: {token}")
        os.system('cls' if os.name == 'nt' else 'clear')

payload = {'username': username}
headers = {'Authorization': token}

def send_request(url, headers, payload):
    try:
        r = requests.post(url, headers=headers, json=payload, timeout=10)
        r.raise_for_status()
        return r
    
    except:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"{timestamp} {Fore.RED}[ERROR] Response status code has an error value ({r.status_code}) {Style.RESET_ALL}")

def claim_username(url, headers, payload):
    try:
        # Check if token is valid
        r = requests.get('https://discord.com/api/v9/users/@me', headers=headers, timeout=10)
        if r.status_code == 200:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"{timestamp} {Fore.GREEN}[SUCCESS] Token is valid.{Style.RESET_ALL}")
        else:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"{timestamp} {Fore.RED}[ERROR] Your token is invalid.{Style.RESET_ALL}")
            os.remove("cfg.txt")
            return

        while True:
            r = requests.post(url, headers, payload, timeout=10)
            if r.status_code == 200:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print(f"{timestamp} {Fore.GREEN}[SUCCESS] Claimed username.{Style.RESET_ALL}")
                break
            elif r.status_code == 429:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print(f"{timestamp} {Fore.RED}[ERROR] Too many attempts. Retrying in {r.headers.get('Retry-After')} seconds.{Style.RESET_ALL}")
                time.sleep(int(r.headers.get('Retry-After')))
            elif r.status_code == 401:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print(f"{timestamp} {Fore.RED}[ERROR] 401 - Unauthorized. Retrying in 4 minutes.{Style.RESET_ALL}")
                time.sleep(4 * 60)
            elif r.status_code == 400 and 'username' in r.json():
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print(f"{timestamp} {Fore.RED}[ERROR] Username '{payload['username']}' is taken.{Style.RESET_ALL}")
                return
            else:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print(f"{timestamp} {Fore.RED}[ERROR] {r.status_code} (will re-attempt). Retrying in 4 minutes.{Style.RESET_ALL}")
                time.sleep(4 * 60)
    except requests.exceptions.RequestException as e:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"{timestamp} {Fore.RED}[ERROR] {e}{Style.RESET_ALL}")
        print(f"{timestamp} {Fore.RED}[ERROR] Connection error (will re-attempt). Retrying in 4 minutes.{Style.RESET_ALL}")
        time.sleep(4 * 60)

while True:
    url = 'https://discord.com/api/v9/users/@me/pomelo'

    try:
        claim_username(url, headers, payload)
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}Program stopped manually.{Style.RESET_ALL}")
        break
    except:
        print(f"\n{Fore.RED}[ERROR] Unknown error occurred.{Style.RESET_ALL}")
        time.sleep(4 * 60)
    else:
        time.sleep(4 * 60)
