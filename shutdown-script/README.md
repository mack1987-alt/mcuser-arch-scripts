Custom Shutdown Script

This script prompts the user to confirm if they want to shut down the system. If the user confirms, the script runs the update-system.sh script from a specified directory and then shuts down the system.
Prerequisites

Before using this script, ensure you have the following:

    Necessary permissions to execute scripts and shut down the system.
    A custom update-system.sh script located in a directory of your choice.

Installation

    Clone the repository (or download the script directly):

    bash

git clone https://github.com/your-username/custom-shutdown-script.git
cd custom-shutdown-script

Edit the custom-shutdown.sh script to specify the directory where update-system.sh is located. Replace /path/to/your/scripts with the actual directory path.

Make the script executable:

bash

    chmod +x custom-shutdown.sh

Usage

    Open a terminal.

    Navigate to the directory where the custom-shutdown.sh script is located.

    Run the script:

    bash

    ./custom-shutdown.sh

    Follow the prompts to confirm if you want to shut down the system.

Features

    Prompts the user for confirmation before shutting down.
    Runs the update-system.sh script before shutting down.
    Cancels the shutdown if the user responds with "no".
    Handles invalid responses and exits with an error message.

Example

After running the script (./custom-shutdown.sh), you will see:

sh

Shutting down...
Are you sure you want to shutdown? (yes/no):

    If the user types yes, the update-system.sh script will run, and the system will shut down.
    If the user types no, the shutdown will be canceled, and the script will exit.
    If the user provides any other response, the script will inform them of an invalid response and exit with an error.

Contributing

Contributions are welcome! Fork the repository and submit a pull request with your enhancements.
License

This project is licensed under the MIT License - see the LICENSE file for details.
