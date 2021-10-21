from flask import Flask
from routes import routes_bp

# Initialize Flask Application
app = Flask(__name__)

# Register Blueprints
app.register_blueprint(routes_bp, url_prefix='/')


if __name__ == '__main__':
    app.run()
