import subprocess

def list_services():
    result = subprocess.run(['systemctl', 'list-units', '--type=service', '--all'], capture_output=True, text=True)
    print(result.stdout)

list_services()
