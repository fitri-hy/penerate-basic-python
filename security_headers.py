import requests

def analyze_security_headers(url):
    response = requests.get(url)
    headers = response.headers

    security_headers = {
        "X-Content-Type-Options": headers.get("X-Content-Type-Options"),
        "X-Frame-Options": headers.get("X-Frame-Options"),
        "X-XSS-Protection": headers.get("X-XSS-Protection"),
        "Strict-Transport-Security": headers.get("Strict-Transport-Security"),
        "Content-Security-Policy": headers.get("Content-Security-Policy")
    }

    print(f"Security Headers Analysis: {security_headers}")

if __name__ == "__main__":
    target_url = "http://example.com"
    analyze_security_headers(target_url)
