import os
from flask import Flask
import pdb
#from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
#db = SQLAlchemy(app)

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/sync_data', methods="POST")
def sync():
    print "sync called"
    print request.method
    pdb.set_trace()
    if request.method == "POST":
        print "in if"
        print request
    elif request.method == "GET":
        print "get"
    else:
        print "none"
    print "past"
    return "Data Recieved"
    

if __name__ == '__main__':
    print "here"
    app.run(host='0.0.0.0')
