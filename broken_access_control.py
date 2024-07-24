import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
import logging
import time
from colorama import init, Fore

init(autoreset=True)

def check_access_control(response_text, payload):
    """Check if the payload exposes access control issues."""
    if "admin" in response_text.lower() and payload.lower() not in ["admin", "superuser"]:
        return True
    return False

def fetch_url(test_url, parameter, payload, results, lock):
    """Fetch URL and check for broken access control."""
    full_url = f"{test_url}?{parameter}={payload}"
    try:
        # Add timeout to avoid hanging requests
        response = requests.get(full_url, timeout=10)
        response.raise_for_status()

        if check_access_control(response.text, payload):
            with lock:
                results.append(full_url)
    except requests.RequestException:
        pass

def test_broken_access_control(url, parameters, payloads, max_workers=10):
    """Test for broken access control by sending various payloads to different parameters."""
    from threading import Lock
    
    vulnerabilities = []
    lock = Lock()

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [
            executor.submit(fetch_url, url, parameter, payload, vulnerabilities, lock)
            for parameter in parameters
            for payload in payloads
        ]

        for future in as_completed(futures):
            try:
                future.result()  # Retrieve result to ensure exceptions are raised
            except Exception:
                pass

    return vulnerabilities

if __name__ == "__main__":
    target_url = "http://localhost/demo/admin.php"
    parameters = [
        "role"
    ]
    payloads = [
        "admin", "user", "guest", "superuser", "admin123", "admin1", "administrator", "root", 
        "owner", "developer", "manager", "staff", "employee", "guest123", "editor", "moderator",
        "support", "helpdesk", "customer", "client", "user1", "user2", "user3", "user4", 
        "user5", "test", "testuser", "qa", "lead", "chief", "boss", "director", "executive", 
        "ceo", "cfo", "cto", "coo", "cmo", "intern", "trainee", "newuser", "temporary", 
        "anonymous", "anonymoususer", "special", "premium", "vip", "subuser", "backupadmin", "backupadmin"
    ]

    start_time = time.time()
    vulnerabilities = test_broken_access_control(target_url, parameters, payloads)
    elapsed_time = time.time() - start_time

    if vulnerabilities:
        print(f"{Fore.RED}Vulnerabilities detected:")
        for url in vulnerabilities:
            print(f"{Fore.RED}URL: {url}")
    else:
        print(f"{Fore.GREEN}No vulnerabilities detected.")

    print(f"Test completed in {elapsed_time:.2f} seconds")
