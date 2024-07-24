import requests
from requests.packages.urllib3.util.ssl_ import create_urllib3_context

def check_ssl_tls(url):
    context = create_urllib3_context()
    context.check_hostname = False
    context.verify_mode = False
    
    response = requests.get(url, verify=False)
    if "SSL" in response.text or "TLS" in response.text:
        print(f"SSL/TLS configuration is not secure.")
    else:
        print("SSL/TLS configuration appears secure.")

if __name__ == "__main__":
    target_url = "https://example.com"
    check_ssl_tls(target_url)
