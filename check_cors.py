import requests

def check_cors(url):
    response = requests.options(url)
    headers = response.headers

    cors_settings = {
        "Access-Control-Allow-Origin": headers.get("Access-Control-Allow-Origin"),
        "Access-Control-Allow-Methods": headers.get("Access-Control-Allow-Methods"),
        "Access-Control-Allow-Headers": headers.get("Access-Control-Allow-Headers")
    }

    print(f"CORS settings: {cors_settings}")

if __name__ == "__main__":
    target_url = "http://example.com/api"
    check_cors(target_url)
