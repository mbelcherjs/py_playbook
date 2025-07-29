import ssl, socket
from datetime import datetime

hostname = 'example.com'
context = ssl.create_default_context()
with socket.create_connection((hostname, 443)) as sock:
    with context.wrap_socket(sock, server_hostname=hostname) as ssock:
        expires = datetime.strptime(ssock.getpeercert()['notAfter'], '%b %d %H:%M:%S %Y %Z')
        print(f"{hostname} SSL expires in {(expires - datetime.utcnow()).days} days")
