import time

def tail_log(file_path, lines=10):
    with open(file_path, 'r') as f:
        f.seek(0, 2)
        while True:
            line = f.readline()
            if line:
                print(line.strip())
            else:
                time.sleep(1)

# Example usage: tail_log("/var/log/syslog")
