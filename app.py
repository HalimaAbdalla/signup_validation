from flask import Flask, render_template, url_for
from flask import request

user_credentials = {}


app = Flask (__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login_process', methods = ['GET', 'POST'])
def login_process():
    username = request.values['Username']
    password = request.values['Password']
    if username in user_credentials.keys():
        if password == user_credentials[username][2]:
            return render_template('home.html')
        else:
            return render_template('login-failed.html')
    else:
        return render_template('not-found.html')
    

@app.route('/signup.html')
def signup():
    return render_template('signup.html')

@app.route('/signup_process', methods = ['GET', 'POST'])
def signup_process():
    email = request.values['Email']
    username = request.values['Username']
    password = request.values['Password']

    user_credentials[username] = (email,password)

    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/addnew')
def addnew():
    return render_template('addnew.html')


if __name__ == '__main__':
    app.run(debug = True)


