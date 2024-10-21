from flask import Flask, render_template, url_for, request, jsonify, send_from_directory
from flask_cors import CORS
import json

#Get data from database
def getData():
    with open('db.json', 'r', encoding='utf-8') as file:
        data = json.loads(file.read())
        
    return data['menu']



app = Flask(__name__)

CORS(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/contact', methods=['POST'])
def contact():
    data = request.get_json()
    print(data)
    return jsonify(data)


@app.route('/api/menu')
def menu():
    data = getData()
    return jsonify(data)


@app.route('/<path:filename>')
def send_file(filename):
    return send_from_directory('static', filename)



if "__main__" == __name__:
    app.run(debug=True)