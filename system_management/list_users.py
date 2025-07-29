def list_users():
    with open('/etc/passwd', 'r') as f:
        for line in f:
            print(line.split(':')[0])

list_users()
