import BasicAlgebraDll
import random
import coursesFunctionsBll
from fractions import Fraction
from flask import jsonify
import json
#question type (ax/b)+(c/d)=(e/f) and get the right vaue for x
def firstGradeEquation():
    divisor1 =  random.randint(1,10)*(random.randint(0,1)*2-1)
    dividend1 =  random.randint(1,10)
    divisor3 =  random.randint(1,10)*(random.randint(0,1)*2-1)
    dividend3 =  random.randint(1,10)
    allDividend = (divisor1/dividend1)-(divisor3/dividend3)
    if(allDividend==0):
        return firstGradeEquation()
    divisor2 =  random.randint(1,10)*(random.randint(0,1)*2-1)
    dividend2 =  random.randint(1,10)
    divisor4 =  random.randint(1,10)*(random.randint(0,1)*2-1)
    dividend4 =  random.randint(1,10)
    allDivisor = (divisor4/dividend4)-(divisor2/dividend2)
    
    sol = allDivisor/allDividend
    question = "("+str(divisor1)+"x/"+str(dividend1)+")+("+str(divisor2)+"/"+str(dividend2)+")=("+str(divisor3)+"x/"+str(dividend3)+")+("+str(divisor4)+"/"+str(dividend4)+")"
    solution = round(sol,2)
    options = coursesFunctionsBll.generateOptions(solution)
    jsonResponse = json.dumps({'question':question, 'solution':str(solution), 'options':options})
    return jsonResponse
#giving a function like f(x)=(ax/b)+(c/b) get f(x)^-1
def firstGradeTwoVariables():
    xDivisor = random.randint(1,10)*(random.randint(0,1)*2-1)
    xDividend = random.randint(1,10)
    cDivisor = random.randint(1,10)*(random.randint(0,1)*2-1)
    cDividend = random.randint(1,10)
    components = [xDividend*cDividend, -1*xDividend*cDivisor, cDividend*xDivisor]
    question = 'for f(x)=('+str(xDivisor)+'x/'+str(xDividend)+')+('+str(cDivisor)+'/'+str(cDividend)+') find f(x)^(-1)'
    solution = '[('+str(xDividend*cDividend)+'x+('+str(-1*xDividend*cDivisor)+')]/('+str(cDividend*xDivisor)+')=x'
    options = coursesFunctionsBll.generateTwoVariableOptions(components)
    return json.dumps({'question':question, 'solution':str(solution), 'options':options})
#for a function type ax^2 + bx+ c get the right (dx+e)(fx+g) factorization between the given options
def quadraticFactorizationType2():
    return coursesFunctionsBll.quadraticFactorization(False)
#for a function type ax^2 + bx+ c get the right (dx+e)(fx+g) factorization between the given options
def quadraticFactorizationType1():
    return coursesFunctionsBll.quadraticFactorization(True)
#for an area, with height equals to ax+b and a base equals to cx+d, get the x value wich solves the problem
def areaProblem():
    a = random.randint(1,100)
    b = random.randint(1,100)*(random.randint(0,1)*2-1)
    c = random.randint(10,100)*(-1)
    question = 'if a rectangle area is '+str(-1*c)+', its height is h and its width is equal to ('+str(a)+'h)+('+str(b)+'), which is the perimeter of this rectangle?:'
    solution1 = (-b+((b*b)-(4*a*c))**(0.5))/(2*a)
    solution2 = (-b-((b*b)-(4*a*c))**(0.5))/(2*a)
    solution = round((((solution1*a)+b)*2)+(solution1*2) if solution1>0 else (((solution2*a)+b)*2)+(solution2*2),2)
    options = coursesFunctionsBll.generateOptions(solution)
    jsonResponse = json.dumps({'question':question, 'solution':str(solution), 'options':options})
    return jsonResponse
#for a function like (ax+b)/(cx+d)= e choose the right range when x falls
def firstGradeFraction():
    xUp = random.randint(1,100)*(random.randint(0,1)*2-1)
    xDown = random.randint(1,100)*(random.randint(0,1)*2-1)
    cUp = random.randint(1,100)*(random.randint(0,1)*2-1)
    cDown = random.randint(1,100)*(random.randint(0,1)*2-1)
    cSolution = random.randint(1,100)*(random.randint(0,1)*2-1)
    sol = ((cSolution*cDown)-cUp)/(xUp-(cSolution*xDown))
    question = 'choose right range for x in [('+str(xUp)+'x)+('+str(cUp)+')]/[('+str(xDown)+'x)+('+str(cDown)+')]='+str(cSolution)
    solution = 'x is in range (-infinite,-15)' if (sol<-15) else 'x is in range [-15,-5]' if (sol>=-15 and sol<=-5) else 'x is in range (-5,5)' if (sol>-5 and sol<5) else 'x is in range [5,15]' if (sol>=5 and sol<=15) else 'x is in range (15,infinite)'
    options = json.dumps({'a':'x is in range (-infinite,-15)', 'b':'x is in range [-15,-5]', 'c': 'x is in range (-5,5)', 'd': 'x is in range [5,15]', 'e': 'x is in range (15,infinite)'})
    return json.dumps({'question':question, 'solution':str(solution), 'options':options})
#In a plant, the cost to produce x units is equal to ax^2+bx+c...
def plantProblem():
    a = random.randint(1,10)*(random.randint(0,1)*2-1)
    b = random.randint(1,10)*(random.randint(0,1)*2-1)
    c = random.randint(1,10)*(random.randint(0,1)*2-1)
    y = random.randint(10,100)
    if(a*(c-y)>=0):
        return plantProblem()
    question = 'In a plant, the cost to produce x units is equal to ('+str(a)+'x^2)+('+str(b)+'x)+('+str(c)+'), how many units can be produce with '+str(y)+'? choose the correct range for x value:'
    solution1 = (-b+((b*b)-(4*a*(c-y)))**(0.5))/(2*a)
    solution2 = (-b-((b*b)-(4*a*(c-y)))**(0.5))/(2*a)
    sol = round(solution1 if solution1>0 else solution2,2)
    solution = 'x is in range (0,1)' if (sol<1) else 'x is in range [1,3]' if (sol>=1 and sol<=3) else 'x is in range (3,6)' if (sol>3 and sol<6) else 'x is in range [6,10]' if (sol>=6 and sol<=10) else 'x is in range (10,infinite)'
    options = json.dumps({'a':'x is in range (0,1)', 'b':'x is in range [1,3]', 'c': 'x is in range (3,6)', 'd': 'x is in range [6,10]', 'e': 'x is in range (10,infinite)'})
    return json.dumps({'question':question, 'solution':str(solution), 'options':options})
#for a typical quadratic equation like ax^2 + bx + c determine if it has any solution
def secondGradeEquation():
    a = random.randint(1,100)*(random.randint(0,1)*2-1)
    b = random.randint(1,100)*(random.randint(0,1)*2-1)
    c = random.randint(1,100)*(random.randint(0,1)*2-1)
    solution='yes'
    if(((b**2)-4*a*c)<0):
        solution = 'no'
    question = 'On the next function ('+str(a)+'x^2)+('+str(b)+'x)+('+str(c)+')=0. Has x any solution?:'
    options = json.dumps({'1':'yes', '2':'no'})
    jsonResponse = json.dumps({'question':question, 'solution':str(solution), 'options':options})
    return jsonResponse
#given a ax^3 + bx^2 + cx + d get, from the given options, the right factorization (ex^2 + f)(gx + h)
def cubicFactorization():
    a = random.randint(1,10)*(random.randint(0,1)*2-1)
    b = random.randint(1,10)*(random.randint(0,1)*2-1)
    c = random.randint(1,10)*(random.randint(0,1)*2-1)
    d = random.randint(1,10)*(random.randint(0,1)*2-1)
    question = 'Find the right factorization for ('+str(a*c)+'x^3)+('+str(a*d)+'x^2)+('+str(b*c)+'x)+('+str(b*d)+'):'
    solution = '[('+str(a)+'x^2)+('+str(b)+')]*[('+str(c)+'x)+('+str(d)+')]'
    options = coursesFunctionsBll.generateAlternativesCubicF([a, b, c, d])
    jsonResponse = json.dumps({'question':question, 'solution':str(solution), 'options':options})
    return jsonResponse
#given a fractions like (ax+b)/(cx^2+dx+e) get the right equivalent partial fraction A/(fx+g) + B/(hx+i)
def partialFractions():
    bx = random.randint(1,10)*(random.randint(0,1)*2-1)
    bc = random.randint(1,10)*(random.randint(0,1)*2-1)
    cx = random.randint(1,10)*(random.randint(0,1)*2-1)
    cc = random.randint(1,10)*(random.randint(0,1)*2-1)
    if((bx/cx )== (bc/cc)):
        return partialFractions()
    ax = random.randint(1,10)*(random.randint(0,1)*2-1)
    ac = random.randint(1,10)*(random.randint(0,1)*2-1)
    dx2= (bx*cx)
    dx = (bx*cc)+(bc*cx)
    dc=(bc*cc)
    xComponents = [ax, cx, bx]
    cComponents = [ac, cc, bc]
    tempComponentValue = xComponents[1]
    for i in range(len(xComponents)):
        xComponents[i] =xComponents[i]*cComponents[1]/tempComponentValue
    for i in range(len(cComponents)):
        cComponents[i] =cComponents[i]-xComponents[i]
    tempComponentValue = cComponents[2]
    for i in range(len(cComponents)):
        cComponents[i] =cComponents[i]/tempComponentValue
    tempComponentValue = xComponents[2]
    for i in range(len(xComponents)):
        xComponents[i] =xComponents[i]-(cComponents[i]*tempComponentValue)
    tempComponentValue = xComponents[1]
    for i in range(len(xComponents)):
        xComponents[i] =xComponents[i]/tempComponentValue
    aSolution = round(xComponents[0],2)
    bSolution = round(cComponents[0],2)
    question = 'On the next function [('+str(ax)+'x)+('+str(ac)+')]/[('+str(dx2)+'x^2)+('+str(dx)+'x)+('+str(dc)+')], which of the next partial fraction is equivalent?:'
    solution ='('+str(aSolution)+')/[('+str(bx)+'x)+('+str(bc)+')] + ('+str(bSolution)+')/[('+str(cx)+'x)+('+str(cc)+')]'
    options = coursesFunctionsBll.generateAlternativesPF([aSolution, bx, bc, bSolution, cx, cc])
    jsonResponse = json.dumps({'question':question, 'solution':str(solution), 'options':options})
    return jsonResponse

listMethods =[secondGradeEquation, firstGradeEquation, firstGradeTwoVariables, firstGradeFraction, quadraticFactorizationType1, quadraticFactorizationType2, areaProblem, plantProblem, partialFractions, cubicFactorization]

def generateExam(unit):
    if(unit=='1'):
        return examUnitOne()
    elif(unit=='2'):
        return examUnitTwo()
    elif(unit=='3'):
        return examUnitThree()
    return ''
def examUnitOne():
    solution=''
    for x in range(12):
        question =  random.randint(1,len(listMethods))
        solution +='QUESTION N°'+str(x+1)+': '+ listMethods[question-1]()
    return solution
def examUnitTwo():
    return 'unit 2'
def examUnitThree():
    return 'unit 3'





