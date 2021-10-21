import json
from flask import jsonify


def loadall():
    with open('users.json') as f:
        return json.load(f)

def read_user(Id):
    json_data = loadall()
    for user in json_data:
        if user['Id'] == str(Id):
            return json_data[json_data.index(user)]

