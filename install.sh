#!/bin/bash
sudo rm -rf /var/lib/dpkg/lock
sudo apt install -y python-dev python-pip git
sudo git clone https://github.com/dingboopt/ChatterBot.git
pip install ./ChatterBot
pip install itchat
