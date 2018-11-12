import random
import math
import coursesFunctionsBll
from fractions import Fraction
from flask import jsonify
import json

#choose the right number to follow the series
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

#for the function define the type of series when x tends to infinity
def typeSeriesProblem():
    try:
        addNumber = random.randint(1,5)*(random.randint(0,1)*2-1)
        opNumber = random.randint(1,5)*(random.randint(0,1)*2-1)
        a = random.randint(1,6)
        function=""
        solution=""
        if(a==1):
            function=str(addNumber)+"+("+str(opNumber)+"x)"
            solution = "decreasing" if opNumber<0 else "increasing"
        elif(a==2):
            function=str(addNumber)+"+(("+str(opNumber)+")^x)"
            solution = "alterning" if opNumber<0 else "increasing"
        elif(a==3):
            function=str(addNumber)+"+(x^("+str(opNumber)+"))"
            solution = "decreasing" if opNumber<0 else "increasing"
        elif(a==4):
          function=str(addNumber)+"+ln("+str(opNumber)+"x)"
          solution = "undefined" if opNumber<0 else "increasing"
        elif(a==5):
            function=str(addNumber)+"+ln(("+str(opNumber)+")^x)"
            solution = "undefined" if opNumber<0 else "increasing"
        else:
            function=str(addNumber)+"+ln(x^("+str(opNumber)+"))"
            solution = "decreasing" if opNumber<0 else "increasing"
        question = "for de next function  "+function+", define the series type when x tends to infinity"
        options =json.dumps({'a':'increasing', 'b':'decreasing', 'c':'alterning', 'd':'undefined'})
        jsonResponse = json.dumps({'question':question, 'solution':solution, 'options':options})
        return jsonResponse
    except Exception as er:
        return er
#for the function define the type of series
def boundedSeriesProblem():
    try:
        a = random.randint(1,5)*(random.randint(0,1)*2-1)
        b = random.randint(1,5)*(random.randint(0,1)*2-1)
        c = random.randint(1,5)*(random.randint(0,1)*2-1)
        op = random.randint(1,6)
        function=""
        solution=""
        if(op==1):
            function=str(a)+"*(x^"+str(abs(b*2))+")"
            solution = "superior bounded" if a<0 else "inferior bounded"
        elif(op==2):
            function=str(a)+"*ln("+str(b)+"x)"
            solution = "superior bounded" if a>0 else "inferior bounded"
        elif(op==3):
            function=str(abs(a))+"/((x+("+str(b)+"))^("+str(c)+"))"
            solution = "not bounded" if c%2==0 else "inferior bounded"
        elif(op==4):
            function=str(abs(a))+"/(("+str(b)+")^(x+"+str(c)+"))"
            solution = "not bounded" if b<0 else "inferior bounded"
        elif(op==5):
            function=str(abs(a))+"x/(("+str(abs(b))+")+("+str(c)+"x^2))"
            solution = "not bounded" if c<0 else "bounded"
        else:
            function="cos(x)*(sin(x)^("+str(a)+"))"
            solution = "not bounded" if a<0 else "bounded"
        question = "for de next function  "+function+", define the series type"
        options =json.dumps({'a':'inferior bounded', 'b':'superior bounded', 'c':'not bounded', 'd':'bounded'})
        jsonResponse = json.dumps({'question':question, 'solution':solution, 'options':options})
        return jsonResponse
    except Exception as er:
        return er
exam1 =[seriesProblem, typeSeriesProblem, boundedSeriesProblem]
exam2 =[]
listMethods = [exam1, exam2]
def generateExam(unit):
    solution=''
    lista = listMethods[int(unit)-1]
    for x in range(12):
        question =  random.randint(1,len(lista))
        solution +='QUESTION N°'+str(x+1)+': '+ lista[question-1]()
    return solution