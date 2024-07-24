import requests

def detect_waf(url):
    response = requests.get(url)
    waf_indicators = [
        'Server: cloudflare',
        'X-Security-Token'
    ]

    waf_detected = any(indicator in response.headers for indicator in waf_indicators)
    return waf_detected

if __name__ == "__main__":
    target_url = "http://example.com"
    is_waf_detected = detect_waf(target_url)
    if is_waf_detected:
        print(f"Web Application Firewall detected.")
    else:
        print(f"No Web Application Firewall detected.")
