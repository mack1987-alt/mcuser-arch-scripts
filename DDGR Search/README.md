Command-Line Web Search with ddgr

This script allows you to perform web searches using DuckDuckGo's ddgr tool from the command line, with options to set the terminal title, position, and size.
Prerequisites

Before using this script, ensure you have the following dependencies installed:

    wmctrl: Window Manager Control tool to manipulate window properties.
        Installation on Ubuntu/Debian:

        bash

sudo apt-get update
sudo apt-get install wmctrl

Installation on Arch Linux:

bash

    sudo pacman -S wmctrl

ddgr: Command-line tool for DuckDuckGo searches.

    Installation on Ubuntu/Debian:

    bash

sudo apt-get update
sudo apt-get install ddgr

Installation on Arch Linux:

bash

        sudo pacman -S ddgr

Installation

    Clone the repository:

    bash

git clone https://github.com/your-username/ddgr-search-script.git
cd ddgr-search-script

Make the script executable:

bash

    chmod +x ddgr_search.sh

Usage

    Run the script:

    bash

    ./ddgr_search.sh

    Enter your search query when prompted by the script.

Features

    Sets the terminal title to "Search".
    Positions the terminal window at coordinates (0, 80) with a size of 650x200 pixels.
    Uses ddgr to perform a web search based on user input.

Example

After running the script (./ddgr_search.sh), you will see "Search the web...." in your terminal. Enter your search query (e.g., "trump") and press Enter to perform the search using ddgr.
Contributing

Contributions are welcome! Fork the repository and submit a pull request with your enhancements.
License

This project is licensed under the MIT License - see the LICENSE file for details.
