#!/bin/bash
sudo useradd -m newuser
echo "newuser:newpassword" | sudo chpasswd
sudo usermod -aG wheel newuser
