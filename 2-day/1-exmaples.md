Nice — these keywords are absolutely important for Python and very useful in DevOps scripts. Below I’ll give a short **example** for each keyword you listed plus a one-line note on how it’s commonly used in DevOps. You can copy/run each snippet directly.

# Python keywords — examples (DevOps-focused)

---

**1. `and`** — logical AND

```python
cpu_ok = cpu_usage < 80
mem_ok = mem_usage < 75
if cpu_ok and mem_ok:
    print("resources OK")
```

Tip: combine health checks.

---

**2. `or`** — logical OR

```python
if node_failed or other_issue:
    print("investigate cluster")
```

Tip: trigger alerts if any condition is true.

---

**3. `not`** — logical NOT

```python
service_running = False
if not service_running:
    print("start service")
```

Tip: invert boolean checks (often used in guards).

---

**4. `if`** — conditional start

```python
if cpu > 90:
    print("scale up")
```

Tip: basic branching for decisions (scaling, backups, etc.).

---

**5. `else`** — alternate branch

```python
if os.path.exists("/etc/config"):
    print("config OK")
else:
    print("create config")
```

Tip: fallback actions.

---

**6. `elif`** — else-if chain

```python
if status == "ok":
    print("all good")
elif status == "degraded":
    print("check services")
else:
    print("critical")
```

Tip: check multiple priority conditions.

---

**7. `while`** — loop with condition

```python
retries = 0
while retries < 5:
    if check_service():
        break
    retries += 1
    time.sleep(2)
```

Tip: retry loops for idempotent operations.

---

**8. `for`** — iterate over sequence

```python
hosts = ["host1", "host2"]
for h in hosts:
    print("connect", h)
```

Tip: iterate over inventory, logs, files.

---

**9. `in`** — membership / iteration helper

```python
if "error" in log_line:
    print("found error")
# used with 'for' already: for item in items:
```

Tip: check substrings or membership in lists/sets.

---

**10. `try`** — start exception block
**11. `except`** — handle exceptions
**12. `finally`** — always-run cleanup

```python
import subprocess
try:
    subprocess.check_call(["ping", "-c", "1", "example.com"])
except subprocess.CalledProcessError:
    print("host unreachable")
finally:
    print("check complete")
```

Tip: robust scripting — handle failures and always clean up resources.

---

**13. `def`** — define function
**14. `return`** — return value from function

```python
def get_free_memory_mb():
    with open("/proc/meminfo") as f:
        # parse and return free memory (example)
        return 1024
free = get_free_memory_mb()
```

Tip: wrap repeatable logic into functions for reuse.

---

**15. `class`** — define classes (OO)

```python
class Service:
    def __init__(self, name): self.name = name
    def status(self): return "running"
svc = Service("nginx")
print(svc.status())
```

Tip: model services, resources, or config objects.

---

**16. `import`** — import modules

```python
import os, subprocess
print(os.name)
```

Tip: bring in stdlib or packages (os, subprocess, json, yaml, boto3, etc.).

---

**17. `from`** — import specific names from module
**18. `as`** — alias while importing

```python
from pathlib import Path as P
p = P("/var/log/syslog")
```

Tip: cleaner imports and aliases (e.g., `import boto3 as aws`).

---

**19. `True`** — boolean true
**20. `False`** — boolean false
**21. `None`** — null / no value

```python
enabled = True
disabled = False
result = None
if result is None:
    print("no result yet")
```

Tip: `None` is commonly used to mark absence of value; compare with `is`.

---

**22. `is`** — identity comparison (same object)

```python
a = []
b = a
c = []
print(a == c)   # True (value equality)
print(a is c)   # False (different objects)
print(a is b)   # True  (same object)
# preferred: if x is None:
x = None
if x is None:
    print("x is None")
```

Tip: use `is None` for None-checks; avoid using `is` for value equality.

---

**23. `lambda`** — anonymous function

```python
hosts = [{"name":"h1","latency":10},{"name":"h2","latency":5}]
hosts_sorted = sorted(hosts, key=lambda h: h["latency"])
print(hosts_sorted)
```

Tip: small inline functions for sorting, mapping, filtering.

---

**24. `with`** — context manager (automatic cleanup)

```python
with open("/tmp/mylog.txt", "a") as f:
    f.write("deployment started\n")
# file closed automatically
```

Tip: use `with` for files, locks, network sessions to ensure cleanup.

---

**25. `global`** — declare global var inside function

```python
counter = 0
def inc():
    global counter
    counter += 1
inc()
print(counter)  # 1
```

Tip: use sparingly; better to return values or use objects.

---

**26. `nonlocal`** — modify variable in enclosing (but not global) scope

```python
def make_counter():
    count = 0
    def inc():
        nonlocal count
        count += 1
        return count
    return inc

c = make_counter()
print(c())  # 1
print(c())  # 2
```

Tip: useful when building closures (e.g., small stateful helpers in scripts).

---

If you want, I can:

* Combine these into a **one-page printable cheat-sheet** (compact examples), or
* Create a small **practice file** (`devops_keywords_examples.py`) with runnable examples and comments.

Which would help you most next?
