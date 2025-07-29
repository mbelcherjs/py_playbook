import tarfile
import os

def backup_dir(src_dir, output_name):
    with tarfile.open(output_name, "w:gz") as tar:
        tar.add(src_dir, arcname=os.path.basename(src_dir))
    print(f"Backup complete: {output_name}")

backup_dir('/etc/nginx', 'nginx_backup.tar.gz')
