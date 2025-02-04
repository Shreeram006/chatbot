from flask import Blueprint, render_template
from app.services.model_factory import ModelFactory
from app import socketio

main = Blueprint("main", __name__)

@main.route("/")
def home():
    return render_template("index.html")

@socketio.on('user_message')
def handle_user_message(data):
    user_input = data.get('message')
    if not user_input:
        return

    # Broadcast user message to all clients
    socketio.emit('new_message', {'content': user_input, 'is_user': True})
    
    # Generate bot response
    model_factory = ModelFactory()
    gemini_model = model_factory.get_model("gemini")
    bot_response = gemini_model.generate_response(user_input)
    
    # Broadcast bot response to all clients
    socketio.emit('new_message', {'content': bot_response, 'is_user': False})