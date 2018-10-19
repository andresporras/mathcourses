import random
import json
from flask import jsonify

def generateOptions(solution):
    options =[solution]
    for x in range(4):
        i=random.randint(0,1)
        if(i==0):
            options.insert(0, round(options[0]/2,2))
        else:
            options.append(options[len(options)-1]*2)
    strOptions =json.dumps({'a':str(options[0]), 'b':str(options[1]), 'c': str(options[2]), 'd': str(options[3]), 'e': str(options[4])})
    return strOptions
def generateTwoVariableOptions(options):
    solutions =[options.copy()]
    for x in range(4):
        i=random.randint(0,1)
        j=random.randint(0,2)
        if(i==0):
            nSolution = solutions[0].copy()
            nSolution[j]=round(nSolution[j]/2,2)
            solutions.insert(0,nSolution)
        else:
            nSolution = solutions[len(solutions)-1].copy()
            nSolution[j]=round(nSolution[j]*2,2)
            solutions.append(nSolution)
    tempSolutions =[]
    for y in range(5):
        tempSolutions.append('[('+str(solutions[y][0])+'x+('+str(solutions[y][1])+')]/('+str(solutions[y][2])+')=x')
    strOptions =json.dumps({'a':tempSolutions[0], 'b':tempSolutions[1], 'c': tempSolutions[2], 'd': tempSolutions[3], 'e': tempSolutions[4]})
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
        tempAlternatives.append('[('+(str(alternatives[y][0]) if type_==False else remove(str(alternatives[y][0]), len(str(alternatives[y][0]))-1))+'x+('+str(alternatives[y][1])+')]*[('+(str(alternatives[y][2]) if type_==False else remove(str(alternatives[y][2]), len(str(alternatives[y][2]))-1))+'x+('+str(alternatives[y][3])+')]')
    strOptions =json.dumps({'a':tempAlternatives[0], 'b':tempAlternatives[1], 'c': tempAlternatives[2], 'd': tempAlternatives[3], 'e': tempAlternatives[4]})
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
    strOptions =json.dumps({'a':tempAlternatives[0], 'b':tempAlternatives[1], 'c': tempAlternatives[2], 'd': tempAlternatives[3], 'e': tempAlternatives[4]})
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
        tempAlternatives.append('('+str(round(alternatives[y][0],2))+')/[('+str(alternatives[y][1])+'x)+('+str(alternatives[y][2])+')] + ('+str(round(alternatives[y][3],2))+')/[('+str(alternatives[y][4])+'x)+('+str(alternatives[y][5])+')]')
    strOptions =json.dumps({'a':tempAlternatives[0], 'b':tempAlternatives[1], 'c': tempAlternatives[2], 'd': tempAlternatives[3], 'e': tempAlternatives[4]})
    return strOptions
def quadraticFactorization(type_):
    a=random.randint(2,10)*(random.randint(0,1)*2-1) if type_==False else (random.randint(0,1)*2)-1
    b=random.randint(1,10)*(random.randint(0,1)*2-1)
    c=random.randint(2,10)*(random.randint(0,1)*2-1) if type_==False else (random.randint(0,1))*2-1
    d=random.randint(1,10)*(random.randint(0,1)*2-1)
    question ='for the next cuadratic function: ('+(str(a*c) if type_==False else remove(str(a*c), len(str(a*c))-1))+'x^2)+('+str((a*d)+(b*c))+'x)+('+str(b*d)+') determine which of the next factorizationn is valid'
    solution = '[('+(str(a) if type_==False else remove(str(a), len(str(a))-1))+'x)+('+str(b)+')]*[('+(str(c) if type_==False else remove(str(c), len(str(c))-1))+'x)+('+str(d)+')]'
    options = generateAlternativesQF([a,b,c,d],type_)
    return json.dumps({'question':question, 'solution':str(solution), 'options':options})
def inequationsAlternatives1(sol):
    options =[sol]
    i=random.randint(0,1)
    if(i==0):
        options.insert(0, round(options[0]/2,2))
    else:
        options.append(options[len(options)-1]*2)
    tempAlternatives =[]
    tempAlternatives.append('x>='+str(options[0]))
    tempAlternatives.append('x<='+str(options[0]))
    tempAlternatives.append('x>='+str(options[1]))
    tempAlternatives.append('x<='+str(options[1]))
    strOptions =json.dumps({'a':tempAlternatives[0], 'b':tempAlternatives[1], 'c': tempAlternatives[2], 'd': tempAlternatives[3]})
    return strOptions
def remove(s, indx):
    s1 = ''.join(x for x in s if s.index(x) != indx)
    return s1
