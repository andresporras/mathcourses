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
        combi = math.factorial(f-1+c)/(math.factorial(f-1)*math.factorial(c))
        permu = f**p
        solution=r"a) "+str(combi)+r" b)"+str(permu)
        question=r"from the first "+str(f)+r" characters of alphabet, if you can repeat each character as many times as you want, a) how many ways of choose "+str(c)+r" characters can be done b) how many words of "+str(p)+r" characters can be done: "
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
        sol2 = round(sol2,4)
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
#binomialdistribution
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
        question=r"For certain basketball player, the probability of throwing the ball to the basket and score is "+str(p*100)+"\%. For throwing "+str(f)+r" times, a) what is the probability of score exactly "+str(e)+r" times b) at least "+str(ne)+r" times: "
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
        mode = math.floor((n+1)*p)
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

def unionThreeEventsProblem():
    try:
        p = random.randint(200,250)
        n1 = random.randint(50,75)
        n2 = random.randint(50,75)
        n3 = random.randint(50,75)
        m12 = random.randint(15,25)
        m13 = random.randint(15,25)
        m23 = random.randint(15,25)
        m123 = random.randint(5,10)
        sol1 = p-(n1+n2+n3-m12-m13-m23+m123)
        sol2 = n1-m12-m13+m123
        solution=r"a) "+str(sol1)+r", b) "+str(sol2)+r""
        question=r"A class have "+str(p)+r" students. After scholar year has finished the teacher provide the next report:  "+str(n1)+r" students pass maths, "+str(n2)+r" students pass english, "+str(n3)+r" students pass science, "+str(m12)+r" students pass both math and english,\\ "+str(m13)+r" students pass both math and science, "+str(m23)+r" students pass both english and science,  "+str(m123)+r" students pass three courses,\\ a) how many students fail all the three courses?, b) how many students fail both english and science but pass math?: "
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
#-a U -b U -c = a + a-b + ab-c
def mutuallyExclusiveProblem():
    try:
        p = random.randint(325,350)
        na = random.randint(125,150)
        anb = random.randint(75,100)
        abnc = random.randint(25,50)
        sol1 = na+anb+abnc
        a= p-na
        sol2 = a-anb
        solution=r"a) "+str(sol1)+r", b) "+str(sol2)+r""
        question=r"Microsoft choose a sample of "+str(p)+" employees in order to understand their main habits. They found the next information, "+str(na)+r" employees of the group don't read books,\\ "+str(anb)+r" employees read books but don't play an instrument, "+str(abnc)+r" employees read books and play an instrument but don't exercise.Using the provide information answer the next questions, \\a) how many employees don't read or don't play an instrument or don't exercise?, b) how many employees both read books and play an instrument?: "
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

def conditionalProbabilityProblem():
    try:
        f = random.randint(41,60)
        ft = random.randint(21,40)
        i = random.randint(41,60)
        fi = random.randint(21,40)
        sol1=round(ft*100/f,4)
        sol2 = round(fi*100/(f+i-fi),4)
        solution=r"a) "+str(sol1)+r"\%, b) "+str(sol2)+r"\%"
        question=r"A government made a poll to find the citizens preferences about social networks, they get the next conclusions, "+str(f)+r"\% of citizens use facebook,\\ "+str(ft)+r"\% of citizens use both twitter and facebook, "+str(i)+r"\% of citizens use instagram, "+str(fi)+r"\% of citizens use both instagram and facebook. Using this information solve the next questions\\ a) which is the probability of citizen use twitter if we know he use facebook?, b) which is the probability a citizen use both facebook and instagram if we know he use one of those two social networks?:"
        alternatives = coursesFunctionsBll.multiAritmeticOptions([sol1, sol2],5)
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

def conditionalProbabilityProblem():
    try:
        f = random.randint(41,60)
        ft = random.randint(21,40)
        i = random.randint(41,60)
        fi = random.randint(21,40)
        sol1=round(ft*100/f,4)
        sol2 = round(fi*100/(f+i-fi),4)
        solution=r"a) "+str(sol1)+r"\%, b) "+str(sol2)+r"\%"
        question=r"A government made a poll to find the citizens preferences about social networks, they get the next conclusions, "+str(f)+r"\% of citizens use facebook,\\ "+str(ft)+r"\% of citizens use both twitter and facebook, "+str(i)+r"\% of citizens use instagram, "+str(fi)+r"\% of citizens use both instagram and facebook. Using this information solve the next questions\\ a) which is the probability of citizen use twitter if we know he use facebook?, b) which is the probability a citizen use both facebook and instagram if we know he use one of those two social networks?:"
        alternatives = coursesFunctionsBll.multiAritmeticOptions([sol1, sol2],5)
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



def conditionalProbabilityProblem2():
    try:
        a = random.randint(41,60)/100
        ba = random.randint(41,60)/100
        cab = random.randint(41,60)/100
        sol1=round(a*ba*cab*100,4)
        sol2=round(100-(a*ba*100),4)
        solution=r"a) "+str(sol1)+r"\%, b) "+str(sol2)+r"\%"
        question=r"if A,B,C are events in S, where P(A)="+str(round(a*100))+r"\%,P(B|A)="+str(round(ba*100))+r"\%,P(C|AB)="+str(round(cab*100))+r"\%, then find the value of a) P(ABC) b) P(\neg A \cup \neg B): "
        alternatives = coursesFunctionsBll.multiAritmeticOptions([sol1, sol2],5)
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

#https://www.quora.com/How-do-I-prove-P-A-cap-B-c-P-A-P-A-cap-B
#https://www.quora.com/Does-P-B-C-A-1-P-B-A
def conditionalProbabilityProblem3():
    try:
        a = random.randint(41,60)/100
        b = random.randint(41,60)/100
        ab = random.randint(21,40)/100
        sol1=round((a-ab)*100,4)
        pba = ab/a
        sol2=round((1-pba)*100,4)
        solution=r"a) "+str(sol1)+r"\%, b) "+str(sol2)+r"\%"
        question=r"if A,B are events in S, where P(A)="+str(round(a*100))+r"\%,P(B)="+str(round(b*100))+r"\%,P(AB)="+str(round(ab*100))+r"\%, then find the value of a) P(A \cap B^{c}) b) P(B^{c}|A): "
        alternatives = coursesFunctionsBll.multiAritmeticOptions([sol1, sol2],5)
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


def varianceProblem():
    try:
        cards =[]
        for i in range(5):
            cards.append(random.randint(1,20))
        sums=[]
        for x in range(5):
            y=x+1
            while y<5:
                sums.append(cards[x]+cards[y])
                #sum+=cards[x]+cards[y]
                y+=1
        sol1 = round((sum(s for s in sums))/10,4)
        sol2= round((sum((s-sol1)**2 for s in sums))/10,4)
        sol3 = round(sol2**(1/2),4)

        solution=r"Expected value="+str(sol1)+r", variance="+str(sol2)+r", standard deviation="+str(sol3)+r""
        question=r"In a card game a player has a hand of 5 cards with cards of next values: "+str(cards[0])+r","+str(cards[1])+r","+str(cards[2])+r","+str(cards[3])+r","+str(cards[4])+r". For taking two of this 5 cards find the expected value, variation and standard deviation: "
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

def geometryDistributionProblem():
    try:
        x = random.randint(2,10)
        y = random.randint(2,10)
        p = random.randint(1,9)/100
        q=1-p
        sol1 = round((q**(x-1))*p*100,4)
        sol2=0
        for i in range(y):
            sol2+=(q**(i-1))*p*100
        sol2=round(sol2,4)
        solution=r"a) "+str(sol1)+r"\%, b) "+str(sol2)+r"\%"
        question=r"The probability to call a station radio and get a response is "+str(round(p*100))+r"\%. a) which is the probability to call and only get a response until the call number "+str(x)+r", b) get your first response on less than "+str(y)+r" calls:"
        alternatives = coursesFunctionsBll.arithmeticPercentageOptions([sol1, sol2],5)
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

def geometryVarianceProblem():
    try:
        p = random.randint(11,50)/100
        q=1-p
        sol1 = round(1/p,4)
        sol2= round(q/(p**2),4)
        sol3 = round(sol2**(1/2),4)
        solution=r"Expected value="+str(sol1)+r", variance="+str(sol2)+r", standard deviation="+str(sol3)+r""
        question=r"The probability to call a station radio and get a response is "+str(round(p*100))+r"\%. Find a) \mu b) \sigma^{2} c) \sigma: "
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

def pascalDistributionProblem():
    try:
        x = random.randint(11,15)
        r = random.randint(6,10)
        p = (random.randint(3,4)+(random.randint(0,1)*3))/10
        q=1-p
        sol1 = round(math.factorial(x-1)*(q**(x-r))*(p**(r))*100/(math.factorial(r-1)*math.factorial(x-r)),4)
        x2 = random.randint(7,10)
        r2 = random.randint(6,x2-1)
        sol2=0
        i=r2
        while i<=x2:
            sol2+=round(math.factorial(i-1)*(q**(i-r2))*(p**(r2))*100/(math.factorial(r2-1)*math.factorial(i-r2)),4)
            i+=1
        sol2=round(100-sol2,4)
        solution=r"a) "+str(sol1)+r"\%, b) "+str(sol2)+r"\%"
        question=r"The probability of a soccer player to score in a match is "+str(round(p*100))+r"\%. a) which is the probability that the player achieve his "+str(r)+r" match scoring in the "+str(x)+r" game b) for achieve his "+str(r2)+r" match scoring he needs more than "+str(x2)+r" games:"
        alternatives = coursesFunctionsBll.arithmeticPercentageOptions([sol1, sol2],5)
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

def pascalVarianceProblem():
    try:
        r = random.randint(6,15)
        p = random.randint(1,9)/10
        q=1-p
        sol1 = round(r/p,4)
        sol2= round(r*q/(p**2),4)
        sol3 = round(sol2**(1/2),4)
        solution=r"Expected value="+str(sol1)+r", variance="+str(sol2)+r", standard deviation="+str(sol3)+r""
        question=r"Probability for a soccer player to score in a match is "+str(round(p*100))+r"\%. For scoring in "+str(r)+r" matches, find a) \mu b) \sigma^{2} c) \sigma: "
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

def hyperGeometricDistributionProblem():
    try:
        nk = random.randint(32,64)
        nx = random.randint(8,16)
        k = random.randint(8,16)
        x = random.randint(2,4)
        x2 = random.randint(2,4)
        sol1 = round(coursesFunctionsBll.binomialCoefficient(k,x)*(coursesFunctionsBll.binomialCoefficient(nk-k,nx-x)*100/coursesFunctionsBll.binomialCoefficient(nk,nx)),4)
        sol2=0
        i=0
        while i<x2:
            sol2+=coursesFunctionsBll.binomialCoefficient(k,i)*(coursesFunctionsBll.binomialCoefficient(nk-k,nx-i)*100/coursesFunctionsBll.binomialCoefficient(nk,nx))
            i+=1
        sol2=round(sol2,4)
        solution=r"a) "+str(sol1)+r"\%, b) "+str(sol2)+r"\%"
        question=r"A glasses factory for this month make "+str(nk)+r" glasses, the quality engineer finds that "+str(k)+r" glasses are broken. for a group of "+str(nx)+r" glasses randomly chosen a) which is the probability that "+str(x)+r" glasses are broken b) less than "+str(x2)+r" glasses are broken: "
        alternatives = coursesFunctionsBll.arithmeticPercentageOptions([sol1, sol2],5)
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

def hyperGeometricVarianceProblem():
    try:
        nk = random.randint(32,64)
        nx = random.randint(8,16)
        k = random.randint(8,16)
        p = k/nk
        q=1-p
        sol1 = round(nx*p,4)
        sol2= round(nx*p*q*(nk-nx)/(nk-1),4)
        sol3 = round(sol2**(1/2),4)
        solution=r"Expected value="+str(sol1)+r", variance="+str(sol2)+r", standard deviation="+str(sol3)+r""
        question=r"A glasses factory for this month make "+str(nk)+r" glasses, the quality engineer finds that "+str(k)+r" glasses are broken. for a group of "+str(nx)+r" glasses randomly chosen, find a) \mu b) \sigma^{2} c) \sigma: "
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

def bayesTheoremProblem():
    try:
        a = 0.1
        b = 0.1
        c = 0.1
        for i in range(70):
            d=random.randint(0,2)
            a =a+(0.01 if d==0 else 0)
            b =b+(0.01 if d==1 else 0)
            c =c+(0.01 if d==2 else 0)
        fa = random.randint(10,20)/100
        fb = random.randint(10,20)/100
        fc = random.randint(10,20)/100
        sol1 = round(100*(1-(fc*c/((fa*a)+(fb*b)+(fc*c)))),4)
        sol2= round(100*((1-fb)*b/(1-(fa*a)-(fb*b)-(fc*c))),4)
        solution=r"a) "+str(sol1)+r"\%, b) "+str(sol2)+r"\%"
        question=r"Three machines, A, B and C produce "+str(round(a*100))+r"\%, "+str(round(b*100))+r"\% and "+str(round(c*100))+r"\% of total items. Percentage of broken production for this machines are "+str(round(fa*100))+r"\%, "+str(round(fb*100))+r"\% and "+str(round(fc*100))+r"\%.\\ If you choose a random produced item  a) which is the probability of don't get a machine C item if the item is broken, b) get a machine B item if the item is not broken:"
        alternatives = coursesFunctionsBll.arithmeticPercentageOptions([sol1, sol2],5)
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


def bagBallsProblem():
    try:
        r = random.randint(4,6)
        g = random.randint(4,6)
        b = random.randint(4,6)
        r0 = random.randint(1,3) 
        g0 = random.randint(1,3) 
        b0 = random.randint(1,3) 
        c = math.factorial(r0+g0+b0)/(math.factorial(r0)*math.factorial(g0)*math.factorial(b0))
        m=coursesFunctionsBll.variation(r+g+b,r0+g0+b0)
        p=(r+g+b)**(r0+g0+b0)
        sol1= round(c*coursesFunctionsBll.variation(r, r0)*coursesFunctionsBll.variation(g, g0)*coursesFunctionsBll.variation(b, b0)*100/m,4)
        sol2= round(c*(r**r0)*(g**g0)*(b**b0)*100/p,4)
        solution=r"a) "+str(sol1)+r"\%, b) "+str(sol2)+r"\%"
        question=r"We have a bag with "+str(r+g+b)+r" balls; "+str(r)+r" red, "+str(g)+r" green and "+str(b)+r" blue. If we take out "+str(r0+g0+b0)+r" balls \\ a) which is the probability to get "+str(r0)+r" red, "+str(g0)+r" green and "+str(b0)+r" blue (the order doesn't matter) \\ b) find probability for last question but this time every time you take out a ball, a new one of the same color is add on the bag:"
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

exam1 = [multiplicationCombinationProblem, permutationsProblem, combinationPermutationProblem, cpRepetitionProblem, coinProblem, throwProblem, coinUnfairProblem, binomialDistributionProblem, poissonDistributionProblem, vennDiagramProblem, unionThreeEventsProblem, mutuallyExclusiveProblem]
exam2 = [conditionalProbabilityProblem, conditionalProbabilityProblem2, conditionalProbabilityProblem3, varianceProblem, geometryDistributionProblem, geometryVarianceProblem, pascalDistributionProblem, pascalVarianceProblem, hyperGeometricDistributionProblem, hyperGeometricVarianceProblem, bayesTheoremProblem, bagBallsProblem]
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

#https://www.quora.com/In-how-many-ways-can-5-letters-be-taken-from-the-word-Mississippi take letters for a word with repeated letters