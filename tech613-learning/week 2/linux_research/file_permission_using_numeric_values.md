# File Permissions Using Numeric Values

Tested on VM by setting each value with `chmod` and checking the result:
```bash
chmod 400 test.txt && stat -c '%a %A' test.txt
400 -r--------
# number + letters side by side
```

## Results

| `chmod` | Result | Meaning (user) |
|---------|--------|----------------|
| `400` | `-r--------` | read |
| `200` | `--w-------` | write |
| `100` | `---x------` | execute |
| `000` | `----------` | nothing |
| `600` | `-rw-------` | read + write |
| `700` | `-rwx------` | read + write + execute |
| `500` | `-r-x------` | read + execute |
| `644` | `-rw-r--r--` | user rw, group r, other r |

## Q1: What numeric values are assigned to each permission?
 - read = `4`, write = `2`, execute = `1`, none = `0`
 - Add them up to combine permissions

## Q2: Read + write
 - `6` (4 + 2)

## Q3: Read, write and execute
 - `7` (4 + 2 + 1)

## Q4: Read and execute
 - `5` (4 + 1)

## Q5: What does 644 mean?
 - Each digit is one entity, in order: user, group, other
 - `6` = user can read + write
 - `4` = group can read only
 - `4` = other can read only
 - Common default for normal files: the owner can edit, everyone else can only read
 - Same as `chmod u=rw,g=r,o=r`, which also gave `644 -rw-r--r--`