from flask import Flask  # type: ignore[import]
from flask_jwt_extended import JWTManager  # type: ignore[import]
from config import Config
from database import init_db
from routes.auth import auth_bp
from routes.docs import docs_bp
app = Flask(__name__)
app.config.from_object(Config)

JWTManager(app)

@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
    response.headers['Access-Control-Allow-Methods'] = 'GET,POST,PUT,DELETE,OPTIONS'
    return response

app.register_blueprint(auth_bp, url_prefix='/api/auth')
app.register_blueprint(docs_bp, url_prefix='/api/docs')

@app.route('/')
def home():
    return {"message": "AI Document Chatbot API is running!", "status": "ok"}

with app.app_context():
    init_db()

if __name__ == '__main__':
    app.run(debug=True)