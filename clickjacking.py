import requests

def test_clickjacking(url):
    response = requests.get(url)
    if "X-Frame-Options" in response.headers:
        if response.headers["X-Frame-Options"] in ["DENY", "SAMEORIGIN"]:
            print(f"Clickjacking protection is in place.")
        else:
            print(f"Clickjacking protection is weak: {response.headers['X-Frame-Options']}")
    else:
        print("No clickjacking protection detected.")

if __name__ == "__main__":
    target_url = "http://example.com"
    test_clickjacking(target_url)
