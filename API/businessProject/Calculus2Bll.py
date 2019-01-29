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
#render asciimath: http://asciimath.org/#gettingStarted
#asciimath image: https://dlippman.imathas.com/asciimathtex/AMT.html
#convert ascii to latex and katex: https://www.intmath.com/help/asciimath-input-latex-katex-output.php
#another option to render ascii: http://asciimath.org/
#online converter to image: http://www.sciweavers.org/free-online-latex-equation-editor
#init_session(use_latex=True)

#calculus quotient rule: https://www.maa.org/sites/default/files/switkes01200543268.pdf


#find the values of x for which slope is 0


def basicProblem():
    try:
        #w = symbols('w')
        #z ="𝑥 = (−𝑏 ± √(𝑏² − 4𝑎𝑐))⁄2𝑎"
        #Eq(z, z.doit())
        #z=symbols("z")
        #(a+pi)**2
        a = random.randint(2,10) * (random.randint(0,1) * 2 - 1)
        b = random.randint(2,10) * (random.randint(0,1) * 2 - 1)
        c = random.randint(2,10) * (random.randint(0,1) * 2 - 1)
        d = random.randint(2,10)
        e = random.randint(2,10) * (random.randint(0,1) * 2 - 1)
        solution = r'({'+str(a)+r'e}^{x})+({'+str(round(b/3,4))+r'x}^{3})+('+str(c)+r'*ln(|x|))+(\frac{{'+str(d)+r'}^{x}}{'+str(round(math.log(d),4))+r'})+({'+str(e)+r'x})+C'
        question = r'\int({'+str(a)+r'e}^{x})+({'+str(b)+r'x}^{2})+(\frac{'+str(c)+r'}{x})+({'+str(d)+r'}^{x})+({'+str(e)+r'})'
        alternatives = coursesFunctionsBll.multipleOptions([a,b,c,d,e],5)
        tempAlternatives =[]
        for y1 in range(5):
            tempAlternatives.append(r'({'+str(alternatives[y1][0])+r'e}^{x})+({'+str(round(alternatives[y1][1]/3,4))+r'x}^{3})+('+str(alternatives[y1][2])+r'*ln(|x|))+(\frac{{'+str(alternatives[y1][3])+r'}^{x}}{'+str(round(math.log(alternatives[y1][3]),4))+r'})+({'+str(alternatives[y1][4])+r'x})+C')
        options =json.loads(json.dumps({'a':tempAlternatives[0], 'b':tempAlternatives[1], 'c': tempAlternatives[2], 'd': tempAlternatives[3], 'e': tempAlternatives[4]}))
        #question=r'\left(x^2\right)'
        #\displaystyle\int{e}^{x}+{x}^{3}+\frac{1}{x}+{5}+{7}^{x}
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return jsonResponse
    except Exception as er:
        return er

def sustitutionProblem():
    try:
        a = random.randint(2,10)
        b = random.randint(2,10)
        c = random.randint(2,10)
        d = random.randint(3,10)
        e = random.randint(2,10)
        comp1=round((a*e)/(-c*d*(e-1)),4)
        solution = str(comp1)+r'*({'+str(b)+r'-'+str(c)+r'{x}^{'+str(d)+r'}})^{'+str(round((e-1)/e,4))+r'}+C'
        question = r'\int\frac{'+str(a)+r'x^{'+str(d-1)+r'}}{\sqrt['+str(e)+r']{'+str(b)+r'-'+str(c)+r'{x}^{'+str(d)+r'}}}'
        #question = r'\sqrt[3]{2+3x}'
        alternatives = coursesFunctionsBll.multipleOptions([comp1],5)
        tempAlternatives =[]
        for y1 in range(5):
            tempAlternatives.append(str(alternatives[y1][0])+r'*({'+str(b)+r'-'+str(c)+r'{x}^{'+str(d)+r'}})^{'+str(round((e-1)/e,4))+r'}+C')
        options =json.loads(json.dumps({'a':tempAlternatives[0], 'b':tempAlternatives[1], 'c': tempAlternatives[2], 'd': tempAlternatives[3], 'e': tempAlternatives[4]}))
        #question=r'\left(x^2\right)'
        #\displaystyle\int{e}^{x}+{x}^{3}+\frac{1}{x}+{5}+{7}^{x}
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return jsonResponse
    except Exception as er:
        return er

def symmetryProblem():
    try:
        a = random.randint(2,5)
        b = random.randint(1,2)*2
        c = random.randint(0,5)
        d = random.randint(1,10)
        oddPair = [[r"sin(x)","-"],[r"cos(x)","+"],[r"tan(x)","-"],[r"cot(x)","-"],[r"sec(x)","+"],[r"csc(x)","-"]]
        options =json.loads(json.dumps({'a':r"0", 'b':r"2*\int_{0}^{"+str(d)+r"}\frac{"+str(oddPair[c][0])+r"}{{x}^{"+str(a)+r"}+{x}^{"+str(a+b)+r"}+{x}^{"+str(a+(b*2))+r"}}"}))
        sign1= 1 if a%2==0 else -1
        sign2= 1 if oddPair[c][1]=='+' else -1
        solution = options['a'] if sign1*sign2==-1 else options['b']
        question = r"use symmetry of the integral to find equivalent for \int_{"+str(-d)+r"}^{"+str(d)+r"}\frac{"+str(oddPair[c][0])+r"}{{x}^{"+str(a)+r"}+{x}^{"+str(a+b)+r"}+{x}^{"+str(a+(b*2))+r"}}"
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return jsonResponse
    except Exception as er:
        return er

def partsProblem():
    try:
        a = random.randint(2,20)
        b = random.randint(0,1)
        c = random.randint(0,1)
        question=""
        solution=""
        if b==0:
            question=r'\int '+str(a)+r'^{x}cos(x)'
            solution=r'\frac{'+str(a)+r'^{x}(sin(x)+'+str(round(math.log(a),4))+r'cos(x))}{'+str(1+(round(math.log(a)**2,4)))+r'}'
        elif b==1:
            question=r'\int '+str(a)+r'^{x}sin(x)'
            solution=r'\frac{'+str(a)+r'^{x}('+str(round(math.log(a),4))+r'sin(x)-cos(x))}{'+str(1+(round(math.log(a)**2,4)))+r'}'
        alt = math.log(a)/2 if c==0 else math.log(a)*2
        options =json.loads(json.dumps({'a': r'\frac{'+str(a)+r'^{x}(sin(x)+'+str(round(math.log(a),4))+r'cos(x))}{'+str(1+round((math.log(a)**2),4))+r'}', 'b':r'\frac{'+str(a)+r'^{x}(sin(x)+'+str(round(alt,4))+r'cos(x))}{'+str(round(1+(alt**2),4))+r'}', 'c': r'\frac{'+str(a)+r'^{x}('+str(round(math.log(a),4))+r'sin(x)-cos(x))}{'+str(1+round((math.log(a)**2),4))+r'}', 'd': r'\frac{'+str(a)+r'^{x}('+str(round(alt,4))+r'sin(x)-cos(x))}{'+str(round(1+(alt**2),4))+r'}'}))
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return jsonResponse
    except Exception as er:
        return er
def trigonometryProblem():
    try:
        def assignVariable(ab): #0 item is the expression, 1 is simplification, 2 is derivation
            oddPair = [[r"sin(-"+str(ab)+")",r"-sin("+str(ab)+")",r"cos("+str(ab)+")"],[r"cos(-"+str(ab)+")",r"cos("+str(ab)+")",r"sin("+str(ab)+")"],[r"tan(-"+str(ab)+")",r"-tan("+str(ab)+")",r"ln(cos("+str(ab)+"))"],[r"cot(-"+str(ab)+")",r"-cot("+str(ab)+")",r"-ln(sin("+str(ab)+"))"],[r"sec(-"+str(ab)+")",r"sec("+str(ab)+")",r"ln(sec("+str(ab)+")+tan("+str(ab)+"))"],[r"csc(-"+str(ab)+")",r"-csc("+str(ab)+")",r"ln(csc("+str(ab)+")+cot("+str(ab)+"))"]]
            cofunsion =[[r"sin(\frac{\pi}{2}-"+str(ab)+")",r"cos("+str(ab)+")",r"sin("+str(ab)+")"],[r"cos(\frac{\pi}{2}-"+str(ab)+")",r"sin("+str(ab)+")",r"-cos("+str(ab)+")"],[r"tan(\frac{\pi}{2}-"+str(ab)+")",r"cot("+str(ab)+")",r"ln(sin("+str(ab)+"))"],[r"cot(\frac{\pi}{2}-"+str(ab)+")",r"tan("+str(ab)+")",r"-ln(cos("+str(ab)+"))"]]
            inverseIdentity = [[r"sin(\pi-"+str(ab)+")",r"sin("+str(ab)+")",r"-cos("+str(ab)+")"],[r"sin(\pi+"+str(ab)+")",r"-sin("+str(ab)+")",r"cos("+str(ab)+")"],[r"cos(\pi-"+str(ab)+")",r"-cos("+str(ab)+")",r"-sin("+str(ab)+")"],[r"cos(\pi+"+str(ab)+")",r"-cos("+str(ab)+")",r"-sin("+str(ab)+")"],[r"tan(\pi-"+str(ab)+")",r"-tan("+str(ab)+")",r"ln(cos("+str(ab)+"))"],[r"tan(\pi+"+str(ab)+")",r"tan("+str(ab)+")",r"-ln(cos("+str(ab)+"))"]]
            return [oddPair,cofunsion, inverseIdentity]
        items=[]
        characters=["a","b"]
        for x in range(2):
            identities = assignVariable(characters[x])
            a = random.randint(0,2)
            b = random.randint(0,len(identities[a])-1)
            items.append(identities[a][b])
        solution=r"["+str(items[0][2])+r"]+["+str(items[1][2])+r"]"
        question=r"if f(a)=["+str(items[0][0])+r"] and g(b)=["+str(items[1][0])+r"] find \int f(a) + \int g(b)"
        options =json.loads(json.dumps({'a':r"["+str((items[0][2])[-1*len(items[0][2]) if (items[0][2])[0]!='-' else (-1*len(items[0][2]))+1:])+r"]+["+str((items[1][2])[-1*len(items[1][2]) if (items[1][2])[0]!='-' else (-1*len(items[1][2]))+1:])+r"]", 'b':"[-"+str((items[0][2])[-1*len(items[0][2]) if (items[0][2])[0]!='-' else (-1*len(items[0][2]))+1:])+r"]+["+str((items[1][2])[-1*len(items[1][2]) if (items[1][2])[0]!='-' else (-1*len(items[1][2]))+1:])+r"]", 'c':r"["+str((items[0][2])[-1*len(items[0][2]) if (items[0][2])[0]!='-' else (-1*len(items[0][2]))+1:])+"]+[-"+str((items[1][2])[-1*len(items[1][2]) if (items[1][2])[0]!='-' else (-1*len(items[1][2]))+1:])+r"]", 'd':r"[-"+str((items[0][2])[-1*len(items[0][2]) if (items[0][2])[0]!='-' else (-1*len(items[0][2]))+1:])+r"]+[-"+str((items[1][2])[-1*len(items[1][2]) if (items[1][2])[0]!='-' else (-1*len(items[1][2]))+1:])+r"]"}))
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return jsonResponse
    except Exception as er:
        return er
def trigonometrySubstitutionProblem():
    try:
        a = random.randint(2,10)
        q1=random.randint(0,2)
        q2=random.randint(0,2)
        def assignVariable(ab): #0 item is the expression, 1 is simplification, 2 is derivation
            opt1 = [[r"\frac{\sqrt{"+str(ab**2)+r"-{x}^{2}}}{x}",r"\sqrt{"+str(ab**2)+r"-x^2}-"+str(ab)+r"ln(\sqrt{"+str(ab**2)+r"-x^2}+"+str(ab)+r"ln(x))+"+str(ab)+r"+C",0],
                    [r"\frac{\sqrt{"+str(ab**2)+r"+{x}^{2}}}{x}",r"\sqrt{"+str(ab**2)+r"+x^2}-"+str(ab)+r"ln(\sqrt{"+str(ab**2)+r"+x^2}+"+str(ab)+r"ln(x))+"+str(ab)+r"+C",0],
                    [r"\frac{\sqrt{{x}^{2}-"+str(ab**2)+r"}}{x}",r"\sqrt{x^2-"+str(ab**2)+r"}+"+str(ab)+r"atan(\frac{"+str(ab)+r"}{\sqrt{"+str(ab**2)+r"+x^2}})+C",0]]
            opt2 = [[r"\frac{1}{x\sqrt{"+str(ab**2)+r"-{x}^{2}}}",r"\frac{1}{"+str(ab)+r"}(ln(x)-ln(\sqrt{"+str(ab**2)+r"-{x}^{2}}+"+str(ab)+r"))+C",0],
                    [r"\frac{1}{x\sqrt{"+str(ab**2)+r"+{x}^{2}}}",r"\frac{1}{"+str(ab)+r"}(ln(x)-ln(\sqrt{"+str(ab**2)+r"+{x}^{2}}+"+str(ab)+r"))+C",0],
                    [r"\frac{1}{x\sqrt{{x}^{2}-"+str(ab**2)+r"}}",r"\frac{-1}{"+str(ab)+r"}atan(\frac{"+str(ab)+r"}{\sqrt{{x}^{2}-"+str(ab**2)+r"}})+C",0]]
            opt3 = [[r"\frac{1}{x^2\sqrt{"+str(ab**2)+r"-{x}^{2}}}",r"-\frac{\sqrt{"+str(ab**2)+r"-{x}^{2}}}{"+str(ab**2)+r"x}+C",0],
                    [r"\frac{1}{x^2\sqrt{"+str(ab**2)+r"+{x}^{2}}}",r"\frac{\sqrt{"+str(ab**2)+r"+{x}^{2}}}{"+str(ab**2)+r"x}+C",0],
                    [r"\frac{1}{x^2\sqrt{{x}^{2}-"+str(ab**2)+r"}}",r"\frac{\sqrt{{x}^{2}-"+str(ab**2)+r"}}{"+str(ab**2)+r"x}+C",0]]
            return [opt1,opt2, opt3]
        identities = assignVariable(a)
        identities[q1][q2][2]=1
        solution= identities[q1][q2][1]
        alternatives = [identities[q1][q2][1]]
        while len(alternatives)<5:
            q3=random.randint(0,2)
            q4=random.randint(0,2)
            place = random.randint(0,1)
            if identities[q3][q4][2]==0:
                identities[q3][q4][2]=1
                if place==0:
                    alternatives.append(identities[q3][q4][1])
                else:
                    alternatives.insert(0,identities[q3][q4][1])

        question=r"find \int "+identities[q1][q2][0]+r":"
        #question = r"\arctan(x)"
        options =json.loads(json.dumps({'a':alternatives[0], 'b':alternatives[1], 'c':alternatives[2], 'd':alternatives[3], 'e':alternatives[4]}))
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return jsonResponse
    except Exception as er:
        return er

def fractionProblem():
    try:
        a = random.randint(2,10)*(random.randint(0,1)*2-1)
        b = random.randint(2,10)*(random.randint(0,1)*2-1)
        c = random.randint(2,10)*(random.randint(0,1)*2-1)
        d = random.randint(2,10)*(random.randint(0,1)*2-1)
        e = random.randint(2,10)*(random.randint(0,1)*2-1)
        f = random.randint(2,10)*(random.randint(0,1)*2-1)
        g = random.randint(2,10)*(random.randint(0,1)*2-1)

        a1=d*f
        b1=(d*g)+(e*f)
        c1=e*g

        A=round(c/(e*g),4)
        B=round(((b)-(A*g*d)-(A*e*f)-(a*e/d)+(A*d*f*e/d))*(d/((g*d)-(e*f))),4)
        C=round(((a)-(A*d*f)-(B*f))/d,4)
        solution= r""+str(A)+r"ln|x|+"+str(B)+r"ln|("+str(d)+r"x)+("+str(e)+r")|+"+str(C)+r"ln|("+str(f)+r"x)+("+str(g)+r")|+C"
        question = r"\int \frac{"+str(a)+r"x^{2}+"+str(b)+r"x+"+str(c)+r"}{"+str(a1)+r"x^{3}+"+str(b1)+r"^{2}x+"+str(c1)+r"x}"
        alternatives = coursesFunctionsBll.multipleOptions([A,B,C],5)
        tempAlternatives =[]
        for y1 in range(5):
            tempAlternatives.append(r""+str(alternatives[y1][0])+r"ln|x|+"+str(alternatives[y1][1])+r"ln|("+str(d)+r"x)+("+str(e)+r")|+"+str(alternatives[y1][2])+r"ln|("+str(f)+r"x)+("+str(g)+r")|+C")
        options =json.loads(json.dumps({'a':tempAlternatives[0], 'b':tempAlternatives[1], 'c': tempAlternatives[2], 'd': tempAlternatives[3], 'e': tempAlternatives[4]}))
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return jsonResponse
    except Exception as er:
        return er

def substitutionRootProblem():
    try:
        a = random.randint(2,10)*(random.randint(0,1)*2-1)
        b = random.randint(2,10)*(random.randint(0,1)*2-1)
        c = random.randint(2,10)*(random.randint(0,1)*2-1)
        d = random.randint(2,10)*(random.randint(0,1)*2-1)
        n = random.randint(3,10)

        comp1=round((a*n)/((c**2)*(2*n-1)),4)
        comp2=round((b-(a*d/c))*(n/(c*(n-1))),4)
        power1 = round((2*n-1)/n,4)
        power2 = round((n-1)/n,4)
       
        solution= r""+str(comp1)+r"\sqrt["+str(power1)+r"]{("+str(c)+r"x+"+str(d)+r")}+"+str(comp2)+r"\sqrt["+str(power2)+r"]{("+str(c)+r"x+"+str(d)+r")}+C"
        question = r"\int \frac{"+str(a)+r"x+"+str(b)+r"}{\sqrt["+str(n)+r"]{"+str(c)+r"x+"+str(d)+r"}}"
        alternatives = coursesFunctionsBll.multipleOptions([comp1,power1,comp2, power2],5)
        tempAlternatives =[]
        for y1 in range(5):
            tempAlternatives.append(r""+str(alternatives[y1][0])+r"\sqrt["+str(alternatives[y1][1])+r"]{("+str(c)+r"x+"+str(d)+r")}+"+str(alternatives[y1][2])+r"\sqrt["+str(alternatives[y1][3])+r"]{("+str(c)+r"x+"+str(d)+r")}+C")
        options =json.loads(json.dumps({'a':tempAlternatives[0], 'b':tempAlternatives[1], 'c': tempAlternatives[2], 'd': tempAlternatives[3], 'e': tempAlternatives[4]}))
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return jsonResponse
    except Exception as er:
        return er

def partsPowerProblem():
    try:
        a = random.randint(2,10)
        b = random.randint(2,10)
        comp1= round(math.log(a)*(b-1)*(-1),4)
        comp2= round(math.log(a)*((b-1)**2),4)
        question=r"\int \frac{\log_{"+str(a)+r"}(x)}{{x}^{"+str(b)+r"}}"
        solution=r"\frac{ln(x)}{"+str(comp1)+r"{x}^{"+str(b-1)+r"}}-\frac{1}{"+str(comp2)+r"{x}^{"+str(b-1)+r"}}+C"
        alternatives = coursesFunctionsBll.multipleOptions([comp1,comp2],5)
        tempAlternatives =[]
        for y1 in range(5):
            tempAlternatives.append(r"\frac{ln(x)}{"+str(alternatives[y1][0])+r"{x}^{"+str(b-1)+r"}}-\frac{1}{"+str(alternatives[y1][1])+r"{x}^{"+str(b-1)+r"}}+C")
        options =json.loads(json.dumps({'a':tempAlternatives[0], 'b':tempAlternatives[1], 'c': tempAlternatives[2], 'd': tempAlternatives[3], 'e': tempAlternatives[4]}))
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return jsonResponse
    except Exception as er:
        return er
#use quotient method to solve this problem
def quotientProblem():
    try:
        a = (random.randint(0,4)*2)+1
        b = random.randint(0,1)
        c = random.randint(0,1)
        d = random.randint(2,10)*(random.randint(0,1)*2-1)
        comp1=round(2/(a*d),4)
        comp2=round(2/(a*d*d),4)
        c1 = [comp1,round(comp1/2,4) if c==0 else round(comp1*2,4)]
        c2=  [comp2,round(comp2/2,4) if c==0 else round(comp2*2,4)]
        c1.sort()
        c2.sort()
        question=""
        solution=""
        if b==0:
            question=r'\int \frac{sin({'+str(d)+r'x}^{\frac{-'+str(a)+r'}{2}})}{{x}^{'+str(a+1)+r'}}'
            solution=r'\frac{'+str(comp1)+r'cos({'+str(d)+r'x}^{'+str(-1*a/2)+r'})}{{x}^{'+str(a/2)+r'}}-'+str(comp2)+r'sin({'+str(d)+r'x}^{'+str(-1*a/2)+r'})+C'
        elif b==1:
            question=r'\int \frac{cos({'+str(d)+r'x}^{\frac{-'+str(a)+r'}{2}})}{{x}^{'+str(a+1)+r'}}'
            solution=r'\frac{'+str(-1*comp1)+r'sin({'+str(d)+r'x}^{'+str(-1*a/2)+r'})}{{x}^{'+str(a/2)+r'}}-'+str(comp2)+r'cos({'+str(d)+r'x}^{'+str(-1*a/2)+r'})+C'
        options =json.loads(json.dumps({'a': r'\frac{'+str(c1[0])+r'cos({'+str(d)+r'x}^{'+str(-1*a/2)+r'})}{{x}^{'+str(a/2)+r'}}-'+str(c2[0])+r'sin({'+str(d)+r'x}^{'+str(-1*a/2)+r'})+C', 
                                        'b':r'\frac{'+str(c1[1])+r'cos({'+str(d)+r'x}^{'+str(-1*a/2)+r'})}{{x}^{'+str(a/2)+r'}}-'+str(c2[1])+r'sin({'+str(d)+r'x}^{'+str(-1*a/2)+r'})+C', 
                                        'c': r'\frac{'+str(-1*c1[0])+r'sin({'+str(d)+r'x}^{'+str(-1*a/2)+r'})}{{x}^{'+str(a/2)+r'}}-'+str(c2[0])+r'cos({'+str(d)+r'x}^{'+str(-1*a/2)+r'})+C', 
                                        'd': r'\frac{'+str(-1*c1[1])+r'sin({'+str(d)+r'x}^{'+str(-1*a/2)+r'})}{{x}^{'+str(a/2)+r'}}-'+str(c2[1])+r'cos({'+str(d)+r'x}^{'+str(-1*a/2)+r'})+C'}))
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return jsonResponse
    except Exception as er:
        return er


exam1 = [basicProblem, sustitutionProblem, symmetryProblem, partsProblem, trigonometryProblem, trigonometrySubstitutionProblem, fractionProblem, substitutionRootProblem, partsPowerProblem, quotientProblem]
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

#integrate ((25-x^2)^(1/2))/(x)