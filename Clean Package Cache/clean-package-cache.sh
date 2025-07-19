#!/bin/bash
# Version 2.01
set -euo pipefail  # Exit on errors, unset variables, and pipe failures for robustness

# Colors for better output readability
RED='\e[31m'
GREEN='\e[32m'
BLUE='\e[34m'
RESET='\e[0m'

# Log file for tracking operations
LOG_FILE="$HOME/.cache_cleaner.log"

# Set terminal title (optional; enhances user experience in terminal tabs)
echo -ne "\033]0;Cache Cleaner Tool\007"

# Usage function for --help
usage() {
    echo -e "${BLUE}Usage:${RESET} $0 [options]"
    echo -e "Clean package caches on Arch Linux (pacman, yay, and optional home cache)."
    echo -e ""
    echo -e "${BLUE}Options:${RESET}"
    echo -e "  -h, --help        Show this help message and exit"
    echo -e "  -p, --pacman      Clean pacman cache (default: keep 3 recent versions)"
    echo -e "  -y, --yay         Clean yay/AUR build cache"
    echo -e "  -H, --home        Clean ~/.cache/* (warning: aggressive, affects all apps)"
    echo -e "  -a, --all         Clean all of the above"
    echo -e "  -d, --dry-run    Preview sizes and actions without cleaning"
    echo -e "  -q, --quiet      Suppress output and use notifications (if available)"
    echo -e ""
    echo -e "${BLUE}Run without options for interactive mode.${RESET}"
    exit 0
}

# Function to calculate directory size
get_size() {
    local dir="$1"
    if [[ -d "$dir" ]]; then
        du -sh "$dir" 2>/dev/null | cut -f1 || echo "0B"
    else
        echo "0B"
    fi
}

# Function for notifications (if notify-send is available)
notify() {
    local message="$1"
    local urgency="${2:-normal}"
    if command -v notify-send >/dev/null 2>&1; then
        notify-send "Cache Cleaner" "$message" --urgency="$urgency" --icon=trash
    fi
}

# Function to clean pacman cache
clean_pacman() {
    local dry_run="$1"
    local cache_dir="/var/cache/pacman/pkg/"
    local size_before=$(get_size "$cache_dir")
    echo -e "${BLUE}Pacman cache size: $size_before${RESET}" | tee -a "$LOG_FILE"

    if [[ "$dry_run" = true ]]; then
        echo -e "${BLUE}Dry-run: Would run 'paccache -r' (keep 3 recent versions) and 'paccache -ruk0' (remove uninstalled).${RESET}" | tee -a "$LOG_FILE"
        return
    fi

    if command -v paccache >/dev/null 2>&1; then
        echo -e "${BLUE}Cleaning pacman cache (keeping 3 recent versions)...${RESET}" | tee -a "$LOG_FILE"
        sudo paccache -r  # Remove all but 3 recent versions of installed packages
        sudo paccache -ruk0  # Remove uninstalled packages
    else
        echo -e "${BLUE}Falling back to pacman -Sc (clean uninstalled packages).${RESET}" | tee -a "$LOG_FILE"
        sudo pacman -Sc --noconfirm
    fi

    local size_after=$(get_size "$cache_dir")
    echo -e "${GREEN}Pacman cache cleaned. Freed: ~$(numfmt --from=iec --to=iec $(("$(du -sb "$cache_dir" 2>/dev/null | cut -f1 || echo 0)" - "$(du -sb "$cache_dir" 2>/dev/null | cut -f1 || echo 0)")) )${RESET}" | tee -a "$LOG_FILE"
    notify "Pacman cache cleaned. Freed space: ~$size_before -> $size_after"
}

# Function to clean yay cache
clean_yay() {
    local dry_run="$1"
    local cache_dir="$HOME/.cache/yay/"
    local size_before=$(get_size "$cache_dir")
    echo -e "${BLUE}Yay cache size: $size_before${RESET}" | tee -a "$LOG_FILE"

    if [[ "$dry_run" = true ]]; then
        echo -e "${BLUE}Dry-run: Would run 'yay -Scc' and 'rm -rf $cache_dir'.${RESET}" | tee -a "$LOG_FILE"
        return
    fi

    if command -v yay >/dev/null 2>&1; then
        echo -e "${BLUE}Cleaning yay cache...${RESET}" | tee -a "$LOG_FILE"
        yay -Scc --noconfirm
        rm -rf "$cache_dir"*  # Clean build dirs
    else
        echo -e "${RED}Yay not installed; skipping.${RESET}" | tee -a "$LOG_FILE"
        return
    fi

    local size_after=$(get_size "$cache_dir")
    echo -e "${GREEN}Yay cache cleaned. Freed: ~$size_before -> $size_after${RESET}" | tee -a "$LOG_FILE"
    notify "Yay cache cleaned. Freed space: ~$size_before -> $size_after"
}

# Function to clean home cache (aggressive)
clean_home() {
    local dry_run="$1"
    local cache_dir="$HOME/.cache/"
    local size_before=$(get_size "$cache_dir")
    echo -e "${BLUE}Home cache size: $size_before${RESET}" | tee -a "$LOG_FILE"

    if [[ "$dry_run" = true ]]; then
        echo -e "${BLUE}Dry-run: Would run 'rm -rf $cache_dir*'.${RESET}" | tee -a "$LOG_FILE"
        return
    fi

    echo -e "${RED}Warning: This will delete ALL files in ~/.cache/, affecting browsers, thumbnails, etc.${RESET}"
    read -rp "Proceed? (y/n): " choice
    if [[ ! "$choice" =~ ^[Yy]$ ]]; then
        echo -e "${BLUE}Skipping home cache clean.${RESET}" | tee -a "$LOG_FILE"
        return
    fi

    rm -rf "$cache_dir"*
    mkdir -p "$cache_dir"  # Recreate empty dir

    local size_after=$(get_size "$cache_dir")
    echo -e "${GREEN}Home cache cleaned. Freed: ~$size_before -> $size_after${RESET}" | tee -a "$LOG_FILE"
    notify "Home cache cleaned. Freed space: ~$size_before -> $size_after"
}

# Parse options
clean_pacman=false
clean_yay=false
clean_home=false
dry_run=false
quiet=false
while [[ $# -gt 0 ]]; do
    case "$1" in
        -h|--help)
            usage
            ;;
        -p|--pacman)
            clean_pacman=true
            shift
            ;;
        -y|--yay)
            clean_yay=true
            shift
            ;;
        -H|--home)
            clean_home=true
            shift
            ;;
        -a|--all)
            clean_pacman=true
            clean_yay=true
            clean_home=true
            shift
            ;;
        -d|--dry-run)
            dry_run=true
            shift
            ;;
        -q|--quiet)
            quiet=true
            shift
            ;;
        *)
            echo -e "${RED}Unknown option: $1${RESET}"
            usage
            ;;
    esac
done

# Redirect output if quiet mode
if [[ "$quiet" = true ]]; then
    exec > >(tee -a "$LOG_FILE") 2>&1
fi

# Interactive mode if no clean options specified
if [[ "$clean_pacman" = false && "$clean_yay" = false && "$clean_home" = false ]]; then
    echo -e "${BLUE}No options specified. Select caches to clean:${RESET}"
    read -rp "Clean pacman cache? (y/n): " choice
    [[ "$choice" =~ ^[Yy]$ ]] && clean_pacman=true
    read -rp "Clean yay cache? (y/n): " choice
    [[ "$choice" =~ ^[Yy]$ ]] && clean_yay=true
    read -rp "Clean home ~/.cache/* (aggressive)? (y/n): " choice
    [[ "$choice" =~ ^[Yy]$ ]] && clean_home=true
fi

# Log start
echo "$(date): Starting cache clean (dry-run: $dry_run)" >> "$LOG_FILE"

# Perform cleans
if [[ "$clean_pacman" = true ]]; then
    clean_pacman "$dry_run"
fi
if [[ "$clean_yay" = true ]]; then
    clean_yay "$dry_run"
fi
if [[ "$clean_home" = true ]]; then
    clean_home "$dry_run"
fi

if [[ "$clean_pacman" = false && "$clean_yay" = false && "$clean_home" = false ]]; then
    echo -e "${BLUE}No caches selected to clean.${RESET}" | tee -a "$LOG_FILE"
fi

read -rp "Press Enter to close..."