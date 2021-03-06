#!/usr/bin/env bash

echo "Installing dependencies"
yum install epel-release python-devel gcc  python-pip nginx git -y
pip install virtualenv uwsgi

echo "Installing redis..."
wget http://download.redis.io/releases/redis-3.2.8.tar.gz
tar -xf redis-3.2.8.tar.gz
cd redis-3.2.8
make test, make, make install


echo "Cloning the repo.."
cd /opt
git clone https://github.com/ShipraShalini/lifegoals.git
virtualenv lifegoals
cd /opt/lifegoals/; . bin/activate

echo "Setting up the app..."
pip install -r requirements.txt


cp conf/nginx.conf /etc/nginx/conf.d/lifegoals.conf
pub_ip="$(curl ipecho.net/plain)"
sed -i "s/ip-here/$pub_ip/" /etc/nginx/conf.d/nginx.conf

mkdir -p /var/log/uwsgi/
cp conf/uwsgi.service /etc/systemd/system/

systemctl enable nginx
systemctl enable uwsgi

deactivate