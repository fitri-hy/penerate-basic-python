import requests

def detect_server_misconfigurations(url):
    response = requests.get(url)
    headers = response.headers

    misconfigurations = {
        "Server": headers.get("Server"),
        "X-Powered-By": headers.get("X-Powered-By"),
        "X-Content-Type-Options": headers.get("X-Content-Type-Options")
    }

    print(f"Server Misconfigurations: {misconfigurations}")

if __name__ == "__main__":
    target_url = "http://example.com"
    detect_server_misconfigurations(target_url)
