import os
from flask import Flask

app = Flask(__name__)

@app.route('/', defaults={'name' : 'World'})
@app.route('/<name>')
def hello_world(name):
    return 'Hello {}!\n'.format(name)

@app.route('/end/', defaults={'name': 'Earth'})
@app.route('/end/<name>')
def goodbye_earth(name):
    return 'Goodbye {}!\n'.format(name)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8801)))
