# Linux File Ownership




## Commands to view file ownership

```bash
ls -l            # list files with owner and group
ls -ld mydir     # show the directory itself, not what's inside it
stat myfile.txt  # full details, including owner, group and permissions
```

Output from VM:

```text
$ ls -l
drwxr-xr-x 2 root root 4096 Oct  8 00:52 mydir
-rw-r--r-- 1 root root    0 Oct  8 00:52 myfile.txt
```

How to read it:

```text
-rw-r--r--  1  root   root   0  Oct 8 00:52  myfile.txt
│└┬┘└┬┘└┬┘      └─┬─┘  └─┬─┘
│ │  │  │         │      └── group
│ │  │  │         └── owner (user)
│ │  │  └── others' permissions
│ │  └── group permissions
│ └── owner permissions
└── file type (- = file, d = directory)
```

## 3. What permissions are set when a user creates a file or directory? Who does it belong to?

The default permissions come from the system's maximum default minus the **umask**:

| | Maximum default | umask `022` (root) | umask `002` (normal user on Ubuntu) |
|---|---|---|---|
| File | `666` (rw-rw-rw-) | **`644`** (rw-r--r--) | **`664`** (rw-rw-r--) |
| Directory | `777` (rwxrwxrwx) | **`755`** (rwxr-xr-x) | **`775`** (rwxrwxr-x) |

Tested:

```text
# as root (umask 0022)
-rw-r--r-- 1 root root     0 myfile.txt
drwxr-xr-x 2 root root  4096 mydir

# as testuser (umask 0002)
-rw-rw-r-- 1 testuser testuser    0 notes.txt
drwxrwxr-x 2 testuser testuser 4096 work
```

**Who it belongs to:** the **user who created it** becomes the owner, and the group is that user's **primary group**. On Ubuntu each user gets their own primary group with the same name, so `testuser` creates files owned by `testuser:testuser`.

Check or change the umask:

```bash
umask        # 0022
umask -S     # u=rwx,g=rx,o=rx
umask 077    # new files become rw------- (only the owner can access them)
```

## 4. Why does the owner not get execute (x) permission by default on a new file?

- **Security**: if every new file could be executed, a downloaded or accidentally created file could be run as a program straight away, which could include malicious code. Making execution something you turn on deliberately is safer.
- **Most files aren't programs**: text, config, logs and data files never need to be executed, so `x` would just be an unnecessary permission (principle of least privilege).
- **Files and directories are different**: directories *do* get `x` by default, because on a directory `x` means "allowed to enter it" (`cd`). That's why the starting point is `666` for files but `777` for directories.

Tested on my VM:

```text
$ ls -l hello.sh
-rw-r--r-- 1 root root 23 hello.sh
$ ./hello.sh
bash: ./hello.sh: Permission denied

$ chmod u+x hello.sh
$ ls -l hello.sh
-rwxr--r-- 1 root root 23 hello.sh
$ ./hello.sh
hello
```

## 5. What command is used to change the owner of a file or directory?

`chown` (change owner). You usually need `sudo`.

```bash
sudo chown testuser myfile.txt # change the owner
sudo chown testuser:devs myfile.txt # change the owner and the group
sudo chown :devs myfile.txt # change only the group
sudo chgrp devs myfile.txt # change only the group (alternative)
sudo chown -R testuser:devs mydir # recursive: the directory and everything inside it
```

Tested on my VM:

```text
$ chown testuser myfile.txt
-rw-r--r-- 1 testuser root 0 myfile.txt

$ chown testuser:devs myfile.txt
-rw-r--r-- 1 testuser devs 0 myfile.txt

$ chown -R testuser:devs mydir
-rw-r--r-- 1 testuser devs 0 a
-rw-r--r-- 1 testuser devs 0 b
```

A normal user **can't** give their files away to someone else:

```text
testuser$ chown root notes.txt
chown: changing ownership of 'notes.txt': Operation not permitted
```

## Key takeaways

- `ls -l` shows the owner and group; `chown` changes them; `chmod` changes permissions.
- New files are owned by their creator and the creator's primary group.
- Default permissions = `666` (file) or `777` (directory) minus the umask.
- Files don't get `x` by default for safety. Add it with `chmod u+x` when needed.
- Only root (`sudo`) can change a file's owner.