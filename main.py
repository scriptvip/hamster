import sys, os

from src.core import main
from src.__init__ import _banner, log, mrh

if __name__ == "__main__":
    while True:
        try:
            if not os.path.exists('codes'):os.mkdir('codes')
            _banner()
            main()
        except KeyboardInterrupt:
            print()
            log(mrh + f"Successfully logged out of the bot\n")
            sys.exit()
