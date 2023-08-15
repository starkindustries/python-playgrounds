import concurrent.futures
import requests

# The URL you want to connect to
url = "http://127.0.0.1:12913/"
# url = "https://www.google.com"

# The number of requests you want to make
num_requests = 1000

def make_request(url, n):
    # This could be any function that makes a request to the server
    response = requests.get(url)
    print(f"Request {n} received status code: {response.status_code}")

# Create a ThreadPoolExecutor
# It automatically manages the threads for you
with concurrent.futures.ThreadPoolExecutor(max_workers=num_requests) as executor:
    # Start the load operations and mark each future with its URL
    futures = {executor.submit(make_request, url, n): n for n in range(num_requests)}
    for future in concurrent.futures.as_completed(futures):
        n = futures[future]
        try:
            # If a request completed without raising an error, future.result() will be
            # None. Otherwise, the exception raised by the request will be re-raised here.
            future.result()
        except Exception as exc:
            print(f'Request {n} generated an exception: {exc}')
