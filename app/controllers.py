from flask import Blueprint, request, jsonify
from app.bot_message import BotMessageController

main = Blueprint('main', __name__)

@main.route('/get-message', methods=['POST'])
def get_response():
    """
    The function `get_response` processes a JSON request, retrieves a message prompt, uses a
    BotMessageController to generate a response, and returns the response or an error message.
    :return: The `get_response()` function returns a JSON response containing either the generated
    response from the `BotMessageController` or an error message if an exception occurs during the
    process. The response JSON object includes the key 'response' with the generated response
    or 'error'with the error message, along with the corresponding HTTP status code
    (200 for success, 400 for empty message, and 500 for internal error)
    """
    data = request.get_json()
    prompt = data.get('msg')
    file_name = data.get('filename')

    if not prompt:
        return jsonify({'error': 'Mensagem vazia'}), 400

    bot_controller = BotMessageController()
    try:
        response = bot_controller.get_response(prompt, file_name)
        return jsonify({'response': response})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@main.route('/save-file', methods=['POST'])
def save_file():
    """
    The `save_file` function in Python receives JSON data, extracts file name and Excel dictionary,
    saves the file using a BotMessageController, and returns a success message or error if any.
    :return: returns a JSON response containing either a success message with
    the file saved successfully or an error message if an exception occurs during the file saving
    process.
    """
    data = request.get_json()
    file_name = data.get('file_name')
    excel_dict = data.get('excel_dict')

    if not data:
        return jsonify({'error': "Mensagem vaazia"}), 400

    bot_controller = BotMessageController()

    try:
        response = bot_controller.save_file(file_name, excel_dict)
        return jsonify({'response': f"Arquivo salvo com sucesso: {response}"})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
