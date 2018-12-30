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
#using the middle angle property solve a problem where you have to achieve something like cos(x/2) or sin(x/2)
def trigonometryProblem():
    try:
        def assignVariable(ab): #0 item is the expression, 1 is simplification, 2 is derivation
            oddPair = [["sin(-"+str(ab)+")","-sin("+str(ab)+")","-cos("+str(ab)+")"],["cos(-"+str(ab)+")","cos("+str(ab)+")","-sin("+str(ab)+")"],["tan(-"+str(ab)+")","-tan("+str(ab)+")","-sec^2("+str(ab)+")"],["cot(-"+str(ab)+")","-cot("+str(ab)+")","csc^2("+str(ab)+")"],["sec(-"+str(ab)+")","sec("+str(ab)+")","sec("+str(ab)+")*tan("+str(ab)+")"],["csc(-"+str(ab)+")","-csc("+str(ab)+")","csc("+str(ab)+")*cot("+str(ab)+")"]]
            cofunsion =[["sin((pi/2)-"+str(ab)+")","cos("+str(ab)+")","-sin("+str(ab)+")"],["cos((pi/2)-"+str(ab)+")","sin("+str(ab)+")","cos("+str(ab)+")"],["tan((pi/2)-"+str(ab)+")","cot("+str(ab)+")","-csc^2("+str(ab)+")"],["cot((pi/2)-"+str(ab)+")","tan("+str(ab)+")","sec^2("+str(ab)+")"]]
            inverseIdentity = [["sin(pi-"+str(ab)+")","sin("+str(ab)+")","cos("+str(ab)+")"],["sin(pi+"+str(ab)+")","-sin("+str(ab)+")","-cos("+str(ab)+")"],["cos(pi-"+str(ab)+")","-cos("+str(ab)+")","sin("+str(ab)+")"],["cos(pi+"+str(ab)+")","-cos("+str(ab)+")","sin("+str(ab)+")"],["tan(pi-"+str(ab)+")","-tan("+str(ab)+")","-sec^2("+str(ab)+")"],["tan(pi+"+str(ab)+")","tan("+str(ab)+")","sec^2("+str(ab)+")"]]
            return [oddPair,cofunsion, inverseIdentity]
        items=[]
        characters=["a","b"]
        for x in range(2):
            identities = assignVariable(characters[x])
            a = random.randint(0,2)
            b = random.randint(0,len(identities[a])-1)
            items.append(identities[a][b])
        solution="["+str(items[0][2])+"]+["+str(items[1][2])+"]"
        question="if f(a)=["+str(items[0][0])+"] and g(b)=["+str(items[1][0])+"] find f'(a)+g'(b)"
        options =json.loads(json.dumps({'a':"["+str((items[0][2])[-1*len(items[0][2]) if (items[0][2])[0]!='-' else (-1*len(items[0][2]))+1:])+"]+["+str((items[1][2])[-1*len(items[1][2]) if (items[1][2])[0]!='-' else (-1*len(items[1][2]))+1:])+"]", 'b':"[-"+str((items[0][2])[-1*len(items[0][2]) if (items[0][2])[0]!='-' else (-1*len(items[0][2]))+1:])+"]+["+str((items[1][2])[-1*len(items[1][2]) if (items[1][2])[0]!='-' else (-1*len(items[1][2]))+1:])+"]", 'c':"["+str((items[0][2])[-1*len(items[0][2]) if (items[0][2])[0]!='-' else (-1*len(items[0][2]))+1:])+"]+[-"+str((items[1][2])[-1*len(items[1][2]) if (items[1][2])[0]!='-' else (-1*len(items[1][2]))+1:])+"]", 'd':"[-"+str((items[0][2])[-1*len(items[0][2]) if (items[0][2])[0]!='-' else (-1*len(items[0][2]))+1:])+"]+[-"+str((items[1][2])[-1*len(items[1][2]) if (items[1][2])[0]!='-' else (-1*len(items[1][2]))+1:])+"]"}))
        jsonResponse = json.dumps({"question":question, "solution":solution, "options":options})
        return jsonResponse
    except Exception as er:
        return er

def ruleChainProblem():
    try:
        a = random.randint(2,10)*(random.randint(0,1)*2-1)
        b = random.randint(2,10)
        c = random.randint(2,10)
        d = random.randint(2,10)
        e = random.randint(1,5)*2
        f = random.randint(2,5)
        a = math.e if a<0 else a
        comp1=round(b*math.log(a),4)
        comp2=d*e
        comp3=round((f-1)/f,4)
        solution= "f(x)'=["+str(comp1)+"*"+str(a if a!=math.e else "e")+"^("+str(b*f)+"x+"+str(c)+")+"+str(comp2)+"x^"+str(e-1)+"]/[("+str(a if a!=math.e else "e")+"^("+str(b*f)+"x+"+str(c)+")+"+str(d)+"x^"+str(e)+")^("+str(comp3)+")]"
        question = "using chain rule find f(x)' where f(x)=("+str(a if a!=math.e else "e")+"^("+str(b*f)+"x+"+str(c)+")+"+str(d)+"x^"+str(e)+")^(1/"+str(f)+"): "
        options = coursesFunctionsBll.ruleChainOptions([comp1,comp2,comp3],a,b,c,d,e,f)
        jsonResponse = json.dumps({"question":question, "solution":solution, "options":options})
        return jsonResponse
    except Exception as er:
        return er

#using the middle angle property solve a problem where you have to achieve something like cos(x/2) or sin(x/2)
def trigonometryProblem2():
    try:
        def assignVariable(ab): #0 item is the expression, 1 is simplification, 2 is derivation
            oddPair = [["sin(-"+str(ab)+")","-sin("+str(ab)+")","-cos("+str(ab)+")"],["cos(-"+str(ab)+")","cos("+str(ab)+")","-sin("+str(ab)+")"],["tan(-"+str(ab)+")","-tan("+str(ab)+")","-sec^2("+str(ab)+")"],["cot(-"+str(ab)+")","-cot("+str(ab)+")","csc^2("+str(ab)+")"],["sec(-"+str(ab)+")","sec("+str(ab)+")","sec("+str(ab)+")*tan("+str(ab)+")"],["csc(-"+str(ab)+")","-csc("+str(ab)+")","csc("+str(ab)+")*cot("+str(ab)+")"]]
            cofunsion =[["sin((pi/2)-"+str(ab)+")","cos("+str(ab)+")","-sin("+str(ab)+")"],["cos((pi/2)-"+str(ab)+")","sin("+str(ab)+")","cos("+str(ab)+")"],["tan((pi/2)-"+str(ab)+")","cot("+str(ab)+")","-csc^2("+str(ab)+")"],["cot((pi/2)-"+str(ab)+")","tan("+str(ab)+")","sec^2("+str(ab)+")"]]
            inverseIdentity = [["sin(pi-"+str(ab)+")","sin("+str(ab)+")","cos("+str(ab)+")"],["sin(pi+"+str(ab)+")","-sin("+str(ab)+")","-cos("+str(ab)+")"],["cos(pi-"+str(ab)+")","-cos("+str(ab)+")","sin("+str(ab)+")"],["cos(pi+"+str(ab)+")","-cos("+str(ab)+")","sin("+str(ab)+")"],["tan(pi-"+str(ab)+")","-tan("+str(ab)+")","-sec^2("+str(ab)+")"],["tan(pi+"+str(ab)+")","tan("+str(ab)+")","sec^2("+str(ab)+")"]]
            return [oddPair,cofunsion, inverseIdentity]
        items=[]
        characters=["a","b"]
        a=0
        b=0
        for x in range(3):
            identities = assignVariable(characters[x]) if x<2 else assignVariable("["+items[0][1]+"]")
            a = random.randint(0,2) if x<2 else a
            b = random.randint(0,len(identities[a])-1) if x<2 else b
            items.append(identities[a][b])
        solution="["+str(items[2][2])+"]*["+str(items[0][2])+"]"
        listOptions = ["["+str(items[2][2])+"]*["+str(items[0][2])+"]", "["+str(items[2][1])+"]*["+str(items[0][2])+"]", "["+str(items[2][2])+"]*["+str(items[0][1])+"]", "["+str(items[2][1])+"]*["+str(items[0][1])+"]"]
        listOptions.sort()
        question="if f(a)=["+str(items[0][0])+"] and g(b)=["+str(items[1][0])+"] find g'(f(a))"
        options =json.loads(json.dumps({'a':listOptions[0], 'b':listOptions[1], 'c':listOptions[2], 'd':listOptions[3]}))
        jsonResponse = json.dumps({"question":question, "solution":solution, "options":options})
        return jsonResponse
    except Exception as er:
        return er

def implicitProblem():
    try:
        a = random.randint(2,10)
        b = random.randint(2,10)
        c = random.randint(2,3)
        d = random.randint(2,10)
        e = random.randint(2,3)
        f = random.randint(2,10)
        g = random.randint(2,10)
        h = random.randint(2,3)
        solution= "dy/dx=["+str(d*e)+"x"+str("^2" if e==3 else "")+"+"+str(f)+"y]/["+str(c*a)+"("+str(a)+"y+"+str(b)+")"+str("^2" if c==3 else "")+"-("+str(f)+"x+"+str(g*h)+"y"+str("^2" if h==3 else "")+")]"
        question = "find dy/dx from ("+str(a)+"y+"+str(b)+")^"+str(c)+"="+str(d)+"x^"+str(e)+"+"+str(f)+"xy+"+str(g)+"y^"+str(h)+": "
        options = coursesFunctionsBll.implicitOptions([a,b,d,f,g],c,e,h)
        jsonResponse = json.dumps({"question":question, "solution":solution, "options":options})
        return jsonResponse
    except Exception as er:
        return er

exam1 =[lineTanProblem, logarithmProblem, productProblem, divisionProblem, trigonometryProblem, ruleChainProblem, trigonometryProblem2, implicitProblem]
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