import random
import math
import coursesFunctionsBll
from fractions import Fraction
from flask import jsonify
import json

#find the values of x for which slope is 0
def lineTanProblem():
    try:
        a = random.randint(2,10)*(random.randint(0,1)*2-1)
        b = random.randint(2,10)*(random.randint(0,1)*2-1)
        c = random.randint(2,10)*(random.randint(0,1)*2-1)
        d = random.randint(2,10)*(random.randint(0,1)*2-1)
        alpha=(b*2)**2-(4*3*a*c)
        if alpha<0:
            return lineTanProblem()
        sol1 = round((-(b*2)+(alpha**(1/2)))/(2*3*a),4)
        sol2 = round((-(b*2)-(alpha**(1/2)))/(2*3*a),4)
        solution = "x1="+str(sol1)+" and x2="+str(sol2)
        question = "for which values of x the function ("+str(a)+"x^3)+("+str(b)+"x^2)+("+str(c)+"x)+("+str(d)+") has tangent equals to zero:"
        options = coursesFunctionsBll.twoXSolutions([sol1, sol2])
        jsonResponse = json.dumps({"question":question, "solution":solution, "options":options})
        return jsonResponse
    except Exception as er:
        return er

#find the values of x for which slope is 0
#use this: ln(x^y)=yln(x)
def logarithmProblem():
    try:
        a = random.randint(2,100)
        b = random.randint(2,100)*(random.randint(0,1)*2-1)
        sol= round(math.log(math.log(a))/math.log(math.e/a),4)
        solution=str(sol)
        question = "for which value of x the function (e^x)-("+str(a)+"^x)+("+str(b)+") has slope equals to zero:"
        options = coursesFunctionsBll.generateOptions(sol)
        jsonResponse = json.dumps({"question":question, "solution":solution, "options":options})
        return jsonResponse
    except Exception as er:
        return er

def productProblem():
    try:
        a = random.randint(2,100)
        b = random.randint(2,100)
        c = random.randint(2,100)
        log_c = round(math.log(c),4)
        solution= "x="+str(log_c)+"-ln(|("+str(a)+"x)+("+str(a+b)+")|)"
        question = "find equivalent expression to x where f(x)'="+str(c)+" if f(x)=("+str(a)+"x+("+str(b)+"))*e^x: "
        options = coursesFunctionsBll.productRuleOptions([log_c,a,a+b])
        jsonResponse = json.dumps({"question":question, "solution":solution, "options":options})
        return jsonResponse
    except Exception as er:
        return er

def divisionProblem():
    try:
        a = random.randint(2,10)
        b = random.randint(2,10)
        c = random.randint(2,10)
        d = random.randint(2,10)
        comp1 = round(a+(math.log(c)*b),4)
        comp2 = round(math.log(c)*a,4) 
        comp3 = round(1/math.log(c),4)
        comp4 = round(math.log(d)/math.log(c),4)
        solution= "x=ln(|["+str(comp1)+"-("+str(comp2)+"x)]^("+str(comp3)+")|)-"+str(comp4)
        question = "find equivalent expression to x where f(x)'="+str(d)+" if f(x)=("+str(a)+"x-("+str(b)+"))/"+str(c)+"^x: "
        options = coursesFunctionsBll.divisionRuleOptions([comp1, comp2, comp3, comp4])
        jsonResponse = json.dumps({"question":question, "solution":solution, "options":options})
        return jsonResponse
    except Exception as er:
        return er

exam1 =[lineTanProblem, logarithmProblem, productProblem, divisionProblem]
exam2 =[]
listMethods = [exam1, exam2]
def generateExam(unit):
    solution=[]
    lista = listMethods[int(unit)-1]
    for x in range(10):
        question =  random.randint(1,len(lista))
        #numberQuestion='QUESTION '+str(x+1)
        item = str(lista[question-1]())
        #jsonData = json.loads(json.dumps({numberQuestion: json.loads(item)}))
        solution.append(json.loads(item))
    return solution