from flask import Blueprint, request, render_template, redirect, url_for
from json_files.operations import *

routes_bp = Blueprint('routes', __name__)


# Home Page, Read all users
@routes_bp.route('/')
def index():
    user_data = read_all()
    return render_template('index.html', users=user_data)


# Create New User
@routes_bp.route('/create', methods=["POST"])
def create():

    if request.method == 'POST':
        Id = request.form['Id']
        name = request.form['name']
        age = request.form['age']
        occupation = request.form['occupation']
        email = request.form['email']
        number = request.form['number']

        data = {"Id": Id, "Name": name, "Age": age, "Occupation": occupation, "Email": email, "Phone": number}
        add_to(data)

        return redirect(url_for('routes.index'))


@routes_bp.route('/read/<Id>')
def read_by_id(Id):
    if request.method == 'GET':
        return read_user(Id)


# Update User
@routes_bp.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        Id = request.form['Id']
        name = request.form['name']
        age = request.form['age']
        occupation = request.form['occupation']
        email = request.form['email']
        number = request.form['number']
        data = {"Id": Id, "Name": name, "Age": age, "Occupation": occupation, "Email": email, "Phone": number}
        update_json(Id, data)

        return redirect(url_for('routes.index'))


# Delete User
@routes_bp.route('/delete/<Id>', methods=['GET', 'POST'])
def delete(Id):
    if request.method == 'GET':
        delete_record(Id)
        return redirect(url_for('routes.index'))
