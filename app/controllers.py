from flask import Blueprint, request, jsonify
from app.bot_message import BotMessageController

main = Blueprint('main', __name__)

@main.route('/get-message', methods=['POST'])
def get_response():
    data = request.get_json()
    prompt = data.get('msg')

    if not prompt:
        return jsonify({'error': 'Mensagem vazia'}), 400

    bot_controller = BotMessageController()
    try:
        response = bot_controller.get_response(prompt)
        return jsonify({'response': response})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
