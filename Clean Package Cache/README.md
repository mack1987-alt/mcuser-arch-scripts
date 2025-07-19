Arch Cache Cleaner
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Bash](https://img.shields.io/badge/Bash-Script-blue)

A Bash script to clean package caches on Arch Linux systems, including pacman, yay (AUR), and optional home ~/.cache/. This tool helps reclaim disk space by safely removing unnecessary cache files, with options for selective cleaning, dry-runs, and detailed reporting—making maintenance efficient and user-friendly.

Problem Solved
Arch Linux users often accumulate large caches from package managers like pacman and AUR helpers (e.g., yay), leading to wasted disk space (e.g., gigabytes in /var/cache/pacman/pkg/ or ~/.cache/yay/). Manual cleaning can be error-prone or incomplete. This script automates the process intelligently:

Frees Space Efficiently: Removes old package versions while keeping recent ones (e.g., last 3 via paccache), cleans uninstalled packages, and handles AUR build artifacts.

Reduces Risks: Dry-run previews actions/sizes, warnings for aggressive cleans, and fallbacks if tools are missing.

Saves Time: One command for multiple caches, with logging and notifications for quick audits—ideal for routine maintenance on low-storage setups like laptops or servers.

Perfect for Arch enthusiasts, developers, or anyone optimizing their system without third-party GUIs.

Features
Selective cleaning: Target pacman, yay, home cache, or all.
Dry-run mode: Preview cache sizes and actions without deleting.
Size reporting: Shows before/after sizes and freed space.
Interactive mode: Prompts for choices if no options provided.
Color-coded output: Errors in red, success in green for clarity.
Logging: Tracks operations in ~/.cache_cleaner.log.
Desktop notifications: Via notify-send (if available) for feedback.
Quiet mode: Suppresses output, relies on log/notifications.
Safe defaults: Uses paccache for pacman (keeps 3 versions), falls back to pacman -Sc.

Installation
Prerequisites:

Arch Linux or Arch-based distro.

For pacman cleaning: pacman (built-in); optionally paccache from pacman-contrib for advanced features (sudo pacman -S pacman-contrib).

For yay cleaning: yay installed.

For notifications: libnotify (for notify-send).
numfmt (from coreutils) for human-readable sizes (usually pre-installed).

Clone the Repository:
git clone https://github.com/mack1987-alt/mcuser-arch-scripts.git
cd mcuser-arch-scripts/'Clean Package Cache'

Make the Script Executable:
chmod +x clean-package-cache.sh

Options:
-p, --pacman: Clean pacman cache.
-y, --yay: Clean yay/AUR cache.
-H, --home: Clean ~/.cache/* (aggressive, with confirmation).
-a, --all: Clean all caches.
-d, --dry-run: Preview without cleaning.
-q, --quiet: Suppress output (use log/notifications).
-h, --help: Show help.

Clean All with Dry-Run
./cache-cleaner.sh -a -d

Targeted Clean (Pacman Only, Quiet)
./cache-cleaner.sh -p -q

Help Menu
./cache-cleaner.sh --help

License
This project is licensed under the MIT License - see the LICENSE file for details.


