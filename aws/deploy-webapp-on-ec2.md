# Deploying the Node.js 20 Tic-Tac-Toe App on AWS EC2 (Ubuntu)

Step-by-step guide to deploying `nodejs20-sparta-tictactoe-v1` on an Ubuntu EC2 instance and making it reachable in a browser.

> **Where to run each command**
> - **Mac** – run in your local Terminal 
> -  **Server** – run after SSH-ing in (prompt looks like `ubuntu@ip-XX:~$`)

**My values used below**

| Item | Value |
|---|---|
| Key file | `~/.ssh/tech613-daria-aws-key.pem` |
| Public DNS | `e.g ec2-XX.eu-west-1.compute.amazonaws.com` |
| Public IP | "" |
| Region | `eu-west-1` (Ireland) |
| User | `ubuntu` |
| App zip | `~/Downloads/nodejs20-[FOLDER].zip` |



---

## Step 0 – Launch the EC2 instance (AWS Console)

1. **EC2 → Launch instance**
2. **Name:** e.g. `tech613-daria-tictactoe`
3. **AMI:** Ubuntu Server (LTS, e.g. 22.04 or 24.04)
4. **Instance type:** `t2.micro` / `t3.micro` (free-tier eligible)
5. **Key pair:** select/create `tech613-daria-aws-key`
6. **Security group – inbound rules:**

| Type | Port | Source | Why |
|---|---|---|---|
| SSH | 22 | My IP | Log in to the server |
| Custom TCP | 3000 | Anywhere (0.0.0.0/0) | Reach the Node app directly |
| HTTP | 80 | Anywhere (0.0.0.0/0) | Reach the app via Nginx (Step 9, optional) |

7. **Launch**, wait for **Instance state = Running** and **Status checks = 2/2**, then copy the **Public IPv4 DNS**.

---

## Step 1 – Prepare the key 

Move the key into the `.ssh` folder :

```bash
mv ~/Downloads/tech613-daria-aws-key.pem ~/.ssh/
```

Lock down its permissions :

```bash
chmod 400 ~/.ssh/tech613-daria-aws-key.pem
```

## Step 2 – Copy the app to the server

```bash
scp -i ~/.ssh/tech613-daria-aws-key.pem ~/Downloads/[name of zip file].zip ubuntu@[ DNS ].eu-west-1.compute.amazonaws.com:/home/ubuntu
```

- `scp` = secure copy over SSH; pattern is `scp -i <key> <from> <to>`
- The `:` after the address means "path on the remote machine"
---

## Step 3 – Connect to the server 💻 → ☁️

```bash
ssh -i ~/.ssh/tech613-daria-aws-key.pem ubuntu@[DNS].eu-west-1.compute.amazonaws.com
```

---

## Step 4 – Update the system 

```bash
sudo apt update
sudo apt upgrade -y
```

- `sudo` – run as administrator
- `apt update` – refresh the list of available packages
- `apt upgrade -y` – install updates, answering "yes" automatically

---

## Step 5 – Unzip the app 
```bash
sudo apt install unzip -y
unzip [APP].zip
ls
```

You should see the folder.

---

## Step 6 – Install Node.js 20 

Ubuntu's default `nodejs` package is often too old, so use the NodeSource installer for version 20:

```bash
curl -fsSL https://deb.nodesource.com/setup_20.x -o nodesource_setup.sh
sudo -E bash nodesource_setup.sh
sudo apt install nodejs -y
```

- `curl -fsSL ... -o file` – download the setup script and save it
- `sudo -E bash nodesource_setup.sh` – run it, adding the NodeSource Node 20 repository
- `apt install nodejs` – installs Node.js **and** npm

Check the versions:

```bash
node -v    # should show v20.x.x
npm -v
```

---

## Step 7 – Install the app's dependencies 

Move into the app folder (the one containing `package.json`):

If there is an `app` sub-folder, go into it:

```bash
cd app
ls
```

Look at how the app is meant to start:

```bash
cat package.json
```

- Check `"scripts"` → `"start"` (the start command) and `"main"` (entry file, e.g. `app.js`).
- Check which **port** the app listens on (often 3000) – e.g. `grep -rn "listen" --include=*.js . | grep -v node_modules`

Install dependencies:

```bash
npm install
```

- Reads `package.json` and downloads all required libraries into `node_modules/`.
---

## Step 8 – Run the app ☁️

### 8a. Quick test (foreground)

```bash
npm start
```

(or `node app.js` if there is no start script)

Open in your browser:

```
http://3.253.94.62:3000
```

Press **Ctrl + C** in the terminal to stop it. While it runs in the foreground, the app **stops when you close the terminal**.

### 8b. Keep it running with PM2 (recommended)

PM2 is a process manager that runs the app in the background and restarts it if it crashes.

```bash
sudo npm install -g pm2
pm2 start app.js --name tictactoe
```

(Replace `app.js` with the entry file from `package.json`, or use `pm2 start npm --name tictactoe -- start`.)

Make it start automatically after a reboot:

```bash
pm2 startup
```

This prints a `sudo env PATH=...` command – **copy and run that printed command**, then:

```bash
pm2 save
```

Useful PM2 commands:

```bash
pm2 list                  # show running apps
pm2 logs tictactoe        # view live logs (Ctrl + C to exit)
pm2 restart tictactoe     # restart after code changes
pm2 stop tictactoe        # stop the app
pm2 delete tictactoe      # remove from PM2
```

The app is now live at `http://3.253.94.62:3000` even after you log out.

---

## Step 9 – (Optional) Serve on port 80 with Nginx 

Lets users visit `http://3.253.94.62` without `:3000`. Nginx acts as a **reverse proxy**, forwarding port 80 traffic to the app on port 3000.

```bash
sudo apt install nginx -y
```

Replace the default site config:

```bash
sudo tee /etc/nginx/sites-available/default > /dev/null <<'EOF'
server {
    listen 80;
    server_name _;

    location / {
        proxy_pass http://localhost:3000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
    }
}
EOF
```

Test the config and restart Nginx:

```bash
sudo nginx -t
sudo systemctl restart nginx
sudo systemctl enable nginx
```

- `nginx -t` – checks the config for errors (should say "syntax is ok" / "test is successful")
- `systemctl enable` – start Nginx automatically on boot

Open: `http://3.253.94.62`

> Change `3000` in `proxy_pass` if your app uses a different port.

---

## Step 10 – Verify 

```bash
pm2 list                          # app shows "online"
curl http://localhost:3000        # returns the app's HTML from inside the server
sudo systemctl status nginx       # (if using Nginx) shows "active (running)" – press q to exit
```
use nginx as reverse proxy, 