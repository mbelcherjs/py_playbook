import boto3
import subprocess
import sys
import os

# ----------- Configuration ------------
AWS_REGION = "us-east-1"
AWS_PROFILE = None  # Optional: set AWS CLI profile name or leave as None
ECR_REPO = "my-ecr-repo"
LOCAL_IMAGE = "my-app:latest"
TAG = "latest"
# --------------------------------------

def get_account_id():
    sts = boto3.client("sts")
    return sts.get_caller_identity()["Account"]

def ecr_login(region, profile=None):
    login_cmd = [
        "aws", "ecr", "get-login-password",
        "--region", region
    ]
    if profile:
        login_cmd += ["--profile", profile]
    
    password = subprocess.check_output(login_cmd).decode().strip()

    account_id = get_account_id()
    ecr_url = f"{account_id}.dkr.ecr.{region}.amazonaws.com"

    login = subprocess.run(
        ["docker", "login", "--username", "AWS", "--password-stdin", ecr_url],
        input=password.encode(),
        check=True
    )
    print(f"✔ Logged into ECR: {ecr_url}")
    return ecr_url

def push_image_to_ecr(local_image, ecr_repo, ecr_url, tag="latest"):
    remote_tag = f"{ecr_url}/{ecr_repo}:{tag}"
    
    print(f"📦 Tagging image {local_image} as {remote_tag}")
    subprocess.run(["docker", "tag", local_image, remote_tag], check=True)

    print(f"🚀 Pushing {remote_tag}")
    subprocess.run(["docker", "push", remote_tag], check=True)

    print("✅ Image pushed successfully!")

if __name__ == "__main__":
    try:
        ecr_url = ecr_login(AWS_REGION, AWS_PROFILE)
        push_image_to_ecr(LOCAL_IMAGE, ECR_REPO, ecr_url, TAG)
    except Exception as e:
        print("❌ Error:", e)
        sys.exit(1)
