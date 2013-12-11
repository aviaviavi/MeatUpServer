import copy
import time
from flask import Flask, request, json
import pdb
#from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
#db = SQLAlchemy(app)

name_to_number = dict(Danny="4156894685", Avi="5626122483", Lexi="6507146456", Colorado="0123456789", Daniel="9253379725")
number_to_name = {}
for name in name_to_number:
    number_to_name[name_to_number[name]] = name

unsent_data = {}  # Maps phone numbers to data that still needs to be sent
for number in number_to_name:
    unsent_data[number] = {'lunches': [], 'friend_invites': []}


@app.route('/')
def hello():
    return 'Hello World!'


@app.route('/sync_data', methods=["POST"])
def sync():
    pdb.set_trace()
    return "Data Recieved"
    

@app.route('/update', methods=["GET"])
def update():
    identifier = request.args.get('identifier')
    data = unsent_data.pop(identifier, {})
    unsent_data[identifier] = {'lunches': [], 'friend_invites': []}
    return json.dumps(data)


@app.route('add_friend', methods=["POST"])
def add_friend():
    friend = request.form['friend']
    identifier = request.form['identifier']
    unsent_data[name_to_number[friend]]['friend_invites'].append(name_to_number[identifier])

@app.route('/new_or_edit_lunch', methods=["POST"])
def add_data():
    """
    unsent_data["9876543210"] = {
        # Lunches should map to an array of dicts containing lunch info. These dicts contain the following keys:
        # Time should be seconds since epoch (cast to int?)
        # People should be list of strings, remove the person who this is being sent to from the list before
        #   adding it to the unsent_data dict
        # Place should be either a string or an index into our hardcoded list of restaurants,
        #   but more likely just a string
        'lunches': [{'time': time.time(), 'attendees': ['Danny', 'Colorado', 'Avi', 'Lexi'], 'location': 'Sliver Pizzeria'}],
        'friend_invites': [],
    }
    phone must send to server -
    identifier - phone number of sender
    isEdit - 0 or 1
    'data' - data to append to lunch or friend_invites

    """
    data = request.form
    lunch_data = parse_lunch(data)
    print 'lunch_data', lunch_data
    for person in lunch_data['attendees']:
        #print person, lunch_data['attendees']
        if person == number_to_name[lunch_data['identifier']]:
            continue
        num = name_to_number[person]
        unsent_data[num]['lunches'].append(copy.deepcopy(lunch_data))
        unsent_data[num]['lunches'][-1]['attendees'].remove(person)
    return "ok"

def parse_lunch(data):
    """
        data is the full packet sent to the server
    """
    data = dict((key, value) for (key, value) in zip(data.keys(), data.values()))
    data['attendees'] = data['attendees'].strip("_").split("_")
    data['attendees'].append(number_to_name[data['identifier']])
    return data

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)