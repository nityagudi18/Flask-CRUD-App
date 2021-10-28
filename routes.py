from flask import Blueprint, request, render_template, redirect, url_for
from json_files.operations import *
from authentication import token_required

routes_bp = Blueprint('routes', __name__)


# Home Page
@routes_bp.route('/')
def login():
    return render_template('login.html')


# Read all users
@routes_bp.route('/home')
@token_required
def index():
    token = request.args.get('token')
    user_data = read_all()
    return render_template('index.html', users=user_data, token=token)


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


# Update User
@routes_bp.route('/update', methods=['GET', 'POST'])
@token_required
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
@token_required
def delete(Id):
    if request.method == 'GET' or request.method =='POST':
        delete_record(Id)
        return redirect(url_for('routes.index'))
