# Empty Trash Script

This script is designed to empty the trash directory on a Linux system.

## Usage

1. Make the script executable by running `chmod +x empty_trash.sh`.
2. Run the script by executing `./empty_trash.sh`.
3. The script will display the contents of the trash directory.
4. Press Enter to confirm deletion or Ctrl+C to cancel.
5. The script will empty the trash directory and display the number of files and folders deleted.

## Requirements

- The script should be run with Bash shell.
- The script assumes the trash directory is located at `$HOME/.local/share/Trash`.

## Note

This script permanently deletes files and folders from the trash directory. Be careful when using this script, as deleted files and folders cannot be recovered.

## License

This script is released under the MIT License.
