
import random
import math
import json
import coursesFunctionsBll

#find limit when x->0 for the function [(ax+b)(cx+d)-bd*cos(ex)]/(ex)
def basicIdentityProblem1():
    try:
        side_a = ["sin(x)", "cos(x)","[1/sin(x)]","[1/cos(x)]"]
        side_b = ["[tan^2(x)+1]", "[cot^2(x)+1]"]
        solutions = ["tan(x)sec(x)", "sec(x)","csc(x)sec^2(x)","sec^3(x)","csc(x)","cot(x)csc(x)","csc^3(x)","sec(x)csc^2(x)"]
        a = random.randint(0,3)
        b = random.randint(0,1)
        solution = solutions[a + (b * 4)]
        del solutions[a + b]
        question = "simplify " + side_a[a] + "*" + side_b[b]
        options = coursesFunctionsBll.fromGivenRange(solution, solutions.copy())
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return jsonResponse
    except Exception as er:
        return er
#find limit when x->0 for the function [(ax+b)(cx+d)-bd*cos(ex)]/(ex)
def sumIdentityProblem1():
    try:
        a = random.randint(1,100) * (random.randint(0,1) * 2 - 1) * 15
        b = random.randint(1,100) * (random.randint(0,1) * 2 - 1) * 15
        c = random.randint(0,3)
        d = random.randint(0,1)
        solution = ""
        question = ""
        sol = 0
        #if a==b or math.sin(math.radians(a+b))==0: # avoid solution equals 0
        #since this will be a problem generating the options
         #   return sumIdentityProblem1()
        if c == 0: #cos(a-b) = cos(a)cos(b)+sin(a)sin(b)
            sol = a - b
            solution = str("" if d == 0 else "-") + "sin(" + str(a - b) + ")"
            question = "tan(pi" + str(("+" if d == 0 else "-")) + "(" + str(a - b) + "))*[cos(" + str(a) + ")cos(" + str(b) + ")+sin(" + str(a) + ")sin(" + str(b) + ")]"
        elif c == 1: #cos(a+b) = cos(a)cos(b)-sin(a)sin(b)
            sol = a + b
            solution = str("" if d == 0 else "-") + "sin(" + str(a + b) + ")"
            question = "tan(pi" + str(("+" if d == 0 else "-")) + "(" + str(a + b) + "))*[cos(" + str(a) + ")cos(" + str(b) + ")-sin(" + str(a) + ")sin(" + str(b) + ")]"
        elif c == 2: #sin(a+b) = sin(a)cos(b)+cos(a)sin(b)
            sol = a + b
            solution = str("" if d == 0 else "-") + "[sec(" + str(a + b) + ")-cos(" + str(a + b) + ")]"
            question = "tan(pi" + str(("+" if d == 0 else "-")) + "(" + str(a + b) + "))*[sin(" + str(a) + ")cos(" + str(b) + ")+cos(" + str(a) + ")sin(" + str(b) + ")]"
        elif c == 3: #sin(a-b) = sin(a)cos(b)-cos(a)sin(b)
            sol = a - b
            solution = str("" if d == 0 else "-") + "[sec(" + str(a - b) + ")-cos(" + str(a - b) + ")]"
            question = "tan(pi" + str(("+" if d == 0 else "-")) + "(" + str(a + b) + "))*[cos(" + str(a) + ")cos(" + str(b) + ")-sin(" + str(a) + ")sin(" + str(b) + ")]"
        options = json.loads(json.dumps({'a':"sin(" + str(sol) + ")", 'b':"-sin(" + str(sol) + ")", 'c':"[sec(" + str(sol) + ")-cos(" + str(sol) + ")]",'d':"-[sec(" + str(sol) + ")-cos(" + str(sol) + ")]"}))
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return jsonResponse
    except Exception as er:
        return er
#using double angle property find a solution similar to sin(2x) or cos(2x)
def doubleAngleProblem1():
    try:
        a = random.randint(2,10)
        b = random.randint(2,10)
        c = random.randint(0,1)
        solution = str(a / 2) + "*cos(" + str(b / 2) + "a)" if c == 0 else str(a) + "*sin(" + str(b / 2) + "a)"
        question = "simplify " + str(a) + "*sin((pi-" + str(b) + "a)/4)*cos((pi-" + str(b) + "a)/4)" if c == 0 else "simplify " + str(a) + "[cos^2((pi-" + str(b) + "a)/4)-sin^2((pi-" + str(b) + "a)/4)]"
        options = json.loads(json.dumps({'a':str(a / 2) + "*sin(" + str(b / 2) + "a)", 'b':str(a) + "*cos(" + str(b / 2) + "a)", 'c':str(a) + "*sin(" + str(b / 2) + "a)", 'd':str(a / 2) + "*cos(" + str(b / 2) + "a)"}))
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return jsonResponse
    except Exception as er:
        return er
#using the middle angle property solve a problem where you have to achieve
#something like cos(x/2) or sin(x/2)
def middleAngleProblem1():
    try:
        #a = random.randint(2,10)
        b = random.randint(0,1)
        c = random.randint(0,1)
        d = random.randint(2,10)
        e = random.randint(2,10)
        if(e == d):
            return middleAngleProblem1()
        solution = str("sin" if b == 0 else "cos") + str("(" + str(((d + e) / 2 if c == 0 else (d - e) / 2)) + ")")
        question = "simplify  +-([1" + str("-" if b == 0 else "+") + "(" + str("cos(" + str(d) + ")cos(" + str(e) + ") " + str("+" if c == 1 else "-") + " sin(" + str(d) + ")sin(" + str(e) + ")") + ")]/2)^(1/2)"
        options = json.loads(json.dumps({'a':"sin(" + str((d + e) / 2) + ")", 'b':"sin(" + str((d - e) / 2) + ")", 'c':"cos(" + str((d + e) / 2) + ")", 'd':"cos(" + str((d - e) / 2) + ")"}))
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return jsonResponse
    except Exception as er:
        return er
#using the middle angle property solve a problem where you have to achieve
#something like cos(x/2) or sin(x/2)
def productSumProblem1():
    try:
        a = random.randint(0,3)
        b = random.randint(2,10) * (random.randint(0,1) * 2 - 1)
        c = random.randint(2,10) * (random.randint(0,1) * 2 - 1)
        solution = ""
        question = ""
        if b == c or b == (-c):
            return productSumProblem1()
        if a == 0:
            solution = "sin(" + str(b) + ")cos(" + str(c) + ")"
            question = "simplify (1/2)*[+-((1-cos(" + str(2 * (b - c)) + "))/2)^(1/2)+sin(" + str(b + c) + ")]"
        elif a == 1:
            solution = "sin(" + str(b) + ")sin(" + str(c) + ")"
            question = "simplify (1/2)*[+-((1+cos(" + str(2 * (b - c)) + "))/2)^(1/2)-cos(" + str(b + c) + ")]"
        elif a == 2:
            solution = "cos(" + str(b) + ")sin(" + str(c) + ")"
            question = "simplify (1/2)*[+-((1-cos(" + str(2 * (b + c)) + "))/2)^(1/2)-sin(" + str(b - c) + ")]"
        elif a == 3:
            solution = "cos(" + str(b) + ")cos(" + str(c) + ")"
            question = "simplify (1/2)*[+-((1+cos(" + str(2 * (b + c)) + "))/2)^(1/2)+cos(" + str(b - c) + ")]"
        
        options = json.loads(json.dumps({'a':"sin(" + str(b) + ")cos(" + str(c) + ")", 'b':"sin(" + str(b) + ")sin(" + str(c) + ")", 'c':"cos(" + str(b) + ")sin(" + str(c) + ")", 'd':"cos(" + str(b) + ")cos(" + str(c) + ")"}))
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return jsonResponse
    except Exception as er:
        return er
#using the middle angle property solve a problem where you have to achieve
#something like cos(x/2) or sin(x/2)
def sumProductProblem1():
    try:
        a = random.randint(0,3)
        b = random.randint(2,10) * (random.randint(0,1) * 2 - 1)
        c = random.randint(2,10) * (random.randint(0,1) * 2 - 1)
        solution = ""
        question = ""
        if b == c or b == (-c):
            return sumProductProblem1()
        if a == 0:
            solution = "sin(" + str(b) + ")+sin(" + str(c) + ")"
            question = "simplify 2*[[+-((1-cos(" + str(b + c) + "))/2))^(1/2)]cos((" + str((b - c) / 2) + ")]"
        elif a == 1:
            solution = "sin(" + str(b) + ")-sin(" + str(c) + ")"
            question = "simplify 2*[[+-((1+cos(" + str(b + c) + "))/2))^(1/2)]sin((" + str((b - c) / 2) + ")]"
        elif a == 2:
            solution = "cos(" + str(b) + ")+cos(" + str(c) + ")"
            question = "simplify 2*[[+-((1+cos(" + str(b - c) + "))/2))^(1/2)]cos((" + str((b + c) / 2) + ")]"
        elif a == 3:
            solution = "cos(" + str(b) + ")-cos(" + str(c) + ")"
            question = "simplify 2*[[+-((1-cos(" + str(b - c) + "))/2))^(1/2)]sin((" + str((-1) * (b + c) / 2) + ")]" #remember that sin(-a)=-sin(a)
        options = json.loads(json.dumps({'a':"sin(" + str(b) + ")+sin(" + str(c) + ")", 'b':"sin(" + str(b) + ")-sin(" + str(c) + ")", 'c':"cos(" + str(b) + ")+cos(" + str(c) + ")", 'd':"cos(" + str(b) + ")-cos(" + str(c) + ")"}))
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return jsonResponse
    except Exception as er:
        return er
#using the middle angle property solve a problem where you have to achieve
#something like cos(x/2) or sin(x/2)
def basicPropertyProblem1():
    try:
        def assignVariable(ab):
            oddPair = [["sin(-" + str(ab) + ")","-sin(" + str(ab) + ")"],["cos(-" + str(ab) + ")","cos(" + str(ab) + ")"],["tan(-" + str(ab) + ")","-tan(" + str(ab) + ")"],["cot(-" + str(ab) + ")","-cot(" + str(ab) + ")"],["sec(-" + str(ab) + ")","sec(" + str(ab) + ")"],["csc(-" + str(ab) + ")","-csc(" + str(ab) + ")"]]
            cofunsion = [["sin((pi/2)-" + str(ab) + ")","cos(" + str(ab) + ")"],["cos((pi/2)-" + str(ab) + ")","sin(" + str(ab) + ")"],["tan((pi/2)-" + str(ab) + ")","cot(" + str(ab) + ")"],["cot((pi/2)-" + str(ab) + ")","tan(" + str(ab) + ")"]]
            inverseIdentity = [["sin(pi-" + str(ab) + ")","sin(" + str(ab) + ")"],["sin(pi+" + str(ab) + ")","-sin(" + str(ab) + ")"],["cos(pi-" + str(ab) + ")","-cos(" + str(ab) + ")"],["cos(pi+" + str(ab) + ")","-cos(" + str(ab) + ")"],["tan(pi-" + str(ab) + ")","-tan(" + str(ab) + ")"],["tan(pi+" + str(ab) + ")","tan(" + str(ab) + ")"]]
            return [oddPair,cofunsion, inverseIdentity]
        items = []
        characters = ["a","b"]
        for x in range(2):
            identities = assignVariable(characters[x])
            a = random.randint(0,2)
            b = random.randint(0,len(identities[a]) - 1)
            items.append(identities[a][b])
        solution = "[" + str(items[0][1]) + "]+[" + str(items[1][1]) + "]"
        question = "[" + str(items[0][0]) + "]+[" + str(items[1][0]) + "]"
        options = json.loads(json.dumps({'a':"[" + str((items[0][1])[-6:]) + "]+[" + str((items[1][1])[-6:]) + "]", 'b':"[-" + str((items[0][1])[-6:]) + "]+[" + str((items[1][1])[-6:]) + "]", 'c':"[" + str((items[0][1])[-6:]) + "]+[-" + str((items[1][1])[-6:]) + "]", 'd':"[-" + str((items[0][1])[-6:]) + "]+[-" + str((items[1][1])[-6:]) + "]"}))
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return jsonResponse
    except Exception as er:
        return er
#using the middle angle property solve a problem where you have to achieve
#something like cos(x/2) or sin(x/2)
def sumDifTanProblem1():
    try:
        def assignVariable(ab):
            oddPair = [["tan(-" + str(ab) + ")","-tan(" + str(ab) + ")"]]
            cofunsion = [["cot((pi/2)-" + str(ab) + ")","tan(" + str(ab) + ")"]]
            inverseIdentity = [["tan(pi-" + str(ab) + ")","-tan(" + str(ab) + ")"],["tan(pi+" + str(ab) + ")","tan(" + str(ab) + ")"]]
            return [oddPair,cofunsion, inverseIdentity]
        items = []
        characters = ["a","b"]
        solution = ""
        for x in range(2):
            identities = assignVariable(characters[x])
            a = random.randint(0,2)
            b = random.randint(0,len(identities[a]) - 1)
            items.append(identities[a][b])
        if (items[0][1])[0] != "-" and (items[1][1])[0] != "-":
            solution = "tan(a+b)"
        elif (items[0][1])[0] == "-" and (items[1][1])[0] == "-":
            solution = "-tan(a+b)"
        elif (items[0][1])[0] != "-" and (items[1][1])[0] == "-":
            solution = "tan(a-b)"
        elif (items[0][1])[0] == "-" and (items[1][1])[0] != "-":
            solution = "-tan(a-b)"
        question = "([" + str(items[0][0]) + "]+[" + str(items[1][0]) + "])/(1-[" + str(items[0][0]) + "][" + str(items[1][0]) + "])"
        options = json.loads(json.dumps({'a':"tan(a+b)", 'b':"-tan(a+b)", 'c':"tan(a-b)", 'd':"-tan(a-b)"}))
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return jsonResponse
    except Exception as er:
        return er
#using the middle angle property solve a problem where you have to achieve
#something like cos(x/2) or sin(x/2)
def doubleAngleTanProblem1():
    try:
        t = random.randint(0,1)
        def assignVariable(ab):
            oddPair = [["sin(-a)","-sin(a)"],["cos(-a)","cos(a)"]]
            cofunsion = [["cos((pi/2)-a)","sin(a)"],["sin((pi/2)-a)","cos(a)"]]
            inverseIdentity = [["sin(pi-a)","sin(a)"],["sin(pi+a)","-sin(a)"],["cos(pi-a)","-cos(a)"],["cos(pi+a)","-cos(a)"]]
            return [oddPair[ab[0][0]:ab[0][1]],cofunsion[ab[1][0]:ab[1][1]], inverseIdentity[ab[2][0]:ab[2][1]]]
        items = []
        _range = [[[0,1],[0,1],[0,2]],[[1,2],[1,2],[2,4]]]
        firstCharacter = "-"
        solution = ""
        question = ""
        for x in range(2):
            identities = assignVariable(_range[x])
            a = random.randint(0,2)
            b = random.randint(0,len(identities[a]) - 1)
            items.append(identities[a][b])
        if ((items[0][1])[0] != "-" and (items[1][1])[0] != "-") or ((items[0][1])[0] == "-" and (items[1][1])[0] == "-"):
            firstCharacter = ""
        if t == 0:
            question = "[(" + str(items[0][0]) + ")/(" + str(items[1][0]) + ")]*[2/(1-tan^2(a))]"
            solution = firstCharacter + "tan(2a)"
        else:
            question = "[(" + str(items[1][0]) + ")/(" + str(items[0][0]) + ")]*[(1-tan^2(a))/2]"
            solution = firstCharacter + "cot(2a)"
        options = json.loads(json.dumps({'a':"tan(2a)", 'b':"-tan(2a)", 'c':"cot(2a)", 'd':"-cot(2a)"}))
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return jsonResponse
    except Exception as er:
        return er
#using the middle angle property solve a problem where you have to achieve
#something like cos(x/2) or sin(x/2)
def middleAngleTanProblem1():
    try:
        t = random.randint(0,1)
        oddPair = [["sin(-a)","-sin(a)"]]
        cofunsion = [["cos((pi/2)-a)","sin(a)"]]
        inverseIdentity = [["sin(pi-a)","sin(a)"],["sin(pi+a)","-sin(a)"]]
        identities = [oddPair,cofunsion, inverseIdentity]
        firstCharacter = ""
        solution = ""
        question = ""
        a = random.randint(0,2)
        b = random.randint(0,len(identities[a]) - 1)
        item = identities[a][b]
        if (item[1])[0] == "-":
            firstCharacter = "-"
        if t == 0:
            question = "(" + str(item[0]) + ")/(1+cos(a))"
            solution = firstCharacter + "tan(a/2)"
        else:
            question = "(1+cos(a))/(" + str(item[0]) + ")"
            solution = firstCharacter + "cot(a/2)"
        options = json.loads(json.dumps({'a':"tan(a/2)", 'b':"-tan(a/2)", 'c':"cot(a/2)", 'd':"-cot(a/2)"}))
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return jsonResponse
    except Exception as er:
        return er


exam1 = [basicIdentityProblem1, sumIdentityProblem1, doubleAngleProblem1, middleAngleProblem1, productSumProblem1, sumProductProblem1, basicPropertyProblem1, sumDifTanProblem1, doubleAngleTanProblem1, middleAngleTanProblem1]
exam2 = []
listMethods = [exam1, exam2]
def generateExam(unit):
    solution = []
    lista = listMethods[int(unit) - 1]
    for x in range(12):
        question = random.randint(1,len(lista))
        #numberQuestion='QUESTION '+str(x+1)
        item = str(lista[question - 1]())
        #jsonData = json.loads(json.dumps({numberQuestion: json.loads(item)}))
        solution.append(json.loads(item))
    return solution