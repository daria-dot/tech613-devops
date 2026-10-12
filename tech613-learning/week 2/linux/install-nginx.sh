# ! /bin/bash

# puropose of this script: run on fresh ubuntu 24.04, install nginx
# update
sudo apt-get update
# upgrade
# get new versions of packages
sudo apt-get upgrade -y
# install nginx
# then find and install the packages
sudo apt-get install nginx -y
# restart nginx --> stop the process, start again --> 
# useful for when applying changes, as must restart to see changes
sudo systemctl restart nginx
# enable nginx --> enable means its starting when the machine
# starts

sudo systemctl enable nginx