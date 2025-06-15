from flask import Flask
import pytest

app = Flask(__name__)

@app.route('/hello')
def hello():
    return 'Hello, World!'

def test_hello_world(client):
    response = client.get('/hello')
    assert response.data == b'Hello, World!'
    assert response.status_code == 200