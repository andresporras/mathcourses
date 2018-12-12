import BasicAlgebraDll
import random
import math
import coursesFunctionsBll
from fractions import Fraction
from flask import jsonify
import json
#https://aerodynamics.lr.tudelft.nl/~rdwight/work_multiple_choice_code.html useful link for latex format
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
    solution = round(sol,4)
    options = coursesFunctionsBll.generateOptions(solution)
    jsonResponse = json.dumps({"question":question, "solution":solution, "options":options})
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
    jsonResponse = json.dumps({"question":question, "solution":solution, "options":options})
    return jsonResponse
#for a function type ax^2 + bx+ c get the right (dx+e)(fx+g) factorization between the given options
def quadraticFactorizationType2():
    return coursesFunctionsBll.quadraticFactorization(False)
#for a function type ax^2 + bx+ c get the right (dx+e)(fx+g) factorization between the given options
def quadraticFactorizationType1():
    return coursesFunctionsBll.quadraticFactorization(True)
#for an rectangle, with height equals to x and a base equals to cx+d, get the perimeter of the rectangle
def areaProblem():
    a = random.randint(1,100)
    b = random.randint(1,100)*(random.randint(0,1)*2-1)
    c = random.randint(10,100)*(-1)
    question = 'if a rectangle area is '+str(-1*c)+', its height is h and its width is equal to ('+str(a)+'h)+('+str(b)+'), which is the perimeter of this rectangle?:'
    solution1 = (-b+((b*b)-(4*a*c))**(0.5))/(2*a)
    solution2 = (-b-((b*b)-(4*a*c))**(0.5))/(2*a)
    solution = round(solution1*4, 4) if solution1>0 else round(solution2,4)
    options = coursesFunctionsBll.generateOptions(solution)
    jsonResponse = json.dumps({"question":question, "solution":solution, "options":options})
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
    options = json.loads(json.dumps({'a':'x is in range (-infinite,-15)', 'b':'x is in range [-15,-5]', 'c': 'x is in range (-5,5)', 'd': 'x is in range [5,15]', 'e': 'x is in range (15,infinite)'}))
    jsonResponse = json.dumps({"question":question, "solution":solution, "options":options})
    return jsonResponse 
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
    sol = round(solution1 if solution1>0 else solution2,4)
    solution = 'x is in range (0,1)' if (sol<1) else 'x is in range [1,3]' if (sol>=1 and sol<=3) else 'x is in range (3,6)' if (sol>3 and sol<6) else 'x is in range [6,10]' if (sol>=6 and sol<=10) else 'x is in range (10,infinite)'
    options = json.loads(json.dumps({'a':'x is in range (0,1)', 'b':'x is in range [1,3]', 'c': 'x is in range (3,6)', 'd': 'x is in range [6,10]', 'e': 'x is in range (10,infinite)'}))
    jsonResponse = json.dumps({"question":question, "solution":solution, "options":options})
    return jsonResponse
#for a typical quadratic equation like ax^2 + bx + c determine if it has any solution
def secondGradeEquation():
    a = random.randint(1,100)*(random.randint(0,1)*2-1)
    b = random.randint(1,100)*(random.randint(0,1)*2-1)
    c = random.randint(1,100)*(random.randint(0,1)*2-1)
    solution='Yes'
    if(((b**2)-4*a*c)<0):
        solution = 'No'
    question = 'On the next function ('+str(a)+'x^2)+('+str(b)+'x)+('+str(c)+')=0. Has x any solution?:'
    options = json.loads(json.dumps({"1":"Yes", "2":"No"}))
    jsonResponse = json.dumps({"question":question, "solution":solution, "options":options})
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
    jsonResponse = json.dumps({"question":question, "solution":solution, "options":options})
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
    aSolution = round(xComponents[0],4)
    bSolution = round(cComponents[0],4)
    question = 'On the next function [('+str(ax)+'x)+('+str(ac)+')]/[('+str(dx2)+'x^2)+('+str(dx)+'x)+('+str(dc)+')], which of the next partial fraction is equivalent?:'
    solution ='('+str(aSolution)+')/[('+str(bx)+'x)+('+str(bc)+')] + ('+str(bSolution)+')/[('+str(cx)+'x)+('+str(cc)+')]'
    options = coursesFunctionsBll.generateAlternativesPF([aSolution, bx, bc, bSolution, cx, cc])
    jsonResponse = json.dumps({"question":question, "solution":solution, "options":options})
    return jsonResponse
#given an inequation like (ax+b)/c <=(dx+e)/f, define the solution range for x
def inequations1():
    a = random.randint(1,100)*(random.randint(0,1)*2-1)
    b = random.randint(1,100)*(random.randint(0,1)*2-1)
    c = random.randint(1,100)*(random.randint(0,1)*2-1)
    d = random.randint(1,100)*(random.randint(0,1)*2-1)
    e = random.randint(1,100)*(random.randint(0,1)*2-1)
    f = random.randint(1,100)*(random.randint(0,1)*2-1)
    if(((a*f)-(d*c))==0):
        return inequations1()
    question = 'let x alone in the next inequality [('+str(a)+'x)+('+str(b)+')]/('+str(c)+') <= [('+str(d)+'x)+('+str(e)+')]/('+str(f)+')'
    sol = round(((e*c)-(b*f))/((a*f)-(d*c)),4)
    solution ='x'+('<=' if (((a*f)-(d*c))*c*f>=0) else '>=')+str(sol)
    options = coursesFunctionsBll.inequationsAlternatives1(sol)
    jsonResponse = json.dumps({"question":question, "solution":solution, "options":options})
    return jsonResponse

#given an inequation like (ax+b)/(cx+d)>0 get the right range
def rationalInequations():
    try:
        a = random.randint(1,100)*(random.randint(0,1)*2-1)
        b = random.randint(1,100)*(random.randint(0,1)*2-1)
        c = random.randint(1,100)*(random.randint(0,1)*2-1)
        d = random.randint(1,100)*(random.randint(0,1)*2-1)
        range = []
        range1 = [-1000, -b/a] if a>0 else [-b/a, 1000]
        range2 = [-1000, -d/c] if c>0 else [-d/c, 1000]
        range3 = [-b/a, 1000] if a>0 else [-1000, -b/a]
        range4 = [-d/c, 1000] if c>0 else [-1000, -d/c]
        intersect_range1 = [range1[0] if range1[0]>range2[0] else range2[0], range1[1] if range1[1]<range2[1] else range2[1]]
        intersect_range2 = [range3[0] if range3[0]>range4[0] else range4[0], range3[1] if range3[1]<range4[1] else range4[1]]
        union_range= []
        solution=""
        if(intersect_range1[0]<intersect_range1[1]):
            union_range.append(intersect_range1)
        if(intersect_range2[0]<intersect_range2[1]):
            union_range.append(intersect_range2)
        if(len(union_range)==0):
            solution="no solution"
        if(len(union_range)==1):
            solution='('+(str(round(union_range[0][0],4)) if union_range[0][0]!=-1000 else '-'+str(math.inf))+','+(str(round(union_range[0][1],4)) if union_range[0][1]!=1000 else str(math.inf))+')'
        if(len(union_range)==2):
            min_range = [union_range[0][0] if union_range[0][0]>union_range[1][0] else union_range[1][0], union_range[0][1] if union_range[0][1]<union_range[1][1] else union_range[1][1]]
            if(min_range[0]>min_range[1]):
                if(union_range[0][0]<union_range[1][0]):
                    solution = '('+(str(round(union_range[0][0],4)) if union_range[0][0]!=-1000 else '-'+str(math.inf))+','+(str(round(union_range[0][1],4)) if union_range[0][1]!=1000 else str(math.inf))+') U ('+(str(round(union_range[1][0],4)) if union_range[1][0]!=-1000 else '-'+str(math.inf))+','+(str(round(union_range[1][1],4)) if union_range[1][1]!=1000 else str(math.inf))+')'
                else:
                    solution = '('+(str(round(union_range[1][0],4)) if union_range[1][0]!=-1000 else '-'+str(math.inf))+','+(str(round(union_range[1][1],4)) if union_range[1][1]!=1000 else str(math.inf))+') U ('+(str(round(union_range[0][0],4)) if union_range[0][0]!=-1000 else '-'+str(math.inf))+','+(str(round(union_range[0][1],4)) if union_range[0][1]!=1000 else str(math.inf))+')'
            else:
                max_range = [union_range[0][0] if union_range[0][0]<union_range[1][0] else union_range[1][0], union_range[0][1] if union_range[0][1]>union_range[1][1] else union_range[1][1]]
                solution='('+(str(round(max_range[0],4)) if max_range[0]!=-1000 else '-'+str(math.inf))+','+(str(round(max_range[1],4)) if max_range[1]!=1000 else str(math.inf))+')'
        question = 'Which is the right range for x in the next inequality?: [('+str(a)+'x)+('+str(b)+')]/[('+str(c)+'x)+('+str(d)+')]>0'
        options = coursesFunctionsBll.rationalInequations([intersect_range1, intersect_range2])
        jsonResponse = json.dumps({"question":question, "solution":solution, "options":options})
        return jsonResponse
    except Exception as er:
        return er
#given an inequation like a<=(bx+c)/d<=e determine if it has any valid solution
def inequationTwoSides():
    try:
        a = random.randint(1,100)*(random.randint(0,1)*2-1)
        b = random.randint(1,100)*(random.randint(0,1)*2-1)
        c = random.randint(1,100)*(random.randint(0,1)*2-1)
        d = random.randint(1,100)*(random.randint(0,1)*2-1)
        e = random.randint(1,100)*(random.randint(0,1)*2-1)
        sol1 = ((a*d)-c)/b
        sol2 = ((e*d)-c)/b
        solution='No'
        if((sol1<=sol2 and b*c>0) or (sol1>=sol2 and b*c<0)):
            solution='Yes'
        question = 'for the next inequation, has x any valid solution?: '+str(a)+'<=[('+str(b)+'x)+('+str(c)+')]/('+str(d)+')<='+str(e)
        options = json.dumps({"1":"yes", "2":"no"})
        jsonResponse = json.dumps({"question":question, "solution":solution, "options":options})
        return jsonResponse
    except Exception as er:
        return er
#get the valid range for x in the inequation type (ax+b)/c <= (dy+e)/(fy+g)
def inequations2():
    a = random.randint(1,10)*(random.randint(0,1)*2-1)
    b = random.randint(1,10)*(random.randint(0,1)*2-1)
    c = random.randint(1,10)*(random.randint(0,1)*2-1)
    d = random.randint(1,10)*(random.randint(0,1)*2-1)
    e = random.randint(1,10)*(random.randint(0,1)*2-1)
    f = random.randint(1,10)*(random.randint(0,1)*2-1)
    g = random.randint(1,10)*(random.randint(0,1)*2-1)
    sola = (d*c)-(b*f)
    solb = (e*c)-(b*g)
    solc = a*f
    sold = a*g
    solution = 'x'+('<=' if a*c>0 else '>=')+'[('+str(sola)+'y)+('+str(solb)+')]/[('+str(solc)+'y)+('+str(sold)+')]'
    question = 'let x alone in the next inequality [('+str(a)+'x)+('+str(b)+')]/('+str(c)+') <= [('+str(d)+'y)+('+str(e)+')]/[('+str(f)+'y)+('+str(g)+')]'
    options = coursesFunctionsBll.inequationsAlternatives2([sola, solb, solc, sold])
    jsonResponse = json.dumps({"question":question, "solution":solution, "options":options})
    return jsonResponse
#given a problem like ax^2 +bx + c>=0 determina the valid range for x
def inequationGrade2():
    try:
        a = random.randint(1,10)*(random.randint(0,1)*2-1)
        b = random.randint(1,10)*(random.randint(0,1)*2-1)
        c = random.randint(1,10)*(random.randint(0,1)*2-1)
        deriv = -b/(2*a)
        minMax = (a*(deriv**2))+(b*deriv)+c
        sol1= (random.randint(1,100)*(-1))+deriv
        sol2= random.randint(1,100)+deriv
        solution=''
        if(((b**2)-(4*a*c))<=0):
            if(minMax>0):
                solution='(-inf,inf)'
            elif(minMax==0):
                solution='('+str(round(deriv,4))+')'
            else:
                solution='(void)'
        else:
            sol1= (-b+((b**2)-(4*a*c))**(0.5))/(2*a)
            sol2= (-b-((b**2)-(4*a*c))**(0.5))/(2*a)
            if(minMax>0):
                solution= '('+str(round(sol1 if sol1<sol2 else sol2, 4))+','+str(round(sol1 if sol1>sol2 else sol2, 4))+')'
            else:
                solution = '(-inf, '+str(round(sol1 if sol1<sol2 else sol2, 4))+') U ('+str(round(sol1 if sol1>sol2 else sol2, 4))+',inf)'
        question = 'for the next inequation, define the valid range for x: ('+str(a)+'x^2)+('+str(b)+'x)+('+str(c)+')>=0'
        options = coursesFunctionsBll.inequationGrade2([deriv, sol1, sol2])
        jsonResponse = json.dumps({"question":question, "solution":solution, "options":options})
        return jsonResponse
    except Exception as er:
        return er
#using the final disntant formula for constant accelerated object (df = (1/2)ax^2 + vx + di) define the range of time where a car equals or surpass a distance x having the acceleration and the initial speed
def inequationProblem1():
    try:
        acceleration = random.randint(1,10)*(random.randint(0,1)*2-1)
        velocity = random.randint(1,10)*(random.randint(0,1)*2-1)
        distance = random.randint(1,100)
        a = acceleration/2
        b = velocity
        c = (-1)*distance
        deriv = -b/(2*a)
        if(deriv<0):
            inequationProblem1()
        minMax = (a*(deriv**2))+(b*deriv)+c
        sols = [random.randint(1,10),random.randint(11,20)]
        solution=''
        if(((b**2)-(4*a*c))<=0):
            if(minMax>0):
                solution='(0,inf)'
            elif(minMax==0):
                solution='('+str(round(deriv,4))+')'
            else:
                solution='(void)'
        else:
            sol1= (-b+((b**2)-(4*a*c))**(0.5))/(2*a)
            sol2= (-b-((b**2)-(4*a*c))**(0.5))/(2*a)
            sols = [sol1,sol2]
            sols.sort()
            if(sols[0]<0):
                solution = '('+str(round(sols[1],4))+',inf)'
            elif(minMax>0):
                solution= '('+str(round(sols[0], 4))+','+str(round(sols[1], 4))+')'
            else:
                solution = '(0, '+str(round(sols[0], 4))+') U ('+str(round(sols[1], 4))+',inf)'
        question = 'a car is moving with constant acceleration of '+str(acceleration)+'m/s^2 and initial speed of '+str(velocity)+'m/s, on which range of time (in seconds) the car equals or surpass the distance of '+str(distance)+' meters?. PS: Use the final distance formula for objects with constant acceleration'
        options = coursesFunctionsBll.inequationProblem1([deriv, sols[0], sols[1]])
        jsonResponse = json.dumps({"question":question, "solution":solution, "options":options})
        return jsonResponse
    except Exception as er:
        return er
#the final note of a math college course is define by 3 notes, the first two with equal value, and the final exam which is the n% of the course
#given the first two notes and the percentage  for the exam note, which should be the exam note so the student get Acceptable note
#a student get acceptable note when the final note of the course is betweeen 60% and 80%
def inequationProblem2():
    try:
        nota1 = random.randint(1,100)
        nota2 = random.randint(1,100)
        percentage = random.randint(40,60)
        rangoMenor= (12000-(100*nota1)+(nota1*percentage)-(100*nota2)+(nota2*percentage))/(2*percentage)
        rangoMayor= (16000-(100*nota1)+(nota1*percentage)-(100*nota2)+(nota2*percentage))/(2*percentage)
        solution=''
        if(rangoMayor<0):
            solution='student already lost the course'
        elif(rangoMenor>100):
            solution='student already surpassed the acceptable note (>80)'
        else:
            solution='('+str(round(rangoMenor if rangoMenor>=0 else 0,4))+','+str(round(rangoMayor if rangoMayor<=100 else 100,4))+')'
        question = 'On a math course, the note is defined for two notes with same value and the final exam which value is '+str(percentage)+'% of the course. If a student get '+str(nota1)+' in the first note and '+str(nota2)+' for the second note, which note student should achieve in the final exam in order to get acceptable note (betwen 60& and 80% of the course)?'
        rangoMenor = rangoMenor if rangoMenor>0 else 0
        rangoMayor = rangoMayor if rangoMayor<100 else 100
        options = coursesFunctionsBll.inequationProblem2([rangoMenor, rangoMayor])
        jsonResponse = json.dumps({"question":question, "solution":solution, "options":options})
        return jsonResponse
    except Exception as er:
        return er
#get the two solutions for x on |(ax+b)/(cx+d)| = c
def absoluteValue1():
    try:
        a = random.randint(1,100)*(random.randint(0,1)*2-1)
        b = random.randint(1,100)*(random.randint(0,1)*2-1)
        c = random.randint(1,100)*(random.randint(0,1)*2-1)
        d = random.randint(1,100)*(random.randint(0,1)*2-1)
        e = random.randint(1,100)
        sol1 = ((d*e)-b)/(a-(e*c))
        sol2 = ((d*(-e))-b)/(a-((-e)*c))
        solution=''+str(round(sol1,4))+','+str(round(sol2,4))+''
        question = 'which are the two solutions for |[('+str(a)+'x)+('+str(b)+')]/[('+str(c)+'x)+('+str(d)+')]|='+str(e)+''
        options = coursesFunctionsBll.absoluteValue1([round(sol1,4), round(sol2,4)])
        jsonResponse = json.dumps({"question":question, "solution":solution, "options":options})
        return jsonResponse
    except Exception as er:
        return er
#get the range of solutions for x on |(ax+b)/c| < d
def absoluteValue2():
    try:
        a = random.randint(1,100)*(random.randint(0,1)*2-1)
        b = random.randint(1,100)*(random.randint(0,1)*2-1)
        c = random.randint(1,100)*(random.randint(0,1)*2-1)
        d = random.randint(1,100)
        solPos = round(((d*c)-b)/a if a*c>0 else (((-d)*c)-b)/a,4)
        solNeg = round((((-d)*c)-b)/a if a*c>0 else ((d*c)-b)/a,4)
        solution=''
        if(solNeg>solPos):
            solution='(null)'
        else:
            solution=''+str(solNeg)+'<x<'+str(solPos)+''
        question = 'get valid range for x in |[('+str(a)+'x)+('+str(b)+')]/('+str(c)+')|<'+str(d)+''
        options = coursesFunctionsBll.absoluteValue2([solNeg, solPos])
        jsonResponse = json.dumps({"question":question, "solution":solution, "options":options})
        return jsonResponse
    except Exception as er:
        return er
#the force acting on an object is equal to at^2+bt+c
#which of the next options is not a valid time when the magnitude of force was equal to d
def absoluteValueProblem():
    try:
        a = random.randint(1,50)
        b = random.randint(51,100)*(-1)
        c = random.randint(26,50)
        d = random.randint(1,25)
        e1= c-d
        e2=c+d
        if((b*b)<=4*a*e2):
            return absoluteValueProblem()
        sols=[]
        while True:
            sols.append(round((-b+(((b**2)-(4*a*e1))**(0.5)))/(2*a),4))
            sols.append(round((-b-(((b**2)-(4*a*e1))**(0.5)))/(2*a),4))
            sols.append(round((-b+(((b**2)-(4*a*e2))**(0.5)))/(2*a),4))
            sols.append(round((-b-(((b**2)-(4*a*e2))**(0.5)))/(2*a),4))
            sols.append(round(random.uniform(0, max(sols)+min(sols)),4))
            if sols[4]!=sols[0] and sols[4]!=sols[1] and sols[4]!=sols[2] and sols[4]!=sols[3]:
                break
            sols=[]
        options = coursesFunctionsBll.absoluteValueProblem(sols)
        question = 'the force acting on an object is equal to ('+str(a)+'t^2)+('+str(b)+'t)+('+str(c)+'), where t is time, which of the options is not a valid time when the magnitude of force on the object was equal to '+str(d)+''
        solution=str(sols[4])
        jsonResponse = json.dumps({"question":question, "solution":solution, "options":options})
        return jsonResponse
    except Exception as er:
        return er
exam1 =[secondGradeEquation, firstGradeEquation, firstGradeTwoVariables, firstGradeFraction, quadraticFactorizationType1, quadraticFactorizationType2, areaProblem, plantProblem, partialFractions, cubicFactorization]
exam2 =[inequations1, rationalInequations, inequationTwoSides, inequations2, inequationGrade2,inequationProblem1, inequationProblem2, absoluteValue1, absoluteValue2, absoluteValueProblem]
listMethods = [exam1, exam2]
def generateExam(unit):
    solution=[]
    lista = listMethods[int(unit)-1]
    for x in range(12):
        question =  random.randint(1,len(lista))
        #numberQuestion='QUESTION '+str(x+1)
        item = str(lista[question-1]())
        #jsonData = json.loads(json.dumps({numberQuestion: json.loads(item)}))
        solution.append(json.loads(item))
    return solution





