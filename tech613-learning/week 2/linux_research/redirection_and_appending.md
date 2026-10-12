# Redirection and Appending


## `>`
 - sends output into a file
 - **overwrites** whatever was there before

```bash
echo "first line" > msg.txt
echo "second line" > msg.txt
cat msg.txt
second line
# first line gone
```

## `>>`
 - appends --> adds to the end, keeps old stuff

```bash
echo "third line" >> msg.txt
echo "fourth line" >> msg.txt
cat msg.txt
second line
third line
fourth line
```

## example
```bash
ls >> msg.txt
date >> msg.txt
cat msg.txt
second line
third line
fourth line
msg.txt
Sun Oct 11 23:18:55 BST 2026
```

`>` = overwrite, `>>` = add to end

good for logs eg `date >> log.txt`

‼️one `>` by accident wipes the file 