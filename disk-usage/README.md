Disk Usage Script

This script displays disk usage information using ncdu in a terminal window and sets the window's position and size for optimal viewing.
Description

The Disk Usage Script sets the terminal title to "Disk Usage", clears the screen, and launches ncdu to analyze disk usage starting from the root directory (/). After the analysis, it prompts the user to press Enter to close the terminal window.
Features

    Sets the terminal title to "Disk Usage".
    Clears the terminal screen for clean output.
    Positions the terminal window at coordinates (0, 80) with a size of 650x200 pixels using wmctrl.
    Uses ncdu to provide a detailed and interactive disk usage analysis.

Prerequisites

Before running the script, ensure you have the following installed:

    wmctrl: Window Manager Control tool to manipulate window properties.
    ncdu: Disk usage analyzer with an ncurses interface.

Installation on Ubuntu/Debian

bash

sudo apt-get update
sudo apt-get install wmctrl ncdu

Installation on Arch Linux

bash

sudo pacman -S wmctrl ncdu

Usage

    Open a terminal.

    Navigate to the directory where the script (disk_usage.sh) is located.

    Make the script executable if it isn't already:

    bash

chmod +x disk_usage.sh

Run the script:

bash

    ./disk_usage.sh

    Enter your password when prompted by sudo to allow ncdu to analyze disk usage.

    After ncdu completes its analysis, press Enter to close the terminal window.

Example Output

After running the script (./disk_usage.sh), you will see:

mathematica

Disk usage analysis....

The ncdu tool will display interactive disk usage information starting from the root directory (/). Use the arrow keys and Enter key to navigate and interact with the ncdu interface.
Script Contents

Here is the content of the disk_usage.sh script:

bash

#!/bin/bash

# Set terminal title
echo -ne "\033]0;Disk Usage\007"

clear
echo "Disk usage analysis...."

# Set terminal geometry
wmctrl -r :ACTIVE: -e 0,0,80,650,200

# Run ncdu in the terminal
sudo ncdu /

read -rp "Press Enter to close..."

Contributing

Contributions are welcome! Fork the repository and submit a pull request with your enhancements.
License

This project is licensed under the MIT License. See the LICENSE file for more details.
