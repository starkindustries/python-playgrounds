import requests

# Define the URL to send the POST request to
url = "http://127.0.0.1:5000/posthere"

# Define the data to send in the POST request body
data = {"key1": "value1", "key2": "value2"}

# Send the POST request with the data
response = requests.post(url, json=data)

# Check the response status code and content
if response.status_code == 200:
    print("POST request successful")
    print(response.content)
else:
    print("POST request failed")
