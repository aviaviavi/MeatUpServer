import time
import os
from flask import Flask, request, json
import pdb
#from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
#db = SQLAlchemy(app)


lunch_requests = {}  # Maps phone numbers to lunch requests


@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/sync_data', methods=["GET"])
def sync():
    print "sync called"
    print request.method
    if request.method == "POST":
        print "in if"
        print request
    elif request.method == "GET":
        print "get"
    else:
        print "none"
    print "past"
    return "Data Recieved"
    

@app.route('/update', methods=["GET"])
def update():
    identifier = request.args.get('identifier')
    data = lunch_requests.pop(identifier, {})
    return json.dumps(data)


@app.route('/test_add_data', methods=["GET"])
def add_data():
    lunch_requests["9876543210"] = {
        'lunches': [{'time': time.time(), 'people': ['Danny', 'Colorado', 'Avi', 'Lexi'], 'place': 'Sliver Pizzeria'}],
        'friend_invites': [],
    }
    return "ok"


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)