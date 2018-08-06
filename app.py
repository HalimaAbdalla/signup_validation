from flask import Flask, render_template, url_for

app = Flask (__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/addnew')
def addnew():
    return render_template('addnew.html')


if __name__ == '__main__':
    app.run(debug = True)


