import random
import math
import json
import coursesFunctionsBll

#find limit when x->0 for the function [(ax+b)(cx+d)-bd*cos(ex)]/(ex)
def basicIdentityProblem1():
    try:
        side_a = ["sin(x)", "cos(x)","[1/sin(x)]","[1/cos(x)]"]
        side_b = ["[tan^2(x)+1]", "[cot^2(x)+1]"]
        solutions=["tan(x)sec(x)", "sec(x)","csc(x)sec^2(x)","sec^3(x)","csc(x)","cot(x)csc(x)","csc^3(x)","sec(x)csc^2(x)"]
        a = random.randint(0,3)
        b = random.randint(0,1)
        solution=solutions[a+(b*4)]
        del solutions[a+b]
        question="simplify "+side_a[a]+"*"+side_b[b]
        options =coursesFunctionsBll.fromGivenRange(solution, solutions.copy())
        jsonResponse = json.dumps({"question":question, "solution":solution, "options":options})
        return jsonResponse
    except Exception as er:
        return er
#find limit when x->0 for the function [(ax+b)(cx+d)-bd*cos(ex)]/(ex)
def sumIdentityProblem1():
    try:
        a = random.randint(1,100)*(random.randint(0,1)*2-1)*15
        b = random.randint(1,100)*(random.randint(0,1)*2-1)*15
        c= random.randint(0,3)
        d= random.randint(0,1)
        solution=""
        question=""
        sol=0
        #if a==b or math.sin(math.radians(a+b))==0: # avoid solution equals 0 since this will be a problem generating the options
         #   return sumIdentityProblem1()
        if c==0: #cos(a-b) = cos(a)cos(b)+sin(a)sin(b)
            sol=a-b
            solution=str("" if d==0 else "-")+"sin("+str(a-b)+")"
            question = "tan(pi"+str(("+" if d==0 else "-"))+"("+str(a-b)+"))*[cos("+str(a)+")cos("+str(b)+")+sin("+str(a)+")sin("+str(b)+")]"
        elif c==1: #cos(a+b) = cos(a)cos(b)-sin(a)sin(b)
            sol=a+b
            solution=str("" if d==0 else "-")+"sin("+str(a+b)+")"
            question = "tan(pi"+str(("+" if d==0 else "-"))+"("+str(a+b)+"))*[cos("+str(a)+")cos("+str(b)+")-sin("+str(a)+")sin("+str(b)+")]"
        elif c==2: #sin(a+b) = sin(a)cos(b)+cos(a)sin(b)
            sol=a+b
            solution=str("" if d==0 else "-")+"[sec("+str(a+b)+")-cos("+str(a+b)+")]"
            question = "tan(pi"+str(("+" if d==0 else "-"))+"("+str(a+b)+"))*[sin("+str(a)+")cos("+str(b)+")+cos("+str(a)+")sin("+str(b)+")]"
        elif c==3: #sin(a-b) = sin(a)cos(b)-cos(a)sin(b)
            sol=a-b
            solution=str("" if d==0 else "-")+"[sec("+str(a-b)+")-cos("+str(a-b)+")]"
            question = "tan(pi"+str(("+" if d==0 else "-"))+"("+str(a+b)+"))*[cos("+str(a)+")cos("+str(b)+")-sin("+str(a)+")sin("+str(b)+")]"
        options =json.loads(json.dumps({'a':"sin("+str(sol)+")", 'b':"-sin("+str(sol)+")", 'c':"[sec("+str(sol)+")-cos("+str(sol)+")]",'d':"-[sec("+str(sol)+")-cos("+str(sol)+")]"}))
        jsonResponse = json.dumps({"question":question, "solution":solution, "options":options})
        return jsonResponse
    except Exception as er:
        return er
#using double angle property find a solution similar to sin(2x) or cos(2x)
def doubleAngleProblem1():
    try:
        a = random.randint(2,10)
        b = random.randint(2,10)
        c= random.randint(0,1)
        solution=str(a/2)+"*cos("+str(b/2)+"a)" if c==0 else str(a)+"*sin("+str(b/2)+"a)"
        question= "simplify "+str(a)+"*sin((pi-"+str(b)+"a)/4)*cos((pi-"+str(b)+"a)/4)" if c==0 else "simplify "+str(a)+"[cos^2((pi-"+str(b)+"a)/4)-sin^2((pi-"+str(b)+"a)/4)]"
        options =json.loads(json.dumps({'a':str(a/2)+"*sin("+str(b/2)+"a)", 'b':str(a)+"*cos("+str(b/2)+"a)", 'c':str(a)+"*sin("+str(b/2)+"a)", 'd':str(a/2)+"*cos("+str(b/2)+"a)"}))
        jsonResponse = json.dumps({"question":question, "solution":solution, "options":options})
        return jsonResponse
    except Exception as er:
        return er
#using the middle angle property solve a problem where you have to achieve something like cos(x/2) or sin(x/2)
def middleAngleProblem1():
    try:
        #a = random.randint(2,10)
        b = random.randint(0,1)
        c= random.randint(0,1)
        d = random.randint(2,10)
        e = random.randint(2,10)
        if(e==d):
            return middleAngleProblem1()
        solution= str("sin" if b==0 else "cos")+str("("+str(((d+e)/2 if c==0 else (d-e)/2))+")")
        question= "simplify  +-([1"+str("-" if b==0 else "+")+"("+str("cos("+str(d)+")cos("+str(e)+") "+str("+" if c==1 else "-")+" sin("+str(d)+")sin("+str(e)+")")+")]/2)^(1/2)"
        options =json.loads(json.dumps({'a':"sin("+str((d+e)/2)+")", 'b':"sin("+str((d-e)/2)+")", 'c':"cos("+str((d+e)/2)+")", 'd':"cos("+str((d-e)/2)+")"}))
        jsonResponse = json.dumps({"question":question, "solution":solution, "options":options})
        return jsonResponse
    except Exception as er:
        return er
#using the middle angle property solve a problem where you have to achieve something like cos(x/2) or sin(x/2)
def productSumProblem1():
    try:
        a = random.randint(0,3)
        b = random.randint(2,10)*(random.randint(0,1)*2-1)
        c= random.randint(2,10)*(random.randint(0,1)*2-1)
        solution=""
        question=""
        if b==c or b==(-c):
            return productSumProblem1()
        if a==0:
            solution="sin("+str(b)+")cos("+str(c)+")"
            question="simplify (1/2)*[+-((1-cos("+str(2*(b-c))+"))/2)^(1/2)+sin("+str(b+c)+")]"
        elif a==1:
            solution="sin("+str(b)+")sin("+str(c)+")"
            question="simplify (1/2)*[+-((1+cos("+str(2*(b-c))+"))/2)^(1/2)-cos("+str(b+c)+")]"
        elif a==2:
            solution="cos("+str(b)+")sin("+str(c)+")"
            question="simplify (1/2)*[+-((1-cos("+str(2*(b+c))+"))/2)^(1/2)-sin("+str(b-c)+")]"
        elif a==3:
            solution="cos("+str(b)+")cos("+str(c)+")"
            question="simplify (1/2)*[+-((1+cos("+str(2*(b+c))+"))/2)^(1/2)+cos("+str(b-c)+")]"
        
        options =json.loads(json.dumps({'a':"sin("+str(b)+")cos("+str(c)+")", 'b':"sin("+str(b)+")sin("+str(c)+")", 'c':"cos("+str(b)+")sin("+str(c)+")", 'd':"cos("+str(b)+")cos("+str(c)+")"}))
        jsonResponse = json.dumps({"question":question, "solution":solution, "options":options})
        return jsonResponse
    except Exception as er:
        return er
#using the middle angle property solve a problem where you have to achieve something like cos(x/2) or sin(x/2)
def sumProductProblem1():
    try:
        a = random.randint(0,3)
        b = random.randint(2,10)*(random.randint(0,1)*2-1)
        c= random.randint(2,10)*(random.randint(0,1)*2-1)
        solution=""
        question=""
        if b==c or b==(-c):
            return sumProductProblem1()
        if a==0:
            solution="sin("+str(b)+")+sin("+str(c)+")"
            question="simplify 2*[[+-((1-cos("+str(b+c)+"))/2))^(1/2)]cos(("+str((b-c)/2)+")]"
        elif a==1:
            solution="sin("+str(b)+")-sin("+str(c)+")"
            question="simplify 2*[[+-((1+cos("+str(b+c)+"))/2))^(1/2)]sin(("+str((b-c)/2)+")]"
        elif a==2:
            solution="cos("+str(b)+")+cos("+str(c)+")"
            question="simplify 2*[[+-((1+cos("+str(b-c)+"))/2))^(1/2)]cos(("+str((b+c)/2)+")]"
        elif a==3:
            solution="cos("+str(b)+")-cos("+str(c)+")"
            question="simplify 2*[[+-((1-cos("+str(b-c)+"))/2))^(1/2)]sin(("+str((-1)*(b+c)/2)+")]" #remember that sin(-a)=-sin(a)
        options =json.loads(json.dumps({'a':"sin("+str(b)+")+sin("+str(c)+")", 'b':"sin("+str(b)+")-sin("+str(c)+")", 'c':"cos("+str(b)+")+cos("+str(c)+")", 'd':"cos("+str(b)+")-cos("+str(c)+")"}))
        jsonResponse = json.dumps({"question":question, "solution":solution, "options":options})
        return jsonResponse
    except Exception as er:
        return er
#using the middle angle property solve a problem where you have to achieve something like cos(x/2) or sin(x/2)
def basicPropertyProblem1():
    try:
        def assignVariable(ab):
            oddPair = [["sin(-"+str(ab)+")","-sin("+str(ab)+")"],["cos(-"+str(ab)+")","cos("+str(ab)+")"],["tan(-"+str(ab)+")","-tan("+str(ab)+")"],["cot(-"+str(ab)+")","-cot("+str(ab)+")"],["sec(-"+str(ab)+")","sec("+str(ab)+")"],["csc(-"+str(ab)+")","-csc("+str(ab)+")"]]
            cofunsion =[["sin((pi/2)-"+str(ab)+")","cos("+str(ab)+")"],["cos((pi/2)-"+str(ab)+")","sin("+str(ab)+")"],["tan((pi/2)-"+str(ab)+")","cot("+str(ab)+")"],["cot((pi/2)-"+str(ab)+")","tan("+str(ab)+")"]]
            inverseIdentity = [["sin(pi-"+str(ab)+")","sin("+str(ab)+")"],["sin(pi+"+str(ab)+")","-sin("+str(ab)+")"],["cos(pi-"+str(ab)+")","-cos("+str(ab)+")"],["cos(pi+"+str(ab)+")","-cos("+str(ab)+")"],["tan(pi-"+str(ab)+")","-tan("+str(ab)+")"],["tan(pi+"+str(ab)+")","tan("+str(ab)+")"]]
            return [oddPair,cofunsion, inverseIdentity]
        items=[]
        characters=["a","b"]
        for x in range(2):
            identities = assignVariable(characters[x])
            a = random.randint(0,2)
            b = random.randint(0,len(identities[a])-1)
            items.append(identities[a][b])
        solution="["+str(items[0][1])+"]+["+str(items[1][1])+"]"
        question="["+str(items[0][0])+"]+["+str(items[1][0])+"]"
        options =json.loads(json.dumps({'a':"["+str((items[0][1])[-6:])+"]+["+str((items[1][1])[-6:])+"]", 'b':"[-"+str((items[0][1])[-6:])+"]+["+str((items[1][1])[-6:])+"]", 'c':"["+str((items[0][1])[-6:])+"]+[-"+str((items[1][1])[-6:])+"]", 'd':"[-"+str((items[0][1])[-6:])+"]+[-"+str((items[1][1])[-6:])+"]"}))
        jsonResponse = json.dumps({"question":question, "solution":solution, "options":options})
        return jsonResponse
    except Exception as er:
        return er
#using the middle angle property solve a problem where you have to achieve something like cos(x/2) or sin(x/2)
def sumDifTanProblem1():
    try:
        def assignVariable(ab):
            oddPair = [["tan(-"+str(ab)+")","-tan("+str(ab)+")"]]
            cofunsion =[["cot((pi/2)-"+str(ab)+")","tan("+str(ab)+")"]]
            inverseIdentity = [["tan(pi-"+str(ab)+")","-tan("+str(ab)+")"],["tan(pi+"+str(ab)+")","tan("+str(ab)+")"]]
            return [oddPair,cofunsion, inverseIdentity]
        items=[]
        characters=["a","b"]
        solution=""
        for x in range(2):
            identities = assignVariable(characters[x])
            a = random.randint(0,2)
            b = random.randint(0,len(identities[a])-1)
            items.append(identities[a][b])
        if (items[0][1])[0]!="-" and (items[1][1])[0]!="-":
            solution="tan(a+b)"
        elif (items[0][1])[0]=="-" and (items[1][1])[0]=="-":
            solution="-tan(a+b)"
        elif (items[0][1])[0]!="-" and (items[1][1])[0]=="-":
            solution="tan(a-b)"
        elif (items[0][1])[0]=="-" and (items[1][1])[0]!="-":
            solution="-tan(a-b)"
        question="(["+str(items[0][0])+"]+["+str(items[1][0])+"])/(1-["+str(items[0][0])+"]["+str(items[1][0])+"])"
        options =json.loads(json.dumps({'a':"tan(a+b)", 'b':"-tan(a+b)", 'c':"tan(a-b)", 'd':"-tan(a-b)"}))
        jsonResponse = json.dumps({"question":question, "solution":solution, "options":options})
        return jsonResponse
    except Exception as er:
        return er
#using the middle angle property solve a problem where you have to achieve something like cos(x/2) or sin(x/2)
def doubleAngleTanProblem1():
    try:
        t = random.randint(0,1)
        def assignVariable(ab):
            oddPair = [["sin(-a)","-sin(a)"],["cos(-a)","cos(a)"]]
            cofunsion =[["cos((pi/2)-a)","sin(a)"],["sin((pi/2)-a)","cos(a)"]]
            inverseIdentity = [["sin(pi-a)","sin(a)"],["sin(pi+a)","-sin(a)"],["cos(pi-a)","-cos(a)"],["cos(pi+a)","-cos(a)"]]
            return [oddPair[ab[0][0]:ab[0][1]],cofunsion[ab[1][0]:ab[1][1]], inverseIdentity[ab[2][0]:ab[2][1]]]
        items=[]
        _range=[[[0,1],[0,1],[0,2]],[[1,2],[1,2],[2,4]]]
        firstCharacter ="-"
        solution=""
        question=""
        for x in range(2):
            identities = assignVariable(_range[x])
            a = random.randint(0,2)
            b = random.randint(0,len(identities[a])-1)
            items.append(identities[a][b])
        if ((items[0][1])[0]!="-" and (items[1][1])[0]!="-") or ((items[0][1])[0]=="-" and (items[1][1])[0]=="-"):
            firstCharacter=""
        if t==0:
            question="[("+str(items[0][0])+")/("+str(items[1][0])+")]*[2/(1-tan^2(a))]"
            solution=firstCharacter+"tan(2a)"
        else:
            question="[("+str(items[1][0])+")/("+str(items[0][0])+")]*[(1-tan^2(a))/2]"
            solution=firstCharacter+"cot(2a)"
        options =json.loads(json.dumps({'a':"tan(2a)", 'b':"-tan(2a)", 'c':"cot(2a)", 'd':"-cot(2a)"}))
        jsonResponse = json.dumps({"question":question, "solution":solution, "options":options})
        return jsonResponse
    except Exception as er:
        return er
#using the middle angle property solve a problem where you have to achieve something like cos(x/2) or sin(x/2)
def middleAngleTanProblem1():
    try:
        t = random.randint(0,1)
        oddPair = [["sin(-a)","-sin(a)"]]
        cofunsion =[["cos((pi/2)-a)","sin(a)"]]
        inverseIdentity = [["sin(pi-a)","sin(a)"],["sin(pi+a)","-sin(a)"]]
        identities=  [oddPair,cofunsion, inverseIdentity]
        firstCharacter =""
        solution=""
        question=""
        a = random.randint(0,2)
        b = random.randint(0,len(identities[a])-1)
        item=identities[a][b]
        if (item[1])[0]=="-":
            firstCharacter="-"
        if t==0:
            question="("+str(item[0])+")/(1+cos(a))"
            solution=firstCharacter+"tan(a/2)"
        else:
            question="(1+cos(a))/("+str(item[0])+")"
            solution=firstCharacter+"cot(a/2)"
        options =json.loads(json.dumps({'a':"tan(a/2)", 'b':"-tan(a/2)", 'c':"cot(a/2)", 'd':"-cot(a/2)"}))
        jsonResponse = json.dumps({"question":question, "solution":solution, "options":options})
        return jsonResponse
    except Exception as er:
        return er

#find the equation which pass through a given point and is parallel to a given line
def parallelProblem():
    try:
        x0=random.randint(2,10)*(random.randint(0,1)*2-1)
        y0=random.randint(2,10)*(random.randint(0,1)*2-1)
        x1=random.randint(2,10)*(random.randint(0,1)*2-1)
        y1=random.randint(2,10)*(random.randint(0,1)*2-1)
        x2=random.randint(2,10)*(random.randint(0,1)*2-1)
        y2=random.randint(2,10)*(random.randint(0,1)*2-1)
        if x2==x1:
            return parallelProblem()
        slope= round((y2-y1)/(x2-x1),4)
        intersection = round(y0-(x0*slope),4)
        solution = "y=("+str(slope)+"x)+("+str(intersection)+")"
        question = "which is the straight line which pass through the point ("+str(x0)+","+str(y0)+") and is parallel to the straigh line which pass through the points ("+str(x1)+","+str(y1)+") and ("+str(x2)+","+str(y2)+"): "
        options =coursesFunctionsBll.parallelProblemOptions(slope, intersection)
        jsonResponse = json.dumps({"question":question, "solution":solution, "options":options})
        return jsonResponse
    except Exception as er:
        return er
#find perpendicular line which connect a given point with a given line
def perpendicularProblem():
    try:
        x0=random.randint(2,10)*(random.randint(0,1)*2-1)
        y0=random.randint(2,10)*(random.randint(0,1)*2-1)
        x1=random.randint(2,10)*(random.randint(0,1)*2-1)
        y1=random.randint(2,10)*(random.randint(0,1)*2-1)
        x2=random.randint(2,10)*(random.randint(0,1)*2-1)
        y2=random.randint(2,10)*(random.randint(0,1)*2-1)
        if x2==x1:
            return parallelProblem()
        slope= round(-1/((y2-y1)/(x2-x1)),4)
        intersection = round(y0-(x0*slope),4)
        solution = "y=("+str(slope)+"x)+("+str(intersection)+")"
        question = "which is the straight line which pass through the point ("+str(x0)+","+str(y0)+") and is perpendicular to the straigh line which pass through the points ("+str(x1)+","+str(y1)+") and ("+str(x2)+","+str(y2)+"): "
        options =coursesFunctionsBll.parallelProblemOptions(slope, intersection)
        jsonResponse = json.dumps({"question":question, "solution":solution, "options":options})
        return jsonResponse
    except Exception as er:
        return er
#find circle equation having one point of the circle an its center
def circleProblem():
    try:
        x0=random.randint(2,19)*(random.randint(0,1)*2-1)
        y0=random.randint(2,19)*(random.randint(0,1)*2-1)
        x1=random.randint(2,19)*(random.randint(0,1)*2-1)
        y1=random.randint(2,19)*(random.randint(0,1)*2-1)
        r = (((x1-x0)**2)+((y1-y0)**2))**(1/2)
        perimeter = round(2*3.1416*r,4)
        area = round(3.1416*r*r,4)
        solution = "Perimeter= "+str(perimeter)+" and Area="+str(area)
        question = "Find the perimeter and area of the circle which center is ("+str(x0)+","+str(y0)+") and pass through the point ("+str(x1)+","+str(y1)+"): "
        options =coursesFunctionsBll.perimeterAreaOptions(perimeter, area)
        jsonResponse = json.dumps({"question":question, "solution":solution, "options":options})
        return jsonResponse
    except Exception as er:
        return er
#find ellipse having the foci and a point of the ellipse
def ellipseProblem():
    try:
        x01=random.randint(2,10)*(random.randint(0,1)*2-1)
        x02=random.randint(2,10)*(random.randint(0,1)*2-1)
        y0=random.randint(2,10)*(random.randint(0,1)*2-1)
        x1=random.randint(2,10)*(random.randint(0,1)*2-1)
        y1=random.randint(2,10)*(random.randint(0,1)*2-1)
        x0 = (x01+x02)/2 #HERE IS X0
        if x01==x02 or y0==y1:
            ellipseProblem()
        constant = ((((x1-x01)**2)+((y1-y0)**2))**(1/2))+((((x1-x02)**2)+((y1-y0)**2))**(1/2))
        vertice01 = (x01+x02-constant)/2
        vertice02 = (x01+x02+constant)/2
        xDistance = abs(vertice02-x0)
        yDistance = ((xDistance**2)-((x01-x0)**2))**(1/2)
        solution = "[(x-("+str(x0)+"))^2/"+str(round(xDistance**2,4))+"]+[(y-("+str(y0)+"))^2/"+str(round(yDistance**2,4))+"]=1"
        #solutions = ["[(x-("+str(x0)+"))^2/"+str(xDistance**2)+"]+[(y-("+str(y0)+"))^2/"+str(yDistance**2)+"]=1", "[(x-("+str(x0)+"))^2/"+str(xDistance)+"]+[(y-("+str(y0)+"))^2/"+str(yDistance)+"]=1", "[(x-("+str(x0)+"))^2/"+str(xDistance**2)+"]+[(y-("+str(y0)+"))^2/"+str(yDistance**2)+"]=1", "[(x-("+str(x0)+"))^2/"+str(xDistance**2)+"]+[(y-("+str(y0)+"))^2/"+str(yDistance**2)+"]=1"]
        #random.shuffle(solutions)
        #options =json.loads(json.dumps({'a':solutions[0], 'b':solutions[1], 'c':solutions[2], 'd':solutions[3]}))
        options =coursesFunctionsBll.ellipseProblemOptions([x0, round(xDistance**2,4), y0, round(yDistance**2,4)])
        question = "which is the canonical equation of the ellipse  which focus are ("+str(x01)+","+str(y0)+") ("+str(x02)+","+str(y0)+") and pass through the point ("+str(x1)+","+str(y1)+"): "
        jsonResponse = json.dumps({"question":question, "solution":solution, "options":options})
        return jsonResponse
    except Exception as er:
        return er
#get parabola equation through focus and directrix
#this is how you get equation form focus and directrix: https://www.khanacademy.org/math/algebra2/intro-to-conics-alg2/focus-and-directrix-of-a-parabola-alg2/v/equation-for-parabola-from-focus-and-directrix
def parabolaProblem():
    try:
        focusx=random.randint(2,20)*(random.randint(0,1)*2-1)
        focusy=random.randint(2,20)*(random.randint(0,1)*2-1)
        directrix=(random.randint(2,20)*(random.randint(0,1)*2-1))
        if(directrix>=focusy):
            parabolaProblem()
        c1=round((focusy+directrix)/2,4)
        c2=round(1/(2*(focusy-directrix)),4)
        c3=focusx
        solution = "y-("+str(c1)+")="+str(c2)+"*(x-("+str(c3)+"))^2"
        options =coursesFunctionsBll.parabolaProblemOptions([c1, c2, c3])
        question = "which is the canonical equation of the parabola which focus ("+str(focusx)+","+str(focusy)+") and directrix y="+str(directrix)+":"
        jsonResponse = json.dumps({"question":question, "solution":solution, "options":options})
        return jsonResponse
    except Exception as er:
        return er
#given the center and one vertix find the equation of hyperbola
def hyperbolaProblem():
    try:
        x01=random.randint(2,20)*(random.randint(0,1)*2-1)
        x02=random.randint(2,20)*(random.randint(0,1)*2-1)
        if abs(x01-x02)<=2:
            return hyperbolaProblem()
        y0=random.randint(2,20)*(random.randint(0,1)*2-1)
        x0 = (x01+x02)/2
        vertice = x0
        while vertice==x0:
            vertice=random.randint(1,abs(x01-x02)-1)+(x01 if x01<x02 else x02)
        x0 = (x01+x02)/2
        a= abs(vertice-x0)
        c=abs(x01-x0)
        b = round(((c**2)-(a**2))**(1/2),4)

        solution = "[(x-("+str(x0)+"))^2/"+str(round(a**2,4))+"]-[(y-("+str(y0)+"))^2/"+str(round(b**2,4))+"]=1"
        options =coursesFunctionsBll.hyperbolaProblemOptions([x0, round(a**2,4), y0, round(b**2,4)])
        question = "which is the canonical equation of the hyperbola  which foci are ("+str(x01)+","+str(y0)+") ("+str(x02)+","+str(y0)+") and one of vertices is in ("+str(vertice)+","+str(y0)+"): "
        jsonResponse = json.dumps({"question":question, "solution":solution, "options":options})
        return jsonResponse
    except Exception as er:
        return er
#find the diameter of the circle which a given center and a given tangent line
#use the perpendicular line between the center an the tangent line
def circleTanProblem():
    try:
        x=random.randint(2,10)*(random.randint(0,1)*2-1)
        y=random.randint(2,10)*(random.randint(0,1)*2-1)
        m=random.randint(2,10)*(random.randint(0,1)*2-1)
        c=random.randint(2,10)*(random.randint(0,1)*2-1)
        slope = -1/m
        intersection=y-(x*slope)
        x1 = (intersection-c)/(m-slope)
        y1=(x1*m)+c
        distance = ((x1-x)**2+(y1-y)**2)**(1/2)
        diameter = round(distance*2,4)
        solution = str(diameter)
        options =coursesFunctionsBll.generateOptions(diameter)
        question = "which is the diameter of a circle where center is in ("+str(x)+","+str(y)+") and is tangent to the line y=("+str(m)+"x)+("+str(c)+")"
        jsonResponse = json.dumps({"question":question, "solution":solution, "options":options})
        return jsonResponse
    except Exception as er:
        return er
#find the are  havinf the foci and the minor semiaxis, to do this you must find the major semi-axis
def ellipseAreaProblem():
    try:
        x01=random.randint(2,10)*(random.randint(0,1)*2-1)
        x02=random.randint(2,10)*(random.randint(0,1)*2-1)
        y0=random.randint(2,10)*(random.randint(0,1)*2-1)
        minor=random.randint(2,10)
        if x01==x02:
            return ellipseProblem()
        x0 = (x01+x02)/2 #HERE IS X0
        major = ((x01-x0)**2+(minor)**2)**(1/2)
        area = round(3.1416*minor*major,4)
        solution = str(area)
        options =coursesFunctionsBll.generateOptions(area)
        question = "which is the area of ellipse which focus on ("+str(x01)+","+str(y0)+") ("+str(x02)+","+str(y0)+") and minor semiaxis equal to "+str(minor)+""
        jsonResponse = json.dumps({"question":question, "solution":solution, "options":options})
        return jsonResponse
    except Exception as er:
        return er
#to the triangle with given three points find the area and perimeter
#find the perpendicular line between any of the three point and the line build with the other two points
def triangleProblem():
    try:
        x1=random.randint(2,10)*(random.randint(0,1)*2-1)
        y1=random.randint(2,10)*(random.randint(0,1)*2-1)
        x2=random.randint(2,10)*(random.randint(0,1)*2-1)
        y2=random.randint(2,10)*(random.randint(0,1)*2-1)
        x3=random.randint(2,10)*(random.randint(0,1)*2-1)
        y3=random.randint(2,10)*(random.randint(0,1)*2-1)
        if x2==(-1*x1):
            return triangleProblem()
        m1=(y2-y1)/(x2-x1)
        b1=y1-(m1*x1)
        m2= -1/m1
        b2= y3-(m2*x3)
        x4= (b2-b1)/(m1-m2)
        y4=(m2*x4)+b2
        base = ((x2-x1)**2+(y2-y1)**2)**(1/2)
        height = ((x4-x3)**2+(y4-y3)**2)**(1/2)
        side2 = ((x3-x1)**2+(y3-y1)**2)**(1/2)
        side3 = ((x3-x2)**2+(y3-y2)**2)**(1/2)
        area=round(base*height/2,4)
        perimeter= round(base+side2+side3,4)
        solution = "Perimeter= "+str(perimeter)+" and Area="+str(area)
        options =coursesFunctionsBll.perimeterAreaOptions(perimeter, area)
        question = "which is the perimeter and area of triangle where vertixes are ("+str(x1)+","+str(y1)+") ("+str(x2)+","+str(y2)+") ("+str(x3)+","+str(y3)+"):"
        jsonResponse = json.dumps({"question":question, "solution":solution, "options":options})
        return jsonResponse
    except Exception as er:
        return er
#for the triangle with the given three vertixes find if is acute, obtuse or right
#get the biggest line, find perpendicular line which connect biggest line with the lef point
def triangleAngleProblem():
    try:
        x1=random.randint(2,10)*(random.randint(0,1)*2-1)
        y1=random.randint(2,10)*(random.randint(0,1)*2-1)
        x2=random.randint(2,10)*(random.randint(0,1)*2-1)
        y2=random.randint(2,10)*(random.randint(0,1)*2-1)
        x3=random.randint(2,10)*(random.randint(0,1)*2-1)
        y3=random.randint(2,10)*(random.randint(0,1)*2-1)
        if x1==x2 or x1==x3 or x2==x3:
            return triangleAngleProblem()
        side1 = ((x2-x1)**2+(y2-y1)**2)**(1/2)
        side2 = ((x3-x1)**2+(y3-y1)**2)**(1/2)
        side3 = ((x3-x2)**2+(y3-y2)**2)**(1/2)
        line=[]
        point=[]
        sides=[]
        if side1>side2 and side1>side3:
            line=[[x1,y1],[x2,y2]]
            point=[x3,y3]
            sides =[side2,side3]
        elif side2>side3:
            line=[[x1,y1],[x3,y3]]
            point=[x2,y2]
            sides =[side1,side3]
        else:
            line=[[x2,y2],[x3,y3]]
            point=[x1,y1]
            sides =[side1,side2]
        m=(line[1][1]-line[0][1])/(line[1][0]-line[0][0])
        b=line[0][1]-(m*line[0][0])
        m1=-1/m
        b1= point[1]-(m1*point[0])
        x4=(b1-b)/(m-m1)
        y4 = (m1*x4)+b1
        side4 = ((x4-point[0])**2+(y4-point[1])**2)**(1/2)
        angle1=math.degrees(math.asin(side4/sides[0]))
        angle2=math.degrees(math.asin(side4/sides[1]))
        maxAngle=180-(angle1+angle2)
        solution = "right" if (maxAngle>89.99 and maxAngle<90.01) else ("obtuse" if maxAngle>=90.01 else "acute")
        options =json.loads(json.dumps({'a':'right', 'b':'obtuse', 'c':'acute'}))
        question = "which is the triangle type if vertix are ("+str(x1)+","+str(y1)+") ("+str(x2)+","+str(y2)+") ("+str(x3)+","+str(y3)+"): "
        jsonResponse = json.dumps({"question":question, "solution":solution, "options":options})
        return jsonResponse
    except Exception as er:
        return er
exam1 =[basicIdentityProblem1, sumIdentityProblem1, doubleAngleProblem1, middleAngleProblem1, productSumProblem1, sumProductProblem1, basicPropertyProblem1, sumDifTanProblem1, doubleAngleTanProblem1, middleAngleTanProblem1]
exam2 =[parallelProblem, perpendicularProblem, circleProblem, ellipseProblem, parabolaProblem, hyperbolaProblem, circleTanProblem, ellipseAreaProblem, triangleProblem, triangleAngleProblem]
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

