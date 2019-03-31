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
        alternatives = coursesFunctionsBll.multipleOptions([m, p],5)
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

exam1 = [multiplicationCombinationProblem]
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
