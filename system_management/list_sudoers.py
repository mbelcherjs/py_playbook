def list_sudoers():
    with open('/etc/sudoers', 'r') as f:
        print("--- /etc/sudoers ---")
        print(f.read())

    sudoers_dir = "/etc/sudoers.d/"
    if os.path.isdir(sudoers_dir):
        for fname in os.listdir(sudoers_dir):
            with open(os.path.join(sudoers_dir, fname), 'r') as f:
                print(f"--- /etc/sudoers.d/{fname} ---")
                print(f.read())

list_sudoers()
