from flask import Flask, jsonify, request
from app.request_handler import get_user_list, create_user
from app.exc.emailError import emailError
from app.exc.nameOrMailInvalid import nameOrMailInvalid
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
    except emailError:
        return {'error': 'User already exists.'}, HTTPStatus.CONFLICT
    except nameOrMailInvalid:
        main_dict = {}
        if type(user_info["nome"]) != str:
            main_dict['nome'] = f"{type(user_info['nome'])}"
        if type(user_info['email']) != str:
            main_dict['email'] = f"{type(user_info['email'])}"
        return {"wrong fields": main_dict}, HTTPStatus.BAD_REQUEST
