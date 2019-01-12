import random
import math
import coursesFunctionsBll
from fractions import Fraction
from flask import jsonify
import json
from sympy import *
#best solution ever: https://www.codecogs.com/latex/integration/htmlequations.php
#horizontal spaces in latex: https://tex.stackexchange.com/questions/74353/what-commands-are-there-for-horizontal-spacing
#vertical spaces: https://tex.stackexchange.com/questions/33370/adding-vertical-space-at-the-start-of-a-page
#init_session(use_latex=True)


#find the values of x for which slope is 0


def lineTanProblem():
    try:
        #w = symbols('w')
        #z ="𝑥 = (−𝑏 ± √(𝑏² − 4𝑎𝑐))⁄2𝑎"
        #Eq(z, z.doit())
        #z=symbols("z")
        #(a+pi)**2
        a = random.randint(2,10) * (random.randint(0,1) * 2 - 1)
        b = random.randint(2,10) * (random.randint(0,1) * 2 - 1)
        c = random.randint(2,10) * (random.randint(0,1) * 2 - 1)
        d = random.randint(2,10) * (random.randint(0,1) * 2 - 1)
        alpha = (b * 2) ** 2 - (4 * 3 * a * c)
        if alpha < 0:
            return lineTanProblem()
        sol1 = round((-(b * 2) + (alpha ** (1 / 2))) / (2 * 3 * a),4)
        sol2 = round((-(b * 2) - (alpha ** (1 / 2))) / (2 * 3 * a),4)
        solution = " When \(a \ne 0\), there are two solutions to \(ax^2 + bx + c = 0\) and they are $$ x={-b \pm \sqrt{b^2-4ac} \over 2a}.$$"
        question = '$$x = {-b \pm \sqrt{b^2-4ac} \over 2a}.$$'
        options = coursesFunctionsBll.twoXSolutions([sol1, sol2])
        jsonResponse = json.dumps({"question":question, "solution":solution, "options":options})
        return jsonResponse
    except Exception as er:
        return er

exam1 = [lineTanProblem]
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