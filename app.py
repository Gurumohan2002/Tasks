#Practice Programs

from nt import environ
from flask import Flask
from markupsafe import escape

# app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"

# @app.route('/user/<username>')
# def show_user_profile(username):
#     # show the user profile for that user
#     return f'User {escape(username)}'

# @app.route('/post/<int:post_id>')
# def show_post(post_id):
#     # show the post with the given id, the id is an integer
#     return f'Post {post_id}'

# @app.route('/path/<path:subpath>')
# def show_subpath(subpath):
#     # show the subpath after /path/
#     return f'Subpath {escape(subpath)}'

# @app.route('/projects/')
# def projects():
#     return 'The project page'

# @app.route('/about')
# def about():
#     return 'The about page'

# @app.route('/about/')
# def about1():
#     return 'The about page new'

from flask import url_for
from flask import Flask

app = Flask(__name__)


# @app.route('/')
# def index():
#     return 'index'

# @app.route('/login')
# def login():
#     return 'login'

# @app.route('/user/<username>')
# def profile(username):
#     return f'{username}\'s profile'

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='Gurumohan'))

from flask import request

@app.route('/login', methods=['POST','GET' ])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()

# @app.get('/login')
# def login_get():
#     return show_the_login_form()

# @app.get('/login')
# def login_post():
#     return do_the_login()

def do_the_login():
    # Implement your login logic here
    return "Login Successful!"

def show_the_login_form():
    # Implement your login form display logic here
    return "Login Form Displayed!"

# @app.get('/login')
# def login_get():
#     return show_the_login_form()

# @app.post('/login')
# def login_post():
#     return do_the_login()

# @app.route('/')
# def index():
#     # Use url_for here within the context of the app route
#     static_url = url_for('static', filename='style.css')
#     return f"<h1> Static URL: </h1> {static_url}"

# from flask import render_template

# @app.route('/hello/')
# @app.route('/hello/<name>')
# def hello(name=None):
#     return render_template('hello.html', name=name)

from flask import request

# with app.test_request_context('/hello', method='POST'):
#     # now you can do something with the request until the
#     # end of the with block, such as basic assertions:
#     assert request.path == '/hello'
#     assert request.method == 'POST'

# with app.request_context(environ):
#     assert request.method == 'POST'

# @app.route('/login', methods=['POST', 'GET'])
# def login():
#     error = None
#     if request.method == 'GET':
#         if valid_login(request.form['username'],
#                        request.form['password']):
#             return log_the_user_in(request.form['username'])
#         else:
#             error = 'Invalid username/password'
#     # the code below is executed if the request method
#     # was GET or the credentials were invalid
#     return render_template('login.html', error=error)

def valid_login(username, password):
    # Hardcoded valid credentials for demonstration purposes
    valid_user = "admin"
    valid_password = "password123"

    return username == valid_user and password == valid_password

from flask import session, redirect, url_for

# def log_the_user_in(username):
#     # Set a session variable to indicate the user is logged in
#     session['logged_in'] = True
#     session['username'] = username

#     # Redirect the user to the dashboard or some other page
#     return redirect(url_for('dashboard'))  # Assuming you have a 'dashboard' route defined


    
if __name__ == '__main__':
    app.run(debug=True)
