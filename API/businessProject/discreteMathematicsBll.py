
import random
import math
import json
import coursesFunctionsBll



def truthTableProblem():
    try:
        truthOptions=[["F","F","F","F",r"F"],
                      ["F","F","F","T",r"NOR"],
                      ["F","F","T","F",r"nonimplication"],
                      ["F","F","T","T",r"\neg p"],
                      ["F","T","F","F",r"abjunction"],
                      ["F","T","F","T",r"\neg q"],
                      ["F","T","T","F",r"XOR"],
                      ["F","T","T","T",r"NAND"],
                      ["T","F","F","F",r"AND"],
                      ["T","F","F","T",r"XNOR"],
                      ["T","F","T","F",r"q"],
                      ["T","F","T","T",r"conditional"],
                      ["T","T","F","F",r"p"],
                      ["T","T","F","T",r"implication"],
                      ["T","T","T","F",r"OR"],
                      ["T","T","T","T",r"T"]]
        optValues=[]
        for x in range(5):
            i= random.randint(0,len(truthOptions)-1)
            optValues.append(truthOptions[i])
            del truthOptions[i]
        solOpt= random.randint(0,4)
        trueTable=[["p","q","?"],["T","T",optValues[solOpt][0]],["T","F",optValues[solOpt][1]],["F","T",optValues[solOpt][2]],["F","F",optValues[solOpt][3]]]
        solution= r""+optValues[solOpt][4]
        matrix_ = coursesFunctionsBll.tableString(trueTable)
        question=r'find the correct logic relation for the next truth table: \\ '+str(matrix_)+r''
        options =json.loads(json.dumps({'a':r""+optValues[0][4],
                                        'b':r""+optValues[1][4], 
                                        'c':r""+optValues[2][4], 
                                        'd':r""+optValues[3][4], 
                                        'e':r""+optValues[4][4]}))
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return [jsonResponse]
    except Exception as er:
        return er

exam1 = [truthTableProblem]
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
