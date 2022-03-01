from flask import request, jsonify
from app import app


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print("<Request: {}>".format(request.json))
    return "Welcome"


@app.route('/api/v1', methods=['GET', 'POST'])
def api1():
    if request.method == 'GET':
        construct = {
            'error': [],
            'success': True,
            'API_type' :'GET'
        }
        response = jsonify(construct)
        response.status_code = 200
    elif request.method == 'POST':
        construct = {
            'error': [],
            'success': True,
            'API_type' :'POSt'
        }
        response = jsonify(construct)
        response.status_code = 200
    return response