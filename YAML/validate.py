import yaml

def load_yaml(file):
    with open(file, 'r') as f:
        data = yaml.safe_load(f)
        print(data)

load_yaml("deployment.yaml")
