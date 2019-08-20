"""
The flask application package.
"""

from flask import Flask, request
#from user import UserController 
from flask_restful import reqparse, abort, Api, Resource
from flask_cors import CORS
from functools import wraps
from jwt import encode, decode

app = Flask(__name__)
#cors = CORS(app, resources={r"/*": {"origins": "*"}})
CORS(app)

app.config['SECRET_KEY']='mySecretKey'

#def token_required(f):
#    @wraps(f)
#    def decorated(*args, **kwargs):
#        token = request.args.get('token'), 401
#        if not token:
#            return 'token is missing'
#        try:
#            data = decode(token, app.config['SECRET_KEY']), 403
#        except:
#            return 'token is invalid'
#        return f(*args, **kwargs)

import FlaskWebProject1.views
import FlaskWebProject1.todo
import FlaskWebProject1.userController
import FlaskWebProject1.coursesController


