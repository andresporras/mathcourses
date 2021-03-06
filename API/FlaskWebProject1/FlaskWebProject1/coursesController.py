from flask import Flask, request, jsonify, make_response
from flask_restful import reqparse, abort, Api, Resource
from FlaskWebProject1 import app
import BasicAlgebraBll
import PreCalculusBll
import coursesBll
import GeometryBll
import CalculusBll
import Calculus2Bll
import LinearAlgebraBll
import TrigonometryBll
import ProbabilityBll
import statisticsBll
import StatisticalInferenceBll
import discreteMathematicsBll
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
        elif(course=='3'):
            return json.dumps(GeometryBll.generateExam(unit))
        elif(course=='4'):
            return json.dumps(CalculusBll.generateExam(unit))
        elif(course=='5'):
            return json.dumps(Calculus2Bll.generateExam(unit))
        elif(course=='6'):
            return json.dumps(LinearAlgebraBll.generateExam(unit))
        elif(course=='7'):
            return json.dumps(TrigonometryBll.generateExam(unit))
        elif(course=='8'):
            return json.dumps(ProbabilityBll.generateExam(unit))
        elif(course=='9'):
            return json.dumps(statisticsBll.generateExam(unit))
        elif(course=='10'):
            return json.dumps(StatisticalInferenceBll.generateExam(unit))
        elif(course=='11'):
            return json.dumps(discreteMathematicsBll.generateExam(unit))
        return 'course or unit invalid'
    @app.route(defaultRoute+'/getData', methods=['GET'])
    def getData():
        cursos = coursesBll.getData()
        return json.dumps(cursos)
    @app.route(defaultRoute+'/mixExam', methods=['POST'])
    def mixExam():
        json_data = request.json
        selected = coursesBll.getQuetions(json_data)
        return json.dumps(selected)

if __name__ == '__main__':
    app.run(debug=True)


