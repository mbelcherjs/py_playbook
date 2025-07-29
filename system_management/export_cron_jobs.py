import os
import pwd
import subprocess

def export_all_crons():
    for p in pwd.getpwall():
        username = p.pw_name
        try:
            output = subprocess.check_output(['crontab', '-l', '-u', username], stderr=subprocess.DEVNULL)
            print(f"--- Cron for {username} ---")
            print(output.decode())
        except subprocess.CalledProcessError:
            continue

export_all_crons()
