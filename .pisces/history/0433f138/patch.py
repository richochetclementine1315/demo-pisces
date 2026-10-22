def run_cmd(user_input):
    subprocess.run(['ls', user_input], shell=False)  # Removed shell=True to prevent command injection