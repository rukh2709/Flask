from flask import Flask, url_for

app = Flask(__name__)

@app.route('/hello/<name>')
def hello(name):
    return f'Hello, {name}!'

with app.test_request_context():
    url = url_for('hello', name='Alice')
    print(url)  # Output: '/hello/Alice'

if __name__=="__main__":
    app.run(host="0.0.0.0")