from flask import Flask
from flask_cors import CORS
from flask_socketio import SocketIO

socketio = SocketIO()

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config.from_object("config.Config")

    from app.routes import main
    app.register_blueprint(main)

    socketio.init_app(app, cors_allowed_origins="*")

    return app