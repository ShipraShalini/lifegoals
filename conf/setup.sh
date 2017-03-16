#!/bin/bash

# Remove old caches and update
apt-get clean
apt-get upgrade -y

# Install dev tools
apt-get install git htop -y

# Install redis server & tools
apt-get install redis-server redis-tools -y

# Install nginx, python & development libs.
apt-get install python-dev gcc python-pip nginx -y

# Upgrade pip
pip install pip --upgrade

# Install python tools
/usr/local/bin/pip install virtualenv uwsgi uwsgitop

# create user for the app
mkdir -p /opt/oggy
useradd -s /bin/false -M -d /opt/oggy uwsgi
touch /var/run/uwsgi.pid

mkdir -p /var/log/uwsgi
touch /var/log/uwsgi/lifegoals.log

# Switch to the working dir.
cd /opt/oggy

# Fetch codebase from github
git clone https://github.com/ShipraShalini/lifegoals.git

virtualenv venv
. ./venv/bin/activate

cd lifegoals
pip install -r requirements.txt

# place config files at correct location
cp ./conf/nginx /etc/nginx/sites-enabled/lifegoals.conf
cp ./conf/uwsgi.ini /opt/oggy

chown uwsgi.uwsgi /opt/oggy -R
