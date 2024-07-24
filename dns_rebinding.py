import requests

def test_dns_rebinding(url):
    payload = "http://internal-service.local"
    response = requests.get(url, headers={'Host': payload})
    
    if "Internal Service" in response.text:  # Adjust based on actual service response
        print(f"DNS Rebinding vulnerability detected.")
    else:
        print(f"No DNS Rebinding vulnerability detected.")

if __name__ == "__main__":
    target_url = "http://example.com"
    test_dns_rebinding(target_url)
