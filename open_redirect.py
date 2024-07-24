import requests

def test_open_redirect(url, parameter):
    payloads = ["http://malicious.com", "https://malicious.com"]
    open_redirects = []

    for payload in payloads:
        test_url = f"{url}?{parameter}={payload}"
        response = requests.get(test_url)
        if response.url != url:
            open_redirects.append(test_url)
    
    return open_redirects

if __name__ == "__main__":
    target_url = "http://example.com/redirect"
    parameter = "url"
    open_redirects = test_open_redirect(target_url, parameter)
    print(f"Possible open redirect vulnerabilities: {open_redirects}")
