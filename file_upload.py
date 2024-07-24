import requests

def test_file_upload(url, file_path):
    files = {'file': open(file_path, 'rb')}
    response = requests.post(url, files=files)
    
    if response.status_code == 200:
        print(f"File upload is allowed. Response: {response.text}")
    else:
        print(f"File upload is not allowed or failed.")

if __name__ == "__main__":
    upload_url = "http://example.com/upload"
    file_to_upload = "malicious_file.exe"
    test_file_upload(upload_url, file_to_upload)
