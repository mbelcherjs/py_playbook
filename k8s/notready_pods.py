import json, subprocess, shlex
cmd = "kubectl get pods -A -o json"
data = json.loads(subprocess.run(shlex.split(cmd), check=True, capture_output=True, text=True).stdout)

bad = []
for item in data["items"]:
    ns = item["metadata"]["namespace"]
    name = item["metadata"]["name"]
    conds = {c["type"]: c["status"] for c in item.get("status", {}).get("conditions", [])}
    if conds.get("Ready") != "True":
        bad.append((ns, name))
for ns, name in bad:
    print(f"{ns}/{name}")
