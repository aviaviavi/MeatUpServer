import os
from flask import Flask
from flask import request
import pdb
#from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
#db = SQLAlchemy(app)

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/sync_data', methods=["POST"])
def sync():
    return "Data Received"
    

if __name__ == '__main__':
    print "here"
    app.run(host='0.0.0.0')
