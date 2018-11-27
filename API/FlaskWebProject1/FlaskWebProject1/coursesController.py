from flask import Flask, request, jsonify, make_response
from flask_restful import reqparse, abort, Api, Resource
from FlaskWebProject1 import app
import BasicAlgebraBll
import PreCalculusBll
import coursesBll
from bson import json_util, ObjectId
import json

api=Api(app)


defaultRoute='/courses'

class coursesController(object):
    """description of class"""
    @app.route(defaultRoute+'/generateExam', methods=['POST'])
    def generateExam():
        json_data = request.json
        course = json_data['course']
        unit = json_data['unit']
        if(course=='1'):
            return json.dumps(BasicAlgebraBll.generateExam(unit))
        elif(course=='2'):
            return json.dumps(PreCalculusBll.generateExam(unit))
        return 'course or unit invalid'
    @app.route(defaultRoute+'/getData', methods=['GET'])
    def getData():
        cursos = json.loads(json_util.dumps(coursesBll.getData()))
        return json.dumps(cursos)


if __name__ == '__main__':
    app.run(debug=True)


