from flask import Blueprint, request, jsonify, redirect, url_for, session, make_response
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
from database.db_operations import *
import jwt
import datetime
import json

auth_bp = Blueprint('authentication', __name__)


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = session['api_session_token']
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            return jsonify({'message': 'Token is missing!'}), 403

        try:
            data = jwt.decode(token, session['username'], algorithms=["HS256"])
            current_user = data['user']
            if not current_user:
                return jsonify({'message': 'Unauthorized Access!'}), 401

        except:
            return jsonify({'message': 'Token is invalid!'}), 403

        return f(*args, **kwargs)

    return decorated


@auth_bp.route('/signin', methods=['POST'])
def signin():
    if request.method == 'POST':
        session['username'] = entered_username = request.form['username']
        entered_password = request.form['password']
        sql = f"""SELECT * FROM USERS WHERE USERNAME ='{entered_username}'"""
        data = read_records(sql)
        user_password = data[0][2]
        if check_password_hash(user_password, entered_password):
            token = jwt.encode({'user': entered_username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, entered_username, "HS256")
            session['api_session_token'] = token
            return redirect(url_for('routes.index'))
        return redirect(url_for('routes.login'))


@auth_bp.route('/signup', methods=['POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = generate_password_hash(request.form['password'], method='sha256')
        sql = f"""INSERT INTO USERS (USERNAME, PASSWORD) VALUES("{username}","{password}")"""
        write_record(sql)
        return redirect(url_for('routes.login'))


@auth_bp.route('/logout', methods=['GET', 'POST'])
def logout():
    if request.method == 'GET':
        session.pop('username', None)
        return redirect(url_for('routes.login'))