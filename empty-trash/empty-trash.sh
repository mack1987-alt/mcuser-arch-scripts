#!/bin/bash

# Define the trash directory path
TRASH_DIR="$HOME/.local/share/Trash"

# Initialize counters for deleted files and folders
deleted_files=0
deleted_folders=0

# Check if the trash directory exists
if [ -d "$TRASH_DIR" ]; then
    echo "Trash contents before deletion:"
    find "$TRASH_DIR" -type f -print -o -type d -print
    echo "Press Enter to confirm deletion or Ctrl+C to cancel..."
    read -r
    
    # Get the total number of files and folders in the trash
    total_files=$(find "$TRASH_DIR" -type f | wc -l)
    total_folders=$(find "$TRASH_DIR" -type d | wc -l)
    
    # Check if there are files and folders to delete
    if [ "$total_files" -gt 0 ] || [ "$total_folders" -gt 0 ]; then
        echo "Emptying the trash..."
        for file in "$TRASH_DIR"/* "$TRASH_DIR"/.[!.]* "$TRASH_DIR"/..?*; do
            if [ -f "$file" ]; then
                rm -f "$file"
                ((deleted_files++))
            elif [ -d "$file" ]; then
                rm -rf "$file"
                ((deleted_folders++))
            fi
        done
        
        echo -e "\nTrash has been emptied. $deleted_files files and $deleted_folders folders deleted."
    else
        echo "Trash is already empty. Nothing to delete."
    fi
else
    echo "Trash directory not found. Nothing to empty."
fi