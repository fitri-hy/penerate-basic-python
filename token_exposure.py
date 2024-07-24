import requests
import re

def check_token_exposure(url):
    response = requests.get(url)
    tokens = re.findall(r'csrf_token=[^&]*', response.text)
    
    if tokens:
        print(f"Potential token exposure: {tokens}")
    else:
        print(f"No token exposure detected.")

if __name__ == "__main__":
    target_url = "http://example.com"
    check_token_exposure(target_url)
