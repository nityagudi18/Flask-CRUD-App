from flask import Blueprint, request, render_template, redirect, url_for
from json_files.operations import *
from auth_cmd import cmd_token_required

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
@cmd_token_required
def read_by_id(Id):
    if request.method == 'GET':
        return read_user(Id)


# Update User
@cmd_routes_bp.route('/update/<Id>', methods=['GET', 'POST'])
@cmd_token_required
def update(Id):
    if request.method == 'POST':
        data = request.get_json()
        update_json(Id, data)
        return "User Updated"


# Delete User
@cmd_routes_bp.route('/delete/<Id>', methods=['GET', 'POST'])
@cmd_token_required
def delete(Id):
    if request.method == 'GET':
        delete_record(Id)
        return 'User Deleted'

