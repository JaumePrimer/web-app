from bottle import Bottle, run
import os
from time import sleep

app = Bottle(__name__)

@app.route('/')
@app.route('/<name>')
def hello_world(name='World'):
    return 'Hello {}!\n'.format(name)


@app.route('/end/')
@app.route('/end/<name>')
def goodbye_earth(name='Earth'):
    return 'Goodbye {}!\n'.format(name)


@app.route('/wait/')
@app.route('/wait/<ms:int>')
def wait(ms=10):
    sleep(ms / 1000.0)
    return 'Waited {ms:d} milliseconds!\n'.format(ms=ms)

if __name__ == "__main__":
    run(app, server='meinheld', host='0.0.0.0',
        port=int(os.environ.get('PORT', 8800)))
