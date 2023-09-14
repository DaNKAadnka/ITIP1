from flask import Flask
from functional import formation
import os

app = Flask(__name__)

eport = 5000
ehost = '127.0.0.1'
ename = 'Danil'

@app.route('/')
def hello() -> str:
    return formation('Hello, {}', ename)

if __name__ == '__main__':
    if 'EPORT' in os.environ:
        eport = os.environ['EPORT']
        print(eport)
    if 'EHOST' in os.environ:
        ehost = os.environ['EHOST']
        print(ehost)
    if 'ENAME' in os.environ:
        ename = os.environ['ENAME']
        print(ename)

    app.run(host=ehost, port=eport)
