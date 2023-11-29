import os
import random
import sys
from modules.scan_lan import main_scan
from modules.banners import computer_art, banner_systemshock, hackplanet_banner, lanattack_banner, spider_banner, eagle_main, evil_corp_main, evil_corp
from spoof_lib.spoof_lib import main_spoof_lib
cyan = '\x1b[0;36m'
green = '\x1b[0;32m'
oke_green = '\x1b[0;92m'
light_green = '\x1b[1;32m'
white = '\x1b[1;37m'
red = '\x1b[1;31m'
yellow = '\x1b[0;33m'
BlueF = '\x1b[1;34m'
RESET = "\x1b[0m"
orange = '\x1b[38;5;166m'
Blue = '\033[1;34m'
Green_light = '\033[1;32m'


def randomize_banners():
    numeric = ['1', '2', '3', '4', '5', '6', '7']
    pick = random.choice(numeric)
    if pick == '1':
        computer_art()
    elif pick == '2':
        banner_systemshock()
    elif pick == '3':
        hackplanet_banner()
    elif pick == '4':
        lanattack_banner()
    elif pick == '5':
        spider_banner()
    elif pick == '6':
        evil_corp_main()
    elif pick == '7':
        eagle_main()


def clear():
    os.system('clear')


def main():
    while True:
        try:
            clear()
            randomize_banners()
            shell = input(f'''{white}
{green}┌─[{red}LanAttack{green}]──[{red}~{green}]─[{orange}0x1337{green}]{green}:
└─────►{orange} ''').lower()

            while not shell in ['1', '2', '3', '4', 'clear']:
                print(f'{white}[{red}!{white}]{white} Invalid option!')
                shell = input(f'''{white}
{green}┌─[{red}LanAttack{green}]──[{red}~{green}]─[{orange}0x1337{green}]{green}:
└─────►{orange} ''')

            else:
                if shell == '1':
                    main_spoof_lib()

                elif shell == '2':
                    main_scan()

                elif shell == '3' or shell == 'clear':
                    clear()
                    randomize_banners()

                elif shell == '4':
                    clear()
                    evil_corp()
                    print(f'\t{white}[{green}+{white}]{Green_light}Good Bye!')
                    sys.exit()

        except KeyboardInterrupt:
            print(f'\n{white}[{red}!{white}]{green} Ctrl+C Detected. Exiting...')
            sys.exit(0)

