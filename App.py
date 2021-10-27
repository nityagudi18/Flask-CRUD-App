from flask import Flask
from routes import routes_bp
from cmd_routes import cmd_routes_bp
from authentication import auth_bp

# Initialize Flask Application
app = Flask(__name__)

app.config['SECRET_KEY'] = 'crudsecret'
db_path = 'database/userstore.db'

# Register Blueprints
app.register_blueprint(routes_bp, url_prefix='/')
app.register_blueprint(cmd_routes_bp, url_prefix='/cmd')
app.register_blueprint(auth_bp, url_prefix='/auth')


if __name__ == '__main__':
    app.run(debug=True)
