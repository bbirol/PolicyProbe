import requests
from colorama import Fore, Style
from tabulate import tabulate
import time
import os  

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def header_hunter(url):
    try:
        clear_screen()
        print(Fore.CYAN + "\n[+] Starting HTTP Headers Analysis for: " + url + Style.RESET_ALL)

        time.sleep(1)

        response = requests.get(url, timeout=10)
        headers = response.headers

        for key, value in headers.items():
            print(Fore.GREEN + f"{key}: {value}")
            time.sleep(0.5)

        print(Fore.GREEN + "\n[+] Security Headers Analysis:\n" + Style.RESET_ALL)

        required_headers = {
            "Strict-Transport-Security": 2.0,
            "Content-Security-Policy": 3.0,
            "X-Frame-Options": 1.5,
            "X-Content-Type-Options": 1.0,
            "Referrer-Policy": 1.0,
            "Permissions-Policy": 1.5
        }

        table_data = []
        total_weight = sum(required_headers.values())
        gained_weight = 0

        for header, weight in required_headers.items():
            print(Fore.GREEN + f"Checking: {header}...")
            time.sleep(0.5)
            if header in headers:
                status = f"{Fore.GREEN}✓ Present{Style.RESET_ALL}"
                gained_weight += weight
            else:
                status = f"{Fore.RED}✗ Missing{Style.RESET_ALL}"
            table_data.append([header, weight, status])

        clear_screen()

        print(Fore.CYAN + "\n[+] Results for: " + url + Style.RESET_ALL)
        print("\n" + tabulate(table_data, headers=["Header", "Weight", "Status"], tablefmt="grid"))

        protection_score = (gained_weight / total_weight) * 10

        print(Fore.BLUE + "\n[+] Risk Assessment:" + Style.RESET_ALL)
        print(Fore.GREEN + f"→ Weighted Protection Score: {protection_score:.2f}/10" + Style.RESET_ALL)

        if protection_score == 10:
            print(Fore.GREEN + "[✔] Excellent: All critical headers are present!" + Style.RESET_ALL)
        elif protection_score >= 7:
            print(Fore.CYAN + "[~] Good: Minor issues found." + Style.RESET_ALL)
        elif protection_score >= 4:
            print(Fore.MAGENTA + "[!] Warning: Some important headers are missing." + Style.RESET_ALL)
        else:
            print(Fore.RED + "[X] High Risk: Most important headers are missing!" + Style.RESET_ALL)

        repeat = input(Fore.GREEN + "\nDo you want to scan another URL? (y/n): " + Style.RESET_ALL).lower()
        if repeat == 'y':
            new_url = input("Enter a new URL (with https://): ")
            header_hunter(new_url)
        else:
            print(Fore.GREEN + "\n[✔] Exiting the tool. Goodbye!" + Style.RESET_ALL)
            time.sleep(1.5)

    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"[!] Error: {e}" + Style.RESET_ALL)
        retry = input(Fore.YELLOW + "\nDo you want to try a different URL? (y/n): " + Style.RESET_ALL).lower()
        if retry == 'y':
            clear_screen()
            new_url = input("Enter a valid URL (with https://): ")
            header_hunter(new_url)
        else:
            print(Fore.GREEN + "\n[✔] Exiting the tool. Goodbye!" + Style.RESET_ALL)

if __name__ == "__main__":
    try:
        print(Fore.CYAN +
            r"""
 ____       _ _            ____            _          
|  _ \ ___ | (_) ___ _   _|  _ \ _ __ ___ | |__   ___ 
| |_) / _ \| | |/ __| | | | |_) | '__/ _ \| '_ \ / _ \
|  __/ (_) | | | (__| |_| |  __/| | | (_) | |_) |  __/
|_|   \___/|_|_|\___|\__, |_|   |_|  \___/|_.__/ \___|
                     |___/                            
"""
        )
        url = input("Enter a URL (with https://): ")
        url = url.lower()
        header_hunter(url)
    except KeyboardInterrupt:
        print(Fore.RED + "\n[!] Interrupted by user. Exiting..." + Style.RESET_ALL)
