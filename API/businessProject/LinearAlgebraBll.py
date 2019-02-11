
import random
import math
import coursesFunctionsBll
from fractions import Fraction
from flask import jsonify
import json
from sympy import *


def matrixProblem():
    try:
        #below temp random solutions
        x1= round(random.randint(1,10) * (random.randint(0,1) * 2 - 1)/random.randint(1,10) * (random.randint(0,1) * 2 - 1),4)
        y1= round(random.randint(1,10) * (random.randint(0,1) * 2 - 1)/random.randint(1,10) * (random.randint(0,1) * 2 - 1),4)
        z1= round(random.randint(1,10) * (random.randint(0,1) * 2 - 1)/random.randint(1,10) * (random.randint(0,1) * 2 - 1),4)

        matrix = [[random.randint(1,10) * (random.randint(0,1) * 2 - 1),
                   random.randint(1,10) * (random.randint(0,1) * 2 - 1),
                   random.randint(1,10) * (random.randint(0,1) * 2 - 1),
                   random.randint(1,10) * (random.randint(0,1) * 2 - 1)],
                  [random.randint(1,10) * (random.randint(0,1) * 2 - 1),
                   random.randint(1,10) * (random.randint(0,1) * 2 - 1),
                   random.randint(1,10) * (random.randint(0,1) * 2 - 1),
                   random.randint(1,10) * (random.randint(0,1) * 2 - 1)],
                   [random.randint(1,10) * (random.randint(0,1) * 2 - 1),
                      random.randint(1,10) * (random.randint(0,1) * 2 - 1),
                      random.randint(1,10) * (random.randint(0,1) * 2 - 1),
                      random.randint(1,10) * (random.randint(0,1) * 2 - 1)]]
        Det= (matrix[0][0]*((matrix[1][1]*matrix[2][2])-(matrix[1][2]*matrix[2][1])))
        -(matrix[0][1]*((matrix[1][0]*matrix[2][2])-(matrix[1][2]*matrix[2][0])))
        +(matrix[0][2]*((matrix[1][0]*matrix[2][1])-(matrix[1][1]*matrix[2][0])))

        Detx = (matrix[0][3]*((matrix[1][1]*matrix[2][2])-(matrix[1][2]*matrix[2][1])))
        -(matrix[0][1]*((matrix[1][3]*matrix[2][2])-(matrix[1][2]*matrix[2][3])))
        +(matrix[0][2]*((matrix[1][3]*matrix[2][1])-(matrix[1][1]*matrix[2][3])))

        Dety= (matrix[0][0]*((matrix[1][3]*matrix[2][2])-(matrix[1][2]*matrix[2][3])))
        -(matrix[0][3]*((matrix[1][0]*matrix[2][2])-(matrix[1][2]*matrix[2][0])))
        +(matrix[0][2]*((matrix[1][0]*matrix[2][3])-(matrix[1][3]*matrix[2][0])))

        Detz= (matrix[0][0]*((matrix[1][1]*matrix[2][3])-(matrix[1][3]*matrix[2][1])))
        -(matrix[0][1]*((matrix[1][0]*matrix[2][3])-(matrix[1][3]*matrix[2][0])))
        +(matrix[0][3]*((matrix[1][0]*matrix[2][1])-(matrix[1][1]*matrix[2][0])))
        solution=""
        if Det==0:
            if Detx==0 and Dety==0 and Detz==0:
                solution="dependent system"
            else:
                solution= "inconsistent system"
        else:
            x1=round(Detx/Det,4)
            y1=round(Dety/Det,4)
            z1=round(Detz/Det,4)
            solution=r"x="+str(x1)+r", y="+str(y1)+r", z="+str(z1)
        matrix_=""
        matrix_sol=""
        for row in range(len(matrix)):
            for col in range(len(matrix[row])-1):
                matrix_=matrix_+r""+str(matrix[row][col])+(r" & " if (len(matrix[row])-2)!=col else r"")
            matrix_=matrix_+(r"\\" if (len(matrix)-1)!=row else r"")
            matrix_sol=matrix_sol+r""+str(matrix[row][len(matrix[row])-1])+(r"\\" if (len(matrix)-1)!=row else r"")

        question = r'find the x, y and z in the matrix \begin{bmatrix} '+str(matrix_)+r' \end{bmatrix} = \begin{bmatrix} '+str(matrix_sol)+r' \end{bmatrix}'
        alternatives = coursesFunctionsBll.multipleOptions([x1,y1,z1],3)
        tempAlternatives =[]
        for opt in range(3):
            tempAlternatives.append(r"x="+str(alternatives[opt][0])+r", y="+str(alternatives[opt][1])+r", z="+str(alternatives[opt][2]))
        options =json.loads(json.dumps({'a':tempAlternatives[0], 
                                        'b':tempAlternatives[1], 
                                        'c': tempAlternatives[2], 
                                        'd': "dependent system", 
                                        'e': "inconsistent system"}))
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return jsonResponse
    except Exception as er:
        return er

exam1 = [matrixProblem]
exam2 = []
listMethods = [exam1, exam2]
def generateExam(unit):
    solution = []
    lista = listMethods[int(unit) - 1]
    for x in range(10):
        question = random.randint(1,len(lista))
        #numberQuestion='QUESTION '+str(x+1)
        item = str(lista[question - 1]())
        #jsonData = json.loads(json.dumps({numberQuestion: json.loads(item)}))
        solution.append(json.loads(item))
    return solution

#integrate ((25-x^2)^(1/2))/(x)