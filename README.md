# Pisces security repair exercise

This repository contains an intentionally vulnerable Python module for testing
Pisces detection and repair workflows. The vulnerable code is isolated in
[`pisces_target.py`](./pisces_target.py); it is training material only and must
not be used in production.

## Vulnerabilities included

- hardcoded credential
- SQL injection from string-built SQL
- fast, unsalted MD5 password hashing
- shell command injection through `shell=True`
- insecure temporary-file creation with `tempfile.mktemp`
- disclosure of the complete process environment

The regression checks in
[`tests/test_pisces_target.py`](./tests/test_pisces_target.py) intentionally
describe the secure behavior expected after repair. They should fail against
the starting target and pass after Pisces applies a complete fix.

## Try the exercise

From the repository root:
```cmd
pip install pisces-cli
pisces init
pisces watch .
pisces scan .
pisces explain <YOUR_FILE_NAME>:<LINE_NUMBER>
pisces fix <YOUR_FILE_NAME>:<LINE_NUMBER>
```

```powershell
.venv\Scripts\python.exe -m pytest
.venv\Scripts\pisces.exe scan
```

Review each proposed change before accepting it. Then rerun the tests:

```powershell
.venv\Scripts\python.exe -m pytest
```

The fake API key is included only to exercise secret detection; replace it
with an environment-based configuration or remove it during repair.
