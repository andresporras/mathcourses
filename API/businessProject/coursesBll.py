import coursesDll
import asyncio
import json
from bson import json_util, ObjectId
import random
import math
import BasicAlgebraBll
import PreCalculusBll
import GeometryBll
import CalculusBll
import Calculus2Bll
import LinearAlgebraBll
import TrigonometryBll
import ProbabilityBll

allExams = [
    [BasicAlgebraBll.exam1, BasicAlgebraBll.exam2],
    [PreCalculusBll.exam1, PreCalculusBll.exam2],
    [GeometryBll.exam1, GeometryBll.exam2],
    [CalculusBll.exam1, CalculusBll.exam2],
    [Calculus2Bll.exam1, Calculus2Bll.exam2],
    [LinearAlgebraBll.exam1, LinearAlgebraBll.exam2],
    [TrigonometryBll.exam1, TrigonometryBll.exam2],
    [ProbabilityBll.exam1, ProbabilityBll.exam2],
    ]

def getData():
    try:
        cursos = json.loads(json_util.dumps(coursesDll.getData()))
        for i in range(len(cursos)):
            for j in range(len(cursos[i]['units'])):
                cursos[i]['units'][j].update( {'selected' : 0} )
        return cursos
    except Exception as er:
        return er
def getQuetions(cursos):
    try:
        sExams = getSelected(cursos)
        questions=[]
        for x in range(12):
            indexExam =  random.randint(0,len(sExams)-1)
            exam = allExams[int(sExams[indexExam].course)-1][int(sExams[indexExam].unit)-1]
            q =  random.randint(0,len(exam)-1)
            item = str(exam[q]())
            questions.append(json.loads(item))
        return questions
    except Exception as er:
        return er
def getSelected(cursos):
    try:
        selected=[]
        for i in range(len(cursos)):
            curso=cursos[i]['cod']
            for j in range(len(cursos[i]['units'])):
                if cursos[i]['units'][j]['selected']==1:
                    unidad = cursos[i]['units'][j]['cod']
                    #obj = type('',(object,),{"course": curso, "unit": unidad})()
                    class obj: course=curso; unit=unidad
                    selected.append(obj)
        return selected
    except Exception as er:
        return er
    