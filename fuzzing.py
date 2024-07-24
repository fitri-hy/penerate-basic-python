import requests

def fuzzing(url, parameter, payloads_file):
    with open(payloads_file, 'r') as file:
        payloads = file.readlines()

    fuzz_results = []
    for payload in payloads:
        payload = payload.strip()
        test_url = f"{url}?{parameter}={payload}"
        response = requests.get(test_url)
        if response.status_code != 200:
            fuzz_results.append((test_url, response.status_code))
    
    return fuzz_results

if __name__ == "__main__":
    target_url = "http://example.com/search"
    parameter = "query"
    payloads_file = "fuzz_payloads.txt"  # File with payloads for fuzzing
    results = fuzzing(target_url, parameter, payloads_file)
    print(f"Fuzzing results: {results}")
