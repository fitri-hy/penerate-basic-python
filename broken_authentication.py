import requests

def test_broken_authentication(url, username, password):
    payload = {'username': username, 'password': password}
    response = requests.post(url, data=payload)
    
    if "Welcome" in response.text:  # Adjust based on actual success message
        print(f"Authentication is weak or broken.")
    else:
        print(f"Authentication appears secure.")

if __name__ == "__main__":
    target_url = "http://example.com/login"
    test_username = "admin"
    test_password = "password"
    test_broken_authentication(target_url, test_username, test_password)
