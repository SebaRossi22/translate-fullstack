from flask import Flask, jsonify, request
from flask_cors import CORS
from googletrans import Translator

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/translate', methods=['GET', 'POST'])
def all_books():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        translator = Translator()
        translated = translator.translate(post_data.get('text'), src='en', dest='it')
        response_object['translation'] = str(translated.text)
    return jsonify(response_object)

if __name__ == '__main__':
    app.run()
