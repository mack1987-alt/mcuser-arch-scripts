# User Add Script

A simple Python script to add a new user to the system.

## Requirements

- Python 3.x
- `sudo` permissions

## Usage

1. Run the script as root:

  $ sudo python3 add_user.py

2. Enter the username and password for the new user.
3. The script will add the user and display a success message.

## Features

- Adds a new user to the system
- Sets a password for the new user
- Adds the new user to the `wheel` group for sudo access

## Limitations

- The script does not perform any error checking or validation on the input fields.
- The script assumes that the system has the necessary permissions to add a new user.

## License

This script is licensed under the MIT License.
