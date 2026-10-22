def run_cmd(user_input):
    # Use argument list and avoid shell=True to prevent command injection
    subprocess.run(['ls', user_input])  # fixed S002 — command injection