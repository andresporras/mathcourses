import random
import json
import math
from flask import jsonify
#from mpmath import mp, mpf
#mp.dps = 100
#mp.pretty = True
def yoxterFormat(number):
    number = format(number,'.100g')
    numbers = number.split('.')
    if len(numbers)>1:
        if len(numbers[1])>4:
            numbers[1]=numbers[1][:4]
        number=numbers[0]+'.'+numbers[1]
    return number

def generateOptions(solution):
    options =[solution]
    for x in range(4):
        i=random.randint(0,1)
        if(i==0):
            options.insert(0,round(options[0]/2,4))
        else:
            options.append(round(options[len(options)-1]*2,4))
    strOptions =json.loads(json.dumps({'a':str(options[0]), 'b':str(options[1]), 'c': str(options[2]), 'd': str(options[3]), 'e': str(options[4])}))
    return strOptions
def generateTwoVariableOptions(options):
    solutions =[options.copy()]
    for x in range(4):
        i=random.randint(0,1)
        j=random.randint(0,2)
        if(i==0):
            nSolution = solutions[0].copy()
            nSolution[j]=round(nSolution[j]/2,4)
            solutions.insert(0,nSolution)
        else:
            nSolution = solutions[len(solutions)-1].copy()
            nSolution[j]=round(nSolution[j]*2,4)
            solutions.append(nSolution)
    tempSolutions =[]
    for y in range(5):
        tempSolutions.append('[('+str(solutions[y][0])+'x+('+str(solutions[y][1])+')]/('+str(solutions[y][2])+')=x')
    strOptions =json.loads(json.dumps({'a':tempSolutions[0], 'b':tempSolutions[1], 'c': tempSolutions[2], 'd': tempSolutions[3], 'e': tempSolutions[4]}))
    return strOptions
def generateAlternativesQF(lista, type_):
    alternatives = [lista.copy()]
    for x in range(4):
        i=random.randint(0,1)
        j=random.randint(0,3) if type_==False else (random.randint(0,1)*2)+1
        if(i==0):
            nAlternative = alternatives[0].copy()
            nAlternative[j]=nAlternative[j]-1
            alternatives.insert(0,nAlternative)
        else:
            nAlternative = alternatives[len(alternatives)-1].copy()
            nAlternative[j]=nAlternative[j]+1
            alternatives.append(nAlternative)
    tempAlternatives =[]
    for y in range(5):
        tempAlternatives.append('[('+(str(alternatives[y][0]) if type_==False else remove(str(alternatives[y][0]), len(str(alternatives[y][0]))-1))+'x)+('+str(alternatives[y][1])+')]*[('+(str(alternatives[y][2]) if type_==False else remove(str(alternatives[y][2]), len(str(alternatives[y][2]))-1))+'x)+('+str(alternatives[y][3])+')]')
                               #'[('+(str(a) if type_==False else remove(str(a), len(str(a))-1))+'x)+('+str(b)+')]*[('+(str(c) if type_==False else remove(str(c), len(str(c))-1))+'x)+('+str(d)+')]'                  
    strOptions =json.loads(json.dumps({'a':tempAlternatives[0], 'b':tempAlternatives[1], 'c': tempAlternatives[2], 'd': tempAlternatives[3], 'e': tempAlternatives[4]}))
    return strOptions
def generateAlternativesCubicF(lista):
    alternatives = [lista.copy()]
    for x in range(4):
        i=random.randint(0,1)
        j=random.randint(0,3)
        if(i==0):
            nAlternative = alternatives[0].copy()
            nAlternative[j]=nAlternative[j]-1
            alternatives.insert(0,nAlternative)
        else:
            nAlternative = alternatives[len(alternatives)-1].copy()
            nAlternative[j]=nAlternative[j]+1
            alternatives.append(nAlternative)
    tempAlternatives =[]
    for y in range(5):
        tempAlternatives.append('[('+str(alternatives[y][0])+'x^2)+('+str(alternatives[y][1])+')]*[('+str(alternatives[y][2])+'x)+('+str(alternatives[y][3])+')]')
    strOptions =json.loads(json.dumps({'a':tempAlternatives[0], 'b':tempAlternatives[1], 'c': tempAlternatives[2], 'd': tempAlternatives[3], 'e': tempAlternatives[4]}))
    return strOptions

def generateAlternativesPF(lista):
    alternatives = [lista.copy()]
    for x in range(4):
        i=random.randint(0,1)
        j=random.randint(0,5)
        if(i==0):
            nAlternative = alternatives[0].copy()
            nAlternative[j]=nAlternative[j]-1
            alternatives.insert(0,nAlternative)
        else:
            nAlternative = alternatives[len(alternatives)-1].copy()
            nAlternative[j]=nAlternative[j]+1
            alternatives.append(nAlternative)
    tempAlternatives =[]
    for y in range(5):
        tempAlternatives.append('('+str(round(alternatives[y][0],4))+')/[('+str(alternatives[y][1])+'x)+('+str(alternatives[y][2])+')] + ('+str(round(alternatives[y][3],4))+')/[('+str(alternatives[y][4])+'x)+('+str(alternatives[y][5])+')]')
    strOptions =json.loads(json.dumps({'a':tempAlternatives[0], 'b':tempAlternatives[1], 'c': tempAlternatives[2], 'd': tempAlternatives[3], 'e': tempAlternatives[4]}))
    return strOptions
def quadraticFactorization(type_):
    a=random.randint(2,10)*(random.randint(0,1)*2-1) if type_==False else (random.randint(0,1)*2)-1
    b=random.randint(1,10)*(random.randint(0,1)*2-1)
    c=random.randint(2,10)*(random.randint(0,1)*2-1) if type_==False else (random.randint(0,1))*2-1
    d=random.randint(1,10)*(random.randint(0,1)*2-1)
    question ='for the next cuadratic function: ('+(str(a*c) if type_==False else remove(str(a*c), len(str(a*c))-1))+'x^2)+('+str((a*d)+(b*c))+'x)+('+str(b*d)+') determine which of the next factorizationn is valid'
    solution = '[('+(str(a) if type_==False else remove(str(a), len(str(a))-1))+'x)+('+str(b)+')]*[('+(str(c) if type_==False else remove(str(c), len(str(c))-1))+'x)+('+str(d)+')]'
    options = generateAlternativesQF([a,b,c,d],type_)
    return json.dumps({"question":question, "solution":str(solution), "options":options})
def inequationsAlternatives1(sol):
    options =[sol]
    i=random.randint(0,1)
    if(i==0):
        options.insert(0, round(options[0]/2,4))
    else:
        options.append(options[len(options)-1]*2)
    tempAlternatives =[]
    tempAlternatives.append('x>='+str(options[0]))
    tempAlternatives.append('x<='+str(options[0]))
    tempAlternatives.append('x>='+str(options[1]))
    tempAlternatives.append('x<='+str(options[1]))
    strOptions =json.loads(json.dumps({'a':tempAlternatives[0], 'b':tempAlternatives[1], 'c': tempAlternatives[2], 'd': tempAlternatives[3]}))
    return strOptions
def rationalInequations(union_range):
    try:
        alternatives = []
        alternatives.append("no solution")
        alternatives.append('('+(str(round(union_range[0][0],4)) if union_range[0][0]!=-1000 else '-'+str(math.inf))+','+(str(round(union_range[0][1],4)) if union_range[0][1]!=1000 else str(math.inf))+')')
        alternatives.append('('+(str(round(union_range[1][0],4)) if union_range[1][0]!=-1000 else '-'+str(math.inf))+','+(str(round(union_range[1][1],4)) if union_range[1][1]!=1000 else str(math.inf))+')')
        min_range = [union_range[0][0] if union_range[0][0]>union_range[1][0] else union_range[1][0], union_range[0][1] if union_range[0][1]<union_range[1][1] else union_range[1][1]]
        if(min_range[0]>min_range[1]):
            if(union_range[0][0]<union_range[1][0]):
                alternatives.append('('+(str(round(union_range[0][0],4)) if union_range[0][0]!=-1000 else '-'+str(math.inf))+','+(str(round(union_range[0][1],4)) if union_range[0][1]!=1000 else str(math.inf))+') U ('+(str(round(union_range[1][0],4)) if union_range[1][0]!=-1000 else '-'+str(math.inf))+','+(str(round(union_range[1][1],4)) if union_range[1][1]!=1000 else str(math.inf))+')')
            else:
                alternatives.append('('+(str(round(union_range[1][0],4)) if union_range[1][0]!=-1000 else '-'+str(math.inf))+','+(str(round(union_range[1][1],4)) if union_range[1][1]!=1000 else str(math.inf))+') U ('+(str(round(union_range[0][0],4)) if union_range[0][0]!=-1000 else '-'+str(math.inf))+','+(str(round(union_range[0][1],4)) if union_range[0][1]!=1000 else str(math.inf))+')')
        max_range = [union_range[0][0] if union_range[0][0]<union_range[1][0] else union_range[1][0], union_range[0][1] if union_range[0][1]>union_range[1][1] else union_range[1][1]]
        alternatives.append('('+(str(round(max_range[0],4)) if max_range[0]!=-1000 else '-'+str(math.inf))+','+(str(round(max_range[1],4)) if max_range[1]!=1000 else str(math.inf))+')')
        strOptions =json.loads(json.dumps({'a':alternatives[0], 'b':alternatives[1], 'c': alternatives[2], 'd': alternatives[3], 'e': alternatives[4]}))
        return strOptions
    except Exception as er:
        return er
def inequationsAlternatives2(sol):
    options =[sol.copy()]
    i=random.randint(0,3)
    noption = options[0].copy()
    noption[i] = noption[i]*(-1)
    j=random.randint(0,1)
    if(j==0):
        options.insert(0, noption)
    else:
        options.append(noption)
    tempAlternatives =[]
    tempAlternatives.append('x>='+'[('+str(options[0][0])+'y)+('+str(options[0][1])+')]/[('+str(options[0][2])+'y)+('+str(options[0][3])+')]')
    tempAlternatives.append('x<='+'[('+str(options[0][0])+'y)+('+str(options[0][1])+')]/[('+str(options[0][2])+'y)+('+str(options[0][3])+')]')
    tempAlternatives.append('x>='+'[('+str(options[1][0])+'y)+('+str(options[1][1])+')]/[('+str(options[1][2])+'y)+('+str(options[1][3])+')]')
    tempAlternatives.append('x<='+'[('+str(options[1][0])+'y)+('+str(options[1][1])+')]/[('+str(options[1][2])+'y)+('+str(options[1][3])+')]')
    strOptions =json.loads(json.dumps({'a':tempAlternatives[0], 'b':tempAlternatives[1], 'c': tempAlternatives[2], 'd': tempAlternatives[3]}))
    return strOptions
def inequationGrade2(lista):
    alternatives =[]
    alternatives.append('(void)')
    alternatives.append('(-inf,inf)')
    alternatives.append('('+str(round(lista[0],4))+')')
    alternatives.append('('+str(round(lista[1] if lista[1]<lista[2] else lista[2], 4))+','+str(round(lista[1] if lista[1]>lista[2] else lista[2], 4))+')')
    alternatives.append('(-inf, '+str(round(lista[1] if lista[1]<lista[2] else lista[2], 4))+') U ('+str(round(lista[1] if lista[1]>lista[2] else lista[2], 4))+',inf)')
    strOptions =json.loads(json.dumps({'a':alternatives[0], 'b':alternatives[1], 'c': alternatives[2], 'd': alternatives[3], 'e': alternatives[4]}))
    return strOptions
def inequationProblem1(lista):
    alternatives =[]
    alternatives.append('(void)')
    alternatives.append('(0,inf)')
    alternatives.append('('+str(round(lista[0], 4))+')')
    alternatives.append('('+str(round(lista[1] if lista[1]>0 else 0, 4))+','+str(round(lista[2], 4))+')')
    alternatives.append('(0, '+str(round(lista[1], 4))+') U ' if lista[1]>0 else ''+ '('+str(round(lista[2], 4))+',inf)')
    strOptions =json.loads(json.dumps({'a':alternatives[0], 'b':alternatives[1], 'c': alternatives[2], 'd': alternatives[3], 'e': alternatives[4]}))
    return strOptions
def inequationProblem2(lista):
    tempAlternatives = [lista.copy()]
    for x in range(2):
        i=random.randint(0,1)
        if(i==0):
            nAlternative = tempAlternatives[0].copy()
            nAlternative[0]=nAlternative[0]/2
            nAlternative[1]=nAlternative[1]/2
            tempAlternatives.insert(0,nAlternative)
        else:
            nAlternative = tempAlternatives[len(tempAlternatives)-1].copy()
            nAlternative[0]=(nAlternative[0]+100)/2
            nAlternative[1]=(nAlternative[1]+100)/2
            tempAlternatives.append(nAlternative)
    alternatives =[]
    alternatives.append('student already lost the course')
    alternatives.append('student already surpassed the acceptable note (>80)')
    alternatives.append('['+str(round(tempAlternatives[0][0] if tempAlternatives[0][0]>=0 else 0,4))+','+str(round(tempAlternatives[0][1] if tempAlternatives[0][1]<=100 else 100,4))+')')
    alternatives.append('['+str(round(tempAlternatives[1][0] if tempAlternatives[1][0]>=0 else 0,4))+','+str(round(tempAlternatives[1][1] if tempAlternatives[1][1]<=100 else 100,4))+')')
    alternatives.append('['+str(round(tempAlternatives[2][0] if tempAlternatives[2][0]>=0 else 0,4))+','+str(round(tempAlternatives[2][1] if tempAlternatives[2][1]<=100 else 100,4))+')')
    strOptions =json.loads(json.dumps({'a':alternatives[0], 'b':alternatives[1], 'c': alternatives[2], 'd': alternatives[3], 'e': alternatives[4]}))
    return strOptions
def absoluteValue1(solution):
    options =[solution.copy()]
    for x in range(4):
        i=random.randint(0,1)
        j=random.randint(0,1)
        if(i==0):
            temp = options[0].copy()
            temp[j]=round(temp[j]/2,4)
            options.insert(0, temp)
        else:
            temp = options[len(options)-1].copy()
            temp[j]=temp[j]*2
            options.append(temp)
    strOptions =json.loads(json.dumps({'a':str(options[0][0])+','+str(options[0][1]), 'b':str(options[1][0])+','+str(options[1][1]), 'c': str(options[2][0])+','+str(options[2][1]), 'd': str(options[3][0])+','+str(options[3][1]), 'e': str(options[4][0])+','+str(options[4][1])}))
    return strOptions
def absoluteValue2(solution):
    options =[solution.copy()]
    for x in range(3):
        i=random.randint(0,1)
        j=random.randint(0,1)
        if(i==0):
            temp = options[0].copy()
            temp[j]=round(temp[j]-(abs(temp[1]-temp[0])/2),4)
            options.insert(0, temp)
        else:
            temp = options[len(options)-1].copy()
            temp[j]=round(temp[j]+(abs(temp[1]-temp[0])/2),4)
            options.append(temp)
    alternatives=[]
    alternatives.append('(null)')
    alternatives.append(str(options[0][0])+'<x<'+str(options[0][1]))
    alternatives.append(str(options[1][0])+'<x<'+str(options[1][1]))
    alternatives.append(str(options[2][0])+'<x<'+str(options[2][1]))
    alternatives.append(str(options[3][0])+'<x<'+str(options[3][1]))
    strOptions =json.loads(json.dumps({'a':str(alternatives[0]), 'b':str(alternatives[1]), 'c': str(alternatives[2]), 'd': str(alternatives[3]), 'e': str(alternatives[4])}))
    return strOptions
def absoluteValueProblem(nSols):
    sols = nSols.copy()
    sols.sort()
    strOptions =json.loads(json.dumps({'a':str(sols[0]), 'b':str(sols[1]), 'c': str(sols[2]), 'd': str(sols[3]), 'e': str(sols[4])}))
    return strOptions

def alternativesSequence(solution):
    alternatives = [solution]
    for x in range(4):
        i=random.randint(0,1)
        if(i==0):
            nAlternative = alternatives[0]
            alternatives.insert(0,alternatives[0]-1)
        else:
            alternatives.append(alternatives[len(alternatives)-1]+1)
    strOptions =json.loads(json.dumps({'a':str(alternatives[0]), 'b':str(alternatives[1]), 'c':str( alternatives[2]), 'd':str(alternatives[3]), 'e': str(alternatives[4])}))
    return strOptions
def arithmeticAlternatives(sol):
    alternatives = [sol]
    for x in range(4):
        i=random.randint(0,1)
        j=random.randint(0,3)
        if(i==0):
            nAlternative = alternatives[0]-1
            alternatives.insert(0,nAlternative)
        else:
            nAlternative = alternatives[len(alternatives)-1]+1
            alternatives.append(nAlternative)
    strOptions =json.loads(json.dumps({'a':str(alternatives[0]), 'b':str(alternatives[1]), 'c': str(alternatives[2]), 'd': str(alternatives[3]), 'e': str(alternatives[4])}))
    return strOptions
def arithmeticSinAlternatives(sol):
    alternatives = [sol]
    for x in range(4):
        i=random.randint(0,1)
        j=random.randint(0,3)
        if(i==0):
            nAlternative = alternatives[0]-15
            alternatives.insert(0,nAlternative)
        else:
            nAlternative = alternatives[len(alternatives)-1]+15
            alternatives.append(nAlternative)
    strOptions =json.loads(json.dumps({'a':str(round(math.sin(math.radians(alternatives[0])),4)), 'b':str(round(math.sin(math.radians(alternatives[1])),4)), 'c': str(round(math.sin(math.radians(alternatives[2])),4)), 'd': str(round(math.sin(math.radians(alternatives[3])),4)), 'e': str(round(math.sin(math.radians(alternatives[4])),4))}))
    return strOptions
def fromGivenRange(solution, solutions):
    alternatives = [solution]
    for x in range(4):
        c = random.randint(0,len(solutions)-1)
        d = random.randint(0,1)
        if d==0:
            alternatives.append(solutions[c])
        else:
            alternatives.insert(0,solutions[c])
        del solutions[c]
    strOptions =json.loads(json.dumps({'a':str(alternatives[0]), 'b':str(alternatives[1]), 'c': str(alternatives[2]), 'd': str(alternatives[3]), 'e': str(alternatives[4])}))
    return strOptions
    strOptions =json.loads(json.dumps({'a':str(alternatives[0]), 'b':str(alternatives[1]), 'c': str(alternatives[2]), 'd': str(alternatives[3]), 'e': str(alternatives[4])}))
    return strOptions
def parallelProblemOptions(slope, intersection):
    try:
        alternatives = [[slope, intersection]]
        for x in range(4):
            i=random.randint(0,1)
            j=random.randint(0,1)
            if(i==0):
                nAlternative = alternatives[0].copy()
                nAlternative[j]=round(nAlternative[j]/2,4)
                alternatives.insert(0,nAlternative)
            else:
                nAlternative = alternatives[len(alternatives)-1].copy()
                nAlternative[j]=round(nAlternative[j]*2,4)
                alternatives.append(nAlternative)
        tempAlternatives =[]
        for y in range(5):
            tempAlternatives.append("y=("+str(alternatives[y][0])+"x)+("+str(alternatives[y][1])+")")
        strOptions =json.loads(json.dumps({'a':tempAlternatives[0], 'b':tempAlternatives[1], 'c': tempAlternatives[2], 'd': tempAlternatives[3], 'e': tempAlternatives[4]}))
        return strOptions
    except Exception as er:
        return er
def perimeterAreaOptions(perimeter, area):
    try:
        alternatives = [[perimeter, area]]
        for x in range(4):
            i=random.randint(0,1)
            j=random.randint(0,1)
            if(i==0):
                nAlternative = alternatives[0].copy()
                nAlternative[j]=round(nAlternative[j]/2,4)
                alternatives.insert(0,nAlternative)
            else:
                nAlternative = alternatives[len(alternatives)-1].copy()
                nAlternative[j]=round(nAlternative[j]*2,4)
                alternatives.append(nAlternative)
        tempAlternatives =[]
        for y in range(5):
            tempAlternatives.append("Perimeter= "+str(alternatives[y][0])+" and Area="+str(alternatives[y][1]))
        strOptions =json.loads(json.dumps({'a':tempAlternatives[0], 'b':tempAlternatives[1], 'c': tempAlternatives[2], 'd': tempAlternatives[3], 'e': tempAlternatives[4]}))
        return strOptions
    except Exception as er:
        return er
def ellipseProblemOptions(data):
    try:
        alternatives = [data.copy()]
        for x in range(4):
            i=random.randint(0,1)
            j=random.randint(0,3)
            if(i==0):
                nAlternative = alternatives[0].copy()
                nAlternative[j]=round(nAlternative[j]/2,4)
                alternatives.insert(0,nAlternative)
            else:
                nAlternative = alternatives[len(alternatives)-1].copy()
                nAlternative[j]=round(nAlternative[j]*2,4)
                alternatives.append(nAlternative)
        tempAlternatives =[]
        for y in range(5):
            tempAlternatives.append("[(x-("+str(alternatives[y][0])+"))^2/"+str(alternatives[y][1])+"]+[(y-("+str(alternatives[y][2])+"))^2/"+str(alternatives[y][3])+"]=1")
        strOptions =json.loads(json.dumps({'a':tempAlternatives[0], 'b':tempAlternatives[1], 'c': tempAlternatives[2], 'd': tempAlternatives[3], 'e': tempAlternatives[4]}))
        return strOptions
    except Exception as er:
        return er
def parabolaProblemOptions(data):
    try:
        alternatives = [data.copy()]
        for x in range(4):
            i=random.randint(0,1)
            j=random.randint(0,2)
            if(i==0):
                nAlternative = alternatives[0].copy()
                nAlternative[j]=round(nAlternative[j]/2,4)
                alternatives.insert(0,nAlternative)
            else:
                nAlternative = alternatives[len(alternatives)-1].copy()
                nAlternative[j]=round(nAlternative[j]*2,4)
                alternatives.append(nAlternative)
        tempAlternatives =[]
        for y in range(5):
            tempAlternatives.append("y-("+str(alternatives[y][0])+")="+str(alternatives[y][1])+"*(x-("+str(alternatives[y][2])+"))^2")
        strOptions =json.loads(json.dumps({'a':tempAlternatives[0], 'b':tempAlternatives[1], 'c': tempAlternatives[2], 'd': tempAlternatives[3], 'e': tempAlternatives[4]}))
        return strOptions
    except Exception as er:
        return er
def hyperbolaProblemOptions(data):
    try:
        alternatives = [data.copy()]
        for x in range(4):
            i=random.randint(0,1)
            j=random.randint(0,3)
            if(i==0):
                nAlternative = alternatives[0].copy()
                nAlternative[j]=round(nAlternative[j]/2,4)
                alternatives.insert(0,nAlternative)
            else:
                nAlternative = alternatives[len(alternatives)-1].copy()
                nAlternative[j]=round(nAlternative[j]*2,4)
                alternatives.append(nAlternative)
        tempAlternatives =[]
        for y in range(5):
            tempAlternatives.append("[(x-("+str(alternatives[y][0])+"))^2/"+str(alternatives[y][1])+"]-[(y-("+str(alternatives[y][2])+"))^2/"+str(alternatives[y][3])+"]=1")
        strOptions =json.loads(json.dumps({'a':tempAlternatives[0], 'b':tempAlternatives[1], 'c': tempAlternatives[2], 'd': tempAlternatives[3], 'e': tempAlternatives[4]}))
        return strOptions
    except Exception as er:
        return er
def twoXSolutions(data):
    try:
        alternatives = [data.copy()]
        for x in range(4):
            i=random.randint(0,1)
            j=random.randint(0,1)
            if(i==0):
                nAlternative = alternatives[0].copy()
                nAlternative[j]=round(nAlternative[j]/2,4)
                alternatives.insert(0,nAlternative)
            else:
                nAlternative = alternatives[len(alternatives)-1].copy()
                nAlternative[j]=round(nAlternative[j]*2,4)
                alternatives.append(nAlternative)
        tempAlternatives =[]
        for y in range(5):
            tempAlternatives.append("x1="+str(alternatives[y][0])+" and x2="+str(alternatives[y][1]))
        strOptions =json.loads(json.dumps({'a':tempAlternatives[0], 'b':tempAlternatives[1], 'c': tempAlternatives[2], 'd': tempAlternatives[3], 'e': tempAlternatives[4]}))
        return strOptions
    except Exception as er:
        return er
def productRuleOptions(data):
    try:
        alternatives = [data.copy()]
        for x in range(4):
            i=random.randint(0,1)
            j=random.randint(0,2)
            if(i==0):
                nAlternative = alternatives[0].copy()
                nAlternative[j]=round(nAlternative[j]-1,4)
                alternatives.insert(0,nAlternative)
            else:
                nAlternative = alternatives[len(alternatives)-1].copy()
                nAlternative[j]=round(nAlternative[j]+1,4)
                alternatives.append(nAlternative)
        tempAlternatives =[]
        for y in range(5):
            tempAlternatives.append("x="+str(alternatives[y][0])+"-ln(|("+str(alternatives[y][1])+"x)+("+str(alternatives[y][2])+")|)")
        strOptions =json.loads(json.dumps({'a':tempAlternatives[0], 'b':tempAlternatives[1], 'c': tempAlternatives[2], 'd': tempAlternatives[3], 'e': tempAlternatives[4]}))
        return strOptions
    except Exception as er:
        return er
def divisionRuleOptions(data):
    try:
        alternatives = [data.copy()]
        for x in range(4):
            i=random.randint(0,1)
            j=random.randint(0,3)
            if(i==0):
                nAlternative = alternatives[0].copy()
                nAlternative[j]=round(nAlternative[j]/2,4)
                alternatives.insert(0,nAlternative)
            else:
                nAlternative = alternatives[len(alternatives)-1].copy()
                nAlternative[j]=round(nAlternative[j]*2,4)
                alternatives.append(nAlternative)
        tempAlternatives =[]
        for y in range(5):
            tempAlternatives.append("x=ln(|["+str(alternatives[y][0])+"-("+str(alternatives[y][1])+"x)]^("+str(alternatives[y][2])+")|)-"+str(alternatives[y][3]))
        strOptions =json.loads(json.dumps({'a':tempAlternatives[0], 'b':tempAlternatives[1], 'c': tempAlternatives[2], 'd': tempAlternatives[3], 'e': tempAlternatives[4]}))
        return strOptions
    except Exception as er:
        return er
def ruleChainOptions(data,a,b,c,d,e,f):
    try:
        alternatives = [data.copy()]
        for x in range(4):
            i=random.randint(0,1)
            j=random.randint(0,2)
            if(i==0):
                nAlternative = alternatives[0].copy()
                nAlternative[j]=round(nAlternative[j]/2,4)
                alternatives.insert(0,nAlternative)
            else:
                nAlternative = alternatives[len(alternatives)-1].copy()
                nAlternative[j]=round(nAlternative[j]*2,4)
                alternatives.append(nAlternative)
        tempAlternatives =[]
        for y in range(5):
            tempAlternatives.append("f(x)'=["+str(alternatives[y][0])+"*"+str(a if a!=math.e else "e")+"^("+str(b*f)+"x+"+str(c)+")+"+str(alternatives[y][1])+"x^"+str(e-1)+"]/[("+str(a if a!=math.e else "e")+"^("+str(b*f)+"x+"+str(c)+")+"+str(d)+"x^"+str(e)+")^("+str(alternatives[y][2])+")]")
        strOptions =json.loads(json.dumps({'a':tempAlternatives[0], 'b':tempAlternatives[1], 'c': tempAlternatives[2], 'd': tempAlternatives[3], 'e': tempAlternatives[4]}))
        return strOptions
    except Exception as er:
        return er
def implicitOptions(data,c,e,h):
    try:
        alternatives = [data.copy()]
        for x in range(4):
            i=random.randint(0,1)
            j=random.randint(0,4)
            if(i==0):
                nAlternative = alternatives[0].copy()
                nAlternative[j]=round(nAlternative[j]/2,4)
                alternatives.insert(0,nAlternative)
            else:
                nAlternative = alternatives[len(alternatives)-1].copy()
                nAlternative[j]=round(nAlternative[j]*2,4)
                alternatives.append(nAlternative)
        tempAlternatives =[]
        for y in range(5):
            tempAlternatives.append("dy/dx=["+str(alternatives[y][2]*e)+"x"+str("^2" if e==3 else "")+"+"+str(alternatives[y][3])+"y]/["+str(c*alternatives[y][0])+"("+str(alternatives[y][0])+"y+"+str(alternatives[y][1])+")"+str("^2" if c==3 else "")+"-("+str(alternatives[y][3])+"x+"+str(alternatives[y][4]*h)+"y"+str("^2" if h==3 else "")+")]")
        strOptions =json.loads(json.dumps({'a':tempAlternatives[0], 'b':tempAlternatives[1], 'c': tempAlternatives[2], 'd': tempAlternatives[3], 'e': tempAlternatives[4]}))
        return strOptions
    except Exception as er:
        return er
def logarithm_a_options(data):
    try:
        alternatives = [data.copy()]
        for x in range(4):
            i=random.randint(0,1)
            j=random.randint(0,3)

            if(i==0):
                nAlternative = alternatives[0].copy()
                nAlternative[j]=round(nAlternative[j]/2,4)
                nAlternative[4]= random.randint(0,1)
                alternatives.insert(0,nAlternative)
            else:
                nAlternative = alternatives[len(alternatives)-1].copy()
                nAlternative[j]=round(nAlternative[j]*2,4)
                nAlternative[4]= random.randint(0,1)
                alternatives.append(nAlternative)
        tempAlternatives =[]
        for y in range(5):
            comp1 = "["+str(alternatives[y][1])+"xy^2+"+str(alternatives[y][2])+"y]" if alternatives[y][4]==0 else "["+str(alternatives[y][0])+"^("+str(alternatives[y][3])+"x)]"
            tempAlternatives.append("("+str(round(alternatives[y][3]*math.log(alternatives[y][0]),4))+"*"+str(comp1)+"-"+str(alternatives[y][1])+"y^2)/("+str(2*alternatives[y][1])+"xy+"+str(alternatives[y][2])+")")
        strOptions =json.loads(json.dumps({'a':tempAlternatives[0], 'b':tempAlternatives[1], 'c': tempAlternatives[2], 'd': tempAlternatives[3], 'e': tempAlternatives[4]}))
        return strOptions
    except Exception as er:
        return er

def logarithmMethodOptions(data,tempTri):
    try:
        alternatives = [data.copy()]
        for x in range(4):
            i=random.randint(0,1)
            j=random.randint(0,1)
            if(i==0):
                nAlternative = alternatives[0].copy()
                nAlternative[j]=round(nAlternative[j]/2,4)
                nAlternative[2]=tempTri[x][1]
                alternatives.insert(0,nAlternative)
            else:
                nAlternative = alternatives[len(alternatives)-1].copy()
                nAlternative[j]=round(nAlternative[j]*2,4)
                nAlternative[2]=tempTri[x][1]
                alternatives.append(nAlternative)
        tempAlternatives =[]
        for y in range(5):
            tempAlternatives.append("dy/dx="+str(alternatives[y][0])+"*y/x*ln(x)^2 + ["+str(alternatives[y][2])+"*y] - "+str(alternatives[y][1])+"*y")
        strOptions =json.loads(json.dumps({'a':tempAlternatives[0], 'b':tempAlternatives[1], 'c': tempAlternatives[2], 'd': tempAlternatives[3], 'e': tempAlternatives[4]}))
        return strOptions
    except Exception as er:
        return er
def multipleOptions(data, numberOptions):
    try:
        alternatives = [data.copy()]
        for x in range(numberOptions-1):
            i=random.randint(0,1)
            j=random.randint(0,len(data)-1)
            if(i==0):
                nAlternative = alternatives[0].copy()
                nAlternative[j]=round(nAlternative[j]/2,4)
                alternatives.insert(0,nAlternative)
            else:
                nAlternative = alternatives[len(alternatives)-1].copy()
                nAlternative[j]=round(nAlternative[j]*2,4)
                alternatives.append(nAlternative)
        return alternatives
    except Exception as er:
        return er
def replaceSpace(text0):
    try:
        text1 = text0.replace(' ', '\;')
        return text1
    except Exception as er:
        return er
def replaceOptions(opt):
    try:
        letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        for x in range(len(opt)):
            opt[letters[x]]=replaceSpace(opt[letters[x]])
        return opt
    except Exception as er:
        return er
def remove(s, indx):
    s1 = ''.join(x for x in s if s.index(x) != indx)
    return s1
