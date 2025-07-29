# 🐍 Python DevOps playbook

## Purpose
To catalog and share all my python scripts used in my DevOps journey

## 🚀 How to's

### 📁 AWS
- AWS CLI installed and configured <br>
  ```aws configure```
- Existing services running
#### > push_to_ecr.py
```
Requirements
-Docker installed
-Built docker image 
-Existing ECR

docker build -t my-image .

>> Push to ecr 
python push_to_ecr.py
```

### 📁 File Difference

#### > file_diff.py
```
Save the script locally
file_diff.py

>> Run the script 
python diff_files.py old_config.txt new_config.txt
```
