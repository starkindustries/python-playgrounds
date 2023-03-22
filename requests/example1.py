import requests

# Sending an HTTP GET request
def send_get_request(url, params=None, headers=None):
    response = requests.get(url, params=params, headers=headers)
    return response

# Sending an HTTP POST request
def send_post_request(url, data=None, json=None, headers=None):
    response = requests.post(url, data=data, json=json, headers=headers)
    return response

# Example usage
if __name__ == "__main__":
    # Sample GET request
    get_url = "https://jsonplaceholder.typicode.com/posts/1"
    get_response = send_get_request(get_url)
    print("GET request response:", get_response.text)

    # Sample POST request
    post_url = "https://jsonplaceholder.typicode.com/posts"
    post_data = {
        "title": "Sample Post",
        "body": "This is a sample post.",
        "userId": 1
    }
    post_response = send_post_request(post_url, json=post_data)
    print("POST request response:", post_response.text)
