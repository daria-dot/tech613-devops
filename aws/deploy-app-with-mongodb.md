
# Deploying a database and connecting it to a web-app

1. ## Launch database instance
- Database instance security group: allow inbound Custom
TCP 27017 from the app instance’s security group.

2. ## Launch App instance
 
- **AMI:** Ubuntu Server 24.04 LTS
- **Instance type:** t2.micro or t3.micro
- **VPC:** same as the database instance
- **Auto-assign public IP:** enabled
- **Security group inbound rules:**
  - SSH, port 22, from My IP
  - HTTP, port 80, from Anywhere (0.0.0.0/0)
  - TCP, port 3000, from Anywhere (0.0.0.0/0)
  
3. ## Let the database accept outside connections
```bash
sudo nano /etc/mongod.conf          # change bindIp: 127.0.0.1 -> 0.0.0.0
sudo systemctl restart mongod
sudo ss -tlnp | grep 27017          # check: 0.0.0.0:27017
```

4. ## Update the system

```bash
sudo apt update
sudo DEBIAN_FRONTEND=noninteractive apt upgrade -y
```

  
5. ##  Install git, Node.js 20 and pm2

 
```bash
sudo apt install -y git curl
curl -fsSL https://deb.nodesource.com/setup_20.x -o nodesource_setup.sh
sudo -E bash nodesource_setup.sh
sudo apt install -y nodejs
sudo npm install -g pm2
node -v && npm -v                   # check they're installed
```

6. ## Get the app code

```bash
git clone https://github.com/daria-dot/tech613-tictactoe.git ~/tech613-tictactoe
cd ~/tech613-tictactoe/app
```
 

7. ## Connect to the database
 
```bash
export MONGODB_URI=mongodb://172.31.62.214:27017/tictactoe
printenv MONGODB_URI                # check it's set
nc -zv 172.31.62.214 27017          # check the database is reachable
```
 
8. ##  Install dependencies and start the app
 
```bash
pm2 kill                            # stop any old pm2 processes
npm install
pm2 start index.js --name tic
pm2 list                            # check: tic is online
```
9. ##  Seed the database
 
```bash
node seeds/seed.js                  # expect: Seeded ... (10 records)
```
 
10. ## Check the app on http <instance ip> and see if it has been updated

![Screenshot 2026-10-27 at 15.45.28.png](images/Screenshot%202026-10-27%20at%2015.45.28.png)










