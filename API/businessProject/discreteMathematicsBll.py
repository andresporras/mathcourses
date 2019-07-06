
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
#http://sites.millersville.edu/bikenaga/math-proof/truth-tables/truth-tables.html tautologies
def tautologiesProblem():
    try:
        truthOptions=[[r"P \lor \neg P",r"P \lor P"],
                      [r"\neg(P \land \neg P)",r"P \land \neg P"],
                      [r"[(P \Rightarrow Q) \land \neg Q]  \Rightarrow \neg P",r"[(P \Rightarrow Q) \land \neg Q]  \Rightarrow P"],
                      [r"\neg \neg P \iff P",r"\neg \neg P \iff \neg P"],
                      [r"[(P \Rightarrow Q) \land (Q \Rightarrow R)] \Rightarrow (P \Rightarrow R)",r"[(P \Rightarrow Q) \land (Q \Rightarrow R)] \Rightarrow (R \Rightarrow P)"],
                      [r"(P \land Q) \Rightarrow P",r"(P \land Q) \Rightarrow \neg P"],
                      [r"(P \land Q) \Rightarrow Q",r"(P \land Q) \Rightarrow \neg Q"],
                      [r"P \rightarrow (P \lor Q)",r"\neg P \rightarrow (P \lor Q)"],
                      [r"Q \rightarrow (P \lor Q)",r"\neg Q \rightarrow (P \lor Q)"],
                      [r"(P \iff Q) \iff [(P \Rightarrow Q) \land (P \Rightarrow Q)]",r"\neg (P \iff Q) \iff [(P \Rightarrow Q) \land (P \Rightarrow Q)]"],
                      [r"(P \land Q) \iff (Q \land P)",r"\neg (P \land Q) \iff (Q \land P)"],
                      [r"(P \lor Q) \iff (Q \lor P)",r"(P \lor Q) \iff \neg (Q \lor P)"],
                      [r"[(P \land Q) \land R] \iff [P \land (Q \land R)]",r"[(P \land Q) \land R] \iff \neg [P \land (Q \land R)]"],
                      [r"[(P \lor Q) \lor R] \iff [P \lor (Q \lor R)]",r"[(P \lor Q) \lor R] \iff [\neg P \lor (Q \lor R)]"],
                      [r"\neg (P \lor Q) \iff (\neg P \land \neg Q)",r"(P \lor Q) \iff (\neg P \land \neg Q)"],
                      [r"\neg (P \land Q) \iff (\neg P \lor \neg Q)",r"(P \land Q) \iff (\neg P \lor \neg Q)"],
                      [r"[P \land (Q \lor R)] \iff [(P \land Q) \lor (P \land R)]",r"[P \land (Q \lor R)] \iff [(P \lor Q) \land (P \lor R)]"],
                      [r"[P \lor (Q \land R)] \iff [(P \lor Q) \land (P \lor R)]",r"[P \lor (Q \land R)] \iff [(P \land Q) \lor (P \land R)]"],
                      [r"(P \Rightarrow Q) \iff (\neg Q \Rightarrow \neg P)",r"\neg (P \Rightarrow Q) \iff (\neg Q \Rightarrow \neg P)"],
                      [r"(P \Rightarrow Q) \iff (\neg P \lor Q)",r"(P \Rightarrow Q) \iff (\neg P \land Q)"],
                      [r"[(P \lor Q) \land \neg P] \Rightarrow Q",r"[(P \lor Q) \land \neg P] \iff Q"],
                      [r"(P \lor P) \iff P",r"(\neg P \lor P) \iff P"],
                      [r"(P \land P) \iff P",r"(\neg P \land P) \iff P"]]
        i1=random.randint(0,len(truthOptions)-1)
        j1=random.randint(0,1)
        sol1 = truthOptions[i1][j1]
        del truthOptions[i1]
        i2=random.randint(0,len(truthOptions)-1)
        j2=random.randint(0,1)
        sol2 = truthOptions[i2][j2]
        del truthOptions[i2]
        solution = r"a) "+("Yes" if j1==0 else "No")+r", b) "+("Yes" if j2==0 else "No")+r""
        question=r'which of the next propositions are tautologies: a) '+sol1+r',b) '+sol2+r''
        options =json.loads(json.dumps({'a':r"a) Yes, b) Yes",
                                        'b':r"a) Yes, b) No", 
                                        'c':r"a) No, b) Yes", 
                                        'd':r"a) No, b) No"}))
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return [jsonResponse]
    except Exception as er:
        return er
#http://sites.millersville.edu/bikenaga/math-proof/truth-tables/truth-tables.html tautologies
def tautologyNameProblem():
    try:
        truthOptions=[[r"P \lor \neg P",r"law of the excluded middle"],
                      [r"\neg(P \land \neg P)",r"contradiction"],
                      [r"[(P \Rightarrow Q) \land \neg Q]  \Rightarrow \neg P",r"modus tollens"],
                      [r"\neg \neg P \iff P",r"double negation"],
                      [r"[(P \Rightarrow Q) \land (Q \Rightarrow R)] \Rightarrow (P \Rightarrow R)",r"law of syllogism"],
                      [r"(P \land Q) \Rightarrow P",r"decomposing a conjunction"],
                      [r"(P \land Q) \Rightarrow Q",r"decomposing a conjunction"],
                      [r"P \rightarrow (P \lor Q)",r"constructing a disjunction"],
                      [r"Q \rightarrow (P \lor Q)",r"constructing a disjunction"],
                      [r"(P \iff Q) \iff [(P \Rightarrow Q) \land (P \Rightarrow Q)]",r"definition of the biconditional"],
                      [r"(P \land Q) \iff (Q \land P)",r"commutative law for \land"],
                      [r"(P \lor Q) \iff (Q \lor P)",r"commutative law for \lor"],
                      [r"[(P \land Q) \land R] \iff [P \land (Q \land R)]",r"associative law for \land"],
                      [r"[(P \lor Q) \lor R] \iff [P \lor (Q \lor R)]",r"associative law for \lor"],
                      [r"\neg (P \lor Q) \iff (\neg P \land \neg Q)",r"de morgan's law"],
                      [r"\neg (P \land Q) \iff (\neg P \lor \neg Q)",r"de morgan's law"],
                      [r"[P \land (Q \lor R)] \iff [(P \land Q) \lor (P \land R)]",r"distributivity"],
                      [r"[P \lor (Q \land R)] \iff [(P \lor Q) \land (P \lor R)]",r"distributivity"],
                      [r"(P \Rightarrow Q) \iff (\neg Q \Rightarrow \neg P)",r"contrapositive"],
                      [r"(P \Rightarrow Q) \iff (\neg P \lor Q)",r"conditional disjunction"],
                      [r"[(P \lor Q) \land \neg P] \Rightarrow Q",r"disjunctive sillogism"],
                      [r"(P \lor P) \iff P",r"simplification"],
                      [r"(P \land P) \iff P",r"simplification"]]
        opt = random.randint(0,len(truthOptions)-1)
        sol=truthOptions[opt]
        totalOpts=list(x[1] for x in truthOptions if x!=sol[1])
        uTotalOpts = list(set(totalOpts))[:4]
        uTotalOpts.append(sol[1])
        uTotalOpts.sort()
        solution = sol[1]
        question=r'select is the name of the next tautology: '+sol[0]+r''
        options =json.loads(json.dumps({'a':uTotalOpts[0],
                                        'b':uTotalOpts[1], 
                                        'c':uTotalOpts[2], 
                                        'd':uTotalOpts[3], 
                                        'e':uTotalOpts[4]}))
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return [jsonResponse]
    except Exception as er:
        return er

exam1 = [truthTableProblem, tautologiesProblem, tautologyNameProblem]
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

#http://sites.millersville.edu/bikenaga/math-proof/truth-tables/truth-tables.html two exercises
#https://www.geeksforgeeks.org/mathematical-logic-propositional-equivalences/ two exercises