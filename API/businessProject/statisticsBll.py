#IDEAS FOR QUESTIONS
#population, sample, parameter concepts
#categorcal, continuos, qunatitative variables
#types of sampling methods
#expect money on average
#mode, median, mean
#histogram
#standard deviation
#probability random choose of a group different to a, between a,b or c
#lower quartile
#range of data
#mean intensity number
#empirical rule to derivate the interval
#percentile
#correlation
#predicted number of typos
#
import random
import math
import json
import coursesFunctionsBll

#for two variables
def uniformDistributionProblem():
    try:
        t = random.randint(0,30)
        w = random.randint(15,45)
        square = w**2
        h0 = (2*(w**2))**(1/2)
        h = (2*(((60+t)-w)**2))**(1/2)
        rectangle = h0*h
        sol=round((square+rectangle)*100/((60+t)**2),4)
        solution=r""+str(sol)+r"\%"
        question=r"Carl and Neil decide to meet between 1:00 pm and 2:"+(str(t) if t>9 else "0"+str(t))+r" pm. They agree the one who arrive first will wait "+str(w)+" minutes for the other one.\\ If the probability to arrive in any moment, in the according range of time, is equal, which is the probability they meet?: "
        alternatives = coursesFunctionsBll.multiplePercentageOptions([sol],5)
        tempAlternatives =[]
        for ta in range(5):
            tempAlternatives.append(r""+str(alternatives[ta][0])+r"\%")
        options =json.loads(json.dumps({'a':tempAlternatives[0],
                                        'b':tempAlternatives[1], 
                                        'c': tempAlternatives[2], 
                                        'd': tempAlternatives[3], 
                                        'e': tempAlternatives[4]}))
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return jsonResponse
    except Exception as er:
        return er

def continuousVarianceProblem():
    try:
        problem = random.randint(1,3)
        sol1=0
        sol2=0
        sol3=0
        if problem==1:
            choose = random.randint(0,5)
            ran = (2**(choose))/8
            product = 128/(4**(choose))
            sol1= round(product*(ran**3)/3,4)
            sol2 = round((product*(ran**4)/4)-(2*product*sol1*(ran**3)/3)+(product*(sol1**2)*(ran**2)/2),4)
        elif problem==2:
            choose = random.randint(0,4)
            ran = (2**(choose))/8
            product = 1536/(8**(choose))
            sol1= round(product*(ran**4)/4,4)
            sol2 = round((product*(ran**5)/5)-(2*product*sol1*(ran**4)/4)+(product*(sol1**2)*(ran**3)/3),4)
        elif problem==3:
            choose = random.randint(0,3)
            ran = (2**(choose))/4
            product = 1024/(16**(choose))
            sol1= round(product*(ran**5)/5,4)
            sol2 = round((product*(ran**6)/6)-(2*product*sol1*(ran**5)/5)+(product*(sol1**2)*(ran**4)/4),4)
        sol3 = round(sol2**(1/2),4)
        solution=r"Expected value="+str(sol1)+r", variance="+str(sol2)+r", standard deviation="+str(sol3)+r""
        question=r"For the function f(x)="+str(product)+r"x"+(r"" if problem==1 else r"^{"+str(problem)+r"}")+" between 0<x<"+str(ran)+", find the expected value, variation and standard deviation: "
        alternatives = coursesFunctionsBll.multipleOptions([sol1, sol2, sol3],5)
        tempAlternatives =[]
        for ta in range(5):
            tempAlternatives.append(r"Expected value="+str(alternatives[ta][0])+r", variance="+str(alternatives[ta][1])+r", standard deviation="+str(alternatives[ta][2])+r"")
        options =json.loads(json.dumps({'a':tempAlternatives[0],
                                        'b':tempAlternatives[1], 
                                        'c': tempAlternatives[2], 
                                        'd': tempAlternatives[3], 
                                        'e': tempAlternatives[4]}))
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return jsonResponse
    except Exception as er:
        return er

def uniformVarianceProblem():
    try:
        a = random.randint(5,10)
        b = random.randint(20,40)
        sol1 = (a+b)/2
        sol2 = round((((b-a+1)**2)-1)/12,4)
        sol3 = round(sol2**(1/2),4)
        
        solution=r"Expected value="+str(sol1)+r", variance="+str(sol2)+r", standard deviation="+str(sol3)+r""
        question=r"Random variable x have a discrete uniform distribution between integers "+str(a)+r"$\leq$x$\leq$"+str(b)+r". Find a) \mu b) \sigma^{2} c) \sigma: "
        alternatives = coursesFunctionsBll.multipleOptions([sol1, sol2, sol3],5)
        tempAlternatives =[]
        for ta in range(5):
            tempAlternatives.append(r"Expected value="+str(alternatives[ta][0])+r", variance="+str(alternatives[ta][1])+r", standard deviation="+str(alternatives[ta][2])+r"")
        options =json.loads(json.dumps({'a':tempAlternatives[0],
                                        'b':tempAlternatives[1], 
                                        'c': tempAlternatives[2], 
                                        'd': tempAlternatives[3], 
                                        'e': tempAlternatives[4]}))
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return jsonResponse
    except Exception as er:
        return er

def categoricalQuantitativeProblem():
    try:
        opts = ["discrete quantitative","continuous quantitative","ordinal categorical","nominal categorial"]
        biOpts = []
        for i in range(4):
            for j in range(4):
                biOpts.append(r"a) "+str(opts[i])+r", b) "+str(opts[j]))
        quest = [
            ["coin flips", 0],
            ["temperature",1],
            ["scholar grade",2],
            ["colors",3],
            ["goals scored", 0],
            ["speed",1],
            ["race position",2],
            ["gender",3]
            ]
        
        a0=random.randint(0,7)
        a = quest[a0]
        del quest[a0]
        b0=random.randint(0,6)
        b = quest[b0]
        solution = biOpts[(4*a[1])+b[1]]
        tempAlternatives =[biOpts[(4*a[1])+b[1]]]
        del biOpts[(4*a[1])+b[1]]
        for x in range(4):
            r1=random.randint(0,len(biOpts)-1)
            tempAlternatives.append(biOpts[r1])
            del biOpts[r1]
        random.shuffle(tempAlternatives)
        question=r"define the type for the next variables a)"+str(a[0])+r" b)"+str(b[0])+r": "
        options =json.loads(json.dumps({'a':tempAlternatives[0],
                                        'b':tempAlternatives[1], 
                                        'c': tempAlternatives[2], 
                                        'd': tempAlternatives[3], 
                                        'e': tempAlternatives[4]}))
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return jsonResponse
    except Exception as er:
        return er

exam1 = [uniformDistributionProblem, continuousVarianceProblem, uniformVarianceProblem, categoricalQuantitativeProblem]
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