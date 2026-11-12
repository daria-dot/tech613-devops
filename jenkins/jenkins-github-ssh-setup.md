
# Setting up SSH protocal for Jenkins - authenticating GITHUB

## 1. generate the key
```ssh-keygen -t rsa -b 4096 -C "yourownpersonalemail"```

setup github repo link

## 2. add the key to the ssh agent
```eval `ssh-agent -s` ```

## 3. add the public key to github
```ssh-add <key name> ```

## 4. test the connection
```ssh -T git@github.com```

create repo and create matching local folder then:
on github gui select SSH when copying the link
```git remote add origin git@github.com:dariae-dot/tech613-test-ssh.git```