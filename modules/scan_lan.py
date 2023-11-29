import os
import sys
from prettytable import PrettyTable
from modules.banners import banner_scan, spider_no_banner, eagle, computer_banner, wolf_banner, evil_corp
import re
import subprocess

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
port_list = []


def scan_nmap(LAN):
    clear()
    spider_no_banner()
    if LAN:
        # Создайте временный файл для вывода nmap
        output_file = "nmap_output.txt"

        # Запустите nmap и перенаправьте его вывод в файл
        os.system(f'nmap -T5 --open {LAN} > {output_file}')

        # Откройте файл и извлеките информацию о портах
        with open(output_file, 'r') as file:
            nmap_output = file.read()

        # Создайте таблицу для отображения портов
        port_table = PrettyTable()
        port_table.field_names = ["PORT", "STATE", "SERVICE"]

        # Извлеките информацию о портах из вывода nmap и добавьте ее в таблицу
        for line in nmap_output.splitlines():
            if "/tcp" in line:
                parts = line.strip().split()
                port = parts[0]
                state = parts[1]
                service = parts[2]
                port_table.add_row([port, state, service])

        # Выведите таблицу с информацией о портах
        print(f'{grwh_prompt}Port scan with ip {LAN}:\n{port_table}')

        # Удалите временный файл
        os.remove(output_file)

        input(f'{grwh_prompt}Press Enter to continue...')
    else:
        print(f'{green}[{white}+{green}]{white} Your LAN-IP is not correct!')
        input(f'{grwh_prompt}Press Enter to continue...')


def scan_range(IP_RANGE):
    clear()
    eagle()
    if '/' in IP_RANGE:
        scanned = os.popen(f'nmap -T5 --open {IP_RANGE}').read()
        clear()
        eagle()
        print(f'{grwh_prompt}Scan output:\n{scanned}')
        input(f'{grwh_prompt}Enter to continue. . .')
    else:
        print(f'{green}[{white}+{green}]{white} Your LAN-RANGE is not correct!')
        input(f'{grwh_prompt}Enter to continue. . .')


def full_port_scanner(IP):
    global port_list
    # Your code to scan for open ports and populate port_list
    command = f'nmap -p- {IP} -vv --min-rate=10000 -Pn'
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    if process.returncode != 0:
        print(f'Error running nmap: {stderr.decode("utf-8")}')
        input('Press Enter to continue...')
        return

    nmap_output = stdout.decode("utf-8")
    open_ports = re.findall(r'Discovered open port (\d+)/tcp', nmap_output)
    port_list = open_ports  # Update the global port_list


def full_scan(IP, FILE_SAVE):
    clear()
    wolf_banner()

    # Call full_port_scanner to populate port_list
    full_port_scanner(IP)

    if not port_list:
        print(f'{grwh_prompt}No open ports found. Exiting...')
        return

    # Print the list of open ports
    port_list_str = ','.join(port_list)
    # print(f'Open ports: {port_list_str}')

    print(f'{grwh_prompt}The first stage is completed!\n{grwh_prompt}Please wait for ending 2-stage!')

    # Perform the second nmap scan using the port_list
    command_x2 = f'nmap -p{port_list_str} -sC -sV -Pn -vv {IP} -oN output/{FILE_SAVE}'
    process_x2 = subprocess.Popen(command_x2, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout2, stderr2 = process_x2.communicate()

    if process_x2.returncode != 0:
        print(f'Error running nmap: {stderr2.decode("utf-8")}')
        input('Press Enter to continue...')

    view_or_no = input(f'{grwh_prompt}Output Files scan-results saved: output/{FILE_SAVE}\n'
                       f'{grwh_prompt}View output scan result? (y/n): ').lower()
    view_result_file(view_or_no, FILE_SAVE)


def scan_vulns_windows(IP, FILE_SAVE):
    clear()
    evil_corp()

    # Call full_port_scanner to populate port_list
    full_port_scanner(IP)

    if not port_list:
        print(f'{grwh_prompt} No open ports found. Exiting...')
        return

    # Print the list of open ports
    port_list_str = ','.join(port_list)
    # print(f'Open ports: {port_list_str}')

    print(f'{grwh_prompt}The first stage is completed!\n{grwh_prompt}Please wait for ending 2-stage!')

    # Perform the second nmap scan using the port_list
    command_x2 = f'nmap -p{port_list_str} --script smb-os-discovery,smb-vuln-ms17-010,smb-enum-shares,smb-enum-users,smb-security-mode,rdp-vuln-ms12-020,ftp-anon,http-enum,smb-vuln-ms08-067,smb-enum-domains,smb-enum-sessions -A -sV {IP} -oN output/{FILE_SAVE}'
    process_x2 = subprocess.Popen(command_x2, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout2, stderr2 = process_x2.communicate()

    if process_x2.returncode != 0:
        print(f'Error running nmap: {stderr2.decode("utf-8")}')
        input('Press Enter to continue...')

    view_or_no = input(f'{grwh_prompt}Output Files scan-results saved: output/{FILE_SAVE}\n'
                       f'{grwh_prompt}View output scan result? (y/n): ').lower()
    view_result_file(view_or_no, FILE_SAVE)


def view_result_file(answer ,FILE):
    if answer == 'y':
        with open(f'output/{FILE}', 'r') as f:
            print(f.read())
        input(f'{grwh_prompt} Enter to continue. . .')
    else:
        print(f'{grwh_prompt} OK!')


def clear():
    os.system('clear')


def main_scan():
    while True:
        try:
            clear()
            banner_scan()
            shell = input(f'''{white}
{green}┌─[{red}ScanLan{green}]──[{red}~{green}]─[{orange}0x200{green}]{green}:
└─────►{orange} ''')

            while not shell in ['1', '2', '3', '4', '5']:
                print(f'{white}[{red}!{white}]{white} Invalid option!')
                shell = input(f'''{white}
{green}┌─[{red}ScanLan{green}]──[{red}~{green}]─[{orange}0x200{green}]{green}:
└─────►{orange} ''')

            else:
                if shell == '1':
                    clear()
                    computer_banner()
                    lan = input(f'{green}[{white}+{green}]{white} Enter IP to scan: ')
                    scan_nmap(lan)

                elif shell == '2':
                    clear()
                    eagle()
                    ip_range = input(f'{green}[{white}+{green}]{white} Enter IP-RANGE to scan: ')
                    scan_range(ip_range)

                elif shell == '3':
                    clear()
                    computer_banner()
                    result_file = input(f'{green}[{white}+{green}]{white} Enter result file name(ex. scan): ')
                    ip_scan = input(f'{green}[{white}+{green}]{white} Enter IP to full scanning: ')
                    full_scan(ip_scan, result_file)

                elif shell == '4':
                    clear()
                    evil_corp()
                    ip_scan_smb = input(f'{green}[{white}+{green}]{white} Enter IP to check smb-vulns and more: ')
                    file_save = input(f'{green}[{white}+{green}]{white} Enter name-file to save results-scan: ')
                    scan_vulns_windows(ip_scan_smb, file_save)

                elif shell == '5':
                    break

        except KeyboardInterrupt:
            print(f'\n{white}[{red}!{white}]{green} Ctrl+C Detected. Exiting...')
            sys.exit(0)

