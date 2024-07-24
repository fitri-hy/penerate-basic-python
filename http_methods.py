import requests

def check_http_methods(url):
    methods = ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS', 'HEAD']
    allowed_methods = []
    
    for method in methods:
        response = requests.request(method, url)
        if response.status_code != 405:
            allowed_methods.append(method)
    
    return allowed_methods

if __name__ == "__main__":
    target_url = "http://example.com"
    methods_allowed = check_http_methods(target_url)
    print(f"Allowed HTTP methods: {methods_allowed}")
