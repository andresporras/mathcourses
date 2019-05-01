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
        question=r"State the type for the next variables a)"+str(a[0])+r" b)"+str(b[0])+r": "
        options =json.loads(json.dumps({'a':tempAlternatives[0],
                                        'b':tempAlternatives[1], 
                                        'c': tempAlternatives[2], 
                                        'd': tempAlternatives[3], 
                                        'e': tempAlternatives[4]}))
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return jsonResponse
    except Exception as er:
        return er

def samplingProblem():
    try:
        opts = ["simple random","convenience","systematic","cluster", "stratified"]
        biOpts = []
        for i in range(5):
            for j in range(5):
                biOpts.append(r"a) "+str(opts[i])+r", b) "+str(opts[j]))
        quest = [
            ["Teacher randomly choose three papers from a bag. The bag contains 30 sheets, each one with a different student name.", 0],
            ["The company assign sequential numbers for each employee(1,2,3...n), then use a software to generate random numbers and choose a sample of 10 employees",0],
            ["A student task is to make a poll to 10 random people about political view. He make the poll to the closest students he find in the classroom.",1],
            ["A college research wants to make a poll about local citizens preferences to traveling. They use students volunteers as sample",1],
            ["A teacher wants to choose a sample of 5 students from 30 students class. He use an alphabetical sorted list and choose 1th student in the list, then 7th student, 13th...", 2],
            ["In the chopping center entrance each 20th person to enter is chosen to make a poll about customer satisfaction.",2],
            ["A research about spain hobbies randomly choose a city to make the polls",3],
            ["A college wants to research citizens perception about local traffic. They randomly choose one of city local neighbors as sample the make the research.",3],
            ["An statistic company wants to make a presidential popularity survey. They randomly choose 1000 adults americans from every state to make a total of 50000 surveys.",4],
            ["To make a poll in a college to research group randomly choose 5 students from each college program",4]
            ]
        
        a0=random.randint(0,9)
        a = quest[a0]
        del quest[a0]
        b0=random.randint(0,8)
        b = quest[b0]
        solution = biOpts[(5*a[1])+b[1]]
        tempAlternatives =[biOpts[(5*a[1])+b[1]]]
        del biOpts[(5*a[1])+b[1]]
        for x in range(4):
            r1=random.randint(0,len(biOpts)-1)
            tempAlternatives.append(biOpts[r1])
            del biOpts[r1]
        random.shuffle(tempAlternatives)
        question=r"State the type of sampling method \\ a)"+str(a[0])+r" \\ b)"+str(b[0])+r": "
        options =json.loads(json.dumps({'a':tempAlternatives[0],
                                        'b':tempAlternatives[1], 
                                        'c': tempAlternatives[2], 
                                        'd': tempAlternatives[3], 
                                        'e': tempAlternatives[4]}))
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return jsonResponse
    except Exception as er:
        return er

# simple random: each object is equally likely to be selected.
# convenience: you make it easy, the easiest sample you can get.
# systematic: selection of every k object for your sample, where k=m/n, where m is population and n is sample size.
# cluster: population is divide in clusters and one of the clusters, randomly selected, is chosen as the sample.
# stratified: the sample is formed by choosing objects from different stratified clusters.
#https://www.whatissixsigma.net/box-plot-diagram-to-identify-outliers/
def plotBoxOutlierProblem():
    try:
        n = random.randint(11,16)
        listValues=[]
        for i in range(n):
            m = random.randint(0,4)
            listValues.append(random.randint(1,100) if m==0 else random.randint(55,65))
        listValues.sort()
        q1 = (listValues[math.floor((1/4)*(n+1))-1]+listValues[math.ceil((1/4)*(n+1))-1])/2 
        q3 = (listValues[math.floor((3/4)*(n+1))-1]+listValues[math.ceil((3/4)*(n+1))-1])/2
        iqr=q3-q1
        ll = q1-(1.5*iqr)
        ul = q3+(1.5*iqr)
        sol=0
        sol+= sum((1 if s>ul or s<ll else 0) for s in listValues)
        solution=r""+str(sol)
        question=r"Use the plot box outlier test to find how many potencial outliers are in "+", ".join(str(x) for x in listValues)+r":"
        alternatives = coursesFunctionsBll.arithmeticPercentageOptions([sol],5)
        tempAlternatives =[]
        for ta in range(5):
            tempAlternatives.append(r""+str(alternatives[ta][0]))
        options =json.loads(json.dumps({'a':tempAlternatives[0],
                                        'b':tempAlternatives[1], 
                                        'c': tempAlternatives[2], 
                                        'd': tempAlternatives[3], 
                                        'e': tempAlternatives[4]}))
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return jsonResponse
    except Exception as er:
        return er

#use chevishev theorem
#sigma is standard deviation, mu is average value
def chebyshevProblem():
    try:
        av = random.randint(41,80)
        sd = random.randint(10,20)
        ran = random.randint(21,40)
        k = ran/sd
        prob = 1-(1/(k**2))
        sol = round(prob*100,4)
        solution=r""+str(sol)+r"\%"
        question=r"About the daily driver licenses issued in a city we have the next information, \mu="+str(av)+" and \sigma="+str(sd)+". Having no more information, which is the minimal probability that any day the number of driver licences issued is between "+str(av-ran)+r" and "+str(av+ran)+r": "
        alternatives = coursesFunctionsBll.arithmeticPercentageOptions([sol],5)
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

def linearRegressionProblem():
    try:
        rows = random.randint(4,8)
        matrix = coursesFunctionsBll.tableGenerator1(rows)
        completeMatrix = coursesFunctionsBll.completeTableGenerator1(matrix)
        b = ((len(completeMatrix)*sum(c[2] for c in completeMatrix))-(sum(c[0] for c in completeMatrix)*sum(c[1] for c in completeMatrix)))/((len(completeMatrix)*sum(c[3] for c in completeMatrix))-(sum(c[0] for c in completeMatrix)**2))
        a = (sum(c[1] for c in completeMatrix)-(b*sum(c[0] for c in completeMatrix)))/len(completeMatrix)
        b = round(b,4)
        a = round(a,4)
        solution=r"y="+str(b)+r"x+"+str(a)
        matrix_ = coursesFunctionsBll.tableString(matrix)
        question=r'A marketing department wants to understand the success of a tv daily broadcast commercial to increase sells. The collect the next data\\ '+str(matrix_)+r' \\ Find the simple lienar regression to express the relationship between number os commercials (independent variable) and millions of sells (dependent variable): '
        alternatives = coursesFunctionsBll.multipleOptions([b, a],5)
        tempAlternatives =[]
        for ta in range(5):
            tempAlternatives.append(r"y="+str(alternatives[ta][0])+r"x+"+str(alternatives[ta][1]))
        options =json.loads(json.dumps({'a':tempAlternatives[0],
                                        'b':tempAlternatives[1], 
                                        'c': tempAlternatives[2], 
                                        'd': tempAlternatives[3], 
                                        'e': tempAlternatives[4]}))
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return jsonResponse
    except Exception as er:
        return er

exam1 = [uniformDistributionProblem, continuousVarianceProblem, uniformVarianceProblem, categoricalQuantitativeProblem, samplingProblem, plotBoxOutlierProblem, chebyshevProblem, linearRegressionProblem]
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