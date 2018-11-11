import random
import math
import coursesFunctionsBll
from fractions import Fraction
from flask import jsonify
import json

#the force acting on an object is equal to at^2+bt+c
#which of the next options is not a valid time when the magnitude of force was equal to d
def seriesProblem():
    try:
        addNumber = random.randint(1,5)*(random.randint(0,1)*2-1)
        opNumber = random.randint(1,5)*(random.randint(0,1)*2-1)
        a = random.randint(1,3)
        sequence=[]
        if(a==1):
            for x in range(6):
                sequence.append(addNumber+(opNumber*(x)))
        elif(a==2):
            for x in range(6):
                sequence.append(addNumber+(opNumber**(x)))
        else:
            for x in range(6):
                sequence.append(addNumber+((x)**abs(opNumber)))
        subList = [str(sequence[index]) for index in range(5)]
        question = "which is the next number in the series "+(', '.join(subList))+"..."
        sol = sequence[5]
        solution= str(sol)
        options = coursesFunctionsBll.alternativesSequence(sol)
        jsonResponse = json.dumps({'question':question, 'solution':solution, 'options':options})
        return jsonResponse
    except Exception as er:
        return er

#the force acting on an object is equal to at^2+bt+c
#which of the next options is not a valid time when the magnitude of force was equal to d
def typeSeriesProblem():
    try:
        addNumber = random.randint(1,5)*(random.randint(0,1)*2-1)
        opNumber = random.randint(1,5)*(random.randint(0,1)*2-1)
        a = random.randint(1,3)
        function=""
        solution=""
        if(a==1):
            function=str(addNumber)+"+("+str(opNumber)+"x)"
            solution = "decreasing" if opNumber<0 else "increasing"
        elif(a==2):
            function=str(addNumber)+"+(("+str(opNumber)+")^x)"
            solution = "alterning" if opNumber<0 else "increasing"
        else:
            function=str(addNumber)+"+(x^("+str(opNumber)+"))"
            solution = "decreasing" if opNumber<0 else "increasing"
        question = "for de next function  "+function+", define the series type when x tends to infinity"
        options =json.dumps({'a':'increasing', 'b':'decreasing', 'c':'alterning'})
        jsonResponse = json.dumps({'question':question, 'solution':solution, 'options':options})
        return jsonResponse
    except Exception as er:
        return er

exam1 =[seriesProblem, typeSeriesProblem]
exam2 =[]
listMethods = [exam1, exam2]
def generateExam(unit):
    solution=''
    lista = listMethods[int(unit)-1]
    for x in range(12):
        question =  random.randint(1,len(lista))
        solution +='QUESTION N°'+str(x+1)+': '+ lista[question-1]()
    return solution