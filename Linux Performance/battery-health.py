# Version 1.1
import psutil
import time
import os

def log_battery_status(log_file='/path/to/file/battery_status.log'):
    os.makedirs(os.path.dirname(log_file), exist_ok=True)  # Ensure the directory exists
    with open(log_file, 'a') as f:
        while True:
            battery = psutil.sensors_battery()
            if battery is not None:
                log_entry = f"{time.ctime()}: Battery: {battery.percent}%, Plugged in: {battery.power_plugged}\n"
                f.write(log_entry)
                print(log_entry.strip())  # Print to console for real-time monitoring
            else:
                log_entry = f"{time.ctime()}: No battery information available.\n"
                f.write(log_entry)
                print(log_entry.strip())  # Print to console for real-time monitoring
            time.sleep(300)  # Log every 5 minutes

if __name__ == "__main__":
    log_battery_status()
