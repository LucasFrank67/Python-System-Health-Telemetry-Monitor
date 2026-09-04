import time
import psutil
import os
from datetime import datetime
import win32pdh


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def active_time():
    query = win32pdh.OpenQuery()
    counter_path = r"\PhysicalDisk(_Total)\% Disk Time"
    handle = win32pdh.AddCounter(query, counter_path)
    win32pdh.CollectQueryData(query)
    time.sleep(1)
    win32pdh.CollectQueryData(query)

    values = win32pdh.GetFormattedCounterValue(
        handle,
        win32pdh.PDH_FMT_DOUBLE
    )
    disk_active = values[1]
    return disk_active


def main():
    clear_console()
    while True:
        disk_active = active_time()
        current_time = datetime.now()
        boot_timer = psutil.boot_time()
        dateboot = datetime.fromtimestamp(boot_timer)
        boot_time = current_time - dateboot
        days = boot_time.days
        hours, remainder = divmod(boot_time.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        ram = psutil.virtual_memory()
        print("\033[H", end="")
        print(f"Current CPU usage: {psutil.cpu_percent()}%\n", end="", flush=True)
        print(f"Current RAM usage: {ram.percent}%\n", end="", flush=True)
        print(f"Current Disk usage: {disk_active:.1f}%\n", end="", flush=True)
        print(f"System Uptime: {days} days, {hours} hours, {minutes} minutes, and {seconds} seconds.\n", end="", flush=True)
if __name__ == "__main__":
    main()