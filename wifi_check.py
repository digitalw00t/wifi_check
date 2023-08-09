#!/usr/bin/env python3
# program: wifi_check.py
# purpose: 

import os
import time
import subprocess
import argparse
from datetime import datetime

__VERSION__ = "v1.2.0"

def restart_wlan0():
    subprocess.run(["nmcli", "radio", "wifi", "off"])
    time.sleep(2)
    subprocess.run(["nmcli", "radio", "wifi", "on"])

def get_default_gateway():
    with os.popen("ip route") as routes:
        for route in routes:
            if "default via" in route:
                default_gateway = route.split()[2]
                return default_gateway

def check_ping(default_gateway):
    response = os.system(f"ping -c 1 -W 3 {default_gateway} > /dev/null 2>&1")
    return response == 0

def print_message(message):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{current_time}] {message}")

def main():
    parser = argparse.ArgumentParser(description="Check WiFi status and optionally force restart.")
    parser.add_argument("--version", action="version", version=f"%(prog)s {__VERSION__}") # Added line for --version

    args = parser.parse_args()

    default_gateway = get_default_gateway()
    if default_gateway is None:
        print_message("Unable to determine the default gateway.")
        return

    if args.force:
        print_message("Forcing restart of wlan0...")
        restart_wlan0()
        print_message("wlan0 restarted.")
        return

    while True:
        if not check_ping(default_gateway):
            print_message("Default gateway is unreachable. Restarting wlan0...")
            restart_wlan0()
            print_message("wlan0 restarted.")
        time.sleep(15)


if __name__ == "__main__":
    main()

