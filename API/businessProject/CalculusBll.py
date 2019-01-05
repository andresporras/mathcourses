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
def exponentialProblem():
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
        sol=round((a*(2*math.log(c)+1)-(math.log(c)*b)-(math.log(c)*math.log(c)*b))/(a*math.log(c)*(math.log(c)+1)),4)
        solution= str(sol)
        question = "finds x where f'(x)=f''(x) if f(x)=("+str(a)+"x+"+str(b)+")/("+str(c)+"^x): "
        options = coursesFunctionsBll.generateOptions(sol)
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

def inverseTriProblem():
    try:
        a = random.randint(2,10)
        b = random.randint(2,10)
        c = random.randint(2,10)
        d= random.randint(0,5)
        sol=0
        question=""
        if d==0:
            sol=round(math.log((a*a)/(a*a+c*c))/2,4)
            question = "on which point the function "+str(c)+"*asin(e^x) is parallel to the line "+str(a)+"x+"+str(b)+"?:"
        elif d==1:
            sol=round(math.log((a*a)/(a*a+c*c))/2,4)
            question = "on which point the function "+str(c)+"*acos(e^x) is parallel to the line "+str(a)+"x+"+str(b)+"?:"
        elif d==2:
            sol=round(math.log((a*a+c*c)/(a*a))/2,4)
            question = "on which point the function "+str(c)+"*asec(e^x) is parallel to the line "+str(a)+"x+"+str(b)+"?:"
        elif d==3:
            sol=round(math.log((a*a+c*c)/(a*a))/2,4)
            question = "on which point the function "+str(c)+"*acsc(e^x) is parallel to the line "+str(a)+"x+"+str(b)+"?:"
        elif d==4:
            sol=round(math.log((16*a**4+8*(a**2)*(c**2)+c**4)/(16*a**4))/4,4)
            question = "on which point the function "+str(c)+"*atan(e^x+("+str(c)+"/"+str(2*a)+")) is parallel to the line "+str(a)+"x+"+str(b)+"?:"
        elif d==5:
            sol=round(math.log((16*a**4+8*(a**2)*(c**2)+c**4)/(16*a**4))/4,4)
            question = "on which point the function "+str(c)+"*acot(e^x-("+str(c)+"/"+str(2*a)+")) is parallel to the line "+str(a)+"x+"+str(b)+"?:"
        solution= str(sol)
        options = coursesFunctionsBll.generateOptions(sol)
        jsonResponse = json.dumps({"question":question, "solution":solution, "options":options})
        return jsonResponse
    except Exception as er:
        return er
#using the middle angle property solve a problem where you have to achieve something like cos(x/2) or sin(x/2)
def logarithmProblem():
    try:
        oddPair = [["sin(-x)","-sin(x)","-cos(x)", "2*cos^2(x)/sin(2*x)"],["cos(-x)","cos(x)","-sin(x)","tan(x/2)/[tan(x/2)]+1"],["tan(-x)","-tan(x)","-sec^2(x)","2/sin(2*x)"],["cot(-x)","-cot(x)","csc^2(x)","[tan^2(x)-sec^2(x)]/[sin(x)*cos(x)]"],["sec(-x)","sec(x)","sec(x)*tan(x)","sin(2x)/[1+cos(2x)]"],["csc(-x)","-csc(x)","csc(x)*cot(x)","[cot^2(x)-csc^2(x)]/tan(x)"]]
        cofunsion =[["sin((pi/2)-x)","cos(x)","-sin(x)","tan(x/2)/[tan(x/2)]+1"],["cos((pi/2)-x)","sin(x)","cos(x)", "2*cos^2(x)/sin(2*x)"],["tan((pi/2)-x)","cot(x)","-csc^2(x)","[tan^2(x)-sec^2(x)]/[sin(x)*cos(x)]"],["cot((pi/2)-x)","tan(x)","sec^2(x)","2/sin(2*x)"]]
        inverseIdentity = [["sin(pi-x)","sin(x)","cos(x)", "2*cos^2(x)/sin(2*x)"],["sin(pi+x)","-sin(x)","-cos(x)", "2*cos^2(x)/sin(2*x)"],["cos(pi-x)","-cos(x)","sin(x)","tan(x/2)/[tan(x/2)]+1"],["cos(pi+x)","-cos(x)","sin(x)","tan(x/2)/[tan(x/2)]+1"],["tan(pi-x)","-tan(x)","-sec^2(x)","2/sin(2*x)"],["tan(pi+x)","tan(x)","sec^2(x)","2/sin(2*x)"]]
        identities= [oddPair,cofunsion, inverseIdentity]
        a = random.randint(0,2)
        b = random.randint(0,len(identities[a])-1)
        solution=identities[a][b][3]
        listOptions = ["2*cos^2(x)/sin(2*x)","tan(x/2)/[tan(x/2)]+1","2/sin(2*x)","[tan^2(x)-sec^2(x)]/[sin(x)*cos(x)]","sin(2x)/[1+cos(2x)]","[cot^2(x)-csc^2(x)]/tan(x)"]
        while len(listOptions)==6:
            deleteOption = random.randint(0,5)
            if listOptions[deleteOption]!=solution:
                del listOptions[deleteOption]
        question="find the derivative of ln("+str(identities[a][b][0])+"): "
        options =json.loads(json.dumps({'a':listOptions[0], 'b':listOptions[1], 'c':listOptions[2], 'd':listOptions[3], 'e':listOptions[4]}))
        jsonResponse = json.dumps({"question":question, "solution":solution, "options":options})
        return jsonResponse
    except Exception as er:
        return er
#it has two valid solutions, anyone of those can appear
def logarithm_a_Problem():
    try:
        a = (random.randint(1,5)*2)+1
        b = random.randint(2,10)
        c = random.randint(2,10)
        d = random.randint(2,10)
        e = random.randint(0,1)
        comp1 = "["+str(b)+"xy^2+"+str(c)+"y]" if e==0 else "["+str(a)+"^("+str(d)+"x)]"
        solution = "("+str(round(d*math.log(a),4))+"*"+str(comp1)+"-"+str(b)+"y^2)/("+str(2*b)+"xy+"+str(c)+")"
        question="find dy/dx if log_"+str(a)+"_("+str(b)+"xy^2+"+str(c)+"y)="+str(d)+"x"
        options =coursesFunctionsBll.logarithm_a_options([a,b,c,d])
        jsonResponse = json.dumps({"question":question, "solution":solution, "options":options})
        return jsonResponse
    except Exception as er:
        return er
def logarithmMethodProblem():
    try:
        a = random.randint(2,10)
        b = random.randint(0,5)
        c = random.randint(2,10)
        triOptions=[["sin(x)","cot(x)"],["cos(x)","-tan(x)"],["tan(x)","2*csc(2x)"],["cot(x)","-2*cosc(2x)"],["sec(x)","tan(x)"],["csc(x)","-cot(x)"]]
        tempTri = triOptions.copy()
        del tempTri[b]
        d = random.randint(0,4)
        del tempTri[d]
        comp1= round(-1*math.log(a),4)
        comp2=round(math.log(c),4)
        question = "find dy/dx where y=log_x_("+str(a)+")*"+str(triOptions[b][0])+"/("+str(c)+"^x): "
        solution= "dy/dx="+str(comp1)+"*y/x*ln(x)^2 + ["+str(triOptions[b][1])+"*y] - "+str(comp2)+"*y"
        options =coursesFunctionsBll.logarithmMethodOptions([comp1,comp2,triOptions[b][1]],tempTri)
        jsonResponse = json.dumps({"question":question, "solution":solution, "options":options})
        return jsonResponse
    except Exception as er:
        return er
def positionProblem():
    try:
        a = random.randint(2,20)
        b = random.randint(2,20)
        c = random.randint(2,20)
        d = random.randint(2,20)
        t = random.randint(2,20)
        a1= a*3
        b1=b*2
        a2=a1*2
        velocity= (a1*t*t)+(b1*t)+c
        acceleration= (a2*t)+b1
        question = "A particle position (through time) is given by the function x="+str(a)+"t^3 + "+str(b)+"t^2 + "+str(c)+"t + "+str(d)+". Finds velocity and acceleration when t="+str(t)+"s:"
        solution= "velocity="+str(velocity)+"m/s and acceleration="+str(acceleration)+"m/s^2"
        alternatives = coursesFunctionsBll.multipleOptions([velocity, acceleration])
        tempAlternatives =[]
        for y in range(5):
            tempAlternatives.append("velocity="+str(alternatives[y][0])+"m/s and acceleration="+str(alternatives[y][1])+"m/s^2")
        options =json.loads(json.dumps({'a':tempAlternatives[0], 'b':tempAlternatives[1], 'c': tempAlternatives[2], 'd': tempAlternatives[3], 'e': tempAlternatives[4]}))
        jsonResponse = json.dumps({"question":question, "solution":solution, "options":options})
        return jsonResponse
    except Exception as er:
        return er
def newtonCoolingProblem():
    try:
        tempIni = random.randint(76,100)
        tempFin = random.randint(51,75)
        tempFin2 = random.randint(26,50)
        tempEnvi = random.randint(1,25)
        t= random.randint(2,30)
        d = random.randint(2,20)
        t = random.randint(2,20)
        k = math.log((tempFin-tempEnvi)/(tempIni-tempEnvi))/t
        sol=round(math.log((tempFin2-tempEnvi)/(tempIni-tempEnvi))/k,4)
        sol2=round(k*(tempIni-tempEnvi)*(math.e**(k*sol)),4)
        question = "A drink with an initial temperature of "+str(tempIni)+"°F is put on a fridge with a environment temperature equals to "+str(tempEnvi)+"°F. After "+str(t)+" minutes the drink's temperature is "+str(tempFin)+"°F. How many minutes will be need until drink has cooled to "+str(tempFin2)+"°F and which will be the rate of change (F/m) in that moment? use the newton law of cooling: "
        solution= "time="+str(sol)+"m and rate change="+str(sol2)+"°F/m"
        alternatives = coursesFunctionsBll.multipleOptions([sol,sol2])
        tempAlternatives =[]
        for y in range(5):
            tempAlternatives.append("time="+str(alternatives[y][0])+"m and rate change="+str(alternatives[y][1])+"°F/m")
        options =json.loads(json.dumps({'a':tempAlternatives[0], 'b':tempAlternatives[1], 'c': tempAlternatives[2], 'd': tempAlternatives[3], 'e': tempAlternatives[4]}))
        jsonResponse = json.dumps({"question":question, "solution":solution, "options":options})
        return jsonResponse
    except Exception as er:
        return er
exam1 =[lineTanProblem, exponentialProblem, productProblem, divisionProblem, trigonometryProblem, ruleChainProblem, trigonometryProblem2, implicitProblem, inverseTriProblem, logarithmProblem]
exam2 =[logarithm_a_Problem, logarithmMethodProblem, positionProblem, newtonCoolingProblem]
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