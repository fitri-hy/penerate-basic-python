import requests

def test_http_parameter_pollution(url):
    payloads = ["param=value&param2=value2", "param=value&param=value2"]
    vulnerabilities = []

    for payload in payloads:
        test_url = f"{url}?{payload}"
        response = requests.get(test_url)
        
        if "error" in response.text or "success" in response.text:
            vulnerabilities.append(test_url)
    
    return vulnerabilities

if __name__ == "__main__":
    target_url = "http://example.com/search"
    results = test_http_parameter_pollution(target_url)
    print(f"Possible HTTP Parameter Pollution vulnerabilities: {results}")
