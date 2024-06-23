#!/bin/bash

# Set terminal title
echo -ne "\033]0;Search\007"

clear
echo "Search the web...."

# Set terminal geometry
wmctrl -r :ACTIVE: -e 0,0,80,650,200

# Prompt user for search query
read -p "Enter your search query: " query

# Run ddgr in the terminal with the user-provided search query
ddgr "$query"
