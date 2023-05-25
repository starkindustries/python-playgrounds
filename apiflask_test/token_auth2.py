from flask import jsonify, request
from apiflask import APIFlask, HTTPTokenAuth, abort

app = APIFlask(__name__)
auth = HTTPTokenAuth(scheme='Bearer')

# A simple in-memory storage for users and tokens
users = {'user1': 'password1', 'user2': 'password2'}
tokens = {'token1': 'user1', 'token2': 'user2'}

# Verify tokens
@auth.verify_token
def verify_token(token):
    if token in tokens:
        return tokens[token]
    return None

# Login route
@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    if username in users and users[username] == password:
        # Here, you would normally generate a unique token for the user.
        # In this example, we're using predefined tokens for simplicity.
        token = 'token1' if username == 'user1' else 'token2'
        return jsonify({'token': token})
    return abort(401)

# A protected route
@app.route('/protected')
@auth.login_required
def protected_route():
    print(f"current_user: ")
    return jsonify({'message': f'Hello, {auth.current_user()}!'})

if __name__ == '__main__':
    app.run(debug=True)
