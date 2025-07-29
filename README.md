# 🐍 Python DevOps playbook

## Purpose
To catalog and share all my python scripts used in my DevOps journey

## 🚀How to's

### AWS
- AWS CLI installed and configured <br>
  ```aws configure```
- Existing services running
#### push_to_ecr.py
- Docker installed
- Built docker image <br>
  ```docker build -t my-image .```
- Existing ECR <br>

Push to ecr <br>
```python push_to_ecr.py```

### File Difference (file_diff)

Save the script locally <br>
```file_diff.py```

Run the script <br>
```python diff_files.py old_config.txt new_config.txt```
