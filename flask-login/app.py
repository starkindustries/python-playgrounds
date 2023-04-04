from flask import Flask, redirect, url_for, request
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

login_manager = LoginManager()
login_manager.init_app(app)

class User(UserMixin):
    def __init__(self, id):
        self.id = id

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_id = request.form['user_id']
        password = request.form['password']

        if password == 'your_password_here':
            user = User(user_id)
            login_user(user)
            return redirect(url_for('protected'))

    return '''
    <form method="POST">
        User ID: <input type="text" name="user_id"><br>
        Password: <input type="password" name="password"><br>
        <input type="submit" value="Submit">
    </form>
    '''

@app.route('/protected')
@login_required
def protected():
    return "Welcome to the protected page!"

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug=True)
