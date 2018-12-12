

from flask import Flask, request, jsonify, make_response
from flask_restful import reqparse, abort, Api, Resource
from FlaskWebProject1 import app
from pymongo import MongoClient
import datetime
import UserBll  
from jwt import encode, decode
import json
from munch import munchify
from functools import wraps
import smtplib

#UserBll.path.append(path.abspath('..\businessProject'))


#client = MongoClient('localhost', 27017)

#db = client['users']

#collection = db['userData']

api=Api(app)

defaultRoute='/user'


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers['x-access-token']
        if not token:
            return 'token is missing', 401
        try:
            data = decode(token, app.config['SECRET_KEY']), 403
            current_user='oscar'
        except:
            return 'token is invalid'
        return f(current_user, *args, **kwargs)
    return decorated


parser = reqparse.RequestParser()
parser.add_argument('task')

class UserController(Resource):
   # def get(self):
   #     return "welcome to my little world"
    #def post(self, param1):
    #    if param1=="validateUser":
    #        json_data = request.json
    #        nombre = json_data['nombre']
    #        password = json_data['password']
    #        c=collection.find_one({"nombre": nombre,"password": password})
    #        if c==None:
    #            return "-1"
    #        token = encode({'user': nombre, 'exp': datetime.datetime.utcnow()+datetime.timedelta(minutes=1)}, app.config['SECRET_KEY']);
    #        #return '''return default answer {}'''.format(c)
    #        return jsonify({'token':token.decode('UTF-8')})
    #    return '0'

    #def delete(self, todo_id, todo_id2):
    #    abort_if_todo_doesnt_exist(todo_id2)
    #    del TODOS[todo_id2]
    #    return '', 204

    #def put(self, todo_id,todo_id2):
    #    return '', 201
    @app.route(defaultRoute+'/doSomething', methods=['GET'])
    def doSomething():
        return 'something'
    @app.route(defaultRoute+'/doSomething2', methods=['POST'])
    def doSomething2():
        json_data = request.json
        nombre = json_data['nombre']
        password = json_data['password']
        return 'something'
    #https://stackoverflow.com/questions/26852128/smtpauthenticationerror-when-sending-mail-using-gmail-and-python
    @app.route(defaultRoute+'/signUp', methods=['POST'])
    def signUp():
        try:
            json_data = request.json
            nUsuario = munchify(request.json)
            result = UserBll.signUp(nUsuario)
        except Exception as er:
            return er
        if(result==1):
            token = encode({'user': nUsuario.usuario+'+'+nUsuario.password, 'exp': datetime.datetime.utcnow()+datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])
            return jsonify({'token':token.decode('UTF-8')})
        return jsonify({'token':'-1'})
    #@token_required
    @app.route(defaultRoute+'/createUser', methods=['POST'])
    def createUser():
        #nUsuario = UserModel
        nUsuario = munchify(request.json)
        return str(UserBll.createUser(nUsuario))
    @app.route(defaultRoute+'/loginUser', methods=['POST'])
    def loginUser():
        #nUsuario = UserModel
        nUsuario = munchify(request.json)
        x=2+2
        result = UserBll.loginUser(nUsuario)
        if(result==1):
            token = encode({'user': nUsuario.usuario+'+'+nUsuario.password, 'exp': datetime.datetime.utcnow()+datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])
            return jsonify({'token':token.decode('UTF-8')})
        return jsonify({'token':'-1'})
    #@token_required
    @app.route(defaultRoute+'/getUser', methods=['POST'])
    @token_required
    def getUser(self):
        #nUsuario = UserModel
        nUsuario = munchify(request.json)
        return str(UserBll.getUser(nUsuario))
        
        #password = json_data['password']
         


#api.add_resource(UserController, '/user/<param1>')

if __name__ == '__main__':
    app.run(debug=True)

    #ax^2+bx+c=0
    #x^2+(b/a)x = -(c/a)
    #x^2+(b/a)x + (b^2)/(4a^2)= (b^2)/(4a^2) -(c/a)
    #x^2+(b/a)x + (b^2)/(4a^2)= (b^2)/(4a^2) -(c/a)
    #(x+b/(2a))^2 = (b^2-4ac)/4a^2
    #x+b/(2a) = (b^2-4ac)^(1/2)/2a
    #x =- b/(2a) + (b^2-4ac)^(1/2)/2a
    #x = [-b+-(b^2-4ac)^(1/2)]/2a


#    var text = "";
#    var possible = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
  
#    for (var i = 0; i < 100; i++){
#      text += possible.charAt(Math.floor(Math.random() * possible.length));
#    }
#db.userData.insertOne(
#{
#"documento": "1112223334"
#,"nombre":"andres"
#, "apellido":"firminho"
#, "usuario":"andresf"
#, "password":"1234"
#, "idLogeo": text
#, "genero": "masculino"
#, "residencia": {"ciudad": "bogotá", "pais":"colombia"}
#, "lugarNacimiento": {"ciudad": "bogotá", "pais":"colombia"}
#, "correo1":"andres@andres"
#, "correo2":"andres2@andres2"
#, "fechaRegistro": new Date()
#, "fechaNacimiento": new Date("23-06-1991")
#})
