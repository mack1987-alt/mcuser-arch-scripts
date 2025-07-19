#!/bin/bash

set -euo pipefail  # Exit on errors, unset variables, and pipe failures for robustness

# Colors for better output readability
RED='\e[31m'
GREEN='\e[32m'
BLUE='\e[34m'
RESET='\e[0m'

# Set terminal title (optional; enhances user experience in terminal tabs)
echo -ne "\033]0;AUR Tool\007"

# Usage function for --help
usage() {
    echo -e "${BLUE}Usage:${RESET} $0 [options] [package_name]"
    echo -e "Install or update an AUR package using yay."
    echo -e ""
    echo -e "${BLUE}Options:${RESET}"
    echo -e "  -h, --help    Show this help message and exit"
    echo -e ""
    echo -e "${BLUE}If no package_name is provided, you'll be prompted for one.${RESET}"
    exit 0
}

# Check if yay is installed
check_yay_installed() {
    if ! command -v yay >/dev/null 2>&1; then
        echo -e "${RED}Error: yay is not installed. Please install yay first (e.g., manually from AUR).${RESET}"
        exit 1
    fi
}

# Check if the package exists in AUR (using yay -Si for info query)
package_exists() {
    local pkg="$1"
    if ! yay -Si "$pkg" >/dev/null 2>&1; then
        echo -e "${RED}Error: Package '$pkg' not found in AUR. Check spelling or AUR availability.${RESET}"
        exit 1
    fi
}

# Function to install the package
install_package() {
    local pkg="$1"
    echo -e "${BLUE}Installing '$pkg' from AUR...${RESET}"
    # Use yay -S for full automation: handles deps, build, install. Prompts for PKGBUILD review by default for safety.
    if yay -S "$pkg"; then  # Removed --noconfirm to allow user review; add if non-interactive needed
        echo -e "${GREEN}Installation of '$pkg' complete.${RESET}"
    else
        echo -e "${RED}Error: Failed to install '$pkg'.${RESET}"
        exit 1
    fi
}

# Function to update the package
update_package() {
    local pkg="$1"
    echo -e "${BLUE}Updating '$pkg'...${RESET}"
    # Use --needed to skip if up-to-date; avoids full system upgrade (-Syu)
    if yay -S --needed "$pkg"; then
        echo -e "${GREEN}Package '$pkg' has been updated (or was already up-to-date).${RESET}"
    else
        echo -e "${RED}Error: Failed to update '$pkg'.${RESET}"
        exit 1
    fi
}

# Parse options
while [[ $# -gt 0 ]]; do
    case "$1" in
        -h|--help)
            usage
            ;;
        *)
            aur_package="$1"
            shift
            ;;
    esac
done

# Main logic starts here
check_yay_installed

# Prompt for package if not provided via argument
if [[ -z "${aur_package:-}" ]]; then
    read -rp "Enter the name of the AUR package: " aur_package
fi

if [[ -z "$aur_package" ]]; then
    echo -e "${RED}Error: Package name cannot be empty.${RESET}"
    exit 1
fi

# Verify package exists in AUR before proceeding
package_exists "$aur_package"

# Check if package is already installed
if yay -Qi "$aur_package" >/dev/null 2>&1; then
    read -rp "Package '$aur_package' already installed. Update it? (y/n): " update_choice
    if [[ "$update_choice" =~ ^[Yy]$ ]]; then
        update_package "$aur_package"
    else
        echo -e "${BLUE}Skipping update for '$aur_package'.${RESET}"
    fi
else
    install_package "$aur_package"
fi

read -rp "Press Enter to close..."