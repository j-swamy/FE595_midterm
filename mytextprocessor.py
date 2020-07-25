from flask import Flask
from flask import request
from flask import jsonify
from flask import make_response
from flask_restful import reqparse
from textblob.compat import unicode
from werkzeug.exceptions import abort
import textanalyzer as ta

app = Flask(__name__)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route("/analyze", methods=['POST'])
def analyze_text():
    if not request.json:
        abort(400)
    if 'text' in request.json and type(request.json['text']) is not unicode:
        abort(400)
    text = request.json.get('text')
    result = []
    parser = reqparse.RequestParser()
    parser.add_argument('op', action='append')
    for op in parser.parse_args()['op']:
        if op == "sentiment":
            sentiment = ta.get_sentiment(text)
            result.append({"sentiment": sentiment})
        elif op == "tags":
            tags = ta.get_tags(text)
            result.append({"tags": tags})
        else:
            abort(400)
    return jsonify(result), 201


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8088)
