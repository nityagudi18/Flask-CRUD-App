import json


# Load JSON FILE
def load_all():
    with open('json_files/users.json') as f:
        return json.load(f)


# Save updated data to JSON
def save_data(json_data):
    with open('json_files/users.json', 'w') as f:
        json.dump(json_data, f, indent=4)


# Read JSON records
def read_all():
    json_data = load_all()
    return json_data['users']


# Read single User
def read_user(Id):
    json_data = load_all()
    users = json_data['users']
    for user in users:
        if user['Id'] == str(Id):
            return users[users.index(user)]


# Append to JSON file
def add_to(data):
    json_data = load_all()
    json_data['users'].append(data)
    save_data(json_data)
    return json_data


# Update JSON Object by ID
def update_json(Id, new_data):
    json_data = load_all()
    users = json_data['users']
    for user in users:
        if user["Id"] == Id:
            users[users.index(user)] = new_data
    save_data(json_data)


# Delete JSON object by id
def delete_record(Id):
    json_data = load_all()
    users = json_data['users']
    for user in users:
        if user["Id"] == Id:
            del users[users.index(user)]
    save_data(json_data)

