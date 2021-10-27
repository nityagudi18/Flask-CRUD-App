from flask import Blueprint, request, jsonify, render_template, redirect, url_for, make_response
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
from database.db_operations import *
import jwt
import datetime
import json

auth_bp = Blueprint('authentication', __name__)


def load_db():
    with open('database/cmdstore.json') as f:
        return json.load(f)


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token')

        if not token:
            return jsonify({'message': 'Token is missing!'}), 403

        try:
            data = jwt.decode(token, 'crudsecret', algorithms=["HS256"])

        except:
            return jsonify({'message': 'Token is invalid!'}), 403

        return f(*args, **kwargs)

    return decorated


@auth_bp.route('/token')
def get_cmd_token():
    dummy_db = load_db()
    auth = request.authorization
    if auth and auth.password == dummy_db['db_users'][0]['password']:
        token = jwt.encode({'user': auth.username, 'exp': datetime.datetime.utcnow()+datetime.timedelta(minutes=30)},
                           'crudsecret', "HS256")
        return jsonify({'token': token.decode('UTF-8')})

    return make_response('Could_not_verify', 401, {'WWW-Authenticate': 'Basic realm="Login Required"'})


@auth_bp.route('/signin', methods=['POST'])
def signin():
    if request.method == 'POST':
        entered_username = request.form['username']
        entered_password = request.form['password']
        sql = f"""SELECT * FROM USERS WHERE USERNAME ='{entered_username}'"""
        data = read_records(sql)
        user_password = data[0][2]
        if check_password_hash(user_password, entered_password):
            token = jwt.encode({'public_id': entered_username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=45)}, 'crudsecret', "HS256")
            return redirect(url_for('routes.index'))


@auth_bp.route('/signup', methods=['POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = generate_password_hash(request.form['password'], method='sha256')
        sql = f"""INSERT INTO USERS (USERNAME, PASSWORD) VALUES("{username}","{password}")"""
        write_record(sql)
        return redirect(url_for('routes.login'))
