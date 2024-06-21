AUR Tool Script

This script automates the process of checking, updating, and installing packages from the Arch User Repository (AUR) using yay.
Features

    Sets the terminal title to "AUR tool".
    Checks if yay (Yet Another Yaourt) is installed; prompts to install if not.
    Clones the specified AUR package from https://aur.archlinux.org.
    Updates an existing AUR package if prompted.
    Installs dependencies and builds the AUR package using makepkg.
    Cleans up by removing the cloned package directory after installation or update.

Prerequisites

Before running this script, ensure you have the following prerequisites installed:

    yay: AUR helper tool for Arch Linux.

Installation on Arch Linux

bash

# Install yay
sudo pacman -S yay

Usage

    Open a terminal.

    Navigate to the directory where the script (aur_tool.sh) is located.

    Make the script executable if it isn't already:

    bash

chmod +x aur_tool.sh

Run the script:

bash

    ./aur_tool.sh

    Follow the prompts in the script:
        Enter the name of the AUR package you want to install/update.
        Choose whether to update an existing package if prompted.
        Confirm installation of dependencies and package build.

    After installation or update, press Enter to close the terminal window.

Example

Here's an example of how the script interacts with the user:

bash

$ ./aur_tool.sh
AUR tool

Enter the name of the AUR package: some-package
Cloning 'some-package' from AUR...
Building and installing 'some-package'...
:: Checking for conflicts...
:: Checking for inner conflicts...
[...]
(1/1) checking keys in keyring                     [######################] 100%
(1/1) checking package integrity                   [######################] 100%
(1/1) loading package files                        [######################] 100%
(1/1) checking for file conflicts                  [######################] 100%
(1/1) checking available disk space                [######################] 100%
:: Processing package changes...
[...]
==> Finished making: some-package 1.0-1 (Fri Jun 21 20:09:36 UTC 2024)
Installation of 'some-package' from AUR is complete.
Press Enter to close...

Script Contents

Here is the content of the aur_tool.sh script:

bash

#!/bin/bash

set -e  # Exit on any command failure

# Set terminal title
echo -ne "\033]0;AUR tool\007"

# Check if yay is installed
if ! command -v yay >/dev/null 2>&1; then
  echo "Error: yay is not installed. Please install yay before running this script."
  exit 1
fi

read -rp "Enter the name of the AUR package: " aur_package

if [[ -z $aur_package ]]; then
  echo "Error: Package name cannot be empty."
  exit 1
fi

# Function to perform cleanup
cleanup() {
  cd ..
  rm -rf "$aur_package"
}

# Check if package exists in AUR
if yay -Qi "$aur_package" >/dev/null 2>&1; then
  read -rp "Package '$aur_package' already exists. Do you want to update it? (y/n): " update_choice
  if [[ $update_choice =~ ^[Yy]$ ]]; then
    echo "Updating '$aur_package'..."
    yay -Syu "$aur_package" --needed --noconfirm
    echo "Package '$aur_package' has been updated."
    cleanup
  else
    echo "Skipping update for '$aur_package'."
    cleanup
  fi
else
  echo "Cloning '$aur_package' from AUR..."
  if ! git clone "https://aur.archlinux.org/$aur_package.git"; then
    echo "Error: Failed to clone '$aur_package' from AUR."
    exit 1
  fi

  cd "$aur_package"
  
  # Check if package has dependencies
  if [[ -f PKGBUILD ]]; then
    checkdepends=($(awk -F '=' '/^checkdepends/ {print $2}' PKGBUILD))
    if [[ ${#checkdepends[@]} -gt 0 ]]; then
      echo "Installing dependencies for '$aur_package'..."
      yay -S --needed --noconfirm "${checkdepends[@]}"
    fi
  fi
  
  echo "Building and installing '$aur_package'..."
  if ! makepkg -si; then
    echo "Error: Failed to build and install '$aur_package'."
    cleanup
    read -rp "Press Enter to close..."
  fi

  echo "Installation of '$aur_package' from AUR is complete."
  cleanup
fi

read -rp "Press Enter to close..."

Contributing

Contributions are welcome! Fork the repository and submit a pull request with your enhancements.
License

This project is licensed under the MIT License. See the LICENSE file for more details.
