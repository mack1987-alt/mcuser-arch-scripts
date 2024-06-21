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