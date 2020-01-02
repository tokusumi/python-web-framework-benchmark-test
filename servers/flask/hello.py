from flask import Flask, jsonify, request
app = Flask(__name__)


@app.route('/')
def hello():
    return jsonify({"text": "hello world!"}), 200


@app.route('/query')
def hello_query():
    ids = request.args.get('id')
    return jsonify({"text": f"hello world, {ids}!"}), 200


if __name__ == '__main__':
    app.run(debug=False)
