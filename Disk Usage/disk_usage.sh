#!/bin/bash

# Set terminal title
echo -ne "\033]0;Disk Usage\007"

clear
echo "Device disk usage...."

# Set terminal geometry
wmctrl -r :ACTIVE: -e 0,0,80,650,200

# Run ncdu in the terminal
sudo ncdu /

read -rp "Press Enter to close..."
