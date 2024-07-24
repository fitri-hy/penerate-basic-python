import requests

def test_session_fixation(url, session_param):
    payload = "fixsessionid"
    response = requests.get(f"{url}?{session_param}={payload}")

    # Simulate login and check if the session id is fixed
    login_response = requests.post(url, data={'username': 'test', 'password': 'test'})
    if session_param in login_response.cookies:
        print(f"Session fixation vulnerability detected: {session_param}")
    else:
        print(f"No session fixation vulnerability detected.")

if __name__ == "__main__":
    target_url = "http://example.com/login"
    session_parameter = "sessionid"
    test_session_fixation(target_url, session_parameter)
