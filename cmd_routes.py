from flask import Blueprint, request, render_template, redirect, url_for
from json_files.operations import *

cmd_routes_bp = Blueprint('cmd_routes', __name__)


# Create New User API
@cmd_routes_bp.route('/create', methods=['POST'])
def create_by_id():
    if request.method == 'POST':
        data = request.get_json()
        add_to(data)
        return "Request Processed.\n"


# Read User
@cmd_routes_bp.route('/read/<Id>')
def read_by_id(Id):
    if request.method == 'GET':
        return read_user(Id)


# Update User
@cmd_routes_bp.route('/update/<Id>', methods=['GET', 'POST'])
def update(Id):
    if request.method == 'POST':
        data = request.get_json()
        update_json(Id, data)
        return "User Updated"


# Delete User
@cmd_routes_bp.route('/delete/<Id>', methods=['GET', 'POST'])
def delete(Id):
    if request.method == 'GET':
        delete_record(Id)
        return 'User Deleted'

