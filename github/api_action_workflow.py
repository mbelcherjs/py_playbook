import requests

url = "https://api.github.com/repos/username/repo/actions/workflows/build.yml/dispatches"
headers = {
    "Authorization": "Bearer YOUR_GITHUB_TOKEN",
    "Accept": "application/vnd.github.v3+json"
}
data = {"ref": "main"}

res = requests.post(url, headers=headers, json=data)
print(res.status_code, res.text)
