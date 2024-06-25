from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/')
def home():
    message = os.environ.get('DISPLAY_MESSAGE', 'Hello, World!')
    return f'<h1>{message}</h1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
