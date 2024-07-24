import re
import requests

def detect_api_keys(url):
    response = requests.get(url)
    content = response.text
    
    api_key_patterns = [
        r'api_key=([a-zA-Z0-9_-]+)',
        r'api_key\s*:\s*"([a-zA-Z0-9_-]+)"'
    ]
    
    found_keys = []
    for pattern in api_key_patterns:
        keys = re.findall(pattern, content)
        found_keys.extend(keys)
    
    return found_keys

if __name__ == "__main__":
    target_url = "http://example.com"
    api_keys = detect_api_keys(target_url)
    print(f"Exposed API keys: {api_keys}")
