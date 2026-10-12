# Changing File Permissions



## Q1: What command changes file permissions?
 - `chmod` (change mode)
 - `man chmod` shows the manual

## Q2: To change permissions, what must the user be?
 - The **owner** of the file, or
 - **root** (use `sudo`)

```bash
ubuntu@ip-172-31-62-237:~/chmod-test$ sudo touch rootfile.txt
# file owned by root
ubuntu@ip-172-31-62-237:~/chmod-test$ chmod 777 rootfile.txt
chmod: changing permissions of 'rootfile.txt': Operation not permitted
# ubuntu isn't the owner
ubuntu@ip-172-31-62-237:~/chmod-test$ sudo chmod 777 rootfile.txt && stat -c '%a %A' rootfile.txt
777 -rwxrwxrwx
# root can
```

Tested on my VM, checking each change with:
```bash
stat -c '%a %A' testfile.txt
# shows number + letters

```
## `stat`: show file info

```bash
stat testfile.txt
# shows everything: size, owner, permissions, timestamps
stat -c '%a %A' testfile.txt
# shows only permissions, as number + letters
644 -rw-r--r--
```

| Part | Meaning |
|------|---------|
| `stat` | the command: show file info |
| `-c` | short for `--format`, use a custom format |
| `'...'` | the format; quotes keep it as one piece |
| `%a` | permissions as **numbers**, e.g. `644` |
| `%A` | permissions as **letters**, e.g. `-rw-r--r--` |
| `testfile.txt` | the file to check |

### Other format codes

| Code | Shows |
|------|-------|
| `%U` | owner's name |
| `%G` | group's name |
| `%s` | size in bytes |
| `%n` | file name |
| `%y` | last modified time |

```bash
stat -c '%n %U %G %a' testfile.txt
testfile.txt ubuntu ubuntu 644
```

 - `stat -c` is the Linux version; it doesn't work on Mac

## Q3: Different ways to set permissions on testfile.txt

| Task | Command | Result |
|------|---------|--------|
| User r, Group rwx, Other rw | `chmod u=r,g=rwx,o=rw testfile.txt` | `476 -r--rwxrw-` |
| same, using numbers | `chmod 476 testfile.txt` | `476 -r--rwxrw-` |
| Add execute to all | `chmod a+x testfile.txt` | `577 -r-xrwxrwx` |
| same | `chmod +x testfile.txt` | `577 -r-xrwxrwx` |
| same | `chmod ugo+x testfile.txt` | `577 -r-xrwxrwx` |
| Take write away from Group | `chmod g-w testfile.txt` | `557 -r-xr-xrwx` |
| User rw, Group r, Other none | `chmod 640 testfile.txt` | `640 -rw-r-----` |

## Syntaxes
 - **Numeric** `chmod 640`: sets all three entities at once
 - **Symbolic `=`** `chmod u=r`: sets one entity exactly
 - **Symbolic `+` / `-`** `chmod g-w`: adds or removes, leaving the rest alone
 - Who: `u` = user, `g` = group, `o` = other, `a` = all


# VARS

variable - something stored in the memory
env var - name in CAPITALS
`=` assigns value

making a variable
`MYNAME=daria`
access it with
` echo $MYNAME`