import requests

def check_directory_listing(url):
    response = requests.get(url)
    if "Index of" in response.text:
        return True
    return False

if __name__ == "__main__":
    target_url = "http://example.com/uploads/"
    is_listing_enabled = check_directory_listing(target_url)
    if is_listing_enabled:
        print(f"Directory listing is enabled on {target_url}")
    else:
        print(f"Directory listing is not enabled on {target_url}")
