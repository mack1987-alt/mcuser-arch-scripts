# Make Executable Tool
# AUTHOR: mcuser
# DATE: 08/2024
# Version: 1.1
#!/bin/bash

# Set the directory path
DIR="path/to/your/directory"

# Loop through all files in the directory
for file in "$DIR"/*; do
  # Check if the file is a Python file (ends with .py) or a Bash script (ends with .sh)
  if [[ $file == *.py || $file == *.sh ]]; then
    # Change the permissions to executable
    chmod +x "$file"
    echo "Made $file executable"

  fi

done
# Wait for user to hit enter
read -p "Press enter to continue..."