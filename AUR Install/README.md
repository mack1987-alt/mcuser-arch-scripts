AUR Package Installer

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg) 
![Bash](https://img.shields.io/badge/Bash-Script-blue)


A simple, robust Bash script to install or update packages from the Arch User Repository (AUR) using yay. This tool streamlines AUR package management on Arch Linux systems, automating cloning, dependency resolution, building, and installation—saving users hours of manual setup and troubleshooting during system configuration or software updates.

Problem Solved
Arch Linux's AUR is a treasure trove of community-maintained packages not available in official repositories, but managing them manually can be tedious: cloning repos, resolving dependencies, building with makepkg, and handling updates. 

This script automates the process using yay, reducing errors, ensuring safe installations (with PKGBUILD reviews), and making it beginner-friendly. 
For example:

        ◦ Saves Time on Setups: Automates package management to save hours on fresh Arch installs or maintaining 		custom software.
        ◦ Reduces Errors: Handles edge cases like missing packages, existing installations, and dependency checks 		automatically.
        ◦ Enhances Safety: Leverages yay's built-in prompts for reviewing untrusted PKGBUILD files, preventing 			potential security issues.

Ideal for developers, sysadmins, or Arch enthusiasts who frequently deal with AUR packages like custom themes, drivers, or niche tools (e.g., visual-studio-code-bin or spotify).

Features
        ◦ Checks if yay is installed and prompts if not.
        ◦ Supports command-line arguments for package names (e.g., ./aur-installer.sh package-name).
        ◦ Verifies if the package exists in AUR before proceeding.
        ◦ Handles updates for already-installed packages with user confirmation.
        ◦ Color-coded output for better readability (errors in red, success in green).
        ◦ Help menu with --help flag.
        ◦ No manual cleanup needed—yay manages build artifacts.

Installation
Prerequisites:
        ◦ Arch Linux or an Arch-based distro (e.g., Manjaro).
        ◦ Git for cloning (usually pre-installed).
        ◦ yay installed. If not, install it manually:
		sudo pacman -S --needed git base-devel
		git clone https://aur.archlinux.org/yay.git
		cd yay
		makepkg -si
		cd ..
		rm -rf yay
Clone the Repository:
	git clone https://github.com/mack1987-alt/mcuser-arch-scripts.git
	cd mcuser-arch-scripts/'AUR Install'
    • Make the Script Executable:
	chmod +x aur-package-installer.sh

Usage
Run the script with:
./aur-installer.sh [package_name]

If no package name is provided, it will prompt you.
    • Use -h or --help for usage instructions.
The script will:
    • Check if the package is already installed.
    • Prompt to update if installed, or install if not.
    • Use yay to handle the process securely.
Options
    • -h, --help: Display help message.

Installing a New Package (Prompt Mode)

./aur-installer.sh

Enter package name when prompted (e.g., visual-studio-code-bin).
    • Output:
	Enter the name of the AUR package: visual-studio-code-bin
	Installing 'visual-studio-code-bin' from AUR...
	[yay output here, including PKGBUILD review prompt]
	Installation of 'visual-studio-code-bin' complete.
	Press Enter to close...

Installing via Argument
./aur-installer.sh spotify

Automatically installs spotify if not present, or prompts to update.

Updating an Existing PackageIf the package is installed:
Package 'spotify' already installed. Update it? (y/n): y
Updating 'spotify'...
[Success message]

Help Menu
./aur-installer.sh --help

Output:
Usage: ./aur-installer.sh [options] [package_name]
Install or update an AUR package using yay.

Options:
  -h, --help    Show this help message and exit

If no package_name is provided, you'll be prompted for one.

Contributing
Contributions welcome! Fork the repo, make changes, and submit a pull request. Suggestions:
    • Add support for multiple packages.
    • Integrate with other AUR helpers like paru.
    • Follow Bash best practices (lint with shellcheck).


License:
This project is licensed under the MIT License - see the LICENSE file for details.

