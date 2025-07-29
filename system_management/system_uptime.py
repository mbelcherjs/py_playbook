import subprocess

def system_uptime():
    result = subprocess.run(['uptime', '-p'], capture_output=True, text=True)
    print("System Uptime:", result.stdout.strip())

system_uptime()
