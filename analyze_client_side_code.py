import requests
import re
import logging
from urllib.parse import urlparse
from concurrent.futures import ThreadPoolExecutor, as_completed

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

SENSITIVE_PATTERNS = [
    # API keys and secrets
    r'api[_\-]?key\s*[:=]\s*["\']([^"\']+)["\']',
    r'api[_\-]?secret\s*[:=]\s*["\']([^"\']+)["\']',
    r'api[_\-]?token\s*[:=]\s*["\']([^"\']+)["\']',
    r'auth[_\-]?token\s*[:=]\s*["\']([^"\']+)["\']',
    r'client[_\-]?secret\s*[:=]\s*["\']([^"\']+)["\']',
    r'secret[_\-]?key\s*[:=]\s*["\']([^"\']+)["\']',
    r'private[_\-]?key\s*[:=]\s*["\']([^"\']+)["\']',

    # Credentials
    r'password\s*[:=]\s*["\']([^"\']+)["\']',
    r'username\s*[:=]\s*["\']([^"\']+)["\']',
    r'login[_\-]?id\s*[:=]\s*["\']([^"\']+)["\']',
    r'user[_\-]?id\s*[:=]\s*["\']([^"\']+)["\']',
    r'login\s*[:=]\s*["\']([^"\']+)["\']',
    r'user\s*[:=]\s*["\']([^"\']+)["\']',

    # OAuth credentials
    r'oauth[_\-]?client[_\-]?id\s*[:=]\s*["\']([^"\']+)["\']',
    r'oauth[_\-]?client[_\-]?secret\s*[:=]\s*["\']([^"\']+)["\']',
    r'oauth[_\-]?access[_\-]?token\s*[:=]\s*["\']([^"\']+)["\']',
    r'oauth[_\-]?refresh[_\-]?token\s*[:=]\s*["\']([^"\']+)["\']',

    # Payment credentials
    r'paypal[_\-]?client[_\-]?id\s*[:=]\s*["\']([^"\']+)["\']',
    r'paypal[_\-]?secret\s*[:=]\s*["\']([^"\']+)["\']',
    r'stripe[_\-]?api[_\-]?key\s*[:=]\s*["\']([^"\']+)["\']',
    r'stripe[_\-]?secret[_\-]?key\s*[:=]\s*["\']([^"\']+)["\']',

    # Database credentials
    r'database[_\-]?user\s*[:=]\s*["\']([^"\']+)["\']',
    r'database[_\-]?password\s*[:=]\s*["\']([^"\']+)["\']',
    r'db[_\-]?user\s*[:=]\s*["\']([^"\']+)["\']',
    r'db[_\-]?password\s*[:=]\s*["\']([^"\']+)["\']',
    r'db[_\-]?host\s*[:=]\s*["\']([^"\']+)["\']',

    # AWS credentials
    r'aws[_\-]?access[_\-]?key[_\-]?id\s*[:=]\s*["\']([^"\']+)["\']',
    r'aws[_\-]?secret[_\-]?access[_\-]?key\s*[:=]\s*["\']([^"\']+)["\']',
    r'aws[_\-]?session[_\-]?token\s*[:=]\s*["\']([^"\']+)["\']',

    # Cloud credentials
    r'google[_\-]?cloud[_\-]?api[_\-]?key\s*[:=]\s*["\']([^"\']+)["\']',
    r'azure[_\-]?subscription[_\-]?key\s*[:=]\s*["\']([^"\']+)["\']',
    
    # Other secrets
    r'ssl[_\-]?certificate\s*[:=]\s*["\']([^"\']+)["\']',
    r'ssl[_\-]?private[_\-]?key\s*[:=]\s*["\']([^"\']+)["\']',
    r'private[_\-]?token\s*[:=]\s*["\']([^"\']+)["\']',
    r'private[_\-]?credential\s*[:=]\s*["\']([^"\']+)["\']',

    # Deprecated / old tokens
    r'token\s*[:=]\s*["\']([^"\']+)["\']',
    r'auth[_\-]?key\s*[:=]\s*["\']([^"\']+)["\']',
    r'credential[_\-]?key\s*[:=]\s*["\']([^"\']+)["\']',

    # Custom patterns (Adjust as necessary)
    r'secret[_\-]?value\s*[:=]\s*["\']([^"\']+)["\']',
    r'private[_\-]?info\s*[:=]\s*["\']([^"\']+)["\']',
    r'confidential[_\-]?data\s*[:=]\s*["\']([^"\']+)["\']',
    r'auth[_\-]?credentials\s*[:=]\s*["\']([^"\']+)["\']',
    r'security[_\-]?key\s*[:=]\s*["\']([^"\']+)["\']',
]

def fetch_js_code(url):
    """Fetch JavaScript code from a given URL."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        logging.error(f"Request failed for {url}: {e}")
        return None

def find_sensitive_info(js_code):
    """Find sensitive information in JavaScript code."""
    found_items = []
    for pattern in SENSITIVE_PATTERNS:
        items = re.findall(pattern, js_code, re.IGNORECASE)
        found_items.extend(items)
    return found_items

def analyze_client_side_code(url):
    """Analyze client-side JavaScript code for sensitive information."""
    js_code = fetch_js_code(url)
    if js_code:
        return find_sensitive_info(js_code)
    return []

def analyze_multiple_urls(urls):
    """Analyze multiple URLs concurrently."""
    results = {}
    with ThreadPoolExecutor(max_workers=5) as executor:
        future_to_url = {executor.submit(analyze_client_side_code, url): url for url in urls}
        for future in as_completed(future_to_url):
            url = future_to_url[future]
            try:
                sensitive_items = future.result()
                results[url] = sensitive_items
            except Exception as e:
                logging.error(f"Error analyzing {url}: {e}")
                results[url] = []
    return results

if __name__ == "__main__":
    target_urls = [
        "http://example.com/static/js/app.js",
        # Add more URLs as needed
    ]
    parsed_urls = [urlparse(url) for url in target_urls]

    if all(url.scheme in ["http", "https"] for url in parsed_urls):
        logging.info("Starting analysis...")
        results = analyze_multiple_urls(target_urls)
        for url, sensitive_items in results.items():
            if sensitive_items:
                print(f"Sensitive information found in {url}: {sensitive_items}")
            else:
                print(f"No sensitive information found in {url}.")
    else:
        logging.error("All URLs must use HTTP or HTTPS schemes.")