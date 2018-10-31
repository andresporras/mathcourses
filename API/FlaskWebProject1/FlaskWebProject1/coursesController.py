from flask import Flask, request, jsonify, make_response
from flask_restful import reqparse, abort, Api, Resource
from FlaskWebProject1 import app
import BasicAlgebraBll

api=Api(app)


defaultRoute='/courses'

class coursesController(object):
    """description of class"""
    @app.route(defaultRoute+'/generateExam', methods=['POST'])
    def generateExam():
        json_data = request.json
        course = json_data['course']
        unit = json_data['unit']
        if(course=='BasicAlgebra'):
            return BasicAlgebraBll.generateExam(unit)
        return 'course or unit invalid'


if __name__ == '__main__':
    app.run(debug=True)


