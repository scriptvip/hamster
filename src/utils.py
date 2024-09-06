from fake_useragent import UserAgent

ua = UserAgent()

def get_headers(token: str) -> dict:
    return {
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.9',
        'Authorization': f'Bearer {token}',
        'Connection': 'keep-alive',
        'Origin': 'https://hamsterkombatgame.io',
        'Referer': 'https://hamsterkombatgame.io/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': ua.random,
        'Content-Type': 'application/json'
    }

def load_tokens(filename):
    try:
        with open(filename, 'r') as file:
            return [line.strip() for line in file]
    except FileNotFoundError:
        print(f"File not found: {filename}")
        return []
