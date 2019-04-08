import random
import math
import json
import coursesFunctionsBll

def multiplicationCombinationProblem():
    try:
        b = random.randint(6,10)
        g = random.randint(6,10)
        s = random.randint(2,10)
        m = b*g
        p = (math.factorial(b+g))/(math.factorial(s)*math.factorial((b+g)-s))
        
        solution=r"a) "+str(m)+r", b) "+str(p)
        question=r"For a class with "+str(b)+r" boys and "+str(g)+r" girls, a) if the teacher has to choose one boy and one girl, how many possible outcomes can be? b) from the whole class the teacher must select "+str(s)+r" students, how many different group of students can appear?"
        alternatives = coursesFunctionsBll.multiAritmeticOptions([m, p],5)
        tempAlternatives =[]
        for ta in range(5):
            tempAlternatives.append(r"a) "+str(alternatives[ta][0])+r", b) "+str(alternatives[ta][1])) 
        options =json.loads(json.dumps({'a':tempAlternatives[0],
                                        'b':tempAlternatives[1], 
                                        'c': tempAlternatives[2], 
                                        'd': tempAlternatives[3], 
                                        'e': tempAlternatives[4]}))
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return jsonResponse
    except Exception as er:
        return er

def permutationsProblem():
    try:
        names=["oscar","andres","juan","felipe","carlos","alberto","juan","pablo","jose","luis","sergio","camilo","leonardo","ramiro","fran","fernando","gerardo","patricio","paolo","waldo","wilmer", "nicolas"]
        randomName = names[random.randint(0,21)]+" "+names[random.randint(0,21)]
        listName = list(randomName)
        sol1 = math.factorial(len(listName))
        groups = coursesFunctionsBll.countBy(listName)
        for i in range(len(groups)):
            sol1 = sol1/math.factorial(groups[i][1])
        setName = set(listName)
        sol2 = math.factorial(len(setName))
        solution=r"a) "+str(sol1)+r", b) "+str(sol2)
        question=r"A math student whose name is "+str(randomName)+r" would like to know a) how many different rearrangements can be done with his name, b) taking just one time each different character in his name, how many different rearragements can be? PS: consider white space as another character."
        alternatives = coursesFunctionsBll.multiAritmeticOptions([sol1, sol2],5)
        tempAlternatives =[]
        for ta in range(5):
            tempAlternatives.append(r"a) "+str(alternatives[ta][0])+r", b) "+str(alternatives[ta][1])) 
        options =json.loads(json.dumps({'a':tempAlternatives[0],
                                        'b':tempAlternatives[1], 
                                        'c': tempAlternatives[2], 
                                        'd': tempAlternatives[3], 
                                        'e': tempAlternatives[4]}))
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return jsonResponse
    except Exception as er:
        return er


def combinationPermutationProblem():
    try:
        f=  random.randint(11,14)
        c=  random.randint(2,9)
        p=  random.randint(2,9)
        combi = math.factorial(f)/(math.factorial(f-c)*math.factorial(c))
        permu = math.factorial(f)/math.factorial(f-p)
        solution=r"a) "+str(combi)+r" b)"+str(permu)
        question=r"In a family there are "+str(f)+r" siblings, a) how many groups of "+str(c)+r" siblings can be formed b) how many groups of "+str(p)+r" if order is important: "
        alternatives = coursesFunctionsBll.multiAritmeticOptions([combi, permu],5)
        tempAlternatives =[]
        for ta in range(5):
            tempAlternatives.append(r"a) "+str(alternatives[ta][0])+r" b)"+str(alternatives[ta][1])) 
        options =json.loads(json.dumps({'a':tempAlternatives[0],
                                        'b':tempAlternatives[1], 
                                        'c': tempAlternatives[2], 
                                        'd': tempAlternatives[3], 
                                        'e': tempAlternatives[4]}))
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return jsonResponse
    except Exception as er:
        return er

def cpRepetitionProblem():
    try:
        f=  random.randint(7,11)
        c=  random.randint(2,6)
        p=  random.randint(2,6)
        combi = f**c
        permu = math.factorial(f+p-1)/(math.factorial(f-1)*math.factorial(p))
        solution=r"a) "+str(combi)+r" b)"+str(permu)
        question=r"from the first "+str(f)+r" characters of alphabet, a) how many ways of choose "+str(c)+r" characters can be done b) how many words of "+str(p)+r" characters can be done: "
        alternatives = coursesFunctionsBll.multiAritmeticOptions([combi, permu],5)
        tempAlternatives =[]
        for ta in range(5):
            tempAlternatives.append(r"a) "+str(alternatives[ta][0])+r" b)"+str(alternatives[ta][1])) 
        options =json.loads(json.dumps({'a':tempAlternatives[0],
                                        'b':tempAlternatives[1], 
                                        'c': tempAlternatives[2], 
                                        'd': tempAlternatives[3], 
                                        'e': tempAlternatives[4]}))
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return jsonResponse
    except Exception as er:
        return er

def coinProblem():
    try:
        f=  random.randint(6,9)
        e=  random.randint(2,5)
        ne=  random.randint(2,5)
        sol1 = round(math.factorial(f)/(math.factorial(e)*math.factorial(f-e)*(2**f)),4)
        sol2=0
        for i in range(ne):
            sol2+=math.factorial(f)/(math.factorial(i)*math.factorial(f-i)*(2**f))
        sol2 = round(sol2)
        solution=r"a) "+str(sol1)+r" b)"+str(sol2)
        question=r"from flipping a fair coin  "+str(f)+r" times, a) what is the probability of get exactly "+str(e)+r" heads b) less than "+str(ne)+r" heads: "
        alternatives = coursesFunctionsBll.multipleOptions([sol1, sol2],5)
        tempAlternatives =[]
        for ta in range(5):
            tempAlternatives.append(r"a) "+str(alternatives[ta][0])+r" b)"+str(alternatives[ta][1])) 
        options =json.loads(json.dumps({'a':tempAlternatives[0],
                                        'b':tempAlternatives[1], 
                                        'c': tempAlternatives[2], 
                                        'd': tempAlternatives[3], 
                                        'e': tempAlternatives[4]}))
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return jsonResponse
    except Exception as er:
        return er

def throwProblem():
    try:
        p = (random.randint(1,4)/10)+(random.randint(0,1)/2)
        f=  random.randint(5,8)
        e=  random.randint(1,4)
        ne=  random.randint(1,4)
        sol1 = round(math.factorial(f)*(p**e)*((1-p)**(f-e))*100/(math.factorial(e)*math.factorial(f-e)),4)
        sol2=0
        for i in range(ne):
            sol2+=math.factorial(f)*(p**i)*((1-p)**(f-i))*100/(math.factorial(i)*math.factorial(f-i))
        sol2 = round(100- sol2,4)
        solution=r"a) "+str(sol1)+r"\% b)"+str(sol2)+r"\%"
        question=r"For certain basketall player, the probability of throwing the ball to the basket and score is "+str(p*100)+"\%. For throwing "+str(f)+r" times, a) what is the probability of score exactly "+str(e)+r" times b) at least "+str(ne)+r" times: "
        alternatives = coursesFunctionsBll.multiplePercentageOptions([sol1, sol2],5)
        tempAlternatives =[]
        for ta in range(5):
            tempAlternatives.append(r"a) "+str(alternatives[ta][0])+r"\% b)"+str(alternatives[ta][1])+r"\%")
        options =json.loads(json.dumps({'a':tempAlternatives[0],
                                        'b':tempAlternatives[1], 
                                        'c': tempAlternatives[2], 
                                        'd': tempAlternatives[3], 
                                        'e': tempAlternatives[4]}))
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return jsonResponse
    except Exception as er:
        return er

#for b part use bayesian theorem
def coinUnfairProblem():
    try:
        up = (random.randint(3,4)/10)+(random.randint(0,1)*3/10)
        c=  random.randint(6,9)
        uc =  random.randint(2,5)
        e1=  random.randint(2,5)
        e2=  random.randint(2,5)
        sol1 = round((((uc/c)*(up**e1))+(((c-uc)/c)*(0.5**e1)))*100,4)
        sol2 = round(((uc/c)*(up**e2))*100/(((uc/c)*(up**e2))+(((c-uc)/c)*(0.5**e2))),4)

        solution=r"a) "+str(sol1)+r"\% b)"+str(sol2)+r"\%"
        question=r"having "+str(c)+r" coins in a bag, where "+str(uc)+r" are unfair coins with "+str(up*100)+r"\% chance of head.  If you randomly choose one coin from the bag, a) which is the probability of get  "+str(e1)+r" heads in same number of flips b)  probability of have the unfair coin if you get "+str(e2)+r" heads in same number of flips: "
        alternatives = coursesFunctionsBll.multiplePercentageOptions([sol1, sol2],5)
        tempAlternatives =[]
        for ta in range(5):
            tempAlternatives.append(r"a) "+str(alternatives[ta][0])+r"\% b)"+str(alternatives[ta][1])+r"\%")
        options =json.loads(json.dumps({'a':tempAlternatives[0],
                                        'b':tempAlternatives[1], 
                                        'c': tempAlternatives[2], 
                                        'd': tempAlternatives[3], 
                                        'e': tempAlternatives[4]}))
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return jsonResponse
    except Exception as er:
        return er

def binomialDistributionProblem():
    try:
        p = (random.randint(1,4)/10)+(random.randint(0,1)/2)
        n = random.randint(10,30)
        mean = round(n*p,4)
        mode = round(math.floor((n+1)*p),4)
        variance = round(n*p*(1-p),4)
        solution=r"mean: "+str(mean)+r", mode: "+str(mode)+r", variance: "+str(variance)
        question=r"a soccer player practice throw penaltis everyday. His percentage of scoring is "+str(p*100)+r"\%. If this soccer player throw "+str(n)+r" penaltis every day, find: mean, mode and variance: "
        alternatives = coursesFunctionsBll.multiplePercentageOptions([mean, mode, variance],5)
        tempAlternatives =[]
        for ta in range(5):
            tempAlternatives.append(r"mean: "+str(alternatives[ta][0])+r", mode: "+str(alternatives[ta][1])+r", variance: "+str(alternatives[ta][2]))
        options =json.loads(json.dumps({'a':tempAlternatives[0],
                                        'b':tempAlternatives[1], 
                                        'c': tempAlternatives[2], 
                                        'd': tempAlternatives[3], 
                                        'e': tempAlternatives[4]}))
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return jsonResponse
    except Exception as er:
        return er

def poissonDistributionProblem():
    try:
        n = random.randint(1,8)
        k1=n
        while k1==n:
            k1 = random.randint(0,7)
        k2 = random.randint(0,3)
        sol1 = round((math.e**(-n))*(n**k1)*100/math.factorial(k1),4)
        sol2 = 0
        for i in range(k2+1):
            sol2 = sol2 +(math.e**(-n))*(n**i)*100/math.factorial(i)
        sol2 = round(100-sol2,4)
        solution=r"a) "+str(sol1)+r"\%, b) "+str(sol2)+r"\%"
        question=r"A pharmacy receive around "+str(n)+r" customers per hour. a) which is the probability to receive "+str(k1)+r" customers in an hour b) receive more than "+str(k2)+r" customers: "
        alternatives = coursesFunctionsBll.multiplePercentageOptions([sol1, sol2],5)
        tempAlternatives =[]
        for ta in range(5):
            tempAlternatives.append(r"a) "+str(alternatives[ta][0])+r"\%, b) "+str(alternatives[ta][1])+r"\%")
        options =json.loads(json.dumps({'a':tempAlternatives[0],
                                        'b':tempAlternatives[1], 
                                        'c': tempAlternatives[2], 
                                        'd': tempAlternatives[3], 
                                        'e': tempAlternatives[4]}))
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return jsonResponse
    except Exception as er:
        return er

def vennDiagramProblem():
    try:
        p = random.randint(100,150)
        n1 = random.randint(25,50)
        n2 = random.randint(25,50)
        n3 = random.randint(25,50)
        n4 = random.randint(25,50)
        m1 = random.randint(10,20)
        m2 = random.randint(10,20)
        sol1 = n1+n2-m1
        sol2 = p - (n3+n4-m2)
        solution=r"a) "+str(sol1)+r", b) "+str(sol2)+r""
        question=r"A class have "+str(p)+r" students. After scholar year has finished the teacher provide the next report: "+str(n1)+r" students pass maths, "+str(n2)+r" students pass english, "+str(n3)+r" students pass science, "+str(n4)+r" students pass spanish,\\ "+str(m1)+r" students pass both math and english, "+str(m2)+r" students pass both science and spanish. \\a) how many students pass either math or english?, b) how many students fail both science and spanish?: "
        alternatives = coursesFunctionsBll.multiAritmeticOptions([sol1, sol2],5)
        tempAlternatives =[]
        for ta in range(5):
            tempAlternatives.append(r"a) "+str(alternatives[ta][0])+r", b) "+str(alternatives[ta][1])+r"")
        options =json.loads(json.dumps({'a':tempAlternatives[0],
                                        'b':tempAlternatives[1], 
                                        'c': tempAlternatives[2], 
                                        'd': tempAlternatives[3], 
                                        'e': tempAlternatives[4]}))
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return jsonResponse
    except Exception as er:
        return er

exam1 = [multiplicationCombinationProblem, permutationsProblem, combinationPermutationProblem, cpRepetitionProblem, coinProblem, throwProblem, coinUnfairProblem, binomialDistributionProblem, poissonDistributionProblem, vennDiagramProblem]
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
