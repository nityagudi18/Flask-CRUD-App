from flask import Flask
from routes import routes_bp
from cmd_routes import cmd_routes_bp
from authentication import auth_bp
from auth_cmd import auth_cmd_bp

# Initialize Flask Application
app = Flask(__name__)

# Secret key for session
app.config['SECRET_KEY'] = 'mysecretkey'

# Register Blueprints
app.register_blueprint(routes_bp, url_prefix='/')            # GUI routes
app.register_blueprint(cmd_routes_bp, url_prefix='/cmd')     # For command line routes
app.register_blueprint(auth_bp, url_prefix='/auth')          # Sign in, sign up, JWT, session
app.register_blueprint(auth_cmd_bp, url_prefix='/auth_cmd')  # To fetch token for command line


if __name__ == '__main__':
    app.run(debug=True)
