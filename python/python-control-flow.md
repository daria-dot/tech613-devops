# Python Control Flow: Ops Scripting Notes
 
> Conditions, loops and retries, with examples taken from server-health checks.
 
---
 
## 1. `if / elif / else`: pick one path
 
```python
disk_used = 94
 
if disk_used >= 90:
    print("CRITICAL")
elif disk_used >= 80:
    print("WARNING")
else:
    print("OK")
```
 
**Output:** `CRITICAL`
 
**Key ideas**
 
- Python checks the conditions **top to bottom** and runs **only the first one that's true**.
- **Order matters.** Put the most severe or most specific check first. If `>= 80` came first, a disk at 94% would print `WARNING`.
- `else` catches everything left over. It has no condition.
| `disk_used` | Result |
|---|---|
| 94 | CRITICAL |
| 85 | WARNING |
| 50 | OK |
 
---
 
## 2. Truthiness: empty means False
 
```python
failed_checks = []
 
if not failed_checks:
    print("All checks passed")
else:
    print(f"{len(failed_checks)} checks failed")
```
 
**Output:** `All checks passed`
 
**Key ideas**
 
- Empty things count as **False**: `[]`, `""`, `{}`, `0`, `None`.
- Non-empty things count as **True**.
- `if not failed_checks:` reads as "if there are no failed checks". It's cleaner than `if len(failed_checks) == 0:`.
- `len(x)` gives the number of items.
---
 
## 3. `for` loops with `range()`: repeat a fixed number of times
 
```python
for attempt in range(3):
    print(f"Attempt {attempt}")
```
 
**Output:**
```
Attempt 0
Attempt 1
Attempt 2
```
 
```python
for attempt in range(1, 4):
    print(f"Attempt {attempt} of 3")
```
 
**Output:**
```
Attempt 1 of 3
Attempt 2 of 3
Attempt 3 of 3
```
 
**Key ideas**
 
- `range(n)` gives `0` up to `n - 1`, so it **starts at 0**.
- `range(start, stop)` includes `start` and **excludes** `stop`.
- For human-friendly counting (1, 2, 3), use `range(1, n + 1)`.
| Call | Values |
|---|---|
| `range(3)` | 0, 1, 2 |
| `range(1, 4)` | 1, 2, 3 |
| `range(0, 10, 2)` | 0, 2, 4, 6, 8 |
 
---
 
## 4. `while` loops: repeat *while* a condition is true
 
```python
attempts = 0
 
while attempts < 3:
    print(f"Checking, attempt {attempts + 1}")
    attempts += 1
 
print("Gave up")
```
 
**Output:**
```
Checking, attempt 1
Checking, attempt 2
Checking, attempt 3
Gave up
```
 
**Key ideas**
 
- The condition is checked **before every pass**.
- You manage the counter yourself, so **always update it** (`attempts += 1`). If you forget, the loop runs forever.
- Code after the loop (`"Gave up"`) runs once the condition becomes false.
> **`for` vs `while`:** use `for` when you know how many times to loop. Use `while` when you loop *until something happens*.
 
---
 
## 5. Retry pattern: `while` with two conditions
 
```python
max_attempts = 5
attempt = 0
healthy = False
 
while attempt < max_attempts and not healthy:
    attempt += 1
    print(f"Health check attempt {attempt} of {max_attempts}")
    # on Friday, this is where you would actually call the service
    healthy = attempt == 3
 
if healthy:
    print(f"Healthy after {attempt} attempts")
else:
    print("Failed after all attempts")
```
 
**Output:**
```
Health check attempt 1 of 5
Health check attempt 2 of 5
Health check attempt 3 of 5
Healthy after 3 attempts
```
 
**Key ideas**
 
- The loop stops when **either** condition fails: we run out of attempts, **or** the service becomes healthy.
- `and` means both conditions must be true to keep looping.
- `healthy = attempt == 3` stores the result of the comparison (`True` or `False`) in `healthy`. It simulates the service recovering on the 3rd try.
- After the loop, check **why** it stopped (`if healthy:`) to report success or failure.
**The retry recipe:**
 
1. Set up a limit, a counter and a success flag.
2. Loop while you're under the limit **and** haven't succeeded.
3. Inside the loop, increase the counter, try the action and update the flag.
4. After the loop, report the result.
---
 
## 6. Looping over a list with `continue`
 
```python
servers = ["web-01", "web-02", "api-01", "db-01"]
 
for server in servers:
    if server.startswith("db"):
        continue          # skip databases, keep going
    print(f"Restarting {server}")
```
 
**Output:**
```
Restarting web-01
Restarting web-02
Restarting api-01
```
 
**Key ideas**
 
- `for item in list:` visits every item in order, with no index needed.
- `.startswith("db")` checks how a string begins (there's also `.endswith()`).
- `continue` **skips the rest of this pass** and jumps to the next item.
### `continue` vs `break`
 
| Keyword | What it does | Example use |
|---|---|---|
| `continue` | Skip **this item** and keep looping | Don't restart databases |
| `break` | **Stop the whole loop** right now | Stop once a server is found healthy |
 
---
 
## Quick reference
 
| Concept | Syntax | Remember |
|---|---|---|
| Branching | `if / elif / else` | First true branch wins, so order matters |
| Empty check | `if not my_list:` | Empty means False |
| Fixed repeat | `for i in range(n):` | Starts at 0, excludes `n` |
| Conditional repeat | `while condition:` | Update the counter or it loops forever |
| Retry | `while tries < max and not ok:` | Check *why* it stopped afterwards |
| Iterate a list | `for item in items:` | No index needed |
| Skip one | `continue` | Loop keeps going |
| Stop entirely | `break` | Loop ends |
| f-strings | `f"Attempt {n}"` | Put any expression inside `{}` |
 