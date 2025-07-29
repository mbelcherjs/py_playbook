import subprocess

def restart_service_if_failed(service):
    status = subprocess.run(['systemctl', 'is-active', service], capture_output=True, text=True)
    if status.stdout.strip() != 'active':
        print(f"Service {service} is not active. Restarting...")
        subprocess.run(['sudo', 'systemctl', 'restart', service])
    else:
        print(f"Service {service} is running normally.")

restart_service_if_failed('nginx')
