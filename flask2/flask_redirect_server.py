from flask import Flask, redirect, request

app = Flask(__name__)

@app.before_request
def require_authentication():
    if not is_authenticated(request):
        return redirect("https://example.com/")

def is_authenticated(request):
    # implement your authentication logic here
    print("NOT AUTHENTICATED!")
    return False # return True if authenticated, False otherwise

@app.route("/")
def index():
    return "Hello, world!"

if __name__ == "__main__":
    app.run()
