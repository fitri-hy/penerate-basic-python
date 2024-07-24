import requests
import time
import logging
from concurrent.futures import ThreadPoolExecutor, as_completed

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def fetch_with_rate_limit(url, headers, rate_limit_state):
    """Fetch data from the API and handle rate limiting."""
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        if response.status_code == 429:
            logging.warning("Rate limit triggered.")
            retry_after = int(response.headers.get('Retry-After', 1))
            rate_limit_state['retry_after'] = retry_after
            logging.info(f"Waiting for {retry_after} seconds before retrying.")
            return None, response.headers
        
        if response.status_code != 200:
            logging.error(f"Failed with status code {response.status_code}")
            return None, response.headers
        
        return response.json(), response.headers

    except requests.RequestException as e:
        logging.error(f"Request failed: {e}")
        return None, None


def test_api_rate_limiting(url, headers, num_requests=100, max_workers=10):
    """Test API rate limiting by sending a number of concurrent requests."""
    rate_limit_headers = []
    results = []
    rate_limit_state = {'retry_after': 0}

    def task(request_id):
        """Task to send a request and record the result."""
        while True:
            result, response_headers = fetch_with_rate_limit(url, headers, rate_limit_state)
            if response_headers:
                rate_limit_headers.append(response_headers)

            if result is not None:
                return result

            retry_after = rate_limit_state['retry_after']
            if retry_after > 0:
                logging.info(f"Sleeping for {retry_after} seconds")
                time.sleep(retry_after)

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(task, i) for i in range(num_requests)]
        for future in as_completed(futures):
            try:
                result = future.result()
                results.append(result)
            except Exception as e:
                logging.error(f"Error retrieving result: {e}")

    time.sleep(1)

    total_limit = None
    remaining_limit = None
    reset_time = None
    
    if rate_limit_headers:
        for headers in rate_limit_headers:
            total = headers.get('X-RateLimit-Limit')
            remaining = headers.get('X-RateLimit-Remaining')
            reset = headers.get('X-RateLimit-Reset')

            if total is not None:
                try:
                    total_limit = int(total)
                except ValueError:
                    logging.warning(f"Could not parse total rate limit value: {total}")

            if remaining is not None:
                try:
                    remaining_limit = int(remaining)
                except ValueError:
                    logging.warning(f"Could not parse remaining rate limit value: {remaining}")

            if reset is not None:
                try:
                    reset_time = int(reset)
                except ValueError:
                    logging.warning(f"Could not parse rate limit reset time: {reset}")

        if total_limit is not None:
            logging.info(f"Total rate limit: {total_limit}")

        if remaining_limit is not None:
            logging.info(f"Rate limit remaining: {remaining_limit}")

        if reset_time is not None:
            logging.info(f"Rate limit resets at: {time.ctime(reset_time)}")

if __name__ == "__main__":
    api_url = "http://example/api/v2"
    headers = {'Authorization': 'Bearer your_token_here'}
    test_api_rate_limiting(api_url, headers)
