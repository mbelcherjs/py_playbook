import subprocess

def is_package_installed(pkg_name):
    result = subprocess.run(['dpkg', '-l', pkg_name], capture_output=True, text=True)
    if pkg_name in result.stdout:
        print(f"{pkg_name} is installed.")
    else:
        print(f"{pkg_name} is NOT installed.")

is_package_installed("curl")
