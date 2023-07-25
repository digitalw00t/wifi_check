#!/usr/bin/env python3

import os
import time
import subprocess
import argparse

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

def main():
    parser = argparse.ArgumentParser(description="Check WiFi status and optionally force restart.")
    parser.add_argument("--force", action="store_true", help="Force restart wlan0")
    args = parser.parse_args()

    default_gateway = get_default_gateway()
    if default_gateway is None:
        print("Unable to determine the default gateway.")
        return

    if args.force:
        restart_wlan0()
        print("wlan0 restarted.")
        return

    while True:
        if not check_ping(default_gateway):
            print("Default gateway is unreachable.")
            restart_wlan0()
            print("wlan0 restarted.")
        time.sleep(15)


if __name__ == "__main__":
    main()

