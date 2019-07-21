
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
                      [r"P \Rightarrow (P \lor Q)",r"\neg P \Rightarrow (P \lor Q)"],
                      [r"Q \Rightarrow (P \lor Q)",r"\neg Q \Rightarrow (P \lor Q)"],
                      [r"(P \iff Q) \iff [(P \Rightarrow Q) \land (P \Rightarrow Q)]",r"\neg (P \iff Q) \iff [(P \Rightarrow Q) \land (P \Rightarrow Q)]"],
                      [r"(P \land Q) \iff (Q \land P)",r"\neg (P \land Q) \iff (Q \land P)"],
                      [r"(P \lor Q) \iff (Q \lor P)",r"(P \lor Q) \iff \neg (Q \lor P)"],
                      [r"[(P \land Q) \land R] \iff [P \land (Q \land R)]",r"[(P \land Q) \land R] \iff \neg [P \land (Q \land R)]"],
                      [r"[(P \lor Q) \lor R] \iff [P \lor (Q \lor R)]",r"[(P \lor Q) \lor R] \iff [\neg P \lor \neg (Q \lor R)]"],
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
        question=r'select the name of the next tautology: '+sol[0]+r'' 
        options =json.loads(json.dumps({'a':uTotalOpts[0],
                                        'b':uTotalOpts[1], 
                                        'c':uTotalOpts[2], 
                                        'd':uTotalOpts[3], 
                                        'e':uTotalOpts[4]}))
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return [jsonResponse]
    except Exception as er:
        return er

#https://www.geeksforgeeks.org/mathematical-logic-propositional-equivalences/ equivalences
def equivalencesProblem():
    try:
        truthOptions=[[r"P \land T \equiv P",r"P \land T \equiv \neg P \lor F"],
                      [r"P \lor F \equiv P",r"P \lor F \equiv \neg P \land T"],
                      [r"P \land F \equiv F",r"P \land F \equiv T"],
                      [r"P \lor T \equiv T",r"P \lor T \equiv F"],
                      [r"P \land P \equiv P",r"P \land P \equiv T"],
                      [r"P \lor T \equiv P",r"P \lor T \equiv T"],
                      [r"\neg \neg P \equiv P",r"\neg \neg P \equiv F"],
                      [r"P \land Q \equiv Q \land P",r"P \land Q \equiv \neg Q \land \neg P"],
                      [r"P \lor Q \equiv Q \lor P",r"P \lor Q \equiv \neg Q \lor \neg P"],
                      [r"(P \land Q) \land R \equiv P \land (Q \land R)",r"(P \land Q) land R \equiv \neg (P \land Q) \Rightarrow R "],
                      [r"(P \lor Q) \lor R \equiv P \lor (Q \lor R)",r"(P \lor Q) \lor R \equiv (P \lor Q) \Rightarrow \neg R"],
                      [r"P \land (Q \lor R) \equiv (P \land Q) \lor (P \land R)",r"P \land (Q \lor R) \equiv (P \lor Q) \land (P \lor R)"],
                      [r"P \lor (Q \land R) \equiv (P \lor Q) \land (P \lor R)",r"P \lor (Q \land R) \equiv (P \land Q) \lor (P \land R)"],
                      [r"\neg (P \land Q) \equiv \neg P \lor \neg Q",r"\neg (P \land Q) \equiv P \lor Q"],
                      [r"\neg (P \lor Q) \equiv \neg P \land \neg Q",r"\neg (P \lor Q) \equiv P \land Q"],
                      [r"P \land (P \lor Q) \equiv P",r"P \land (P \lor Q) \equiv P \land Q"],
                      [r"P \lor (P \land Q) \equiv P",r"P \lor (P \land Q) \equiv P \lor Q"],
                      [r"P \land \neg P \equiv F",r"P \land \neg P \equiv P"],
                      [r"P \lor \neg P \equiv T",r"P \lor \neg P \equiv P"],
                      [r"P \Rightarrow Q \equiv \neg P \lor Q",r"P \Rightarrow Q \equiv \neg Q \lor P"],
                      [r"P \Rightarrow Q \equiv \neg Q \Rightarrow \neg P",r"P \Rightarrow Q \equiv \neg P \Rightarrow \neg Q"],
                      [r"P \and Q \equiv \neg (Q \Rightarrow \neg P)",r"P \and Q \equiv Q \Rightarrow \neg P"],
                      [r"(P \Rightarrow Q) \land (P \Rightarrow R) \equiv P \Rightarrow (Q \land R)",r"(P \Rightarrow Q) \land (P \Rightarrow R) \equiv P \Rightarrow (Q \lor R)"],
                      [r"(P \Rightarrow R) \land (Q \Rightarrow R) \equiv (P \lor Q) \Rightarrow R",r"(P \Rightarrow R) \land (Q \Rightarrow R) \equiv (P \land Q) \Rightarrow R"],
                      [r"(P \Rightarrow Q) \lor (P \Rightarrow R) \equiv P \Rightarrow (Q \lor R)",r"(P \Rightarrow Q) \lor (P \Rightarrow R) \equiv P \Rightarrow (Q \land R)"],
                      [r"(P \Rightarrow R) \lor (Q \Rightarrow R) \equiv (P \land Q) \Rightarrow R",r"(P \Rightarrow R) \lor (Q \Rightarrow R) \equiv (P \lor Q) \Rightarrow R"],
                      [r"P \iff Q \equiv (P \Rightarrow Q) \land (Q \Rightarrow P)",r"P \iff Q \equiv (P \Rightarrow Q) \lor (Q \Rightarrow P)"],
                      [r"P \iff Q \equiv \neg P \iff \neg Q",r"P \iff Q \equiv \neg (\neg P \iff \neg Q)"],
                      [r"P \iff Q \equiv (P \land Q) \lor (\neg P \land \neg Q)",r"P \iff Q \equiv (P \lor Q) \land (\neg P \lor \neg Q)"],
                      [r"\neg (P \iff Q) \equiv P \iff \neg Q",r"\neg (P \iff Q) \equiv P \iff Q"],
                      [r"\neg (P \Rightarrow Q) \equiv P \land \neg Q",r"\neg (P \Rightarrow Q) \equiv \neg P \land Q"]]
        i1=random.randint(0,len(truthOptions)-1)
        j1=random.randint(0,1)
        sol1 = truthOptions[i1][j1]
        del truthOptions[i1]
        i2=random.randint(0,len(truthOptions)-1)
        j2=random.randint(0,1)
        sol2 = truthOptions[i2][j2] 
        del truthOptions[i2]
        solution = r"a) "+("Yes" if j1==0 else "No")+r", b) "+("Yes" if j2==0 else "No")+r"" 
        question=r'which of the next equivalences are correct: a) '+sol1+r',b) '+sol2+r''
        options =json.loads(json.dumps({'a':r"a) Yes, b) Yes",
                                        'b':r"a) Yes, b) No", 
                                        'c':r"a) No, b) Yes", 
                                        'd':r"a) No, b) No"}))
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return [jsonResponse]
    except Exception as er:
        return er

#https://www.geeksforgeeks.org/mathematical-logic-propositional-equivalences/ equivalences
def equivalenceNameProblem():
    try:
        truthOptions=[[r"P \land T \equiv P",r"Identity law"],
                      [r"P \lor F \equiv P",r"Identity law"],
                      [r"P \land F \equiv F",r"Domination law"],
                      [r"P \lor T \equiv T",r"Domination law"],
                      [r"P \land P \equiv P",r"Idempotent law"],
                      [r"P \lor T \equiv P",r"Idempotent law"],
                      [r"\neg \neg P \equiv P",r"double negation law"],
                      [r"P \land Q \equiv Q \land P",r"commutative law"],
                      [r"P \lor Q \equiv Q \lor P",r"commutative law"],
                      [r"(P \land Q) \land R \equiv P \land (Q \land R)",r"associative law"],
                      [r"(P \lor Q) \lor R \equiv P \lor (Q \lor R)",r"associative law"],
                      [r"P \land (Q \lor R) \equiv (P \land Q) \lor (P \land R)",r"distributive law"],
                      [r"P \lor (Q \land R) \equiv (P \lor Q) \land (P \lor R)",r"distributive law"],
                      [r"\neg (P \land Q) \equiv \neg P \lor \neg Q",r"De Morgan's law"],
                      [r"\neg (P \lor Q) \equiv \neg P \land \neg Q",r"De Morgan's law"],
                      [r"P \land (P \lor Q) \equiv P",r"absorption law"],
                      [r"P \lor (P \land Q) \equiv P",r"absorption law"],
                      [r"P \land \neg P \equiv F",r"negation law"],
                      [r"P \lor \neg P \equiv T",r"negation law"],
                      [r"P \Rightarrow Q \equiv \neg P \lor Q",r"conditional disjunction"],
                      [r"P \Rightarrow Q \equiv \neg Q \Rightarrow \neg P",r"contrapositive"]]
        opt = random.randint(0,len(truthOptions)-1)
        sol=truthOptions[opt]
        totalOpts=list(x[1] for x in truthOptions if x!=sol[1])
        uTotalOpts = list(set(totalOpts))[:4]
        uTotalOpts.append(sol[1])
        uTotalOpts.sort()
        solution = sol[1]
        question=r'select the name of the next equivalence: '+sol[0]+r'' 
        options =json.loads(json.dumps({'a':uTotalOpts[0],
                                        'b':uTotalOpts[1], 
                                        'c':uTotalOpts[2], 
                                        'd':uTotalOpts[3], 
                                        'e':uTotalOpts[4]}))
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return [jsonResponse]
    except Exception as er:
        return er


def setPropertiesProblem():
    try:
        truthOptions=[[r"If A and B have the same elements then they are the same set and A=B",r"Having the same elements doesnt mean that two sets are the same set"],
                      [r"If A is a set which elements are 3 and 5 then A=\{3 ,5\}. Use brackets",r"If A is a set which elements are 3 and 5 then A=(3,5). Use parentheses"],
                      [r"In a set the order of elements doesn't matter, therefore \{ 3,5\}=\{ 5,3\}",r"In a set the order of elements really matter, therefore \{ 3,5\} \ne \{ 5,3\}"],
                      [r"An element can appear only one time in a set, therefore \{ 3,6,6 \} = \{ 3,6 \} ",r"An element can appear many ties in a set, therefore \{ 3,6,6\} \ne \{ 3,6\}"],
                      [r"A set can be finite or infinite",r"A set must be finite, never infinite"],
                      [r"A set can have zero elements",r"A set can't have zero elements"],
                      [r"If A is the set of x elements with c property then A=\{ x:c(x) \} ",r"If A is the set of x elements with c property then A=(x:c \{ x \})"],
                      [r"\{ x,y \} doesn't mean the set have two elements, because it can be that x=y, in that case \{ x,y \}= \{ x \} = \{ y \} ",r" \{ x,y \} means the set have two different elements, therefore \{ x,y \} \ne \{ x \} \ne \{ y \}"],
                      [r"A=\{ x,y,z \}, if d= \{ x,y \} d \notin A",r"A= \{x,y,z \}, if d= \{ x,y \} then d \in A"],
                      [r"if A= \{ x,y,z \} then \{ A \} is a singleton",r"\{ \} is a singleton"],
                      [r" \mathbb{N} is the symbol for the set of natural numbers. this set has the next property: if n \in \mathbb{N} then n+1 \in \mathbb{N}",r" \mathbb{N} is the set of entire number between 1 and 10"],
                      [r"If A is the set of natural numbers between 4 and 900, this can be show as \{ x \in \mathbb{N} : 4 \leq x \leq 900 \}",r"If A is the set of natural numbers between 4 and 900, this can be show as \{ x : 4 \leq x \leq 900 \}"],
                      [r"A= \{ 3,8,13,18,23 \} therefore A= \{ 3+5j : j=0,1,2,3,4 \}",r"A= \{ 3,8,13,18,23 \} therefore A= \{ 3+5j : 0 \leq j \leq 4 \} "]]
        i1=random.randint(0,len(truthOptions)-1)
        j1=random.randint(0,1)
        sol1 = truthOptions[i1][j1]
        del truthOptions[i1]
        i2=random.randint(0,len(truthOptions)-1)
        j2=random.randint(0,1)
        sol2 = truthOptions[i2][j2] 
        del truthOptions[i2]
        solution = r"a) "+("correct" if j1==0 else "incorrect")+r", b) "+("correct" if j2==0 else "incorrect")+r"" 
        question=r'which of the next set properties/examples are correct: a) '+sol1+r',b) '+sol2+r''
        options =json.loads(json.dumps({'a':r"a) correct, b) correct",
                                        'b':r"a) correct, b) incorrect", 
                                        'c':r"a) incorrect, b) correct", 
                                        'd':r"a) incorrect, b) incorrect"}))
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return [jsonResponse]
    except Exception as er:
        return er

def subSetPropertiesProblem():
    try:
        truthOptions=[[r"(A \subseteq B) \iff [ \forall x : x \in A \rightarrow x \in B]",r"(A = B) \iff [ \forall x : x \in A \rightarrow x \in B]"],
                      [r"(A \supseteq B) \iff (B \subseteq A)",r"(A \supseteq B) \rightarrow (A \ne B)"],
                      [r"[(A \subseteq B) \land (x \notin B)] \rightarrow (x \notin A)",r"[(A \subseteq B) \land (x \notin A)] \rightarrow (x \notin B)"],
                      [r"(A = B) \iff [(A \subseteq B) \land (B \subseteq A)]",r"(A = B) \iff [(A \subset B) \land (B \subset A)]"],
                      [r"(A = B) \iff [ ( \forall x : x \in A \rightarrow x \in B) \land ( \forall x : x \in B \rightarrow x \in A)]",r"(A = B) \iff [ ( \forall x : x \in A \rightarrow x \in B) \lor ( \forall x : x \in B \rightarrow x \in A)]"],
                      [r"(A = B) \iff (\forall x : x \in A \iff x \in B)",r"(A = B) \iff (\forall x : x \in A \rightarrow x \in B)"],
                      [r"(A = B) \iff (\forall x : x \notin A \iff x \notin B)",r"(A = B) \iff (\forall x : x \notin A \rightarrow x \notin B)"],
                      [r"(A \subset B) \iff (A \subseteq B) \land (A \ne B)",r"(A \subset B) \rightarrow (A \nsubseteq B)"],
                      [r"(V = \emptyset) \iff \forall x : x \notin V",r"(V = \emptyset ) \iff [ \forall x : x \notin V \lor x = \emptyset ]"],
                      [r" \forall A : \emptyset \subseteq A",r" \forall A : \emptyset \nsubseteq A"],
                      [r"A = \emptyset \iff ( \forall B : A \subseteq B)",r"A = \emptyset \iff ( \forall B : A \nsubseteq B"],
                      [r"(A \ne \emptyset ) \iff \exists x : x \in A",r"(A \ne \emptyset ) \iff [ \exists x : x \in A \land x \ne \emptyset ]"],
                      [r"(A \subseteq B) \rightarrow [ \nexists x : x \in A \land x \notin B ]",r"(A \subseteq B) \rightarrow [ \exists x : x \in B \land x \notin A ]"]
                      ]
        i1=random.randint(0,len(truthOptions)-1)
        j1=random.randint(0,1)
        sol1 = truthOptions[i1][j1]
        del truthOptions[i1]
        i2=random.randint(0,len(truthOptions)-1)
        j2=random.randint(0,1)
        sol2 = truthOptions[i2][j2] 
        del truthOptions[i2]
        solution = r"a) "+("correct" if j1==0 else "incorrect")+r", b) "+("correct" if j2==0 else "incorrect")+r"" 
        question=r'which of the next subset properties are correct: a) '+sol1+r',b) '+sol2+r''
        options =json.loads(json.dumps({'a':r"a) correct, b) correct",
                                        'b':r"a) correct, b) incorrect", 
                                        'c':r"a) incorrect, b) correct", 
                                        'd':r"a) incorrect, b) incorrect"}))
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return [jsonResponse]
    except Exception as er:
        return er

exam1 = [truthTableProblem, tautologiesProblem, tautologyNameProblem, equivalencesProblem, equivalenceNameProblem, setPropertiesProblem, subSetPropertiesProblem]
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