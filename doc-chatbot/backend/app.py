from flask import Flask, request, Response
from flask_jwt_extended import JWTManager
from config import Config
from database import init_db
from routes.auth import auth_bp
from routes.docs import docs_bp

app = Flask(__name__)
app.config.from_object(Config)
JWTManager(app)

@app.before_request
def handle_options():
    if request.method == 'OPTIONS':
        response = Response()
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
        response.headers['Access-Control-Allow-Methods'] = 'GET,POST,PUT,DELETE,OPTIONS'
        return response

@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
    response.headers['Access-Control-Allow-Methods'] = 'GET,POST,PUT,DELETE,OPTIONS'
    return response

app.register_blueprint(auth_bp, url_prefix='/api/auth')
app.register_blueprint(docs_bp, url_prefix='/api/docs')

with app.app_context():
    init_db()

if __name__ == '__main__':
    app.run(debug=True)