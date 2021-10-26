from flask import Blueprint, request, make_response, jsonify
from functools import wraps
import jwt
import json
import datetime

auth_bp = Blueprint('authentication', __name__)


def load_db():
    with open('json_files/database.json') as f:
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


@auth_bp.route('/')
def login():
    dummy_db = load_db()
    auth = request.authorization
    if auth and auth.password == dummy_db['db_users'][0]['password']:
        token = jwt.encode({'user': auth.username, 'exp': datetime.datetime.utcnow()+datetime.timedelta(minutes=30)},
                           'crudsecret', "HS256")
        return jsonify({'token': token.decode('UTF-8')})

    return make_response('Could_not_verify', 401, {'WWW-Authenticate': 'Basic realm="Login Required"'})

