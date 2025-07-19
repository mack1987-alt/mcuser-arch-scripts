#!/bin/bash

set -euo pipefail  # Exit on errors, unset variables, and pipe failures for robustness

# Colors for better output readability
RED='\e[31m'
GREEN='\e[32m'
BLUE='\e[34m'
RESET='\e[0m'

# Log file for tracking operations
LOG_FILE="$HOME/.aur_install.log"

# Set terminal title (optional; enhances user experience in terminal tabs)
echo -ne "\033]0;AUR Tool\007"

# Usage function for --help
usage() {
    echo -e "${BLUE}Usage:${RESET} $0 [options] [package_name ...]"
    echo -e "Install or update AUR packages using yay. Supports multiple packages."
    echo -e ""
    echo -e "${BLUE}Options:${RESET}"
    echo -e "  -h, --help    Show this help message and exit"
    echo -e "  -s, --search  Search AUR for a query and select a package to install"
    echo -e "  -q, --quiet   Suppress output and use notifications (if available)"
    echo -e ""
    echo -e "${BLUE}If no package_name is provided, you'll be prompted. Use commas for multiple in prompt mode.${RESET}"
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
    echo -e "${BLUE}Installing '$pkg' from AUR...${RESET}" | tee -a "$LOG_FILE"
    # Use yay -S for full automation: handles deps, build, install. Prompts for PKGBUILD review by default for safety.
    if yay -S "$pkg"; then  # Removed --noconfirm to allow user review; add if non-interactive needed
        echo -e "${GREEN}Installation of '$pkg' complete.${RESET}" | tee -a "$LOG_FILE"
        notify "Installation of $pkg complete!"
    else
        echo -e "${RED}Error: Failed to install '$pkg'.${RESET}" | tee -a "$LOG_FILE"
        notify "Error: Failed to install $pkg" --urgency=critical
        exit 1
    fi
}

# Function to update the package
update_package() {
    local pkg="$1"
    echo -e "${BLUE}Fetching diff for '$pkg' update...${RESET}" | tee -a "$LOG_FILE"
    temp_dir="/tmp/aur_diff_$pkg"
    mkdir -p "$temp_dir"
    git clone "https://aur.archlinux.org/$pkg.git" "$temp_dir" >/dev/null 2>&1 || true
    if [[ -f "$temp_dir/PKGBUILD" ]]; then
        # Attempt to get current PKGBUILD; fallback if not available
        current_pkgbuild=$(yay -Gp "$pkg" 2>/dev/null)
        if [[ -n "$current_pkgbuild" ]]; then
            echo "$current_pkgbuild" > "$temp_dir/old_PKGBUILD"
            diff -u --color=always "$temp_dir/old_PKGBUILD" "$temp_dir/PKGBUILD" || true
            read -rp "Proceed with update after diff? (y/n): " diff_choice
            if [[ ! "$diff_choice" =~ ^[Yy]$ ]]; then
                echo -e "${BLUE}Aborting update for '$pkg'.${RESET}" | tee -a "$LOG_FILE"
                rm -rf "$temp_dir"
                return
            fi
        else
            echo -e "${BLUE}No current PKGBUILD found for diff; proceeding without.${RESET}"
        fi
    else
        echo -e "${RED}Failed to fetch new PKGBUILD for diff.${RESET}" | tee -a "$LOG_FILE"
    fi
    rm -rf "$temp_dir"

    echo -e "${BLUE}Updating '$pkg'...${RESET}" | tee -a "$LOG_FILE"
    # Use --needed to skip if up-to-date; avoids full system upgrade (-Syu)
    if yay -S --needed "$pkg"; then
        echo -e "${GREEN}Package '$pkg' has been updated (or was already up-to-date).${RESET}" | tee -a "$LOG_FILE"
        notify "Update of $pkg complete!"
    else
        echo -e "${RED}Error: Failed to update '$pkg'.${RESET}" | tee -a "$LOG_FILE"
        notify "Error: Failed to update $pkg" --urgency=critical
        exit 1
    fi
}

# Function for notifications (if notify-send is available)
notify() {
    local message="$1"
    local urgency="${2:-normal}"
    if command -v notify-send >/dev/null 2>&1; then
        notify-send "AUR Tool" "$message" --urgency="$urgency" --icon=package
    fi
}

# Function for AUR search
search_aur() {
    local query="$1"
    echo -e "${BLUE}Searching AUR for '$query'...${RESET}"
    results=$(yay -Ss "$query" | head -n 20)  # Limit to top 20
    echo "$results"
    read -rp "Enter package to install (or blank to skip): " selected
    if [[ -n "$selected" ]]; then
        aur_packages=("$selected")
    else
        echo -e "${BLUE}No package selected; exiting.${RESET}"
        exit 0
    fi
}

# Parse options
aur_packages=()  # Array for multiple packages
search_mode=false
search_query=""
quiet=false
while [[ $# -gt 0 ]]; do
    case "$1" in
        -h|--help)
            usage
            ;;
        -s|--search)
            search_mode=true
            search_query="$2"
            shift 2
            ;;
        -q|--quiet)
            quiet=true
            shift
            ;;
        *)
            aur_packages+=("$1")
            shift
            ;;
    esac
done

# Redirect output if quiet mode
if [[ "$quiet" = true ]]; then
    exec > >(tee -a "$LOG_FILE") 2>&1
fi

# Main logic starts here
check_yay_installed

# Handle search mode
if [[ "$search_mode" = true ]]; then
    search_aur "$search_query"
fi

# Prompt for packages if none provided
if [[ ${#aur_packages[@]} -eq 0 ]]; then
    read -rp "Enter AUR package names (comma-separated): " input
    IFS=',' read -ra aur_packages <<< "$input"
fi

if [[ ${#aur_packages[@]} -eq 0 ]]; then
    echo -e "${RED}Error: No package names provided.${RESET}" | tee -a "$LOG_FILE"
    exit 1
fi

# Log start
echo "$(date): Starting operation for packages: ${aur_packages[*]}" >> "$LOG_FILE"

# Process each package
for aur_package in "${aur_packages[@]}"; do
    aur_package="${aur_package// /}"  # Trim spaces
    if [[ -z "$aur_package" ]]; then continue; fi

    package_exists "$aur_package"

    if yay -Qi "$aur_package" >/dev/null 2>&1; then
        read -rp "Package '$aur_package' installed. Update? (y/n): " update_choice
        if [[ "$update_choice" =~ ^[Yy]$ ]]; then
            update_package "$aur_package"
        else
            echo -e "${BLUE}Skipping '$aur_package'.${RESET}" | tee -a "$LOG_FILE"
        fi
    else
        install_package "$aur_package"
    fi
done

read -rp "Press Enter to close..."