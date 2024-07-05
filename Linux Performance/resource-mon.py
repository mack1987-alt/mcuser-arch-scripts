import psutil
import time

def log_system_resources(interval=60, log_file='/path/to/file/system_resources.log'):
    with open(log_file, 'a') as f:
        while True:
            cpu_usage = psutil.cpu_percent(interval=1)
            memory_info = psutil.virtual_memory()
            disk_info = psutil.disk_usage('/')
            log_entry = f"{time.ctime()}: CPU: {cpu_usage}%, Memory: {memory_info.percent}%, Disk: {disk_info.percent}%\n"
            f.write(log_entry)
            time.sleep(interval - 1)

if __name__ == "__main__":
    log_system_resources()