from flask import Flask, jsonify, request
from app.request_handler import get_user_list, create_user
from app.exc.exception import error
from http import HTTPStatus

app = Flask(__name__)

@app.get('/user')
def get():
      return  jsonify(get_user_list()), HTTPStatus.OK

@app.post('/user')
def post():
    user_info =  request.get_json()
    try:
        return jsonify(create_user(user_info)), HTTPStatus.CREATED
    except error:
        return {'msg': 'da pra ter mais pessoa n'}, HTTPStatus.CONFLICT
