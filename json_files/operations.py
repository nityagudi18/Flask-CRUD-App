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
    return json_data


# Read single User
def read_user(Id):
    json_data = load_all()
    for user in json_data:
        if user['Id'] == str(Id):
            return json_data[json_data.index(user)]


# Append to JSON file
def add_to(data):
    json_data = load_all()
    json_data.append(data)
    save_data(json_data)
    return json_data


# Update JSON Object by ID
def update_json(Id, new_data):
    json_data = load_all()
    for entity in json_data:
        if entity["Id"] == Id:
            json_data[json_data.index(entity)] = new_data
    save_data(json_data)


# Delete JSON object by id
def delete_record(Id):
    json_data = load_all()
    for entity in json_data:
        if entity["Id"] == Id:
            del json_data[json_data.index(entity)]
    save_data(json_data)

