# Clear Cache Script

A simple script to clear the cache in the current user's home directory.

## Usage

1. Make sure you have the script saved as `clear_cache.sh` and make it executable with `chmod +x clear_cache.sh`.
2. Run the script with `./clear_cache.sh`.
3. The script will prompt you to confirm that you want to clear the cache.
4. If you respond with "yes", the script will clear the cache and print a success message.
5. If you respond with anything else, the script will print a cancellation message and exit.

## Notes

- This script uses `rm -rf` to delete the cache files, which permanently deletes them without sending them to the trash. Be careful when running this script!
- The script only clears the cache in the current user's home directory. If you need to clear the cache for all users, you'll need to modify the script accordingly.
