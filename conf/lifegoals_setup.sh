#!/usr/bin/env bash
# get redis
wget http://download.redis.io/releases/redis-3.2.8.tar.gz
tar -xf redis-3.2.8.tar.gz
cd redis-3.2.8
make test, make, make install

yum install python-devel gcc epel-release python-pip nginx git -y
pip install virtualenv uwsgi

cd /opt
git clone https://github.com/ShipraShalini/lifegoals.git
virtualenv lifegoals
cd lifegoals/

pip install -r requirements.txt
cp conf/nginx.conf /etc/nginx/conf.d/
pub_ip = "$(curl ipecho.net/plain)"

#sed -i "s/ip-here/$pub_ip" /etc/nginx/conf.d/nginx.conf
cp uwsgi.service /etc/systemd/system/

systemctl enable nginx
systemctl enable uwsgi
