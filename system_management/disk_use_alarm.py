import shutil

def check_disk_usage(threshold=80):
    total, used, free = shutil.disk_usage("/")
    percent = used / total * 100
    print(f"Disk Usage: {percent:.2f}%")
    if percent > threshold:
        print("⚠️ Warning: Disk usage exceeds threshold!")

check_disk_usage()
