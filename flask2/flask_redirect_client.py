import requests

if __name__ == "__main__":
    # The base URL for the Flask server
    url = "http://127.0.0.1:5000"

    # Authenticate with the server by sending a username and password
    # response = requests.get(f"{url}/", auth=("username", "password"))
    response = requests.get(f"{url}/", allow_redirects=False)

    print(response)

    # If the authentication is successful, the server will return a 200 OK response
    if response.status_code == 200:
        print("Authentication successful!")            
        exit()
    elif response.status_code == 302:
        redirect_location = response.headers.get("Location")
        print(f"Redirecting to {redirect_location}")
