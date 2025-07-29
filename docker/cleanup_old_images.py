import subprocess

def cleanup_docker_images():
    subprocess.run("docker image prune -af", shell=True)

cleanup_docker_images()
