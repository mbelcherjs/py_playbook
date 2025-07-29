import requests
from requests.auth import HTTPBasicAuth

url = "https://jenkins.example.com/job/myjob/lastBuild/api/json"
auth = HTTPBasicAuth('user', 'api_token')

res = requests.get(url, auth=auth)
status = res.json().get("result", "UNKNOWN")
print(f"Latest build result: {status}")
