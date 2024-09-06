# This file can be empty, it just indicates that this directory should be treated as a package
import os
import json
import time
from datetime import datetime
from colorama import *

mrh = Fore.LIGHTRED_EX
pth = Fore.LIGHTWHITE_EX
hju = Fore.LIGHTGREEN_EX
kng = Fore.LIGHTYELLOW_EX
bru = Fore.LIGHTBLUE_EX
reset = Style.RESET_ALL
htm = Fore.LIGHTBLACK_EX

last_log_message = None

def _banner():
    banner = r"""
  ██████╗ ██╗     ██╗████████╗ ██████╗██╗  ██╗
 ██╔════╝ ██║     ██║╚══██╔══╝██╔════╝██║  ██║
 ██║  ███╗██║     ██║   ██║   ██║     ███████║
 ██║   ██║██║     ██║   ██║   ██║     ██╔══██║
 ╚██████╔╝███████╗██║   ██║   ╚██████╗██║  ██║
  ╚═════╝ ╚══════╝╚═╝   ╚═╝    ╚═════╝╚═╝  ╚═╝
""" 
    print(Fore.GREEN + Style.BRIGHT + banner + Style.RESET_ALL)
    print(hju + f" Hamster Kombat Auto Bot")
    print(kng + f" This code copied and devoloped by abdo_sleem")
    print(hju + f" Elgyar la y5t4e !!")
    print(hju + f" Enzl ya mtdl333 (^__*)")

def _clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def read_config():
    config_path = os.path.join(os.path.dirname(__file__), '../config.json')
    with open(config_path, 'r') as file:
        try:
            config_content = file.read()
            return json.loads(config_content)
        except json.JSONDecodeError as e:
            return {}
        
def log(message,*l, **kwargs):
    global last_log_message
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    flush = kwargs.pop('flush', False)
    end = kwargs.pop('end', '\n')
    if message != last_log_message:
        print(f"{htm}[{current_time}] {message}", flush=flush, end=end)
        last_log_message = message

def log_line():
    print(pth + "~" * 60)

def load_fake_file(filepath):
    with open(filepath, 'r') as file:
        fake_ips = json.load(file)
    return fake_ips

def awak():
    _clear()
    _banner()
    log_line()

def countdown_timer(seconds):
    while seconds:
        m, s = divmod(seconds, 60)
        h, m = divmod(m, 60)
        h = str(h).zfill(2)
        m = str(m).zfill(2)
        s = str(s).zfill(2)
        print(f"{pth}please wait until {h}:{m}:{s} ", flush=True, end="\r")
        seconds -= 1
        time.sleep(1)
    print(f"{pth}please wait until {h}:{m}:{s} ", flush=True, end="\r")

def _number(number):
    return "{:,.0f}".format(number)