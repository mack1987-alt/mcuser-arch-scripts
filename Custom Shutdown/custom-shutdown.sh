#!/bin/bash

# Prompt the user if they want to shut down
echo "Shutting down..."
read -p "Are you sure you want to shutdown? (yes/no): " answer

# Check the user's response
if [[ $answer == "yes" ]]; then
    # Define the directory where the update-system.sh script is located
    SCRIPT_DIR="/path/to/your/scripts"
    
    # Run the update-system.sh script
    "$SCRIPT_DIR/update-system.sh"
    
    # Pause for 1 second
    sleep 1
    
    # Reboot the system
    shutdown -h now
elif [[ $answer == "no" ]]; then
    # If the answer is no, inform the user and exit
    echo "Shutdown canceled. Exiting..."
    exit 0
else
    # If the answer is neither yes nor no, inform the user and exit with an error
    echo "Invalid response. Please enter 'yes' or 'no'. Exiting..."
    exit 1
fi
