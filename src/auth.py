import json
import time
import atexit
import requests
from colorama import *
from src.utils import get_headers
from fake_useragent import UserAgent
from datetime import datetime, timedelta
from src.__init__ import read_config, log, kng, mrh
from requests.exceptions import ConnectionError, Timeout

init(autoreset=True)
ua = UserAgent()
config = read_config()

def save_user_agents(filename='./data/user_agents.json'):
    with open(filename, 'w') as f:
        json.dump(user_agents, f, indent=4)

def load_user_agents(filename='./data/user_agents.json'):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

last_update_time = datetime.now()
timeouts = config.get('LOOP_COUNTDOWN', 3800)
user_agents = load_user_agents()

def get_user_agent(account):
    global last_update_time
    change_interval = 30
    current_time = datetime.now()
    
    if (current_time - last_update_time) > timedelta(minutes=change_interval):
        last_update_time = current_time
        print(kng + f"User agents checked at {current_time.strftime('%Y-%m-%d %H:%M:%S')}")

    if account not in user_agents:
        new_user_agent = ua.random
        while 'Mobile' not in new_user_agent:
            new_user_agent = ua.random
        user_agents[account] = new_user_agent
        save_user_agents()

    return user_agents[account]

def get_token(init_data_raw, account, retries=5, backoff_factor=0.5, timeout=timeouts):
    url = 'https://api.hamsterkombatgame.io/auth/auth-by-telegram-webapp'
    headers = {
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
        'Origin': 'https://hamsterkombatgame.io',
        'Referer': 'https://hamsterkombatgame.io/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': get_user_agent(account),
        'accept': 'application/json',
        'content-type': 'application/json'
    }
    data = json.dumps({"initDataRaw": init_data_raw})

    for attempt in range(retries):
        try:
            res = requests.post(url, headers=headers, data=data, timeout=timeout)
            res.raise_for_status()
            return res.json()['authToken']
        except (requests.ConnectionError, requests.Timeout) as e:
            log(mrh + f"Connection error on attempt {attempt + 1}: {e}", flush=True)
        except Exception as e:
            log(mrh + f"Failed Get Token. Error: {e}", flush=True)
            try:
                error_data = res.json()
                if "invalid" in error_data.get("error_code", "").lower():
                    log(mrh + "Failed Get Token. Invalid init data", flush=True)
                else:
                    log(mrh + f"Failed Get Token. {error_data}", flush=True)
            except Exception as json_error:
                log(mrh + f"Failed Get Token and unable to parse error response: {json_error}", flush=True)
            return None
        time.sleep(backoff_factor * (2 ** attempt))
    log(mrh + "Failed to get token after multiple attempts.", flush=True)
    return None

def authenticate(token, account):
    url = 'https://api.hamsterkombatgame.io/auth/me-telegram'
    headers = get_headers(token)
    headers['User-Agent'] = get_user_agent(account)
    
    try:
        res = requests.post(url, headers=headers)
        res.raise_for_status()
    except Exception as e:
        log(mrh + f"Token Failed : {token[:4]}********* | Status : {res.status_code} | Error: {e}", flush=True)
        return None

    return res

def save_user_agents_at_exit():
    save_user_agents()

atexit.register(save_user_agents_at_exit)