from flask import Flask
import os
from time import sleep

app = Flask(__name__)


@app.route('/', defaults={'name' : 'World'})
@app.route('/<name>')
def hello_world(name):
    return 'Hello {}!\n'.format(name)


@app.route('/end/', defaults={'name': 'Earth'})
@app.route('/end/<name>')
def goodbye_earth(name):
    return 'Goodbye {}!\n'.format(name)


@app.route('/wait/', defaults={'ms': 10})
@app.route('/wait/<int:ms>')
def wait(ms):
    sleep(ms / 1000.0)
    return 'Waited {ms:d} milliseconds!\n'.format(ms=ms)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8801)))
