import requests

def check_csp(url):
    response = requests.get(url)
    headers = response.headers

    csp_header = headers.get('Content-Security-Policy', '')
    if csp_header:
        print(f"CSP Header: {csp_header}")
        return True
    return False

if __name__ == "__main__":
    target_url = "http://example.com"
    csp_present = check_csp(target_url)
    if csp_present:
        print(f"Content Security Policy is implemented.")
    else:
        print(f"Content Security Policy is missing.")
