import requests

def check_unencrypted_data(url):
    response = requests.get(url)
    
    if "https://" not in url:
        print(f"Data is transmitted over unencrypted channel: {url}")
    else:
        print(f"Data is transmitted over encrypted channel.")

if __name__ == "__main__":
    target_url = "http://example.com/sensitive"
    check_unencrypted_data(target_url)
