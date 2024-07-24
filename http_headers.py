import requests

def analyze_http_headers(url):
    response = requests.get(url)
    headers = response.headers

    insecure_headers = {
        "X-Powered-By": "PHP",
        "Server": "nginx",
        "X-Content-Type-Options": "nosniff"
    }

    missing_headers = []
    for header, expected in insecure_headers.items():
        if header not in headers or headers[header] == expected:
            missing_headers.append(header)
    
    return missing_headers

if __name__ == "__main__":
    target_url = "http://example.com"
    missing_headers = analyze_http_headers(target_url)
    print(f"Missing or insecure headers: {missing_headers}")
