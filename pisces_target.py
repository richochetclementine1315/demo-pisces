"""Intentionally vulnerable training target for Pisces.

This module is deliberately insecure. Do not copy it into production code.
Use it to practice detecting and repairing common Python security issues.
"""

import pickle
import sqlite3
import subprocess

password = "super_secret_123"  # S001 — hardcoded secret
api_key = "sk-abc123xyz"  # S001 — hardcoded secret


def run_cmd(user_input):
    subprocess.run(f"ls {user_input}", shell=True)  # S002 — command injection
def load_data(f):
    return pickle.load(f)  # S004 — unsafe deserialization


import requests

r = requests.get("https://api.example.com", verify=False)  # S005 — TLS disabled

result = eval(input("expr: "))  # S006 — code injection


def find_user(username):
    conn = sqlite3.connect("users.db")
    return conn.execute(
        "SELECT * FROM users WHERE username = '" + username + "'"
    ).fetchone()  # S007 — SQL injection



if __name__ == "__main__":
    print("Demo application loaded.")
