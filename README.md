# 🐍 Python DevOps playbook

## Purpose
To catalog and share all my python scripts used in my DevOps journey

## Prerequisites
On Mac 🍏
- AWS cli installed <br>
  ```brew install awscli```
- Docker installed <br>
  ```brew install --cask docker```
- Python and dependencies installed <br>
  ```brew install python```

## 🚀 How to's

### 📁 AWS

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
