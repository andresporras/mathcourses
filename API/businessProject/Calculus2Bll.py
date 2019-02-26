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
#web site to calculate integrals and derivatives: https://www.wolframalpha.com/input/?i=integrate+cos(2x)*x

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
            opt1 = [[r"\frac{\sqrt{"+str(ab**2)+r"-{x}^{2}}}{x}",r"\sqrt{"+str(ab**2)+r"-x^2}-"+str(ab)+r"ln(\sqrt{"+str(ab**2)+r"-x^2}+"+str(ab)+r")+"+str(ab)+r"ln(x)+C",0],
                    [r"\frac{\sqrt{"+str(ab**2)+r"+{x}^{2}}}{x}",r"\sqrt{"+str(ab**2)+r"+x^2}-"+str(ab)+r"ln(\sqrt{"+str(ab**2)+r"+x^2}+"+str(ab)+r")+"+str(ab)+r"ln(x)+C",0],
                    [r"\frac{\sqrt{{x}^{2}-"+str(ab**2)+r"}}{x}",r"\sqrt{x^2-"+str(ab**2)+r"}+"+str(ab)+r"atan(\frac{"+str(ab)+r"}{\sqrt{"+str(ab**2)+r"+x^2}})+C",0]]
            opt2 = [[r"\frac{1}{x\sqrt{"+str(ab**2)+r"-{x}^{2}}}",r"\frac{1}{"+str(ab)+r"}(ln(x)-ln(\sqrt{"+str(ab**2)+r"-{x}^{2}}+"+str(ab)+r"))+C",0],
                    [r"\frac{1}{x\sqrt{"+str(ab**2)+r"+{x}^{2}}}",r"\frac{1}{"+str(ab)+r"}(ln(x)-ln(\sqrt{"+str(ab**2)+r"+{x}^{2}}+"+str(ab)+r"))+C",0],
                    [r"\frac{1}{x\sqrt{{x}^{2}-"+str(ab**2)+r"}}",r"\frac{-1}{"+str(ab)+r"}atan(\frac{"+str(ab)+r"}{\sqrt{{x}^{2}-"+str(ab**2)+r"}})+C",0]]
            opt3 = [[r"\frac{1}{x^2\sqrt{"+str(ab**2)+r"-{x}^{2}}}",r"-\frac{\sqrt{"+str(ab**2)+r"-{x}^{2}}}{"+str(ab**2)+r"x}+C",0],
                    [r"\frac{1}{x^2\sqrt{"+str(ab**2)+r"+{x}^{2}}}",r"-\frac{\sqrt{"+str(ab**2)+r"+{x}^{2}}}{"+str(ab**2)+r"x}+C",0],
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
        A0=c/(e*g)
        B0=((b)-(A0*g*d)-(A0*e*f)-(a*e/d)+(A0*d*f*e/d))*(d/((g*d)-(e*f)))
        C0=((a)-(A0*d*f)-(B0*f))/d
        A=round(A0,4)
        B=round(B0/d,4)
        C=round(C0/f,4)
        solution= r""+str(A)+r"ln|x|+"+str(B)+r"ln|("+str(d)+r"x)+("+str(e)+r")|+"+str(C)+r"ln|("+str(f)+r"x)+("+str(g)+r")|+C"
        question = r"\int \frac{"+str(a)+r"x^{2}+"+str(b)+r"x+"+str(c)+r"}{"+str(a1)+r"x^{3}+"+str(b1)+r"x^{2}+"+str(c1)+r"x}"
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

#use quotient method to solve this problem
def areaBetweenProblem():
    try:
        a1 = random.randint(2,10)*(-1)
        b1 = random.randint(2,10)*(random.randint(0,1)*2-1)
        c1 = random.randint(2,10)*(random.randint(0,1)*2-1)
        a2 = random.randint(2,10)
        b2 = random.randint(2,10)*(random.randint(0,1)*2-1)
        c2 = random.randint(2,10)*(random.randint(0,1)*2-1)

        x1= (-b1)/(2*a1)
        x2= (-b2)/(2*a2)
        if (a1*(x1**2)+b1*x1+c1)>(a2*(x2**2)+b2*x2+c2):
            return areaBetweenProblem()
        p1=random.randint(1,5)
        p2=random.randint(6,10)

        major1= (a1/3)*(p2**3)+(b1/2)*(p2**2)+c1*p2
        minor1= (a1/3)*(p1**3)+(b1/2)*(p1**2)+c1*p1
        major2= (a2/3)*(p2**3)+(b2/2)*(p2**2)+c2*p2
        minor2= (a2/3)*(p1**3)+(b2/2)*(p1**2)+c2*p1

        solution= round((major2-minor2)-(major1-minor1),4)
        question = r"find the area between "+str(a1)+r"x^2"+("+" if b1>0 else "")+str(b1)+r"x"+("+" if c1>0 else "")+str(c1)+r" and "+str(a2)+r"x^2"+("+" if b2>0 else "")+str(b2)+r"x"+("+" if c2>0 else "")+str(c2)+r" in the range between x="+str(p1)+r" and x="+str(p2)+r":"
        alternatives = coursesFunctionsBll.multipleOptions([solution],5)
        tempAlternatives =[]
        for y1 in range(5):
            tempAlternatives.append(r""+str(alternatives[y1][0]))
        options =json.loads(json.dumps({'a':tempAlternatives[0], 'b':tempAlternatives[1], 'c': tempAlternatives[2], 'd': tempAlternatives[3], 'e': tempAlternatives[4]}))

        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return jsonResponse
    except Exception as er:
        return er

#use quotient method to solve this problem
def volumeProblem():
    try:
        a = random.randint(2,4)
        b = random.randint(2,4)
        q = random.randint(0,1)
        x1=random.randint(1,3)
        x2=random.randint(4,6)
        sol=0
        question=""
        if q==0:
            major=((math.log(b*x2)**2)-(2*math.log(b*x2))+(2))*(math.pi*x2)/(math.log(a)**2)
            minor=((math.log(b*x1)**2)-(2*math.log(b*x1))+(2))*(math.pi*x1)/(math.log(a)**2)
            sol=round(major-minor,4)
            question="find the volume that appears when rotate \log _{"+str(a)+r"}("+str(b)+r"x), in x axes, between x="+str(x1)+r" and x="+str(x2)+r":"
        else:
            major=(a**(2*b*x2))*math.pi/(math.log(a)*2*b)
            minor=(a**(2*b*x1))*math.pi/(math.log(a)*2*b)
            sol=round(major-minor,4)
            question="find the volume that appears when rotate {"+str(a)+r"}^{"+str(b)+r"x}, in x axes, find the volume between x="+str(x1)+r" and x="+str(x2)+r":"
        alternatives = coursesFunctionsBll.multipleOptions([sol],5)
        tempAlternatives =[]
        for y1 in range(5):
            tempAlternatives.append(r""+str(coursesFunctionsBll.yoxterFormat(alternatives[y1][0])))
        options =json.loads(json.dumps({'a':tempAlternatives[0], 
                                        'b':tempAlternatives[1], 
                                        'c': tempAlternatives[2], 
                                        'd': tempAlternatives[3], 
                                        'e': tempAlternatives[4]}))
        solution = str(coursesFunctionsBll.yoxterFormat(sol))
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return jsonResponse
    except Exception as er:
        return er


def cylinderVolumeProblem():
    try:
        a = random.randint(2,10)
        b = random.randint(2,10)
        c = random.randint(1,10)
        d = random.randint(0,1)
        x1=random.randint(1,5)
        x2=random.randint(6,10)
        solution=0
        question=""
        if d==0:
            major= ((math.sin(a*x2)/(a*a))-(math.cos(a*x2)*x2/a)+((1/((1/b)+2))*(x2**((1/b)+2)))+((c/2)*(x2**2)))*(2*math.pi)
            minor= ((math.sin(a*x1)/(a*a))-(math.cos(a*x1)*x1/a)+((1/((1/b)+2))*(x1**((1/b)+2)))+((c/2)*(x1**2)))*(2*math.pi)
            solution=round(major-minor,4)
            question="for the cylinder which appears when you rotate, in y axis,  the function sin("+str(a)+r"x)+{x}^{1/"+str(b)+r"}+"+str(c)+r" between x="+str(x1)+r" and x="+str(x2)+r". PS: use radians scale:"
        else:
            major= ((math.sin(a*x2)*x2/a)+(math.cos(a*x2)/(a*a))+((1/((1/b)+2))*(x2**((1/b)+2)))+((c/2)*(x2**2)))*(2*math.pi)
            minor= ((math.sin(a*x1)*x1/a)+(math.cos(a*x1)/(a*a))+((1/((1/b)+2))*(x1**((1/b)+2)))+((c/2)*(x1**2)))*(2*math.pi)
            solution=round(major-minor,4)
            question="for the cylinder which appears when you rotate, in y axis,  the function cos("+str(a)+r"x)+{x}^{1/"+str(b)+r"}+"+str(c)+r", find the volume between x="+str(x1)+r" and x="+str(x2)+r". PS: use radians scale:"
        alternatives = coursesFunctionsBll.multipleOptions([solution],5)
        tempAlternatives =[]
        for y1 in range(5):
            tempAlternatives.append(alternatives[y1][0])
        options =json.loads(json.dumps({'a':tempAlternatives[0], 
                                        'b':tempAlternatives[1], 
                                        'c': tempAlternatives[2], 
                                        'd': tempAlternatives[3], 
                                        'e': tempAlternatives[4]}))
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return jsonResponse
    except Exception as er:
        return er

#use hooke law for this problem
def springProblem():
    try:
        f = random.randint(20,100)
        x0 = random.randint(1,50)
        x1 = random.randint(51,100)
        x2 = random.randint(51,75)
        x3 = random.randint(76,100)

        K = f/((x1-x0)/100)
        J= round((K/2)*(((x3-x0)/100)**2-((x2-x0)/100)**2),4)
        solution = str(J)+r" J"
        question=r"A force of "+str(f)+r" N is required to stop a spring which was stretched from his natural length of "+str(x0)+r" cm to "+str(x1)+r" cm. \\How much work is required to stretch this spring from "+str(x2)+r" cm to "+str(x3)+r" cm?: "
        alternatives = coursesFunctionsBll.multipleOptions([J],5)
        tempAlternatives =[]
        for y1 in range(5):
            tempAlternatives.append(str(alternatives[y1][0])+r" J")
        options =json.loads(json.dumps({'a':tempAlternatives[0], 
                                        'b':tempAlternatives[1], 
                                        'c': tempAlternatives[2], 
                                        'd': tempAlternatives[3], 
                                        'e': tempAlternatives[4]}))
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return jsonResponse
    except Exception as er:
        return er

def averageProblem():
    try:
        a = random.randint(2,10)
        b = random.randint(2,10)
        x1 = random.randint(1,5)
        x2 = random.randint(6,10)

        major = (1/math.log(a))*((math.log(x2)*(x2**(b+1))/(b+1))-((x2**(b+1))/((b+1)**2)))
        minor = (1/math.log(a))*((math.log(x1)*(x1**(b+1))/(b+1))-((x1**(b+1))/((b+1)**2)))

        solution = round((1/(x2-x1))*(major-minor),4)
        question=r"find the average value of the function ln_{"+str(a)+r"}(x){x}^{"+str(b)+r"} between x="+str(x1)+r" and x="+str(x2)+r": "
        alternatives = coursesFunctionsBll.multipleOptions([solution],5)
        tempAlternatives =[]
        for y1 in range(5):
            tempAlternatives.append(str(alternatives[y1][0]))
        options =json.loads(json.dumps({'a':tempAlternatives[0], 
                                        'b':tempAlternatives[1], 
                                        'c': tempAlternatives[2], 
                                        'd': tempAlternatives[3], 
                                        'e': tempAlternatives[4]}))
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return jsonResponse
    except Exception as er:
        return er

def lengthProblem():
    try:
        a = random.randint(2,10)
        b = random.randint(2,10)
        c = random.randint(2,10)*(random.randint(0,1)*2-1)
        x1 = random.randint(1,5)
        x2 = random.randint(6,10)
        major= (2/(3*a*c*c))*(((a*c*c*x2)+((b*c*c)+1))**(3/2))
        minor= (2/(3*a*c*c))*(((a*c*c*x1)+((b*c*c)+1))**(3/2))
        solution= round(major-minor,4)
        question=r"find the arc length for the function "+str(round((2*c)/(3*a),4))+r"{("+str(a)+r"x+"+str(b)+r")}^{3/2} between x="+str(x1)+r" and x="+str(x2)+r": "
        alternatives = coursesFunctionsBll.multipleOptions([solution],5)
        tempAlternatives =[]
        for y1 in range(5):
            tempAlternatives.append(str(alternatives[y1][0]))
        options =json.loads(json.dumps({'a':tempAlternatives[0], 
                                        'b':tempAlternatives[1], 
                                        'c': tempAlternatives[2], 
                                        'd': tempAlternatives[3], 
                                        'e': tempAlternatives[4]}))
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return jsonResponse
    except Exception as er:
        return er

def yAreaProblem():
    try:
        a = random.randint(2,10)
        x1 = random.randint(1,5)
        x2 = random.randint(6,10)
        major= (math.pi/(27*a))*((1+9*(a*a)*(x2**4))**(3/2))
        minor= (math.pi/(27*a))*((1+9*(a*a)*(x1**4))**(3/2))
        solution= round(major-minor,4)
        question=r"Find the area for the revolution (around x axis) of the function "+str(a)+r"x^3 between x="+str(x1)+r" and x="+str(x2)+r":"
        alternatives = coursesFunctionsBll.multipleOptions([solution],5)
        tempAlternatives =[]
        for y1 in range(5):
            tempAlternatives.append(str(alternatives[y1][0]))
        options =json.loads(json.dumps({'a':tempAlternatives[0], 
                                        'b':tempAlternatives[1], 
                                        'c': tempAlternatives[2], 
                                        'd': tempAlternatives[3], 
                                        'e': tempAlternatives[4]}))
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return jsonResponse
    except Exception as er:
        return er

def xAreaProblem():
    try:
        a = random.randint(2,10)
        b = random.randint(0,1)
        x1 = random.randint(1,5)
        x2 = random.randint(6,10)
        major=0
        minor=0
        question=""
        if b==0:
            major= (math.pi*2/(12*(a**2)))*((1+4*(a**2)*(x2**2))**(3/2))
            minor= (math.pi*2/(12*(a**2)))*((1+4*(a**2)*(x1**2))**(3/2))
            question=r"Find the area for the revolution (around y axis) of the function "+str(a)+r"{x}^{2} between x="+str(x1)+r" and x="+str(x2)+r":"
        if b==1:
            major= (math.pi*2*16/(81*(a**4)))*(((2/5)*((1+(9/4)*(a**2)*x2)**(5/2)))-((2/3)*((1+(9/4)*(a**2)*x2)**(3/2))))
            minor= (math.pi*2*16/(81*(a**4)))*(((2/5)*((1+(9/4)*(a**2)*x1)**(5/2)))-((2/3)*((1+(9/4)*(a**2)*x1)**(3/2))))
            question=r"Find the area for the revolution (around y axis) of the function "+str(a)+r"{x}^{3/2} between x="+str(x1)+r" and x="+str(x2)+r":"
        solution= round(major-minor,4)
        alternatives = coursesFunctionsBll.multipleOptions([solution],5)
        tempAlternatives =[]
        for y1 in range(5):
            tempAlternatives.append(str(alternatives[y1][0]))
        options =json.loads(json.dumps({'a':tempAlternatives[0], 
                                        'b':tempAlternatives[1], 
                                        'c': tempAlternatives[2], 
                                        'd': tempAlternatives[3], 
                                        'e': tempAlternatives[4]}))
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return jsonResponse
    except Exception as er:
        return er

def centroidProblem():
    try:
        a = random.randint(0,1)
        b = random.randint(2,10)
        x1 = random.randint(1,5)
        x2 = random.randint(6,10)
        x0=0
        y0=0
        question=""
        if a==0: #b^x
            major= (b**(x2))/math.log(b)
            minor= (b**(x1))/math.log(b)
            area = major-minor
            xmajor=(b**x2)*(x2*math.log(b)-1)/(math.log(b)**2)
            xminor=(b**x1)*(x1*math.log(b)-1)/(math.log(b)**2)
            x0=round((1/area)*(xmajor-xminor),4)
            ymajor=(b**(2*x2))/(2*math.log(b))
            yminor=(b**(2*x1))/(2*math.log(b))
            y0=round((1/(2*area))*(ymajor-yminor),4)
            question=r"Find the centroid for the function {"+str(b)+r"}^{x} between x="+str(x1)+r" and x="+str(x2)+r":"
        if a==1: #ln_b(x)
            major= (x2*math.log(x2)-x2)/math.log(b)
            minor= (x1*math.log(x1)-x1)/math.log(b)
            area = major-minor
            xmajor=((x2**2)*(2*math.log(x2)-1))/(4*math.log(b))
            xminor=((x1**2)*(2*math.log(x1)-1))/(4*math.log(b))
            x0=round((1/area)*(xmajor-xminor),4)
            ymajor=(x2)*((math.log(x2)**2)-(2*math.log(x2))+2)/(math.log(b)**2)
            yminor=(x1)*((math.log(x1)**2)-(2*math.log(x1))+2)/(math.log(b)**2)
            y0=round((1/(2*area))*(ymajor-yminor),4)
            question=r"Find the centroid for the function \log _{"+str(b)+r"}(x) between x="+str(x1)+r" and x="+str(x2)+r":"
        solution= r"x="+str(x0)+r", y="+str(y0)
        alternatives = coursesFunctionsBll.centroidOptions([x0, y0],5,x1,x2)
        tempAlternatives =[]
        for y1 in range(5):
            tempAlternatives.append(r"x="+str(alternatives[y1][0])+r", y="+str(alternatives[y1][1]))
        options =json.loads(json.dumps({'a':tempAlternatives[0], 
                                        'b':tempAlternatives[1], 
                                        'c': tempAlternatives[2], 
                                        'd': tempAlternatives[3], 
                                        'e': tempAlternatives[4]}))
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return jsonResponse
    except Exception as er:
        return er

def definiteIntegralProblem():
    try:
        c = random.randint(0,2)
        x1 = random.randint(1,5)
        x2 = random.randint(6,10)
        d= random.randint(100,1000)
        solution=0
        question=""
        if c==0: #1/(b-ax^2)^(3/2)
            a = random.randint(2,5)
            b = random.randint(501,1000)
            major= x2/(b*math.sqrt(b-(a*(x2**2))))
            minor= x1/(b*math.sqrt(b-(a*(x1**2))))
            solution=round((major-minor)*d,4)
            question=r"\int_{"+str(x1)+r"}^{"+str(x2)+r"} \frac{"+str(d)+r"}{("+str(b)+r"-"+str(a)+r"x^2)^{3/2}}"
        if c==1: #1/(b+ax^2)^(3/2)
            a = random.randint(2,50)
            b = random.randint(2,50)
            major= x2/(b*math.sqrt(b+(a*(x2**2))))
            minor= x1/(b*math.sqrt(b+(a*(x1**2))))
            solution=round((major-minor)*d,4)
            question=r"\int_{"+str(x1)+r"}^{"+str(x2)+r"} \frac{"+str(d)+r"}{("+str(b)+r"+"+str(a)+r"x^2)^{3/2}}"
        if c==2: #1/(ax^2-b)^(3/2)
            a = random.randint(11,20)
            b = random.randint(2,10)
            major= (-x2)/(b*math.sqrt((a*(x2**2))-b))
            minor= (-x1)/(b*math.sqrt((a*(x1**2))-b))
            solution=round((major-minor)*d,4)
            question=r"\int_{"+str(x1)+r"}^{"+str(x2)+r"} \frac{"+str(d)+r"}{("+str(a)+r"x^2-"+str(b)+r")^{3/2}}"
        alternatives = coursesFunctionsBll.multipleOptions([solution],5)
        tempAlternatives =[]
        for y1 in range(5):
            tempAlternatives.append(str(alternatives[y1][0]))
        options =json.loads(json.dumps({'a':tempAlternatives[0], 
                                        'b':tempAlternatives[1], 
                                        'c': tempAlternatives[2], 
                                        'd': tempAlternatives[3], 
                                        'e': tempAlternatives[4]}))
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return jsonResponse
    except Exception as er:
        return er

#besides being extremly difficult to solve, this exercise have some fails, so beware before trying to add to the project
def definiteIntegralProblem2():
    try:
        a = random.randint(0,2)
        b = random.randint(2,10)
        x1 = random.randint(1,5)
        x2 = random.randint(6,10)
        solution=0
        question=""
        if a==0: #(x+1)^2-b
            major= (1/2)*(x2+1)*(math.sqrt(((x2+1)**2)-b))-(1/2)*(b*math.log(math.sqrt(((x2+1)**2)-b)+x2+1))
            minor= (1/2)*(x1+1)*(math.sqrt(((x1+1)**2)-b))-(1/2)*(b*math.log(math.sqrt(((x1+1)**2)-b)+x1+1))
            solution=round(major-minor,4)
            question=r"\int_{"+str(x1)+r"}^{"+str(x2)+r"} \sqrt{x^2+2x-"+str(b-1)+r"}"
        if a==1: #(x+1)^2+b
            major= (1/2)*(x2+1)*(math.sqrt(((x2+1)**2)+b))+(1/2)*(b*math.log(math.sqrt(((x2+1)**2)+b)+x2+1))
            minor= (1/2)*(x1+1)*(math.sqrt(((x1+1)**2)+b))+(1/2)*(b*math.log(math.sqrt(((x1+1)**2)+b)+x1+1))
            solution=round(major-minor,4)
            question=r"\int_{"+str(x1)+r"}^{"+str(x2)+r"} \sqrt{x^2+2x+"+str(b+1)+r"}"
        if a==2: #b-(x+1)^2
            major= (1/2)*(x2+1)*(b-math.sqrt(((x2+1)**2)))+(1/2)*(b*math.asin((x2+1)/(b**(1/2))))
            minor= (1/2)*(x1+1)*(b-math.sqrt(((x1+1)**2)))+(1/2)*(b*math.asin((x1+1)/(b**(1/2))))
            solution=round(major-minor,4)
            question=r"\int_{"+str(x1)+r"}^{"+str(x2)+r"} \sqrt{-x^2-2x+"+str(b-1)+r"}"
        alternatives = coursesFunctionsBll.multipleOptions([solution],5)
        tempAlternatives =[]
        for y1 in range(5):
            tempAlternatives.append(str(alternatives[y1][0]))
        options =json.loads(json.dumps({'a':tempAlternatives[0], 
                                        'b':tempAlternatives[1], 
                                        'c': tempAlternatives[2], 
                                        'd': tempAlternatives[3], 
                                        'e': tempAlternatives[4]}))
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return jsonResponse
    except Exception as er:
        return er

exam1 = [basicProblem, sustitutionProblem, symmetryProblem, partsProblem, trigonometryProblem, trigonometrySubstitutionProblem, fractionProblem, substitutionRootProblem, partsPowerProblem, quotientProblem]
exam2 = [areaBetweenProblem, volumeProblem, cylinderVolumeProblem, springProblem, averageProblem, lengthProblem, yAreaProblem, xAreaProblem, centroidProblem, definiteIntegralProblem]
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