import requests

def test_idor(url, parameter):
    payloads = ["1", "2", "999"]
    vulnerabilities = []

    for payload in payloads:
        test_url = f"{url}?{parameter}={payload}"
        response = requests.get(test_url)
        
        if "object" in response.text:
            vulnerabilities.append(test_url)
    
    return vulnerabilities

if __name__ == "__main__":
    target_url = "http://example.com/object"
    parameter = "id"
    results = test_idor(target_url, parameter)
    print(f"Possible IDOR vulnerabilities: {results}")
