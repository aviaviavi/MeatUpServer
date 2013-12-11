import time
from flask import Flask, request, json
#from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
#db = SQLAlchemy(app)


unsent_data = {}  # Maps phone numbers to data that still needs to be sent


@app.route('/')
def hello():
    return 'Hello World!'


@app.route('/sync_data', methods=["GET"])
def sync():
    return "Data Recieved"
    

@app.route('/update', methods=["GET"])
def update():
    identifier = request.args.get('identifier')
    data = unsent_data.pop(identifier, None)
    if data is not None:
        return json.dumps(data)
    else:
        return ""


@app.route('/test_add_data', methods=["GET"])
def add_data():
    unsent_data["9876543210"] = {
        # Lunches should map to an array of dicts containing lunch info. These dicts contain the following keys:
        # Time should be seconds since epoch (cast to int?)
        # People should be list of strings, remove the person who this is being sent to from the list before
        #   adding it to the unsent_data dict
        # Place should be either a string or an index into our hardcoded list of restaurants,
        #   but more likely just a string
        'lunches': [{'time': int(time.time() * 1000), 'attendees': ['Danny', 'Colorado', 'Avi', 'Lexi'], 'location': 'Sliver Pizzeria'}],
        'friend_invites': [],
    }
    return "ok"


if __name__ == '__main__':
    #app.run(host='localhost', debug=True)
    app.run(host='0.0.0.0', debug=True)