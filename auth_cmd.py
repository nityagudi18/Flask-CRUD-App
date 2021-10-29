from flask import Blueprint, request, jsonify, redirect, url_for, session, make_response
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
from database.db_operations import *
import jwt
import datetime
import json

auth_cmd_bp = Blueprint('auth_cmd', __name__)


# Command line user stored in a JSON file that acts as a dummy database
def load_dummy_db():
    with open('database/cmdstore.json') as f:
        return json.load(f)


def cmd_token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        # Get token from request argument or header
        token = request.args.get('token')
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            return jsonify({'message': 'Token is missing!'}), 403

        # Decode the JWT token
        try:
            data = jwt.decode(token, 'crudsecret', algorithms=["HS256"])
            current_user = data['user']
            if not current_user:
                return jsonify({'message': 'Unauthorized Access!'}), 401

        except:
            return jsonify({'message': 'Token is invalid!'}), 403

        return f(*args, **kwargs)
    return decorated


@auth_cmd_bp.route('/token')
def get_cmd_token():
    # Generate JWT Token for the current user

    dummy_db = load_dummy_db()
    auth = request.authorization
    # sql = f"""SELECT * FROM USERS WHERE USERNAME ='{auth.username}'"""
    # data = read_records(sql)
    # stored_password = data[0][2]
    # if auth and check_password_hash(stored_password, auth.password):
    #     token = jwt.encode({'user': auth.username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}
    #     ,'crudsecret', "HS256")
    #     return jsonify({'token': token.decode('UTF-8')})
    if auth:
        for user in dummy_db['db_users']:
            if user['username'] == auth.username and auth.password == dummy_db['db_users'][0]['password']:
                token = jwt.encode({'user': auth.username, 'exp': datetime.datetime.utcnow()+datetime.timedelta(minutes=30)}, 'crudsecret', "HS256")
                return jsonify({'token': token.decode('UTF-8')})

    return make_response('Could_not_verify', 401, {'WWW-Authenticate': 'Basic realm="Login Required"'})
