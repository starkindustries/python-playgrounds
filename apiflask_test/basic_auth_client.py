import requests
from requests.auth import HTTPBasicAuth

# Replace this with the URL of your server
base_url = 'http://127.0.0.1:5000'

# Replace these with the username and password you want to authenticate with
username = 'userA'
password = 'foo1'

# Send a GET request to the server with basic authentication
response = requests.get(
    f'{base_url}/',
    auth=HTTPBasicAuth(username, password)
)

if response.status_code == 200:
    print('Authenticated successfully.')
    print('Response:', response.text)
else:
    print('Authentication failed.')
    print('Status code:', response.status_code)
