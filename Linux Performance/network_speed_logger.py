import subprocess
import time
import os

def log_network_speed(log_file='/path/to/file/network_speed.log'):
    os.makedirs(os.path.dirname(log_file), exist_ok=True)  # Ensure the directory exists
    with open(log_file, 'a') as f:
        while True:
            try:
                # Use the full path to the speedtest-cli command
                result = subprocess.run(['/location/of/.local/bin/speedtest-cli', '--simple'], stdout=subprocess.PIPE, text=True, check=True)
                log_entry = f"{time.ctime()}:\n{result.stdout}\n"
                f.write(log_entry)
                print(log_entry.strip())  # Print to console for real-time monitoring
            except subprocess.CalledProcessError as e:
                error_message = f"{time.ctime()}: An error occurred while running speedtest-cli: {e}\n"
                f.write(error_message)
                print(error_message.strip())  # Print to console for real-time monitoring
            except FileNotFoundError as e:
                error_message = f"{time.ctime()}: speedtest-cli not found: {e}\n"
                f.write(error_message)
                print(error_message.strip())  # Print to console for real-time monitoring
                break  # Exit the loop if speedtest-cli is not found
            time.sleep(3600)  # Log every hour

if __name__ == "__main__":
    log_network_speed()