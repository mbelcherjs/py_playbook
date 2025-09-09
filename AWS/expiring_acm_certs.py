import boto3, datetime
client = boto3.client("acm")
now = datetime.datetime.now(datetime.timezone.utc)
soon_days = 30

arns = []
token = None
while True:
    resp = client.list_certificates(NextToken=token) if token else client.list_certificates()
    arns += [c["CertificateArn"] for c in resp["CertificateSummaryList"]]
    token = resp.get("NextToken")
    if not token: break

for arn in arns:
    cert = client.describe_certificate(CertificateArn=arn)["Certificate"]
    days = (cert["NotAfter"] - now).days
    if days <= soon_days:
        print(cert["DomainName"], "expires in", days, "days")
