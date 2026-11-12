EC2 -> elastic cloud

a port is at the end of an IP address, it points to which part of server its 
going to 
Ip add -private/public ->wan ->0.0.0.0/0
needs to be opened for access
webserver - e.g enginex
node.js is like a backened javascript extender
monolith-> backend and frontend on the same server, same port


linux -. great for production servers because no updates

SSH keys GUI -> shell -> OS 
secure shell, access to the os via the internet

SSH (Secure Shell) is the protocol: an encrypted way to connect to a 
remote machine and send commands to its operating system through a terminal.

An SSH key is the credential you use to prove who you are when you connect 
over SSH. It’s an alternative to typing a password.



send the zip.file

scp -i ~/.ssh/your-key-pair.pem nodejs20-sparta-tictactoe-v1.zip ubuntu@IP-ADDRESS:/home/ubuntu

reverse proxy
systemctl status nginx

curl -sL https://deb.nodesource.com/setup_20.x -o nodesource_setup.sh

sudo bash nodesource_setup.sh

npm -> no package m

make a guide to do these - codes -ss - md
try github with automation

terminate instance after 3

Nginx is a web server and reverse proxy: a ready-made program you configure, not code you write. It sits in front of your app and handles the internet-facing work:

receiving visitors on port 80 (and 443 for HTTPS)
forwarding requests to your app (proxy_pass http://localhost:3000)
serving static files such as images and CSS quickly
handling HTTPS certificates, load balancing across several app copies, rate limiting, and so on