# Linux Terminal

## Useful basic commands
- `cd ..` — <mark>move up one level (to the parent)</mark>
- `mkdir` — <mark>make directory (make folder)</mark>
- `mv`   — <mark>moving + renaming files</mark>
- `cd /`   — <mark>go straight to the root</mark>
- `cd` or `cd ~` - <mark> takes you to home folder from anywhere</mark>
- `history` - <mark> shows you all previous commands numbered, then you can !number to re-use it</mark>
- `sudo` -  <mark> gives temp superuser access </mark>

## Add and write a file
```
touch chicken.txt
nano chicken.txt
cat chicken.txt 
```

`touch` --> creates new file

`nano` --> opens nano text editor

`cat` --> show contents of file

`-nl` chicken-joke.txt --> prints out the file with numbered lines

`cat chicken-joke.txt | grep the`
searches 'the' in the text file, shows the lines where 'the' shows up - highlighted

use `apt-get` instead of apt (esp for scripts)

there is a root folder > like a home folder for root user

sudo su : if you cant run sudo

to move a file out of a directory, simply `mv`

| Command | Starts from | Works from anywhere? |
|---|---|---|
| `cd ~/abc` | your home folder |  yes |
| `cd /etc` | the root `/` |  yes |
| `cd abc` | the folder you're in now |  only if `abc` is inside your current folder |

# NOTES

`>` OVERWRITE

`>>` APPEND

src/  --> forward slash means its a folder


The **tar command** is a powerful Linux tool for creating and manipulating archive files. "Tar" originally stood for "Tape Archive" because it was designed to write data to magnetic tapes, but today it's commonly used to create compressed archive files on disk.

When you use tar, you're essentially bundling multiple files together into a single file (called an archive), and you can optionally compress this archive to save space. The most common compression format is gzip, which adds the .gz extension to the filename.

The tar command uses different options (flags) to control its behavior:

`c`: Create a new archive

`z`: Compress the archive using gzip

`f`: Specify the filename of the archive

So tar `-czf` archive.tar.gz file1 file2 creates a new compressed archive named archive.tar.gz containing file1 and file2

# VARS

variable - something stored in the memory

env var - name in CAPITALS
`=` assigns value

making a variable |
`MYNAME=daria`
access it with
` echo $MYNAME`

convert into variable `export MYNAME=daria`
access with `printenv MYNAME`

set when other software/other commands need to access that variable

env variables reset when `exit` is run

- need configuration file for everytime you start a session: to keep variables and easily set enviornments

# Manage processess

a program that is running in memory
may be idle until called upon
run `ps` command to check current processes

system processes dont provide an application or GUI for end user -> usually provide web server

use `ps -aux`

TOP command

whats using the most cpu- at the top 
`shift +m` to see memory at the top
`shift + n` to see newest at the top
`shift + p` to go back

parent processes - the process that starts processes
`ps -ef` `PPID` 

child processess

zombie processes

to get out of screen
- `q`
- `crt z`
- `crt c`

`sleep 3` - 3 seconds

`&` run in the background
`kil` -terminate
`systemctl` -
kill parent process

zombie process, parents got killed, still going, no management and will take up memory

if u kill children, the parents will re-create em
soft kill
graceful kill - kills both children, so the system cleans itself up

# Variables (Bash)

## What is a variable?
A **variable** is a named value stored in memory.

- **Environment variables** are written in `CAPITALS` by convention (e.g. `HOME`, `PATH`).
- `=` assigns a value. **No spaces** around it.

## Creating a variable
```bash
MYNAME=daria
```

## Using a variable
Put `$` in front of the name to get its value:
```bash
echo $MYNAME
# → daria
```