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
/usr/local/bin/pip install virtualenv uwsgi uwsgitop supervisor


# create user for the app
mkdir -p /opt/oggy
useradd -s /bin/false -M -d /opt/oggy uwsgi
touch /var/run/uwsgi.pid

mkdir -p /var/log/uwsgi
touch /var/log/uwsgi/lifegoals.log

mkdir -p /var/log/supervisord
touch /var/log/supervisord/supervisor.log

mkdir -p /var/log/celery
touch /var/log/celery/worker.log
touch /var/log/celery/beat.log

mkdir -p /etc/supervisor/

# Switch to the working dir.
cd /opt/oggy

# Fetch codebase from github
git clone https://github.com/ShipraShalini/lifegoals.git

virtualenv venv
. ./venv/bin/activate

cd lifegoals
pip install -r requirements.txt

# migrations
python manage.py makemigrations
python manage.py migrate

# puts public ip in nginx.conf
pub_ip="$(curl ipinfo.io/ip)"
sed -i "s/ip-here/$pub_ip/" ./conf/nginx

# place config files at correct location
cp ./conf/nginx.conf /etc/nginx/sites-available/default
cp ./conf/uwsgi.ini /opt/oggy
cp ./conf/supervisord.conf /etc/supervisor/

chown uwsgi.uwsgi /opt/oggy -R

deactivate

/usr/local/bin/supervisord -c /etc/supervisor/supervisord.conf

service nginx restart
