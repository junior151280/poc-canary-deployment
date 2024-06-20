import requests as rq
import time
import sys
from colorama import Fore, Back, Style

# parameters
IP = sys.argv[1]
web_link = "http://" + str(IP)

HEADERS = {}
READTIMEOUT_COUNT = 0
CONNECTTIMEOUT_COUNT = 0
HTTPERROR_COUNT = 0
UNKNOWNERROR_COUNT = 0

if len(sys.argv) == 3:
    HEADER_HOST = sys.argv[2]
    HEADERS['Host'] = HEADER_HOST

def print_green_on_default(text): return print(Fore.GREEN + text)
def print_blue_on_default(text): return print(Fore.BLUE + text)
def print_red_on_default(text): return print(Fore.RED + text)
def print_yellow_on_default(text): return print(Fore.YELLOW + text)

def main():
    global HEADERS
    global READTIMEOUT_COUNT
    global CONNECTTIMEOUT_COUNT
    global HTTPERROR_COUNT
    global UNKNOWNERROR_COUNT

    while True:
        try:
            if not HEADERS:
                response = rq.get(web_link, verify=False, timeout=(1, 1))
            else:
                response = rq.get(web_link, verify=False, timeout=(1, 1), headers=HEADERS)

            if response.status_code == 200:
                result = response.text
                if "<title>Welcome to Azure Kubernetes Service (AKS) Version 2.0</title>" in result:
                    print_blue_on_default("Welcome to Azure Kubernetes Service (AKS) Version 2.0")
                elif "<title>Welcome to Azure Kubernetes Service (AKS)</title>" in result:
                    print_green_on_default("Welcome to Azure Kubernetes Service (AKS)")
            else:
                HTTPERROR_COUNT += 1
                print_red_on_default(f"Error: Status code is {response.status_code} - count: {HTTPERROR_COUNT}")

        except rq.exceptions.ConnectTimeout:
            CONNECTTIMEOUT_COUNT += 1
            print_red_on_default(f"Error: Connect Timeout - count: {CONNECTTIMEOUT_COUNT}")

        except rq.exceptions.ReadTimeout:
            READTIMEOUT_COUNT += 1
            print_red_on_default(f"Error: Read Timeout - count: {READTIMEOUT_COUNT}")

        except rq.exceptions.RequestException as e:
            UNKNOWNERROR_COUNT += 1
            print_red_on_default(f"Error: {e} - count: {UNKNOWNERROR_COUNT}")

        time.sleep(0.1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("")
        print_yellow_on_default("The Amount of Read Timeout: " + str(READTIMEOUT_COUNT))
        print_yellow_on_default("The Amount of Connect Timeout: " + str(CONNECTTIMEOUT_COUNT))
        print_yellow_on_default("The Amount of HTTP Error: " + str(HTTPERROR_COUNT))
        print_yellow_on_default("The Amount of Unknown Error: " + str(UNKNOWNERROR_COUNT))