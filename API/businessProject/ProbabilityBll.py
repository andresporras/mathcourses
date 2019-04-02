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

exam1 = [multiplicationCombinationProblem, permutationsProblem, combinationPermutationProblem, cpRepetitionProblem]
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
