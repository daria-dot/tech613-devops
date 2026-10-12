# File Permissions - Research

## Q1: does owning a file mean full permissions?

```bash
ubuntu@ip-172-31-62-237:~$ mkdir ~/perm-test && cd ~/perm-test
# opening test folder
ubuntu@ip-172-31-62-237:~/perm-test$ echo 'echo "script ran!"' > test.sh
# sample script
ubuntu@ip-172-31-62-237:~/perm-test$ chmod 000 test.sh
# no perms
ubuntu@ip-172-31-62-237:~/perm-test$ cat test.sh
cat: test.sh: Permission denied
# no access for owner
```
Owner changes perms
```bash
ubuntu@ip-172-31-62-237:~/perm-test$ chmod 644 test.sh #changing perms
ubuntu@ip-172-31-62-237:~/perm-test$ cat test.sh
echo "script ran!"
```

## A1: 
 - The owner only gets whatever the user (u) permissions say
 - Only the owner (or root) can change a file's permissions, `chmod644` shows the owner can change back
 - root bypasses permissions compeletely 

## Q2: Giving perms to user entity

Making a second user to test with
```bash
ubuntu@ip-172-31-62-237:~/perm-test$ whoami
ubuntu
ubuntu@ip-172-31-62-237:~/perm-test$ groups
ubuntu adm cdrom sudo dip lxd
# groups ubuntu is in
ubuntu@ip-172-31-62-237:~/perm-test$ ls -l test.sh
-rw-r--r-- 1 ubuntu ubuntu 19 Oct  8 14:56 test.sh
# owner is ubuntu, group is ubuntu
ubuntu@ip-172-31-62-237:~/perm-test$ sudo adduser --disabled-password --gecos "" tester
# new user, gets its own group called tester
ubuntu@ip-172-31-62-237:~/perm-test$ groups tester
tester : tester users
# tester not in ubuntu group
```
Only user gets perms
```bash
ubuntu@ip-172-31-62-237:~/perm-test$ chmod 600 test.sh
# user: rw-  group: ---  other: ---
ubuntu@ip-172-31-62-237:~/perm-test$ cat test.sh
echo "script ran!"
# owner can read
ubuntu@ip-172-31-62-237:~/perm-test$ sudo -u tester cat test.sh
cat: test.sh: Permission denied
# tester can't
```

## A2:
 - User perms only apply to one account, the file's owner
 - With `600` ubuntu (owner) could read but tester was denied

## Q3: Giving perms to group entity

```bash
ubuntu@ip-172-31-62-237:~/perm-test$ sudo usermod -aG ubuntu tester
# adding tester to ubuntu group
ubuntu@ip-172-31-62-237:~/perm-test$ chmod 660 test.sh
# group: rw-
ubuntu@ip-172-31-62-237:~/perm-test$ sudo -u tester cat test.sh
echo "script ran!"
# tester can read as group member
ubuntu@ip-172-31-62-237:~/perm-test$ chmod 600 test.sh
# group: ---
ubuntu@ip-172-31-62-237:~/perm-test$ sudo -u tester cat test.sh
cat: test.sh: Permission denied
# no group perms, no access
```

## A3:
 - Group perms apply to every member of the file's group (apart from the owner)
 - tester could read with `660` once added to the group, and got denied with `600`
 - Useful for teams sharing files without giving access to everyone

## Q4: Giving perms to other entity

Tested before adding tester to the group, so tester counts as other
```bash
ubuntu@ip-172-31-62-237:~/perm-test$ chmod 600 test.sh
# other: ---
ubuntu@ip-172-31-62-237:~/perm-test$ sudo -u tester cat test.sh
cat: test.sh: Permission denied
ubuntu@ip-172-31-62-237:~/perm-test$ chmod 604 test.sh
# other: r--
ubuntu@ip-172-31-62-237:~/perm-test$ sudo -u tester cat test.sh
echo "script ran!"
# tester can read as other
```

## A4:
 - Other perms apply to everyone who isn't the owner and isn't in the group
 - tester was denied with `600` and could read with `604`
 - Be careful giving other `w`, anyone on the system could change the file

## Q5: User r, group rw, other rwx. I'm the owner, what perms do I have?

```bash
ubuntu@ip-172-31-62-237:~/perm-test$ chmod u=r,g=rw,o=rwx test.sh
# same as chmod 467
ubuntu@ip-172-31-62-237:~/perm-test$ ls -l test.sh
-r--rw-rwx 1 ubuntu ubuntu 19 Oct  8 14:56 test.sh
ubuntu@ip-172-31-62-237:~/perm-test$ cat test.sh
echo "script ran!"
# read works
ubuntu@ip-172-31-62-237:~/perm-test$ echo "new line" >> test.sh
-bash: test.sh: Permission denied
# write denied
ubuntu@ip-172-31-62-237:~/perm-test$ ./test.sh
-bash: ./test.sh: Permission denied
# execute denied
```

## A5:
 - Read only
 - Linux only uses one set: owner → user perms, in group → group perms, everyone else → other perms
 - Perms don't add together, so as owner I only get `r--` even though group and other have more
 - Owner can still fix it with `chmod`

## Q6: What does this line tell us?

```
-rwxr-xr-- 1 tcboony staff  123 Nov 25 18:36 keeprunning.sh
```

Recreating it on my VM
```bash
ubuntu@ip-172-31-62-237:~/perm-test$ chmod 754 test.sh
ubuntu@ip-172-31-62-237:~/perm-test$ ls -l test.sh
-rwxr-xr-- 1 ubuntu ubuntu 19 Oct  8 14:56 test.sh
# same perms as keeprunning.sh
ubuntu@ip-172-31-62-237:~/perm-test$ ./test.sh
script ran!
# owner can run it now (has x)
```

## A6:

| Part | Meaning |
|------|---------|
| `-` | regular file (`d` would be a directory) |
| `rwx` | user (owner) can read, write, execute |
| `r-x` | group can read and execute |
| `r--` | other can only read |
| `1` | number of hard links |
| `tcboony` | owner |
| `staff` | group |
| `123` | size in bytes |
| `Nov 25 18:36` | last modified |
| `keeprunning.sh` | file name, `.sh` = shell script |

 - In numbers it's `754` (rwx = 4+2+1 = 7, r-x = 4+1 = 5, r-- = 4)
 - tcboony can edit and run it, staff can run it but not change it, everyone else can only read it

