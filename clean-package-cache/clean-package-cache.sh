#!/bin/bash

read -p "Are you sure you want to clear the cache? (yes/no): " response

if [ "$response" = "yes" ]; then
  rm -rf ~/.cache/*
  echo "Cache cleared successfully!"
else
  echo "Operation cancelled."
fi

read -rp "Press Enter to exit..."