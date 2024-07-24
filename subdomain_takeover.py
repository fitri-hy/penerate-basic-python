import requests

def check_subdomain_takeover(subdomain_url):
    response = requests.get(subdomain_url)
    if "This domain is available" in response.text:  # Adjust based on actual response
        print(f"Subdomain takeover vulnerability detected: {subdomain_url}")
    else:
        print(f"No subdomain takeover vulnerability detected for: {subdomain_url}")

if __name__ == "__main__":
    subdomain = "http://test.example.com"
    check_subdomain_takeover(subdomain)
