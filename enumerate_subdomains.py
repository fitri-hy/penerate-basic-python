import requests

def enumerate_subdomains(domain, subdomains):
    found_subdomains = []
    for subdomain in subdomains:
        url = f"http://{subdomain}.{domain}"
        try:
            response = requests.get(url, timeout=1)
            if response.status_code == 200:
                found_subdomains.append(url)
        except requests.RequestException:
            continue
    return found_subdomains

if __name__ == "__main__":
    target_domain = "example.com"
    subdomain_list = ["www", "dev", "staging", "test"]
    subdomains = enumerate_subdomains(target_domain, subdomain_list)
    print(f"Found subdomains: {subdomains}")
