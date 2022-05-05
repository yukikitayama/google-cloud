#! /bin/bash
apt -y update
apt install --yes SYSTEM_PACKAGE_NAME
apt install python-dev
apt install python-pip
pip install PACKAGE_NAME==VERSION_NUMBER
