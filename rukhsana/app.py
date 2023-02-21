
from flask import Flask, url_for
from flask import request

app = Flask(__name__)


# @app.route("/")
# def hello_world():
#     return "<h1>Hello, World!</h1>"

@app.route("/Hello_World1")
def hello_world1():
    return "<h1>Hello, World1!</h1>"

@app.route("/Hello_World2")
def hello_world2():
    return "<h1>Hello, World2!</h1>"

@app.route("/test")
def test():
    a=5+6
    return "This is my function to run my app {}".format(a)

@app.route("/test2")
def test2():
    data=request.args.get('x')
    return 'This is my data input from url {}'.format(data)

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

with app.test_request_context():
    print(url_for('index'))
    print(url_for('profile', username='Sumaiya Siddique'))

if __name__=="__main__":
    app.run(host="0.0.0.0")
