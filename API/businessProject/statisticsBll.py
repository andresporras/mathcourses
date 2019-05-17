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

# simple random: each object is equally likely to be selected.
# convenience: you make it easy, the easiest sample you can get.
# systematic: selection of every k object for your sample, where k=m/n, where m is population and n is sample size.
# cluster: population is divide in clusters and one of the clusters, randomly selected, is chosen as the sample.
# stratified: the sample is formed by choosing objects from different stratified clusters.
#https://www.whatissixsigma.net/box-plot-diagram-to-identify-outliers/
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
        alternatives = coursesFunctionsBll.arithmeticPercentageOptions([sol],5, 1)
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
        alternatives = coursesFunctionsBll.arithmeticPercentageOptions([sol],5, 1)
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
        n=len(completeMatrix)
        sum_xy = sum(c[2] for c in completeMatrix)
        sum_x = sum(c[0] for c in completeMatrix)
        sum_y = sum(c[1] for c in completeMatrix)
        sum_x2 = sum(c[3] for c in completeMatrix)
        b = ((n*sum_xy)-(sum_x*sum_y))/((n*sum_x2)-(sum_x**2))
        a = (sum_y-(b*sum_x))/n
        b = round(b,4)
        a = round(a,4)
        solution=r"y="+str(b)+r"x+"+str(a)
        matrix_ = coursesFunctionsBll.tableString(matrix)
        question=r'A marketing department wants to understand the success of a tv daily broadcast commercial to increase sells. The collect the next data\\ '+str(matrix_)+r' \\ Find the simple linear regression to express the relationship between number os commercials (independent variable) and millions of sells (dependent variable): '
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
#https://stattrek.com/statistics/dictionary.aspx?definition=correlation  correlation formula, far easier than book explanation
def coefficientDeterminationProblem():
    try:
        rows = random.randint(4,8)
        matrix = coursesFunctionsBll.tableGenerator1(rows)
        completeMatrix = coursesFunctionsBll.completeTableGenerator1(matrix)
        b = round(((len(completeMatrix)*sum(c[2] for c in completeMatrix))-(sum(c[0] for c in completeMatrix)*sum(c[1] for c in completeMatrix)))/((len(completeMatrix)*sum(c[3] for c in completeMatrix))-(sum(c[0] for c in completeMatrix)**2)),4)
        a = round((sum(c[1] for c in completeMatrix)-(b*sum(c[0] for c in completeMatrix)))/len(completeMatrix),4)
        n=len(completeMatrix)
        sumX =round(sum(c[0] for c in completeMatrix),4)
        sumY =round(sum(c[1] for c in completeMatrix),4)
        sumXY =round(sum(c[2] for c in completeMatrix),4)
        sumX2 =round(sum(c[3] for c in completeMatrix),4)
        sumY2 =round(sum(c[4] for c in completeMatrix),4)
        sumX_X2=round(sum((c[0]-(sumX/n))**2 for c in completeMatrix),4)
        sumY_Y2=round(sum((c[1]-(sumY/n))**2 for c in completeMatrix),4)
        sumX_Y=round(sum((c[0]-(sumX/n))*(c[1]-(sumY/n)) for c in completeMatrix),4)
        sol1 = round(((sumY2-(a*sumX)-(b*sumXY))/(n-2))**(1/2),4)
        sol2 = round(sumX_Y/((sumX_X2*sumY_Y2)**(1/2)),4)
        sol3 = round(sol2**2,4)
        #s2 = (sumY2/n)-((sumY/n)**2)
        #sol2 = 1-((sol1**2)/s2)
        #sol3 = sol2**(1/2)
        solution=r"a) "+str(sol1)+r", b)"+str(sol2)+r", c)"+str(sol3)
        data = [["\sum X","\sum Y","\sum XY","\sum X^{2}","\sum Y^{2}","\sum (X - \overline{X})^{2}","\sum(Y - \overline{Y})^{2}","\sum (X-\overline{X})*(Y-\overline{Y})","a","b","n"],
                [str(sumX),str(sumY),str(sumXY),str(sumX2),str(sumY2), str(sumX_X2), str(sumY_Y2), str(sumX_Y),str(a),str(b),str(n)]]
        matrix_ = coursesFunctionsBll.tableString(data)
        question=r'Using the next table \\ '+str(matrix_)+r' \\ Where a and b are the intersection and the slope get by the linear regression formula, and n is the number of data. \\ Find a) standard error b) coefficient of linear correlation c) coefficient of determination: '
        alternatives = coursesFunctionsBll.correlationOptions([sol1, sol2, sol3],5)
        tempAlternatives =[]
        for ta in range(5):
            tempAlternatives.append(r"a) "+str(alternatives[ta][0])+r", b)"+str(alternatives[ta][1])+r", c)"+str(alternatives[ta][2]))
        options =json.loads(json.dumps({'a':tempAlternatives[0],
                                        'b':tempAlternatives[1], 
                                        'c': tempAlternatives[2], 
                                        'd': tempAlternatives[3], 
                                        'e': tempAlternatives[4]}))
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return jsonResponse
    except Exception as er:
        return er

def correlationRulesProblem():
    try:
        q1 = [random.randint(0,7), random.randint(0,1)]
        while True:
            q2 =  [random.randint(0,7), random.randint(0,1)]
            if q2[0]!=q1[0]:
                break

        questOptions = [
            ["linear correlation coefficient value is always between -1 and 1","linear correlation coefficient value is always between 0 and 1"],
            ["linear correlation coefficient is que square root of the coefficient of determination","coefficient of determination is que square root of the linear correlation coefficient"],
            ["for the linear correlation coefficient, the closer to 0 the less correlation between variables","for the linear correlation coefficient, the lowest the less correlation between variables"],
            ["for the coefficient of determination, the lower the value the less reliability have the linear regression model","for the coefficient of determination, the lower the value the more reliability have the linear regression model"],
            ["standard error shows the variability between the real data and the linear regression model","standard error shows the variability between the data and the mean of the variable"],
            ["for the linear correlation coefficient, a closer value to 1 shows a positive correlation between variables","for the linear correlation coefficient, a closer value to 0 shows a negative correlation between variables"],
            ["linear correlation coefficient is also known as pearson coefficient, while coefficient of determination is also known as R^{2}","linear correlation coefficient is also known as R^{2}, while coefficient of determination is also known as pearson coefficient"],
            ["a bigger variance will mean a bigger coefficient of determination","a lower variance will mean a bigger coefficient of determination"] #keep in mind that coefficient of determination = 1-((e^2)/(s^2)), where e is standard error and s^2 is the variance
            ]
       
        optSolutions=["is true","is false"]
        solution=r"A "+str(optSolutions[q1[1]])+r" and B "+str(optSolutions[q2[1]])+r""
        question = r"Which of the next affirmations are true, \\ A="+str(questOptions[q1[0]][q1[1]])+r" \\ B="+str(questOptions[q2[0]][q2[1]])+r""
        
        options =json.loads(json.dumps({'a':r"A "+str(optSolutions[0])+r" and B "+str(optSolutions[0])+r"",
                                        'b':r"A "+str(optSolutions[0])+r" and B "+str(optSolutions[1])+r"", 
                                        'c':r"A "+str(optSolutions[1])+r" and B "+str(optSolutions[0])+r"", 
                                        'd': r"A "+str(optSolutions[1])+r" and B "+str(optSolutions[1])+r""}))
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return jsonResponse
    except Exception as er:
        return er

def statisticsConceptProblem():
    try:
        q1 = [random.randint(0,8), random.randint(0,1)]
        while True:
            q2 =  [random.randint(0,8), random.randint(0,1)]
            if q2[0]!=q1[0]:
                break

        questOptions = [
            ["sample statistic is a single measure of some attribute of a sample","sample statistic is another name for the mean of a sample"],
            ["statistical parameter is a numerical characteristic of a statistical population","statistical parameter is a numerical characteristic of a statistical sample"],
            ["estimator is the sample statistic used to measure a parameter","estimator is the standard error used to measure a sample statistic"],
            ["consistent is a property of estimator that as the sample increase the measure converges to the true value","consistent is a property of estimator that the sample increase doesn't need to increase to converge to the true value"],
            ["efficiency is a property of estimator, so efficiency is bigger when variance is lower","efficiency is a property of estimator, so efficiency is bigger when  measure converges to the true value"],
            ["bias is a property of estimator, so estimator is unbias when mean of data is equal to estimated parameter","bias is a property of estimator, so estimator is unbias when mode of data is equal to estimated parameter"],
            ["robustness is a property of estimator as it describe how much an statistic change by only one data, for exmaple median is a robust estimator","robustness is a property of estimator as it describe how much an statistic change by only one data, for exaple average is a robust estimator"],
            ["for an estimator there are many sample statistics to measure one parameter","for an estimator there are only one sample statistic to measure one parameter"],
            ["sufficient is a property of estimator as it provides a summary of all the information related to the parameter","sufficient is a property of estimator as it provides a summary of all the information related to the statistic sample"]
            ]
       
        optSolutions=["is true","is false"]
        solution=r"A "+str(optSolutions[q1[1]])+r" and B "+str(optSolutions[q2[1]])+r""
        question = r"Which of the next affirmations are true, \\ A="+str(questOptions[q1[0]][q1[1]])+r" \\ B="+str(questOptions[q2[0]][q2[1]])+r""
        
        options =json.loads(json.dumps({'a':r"A "+str(optSolutions[0])+r" and B "+str(optSolutions[0])+r"",
                                        'b':r"A "+str(optSolutions[0])+r" and B "+str(optSolutions[1])+r"", 
                                        'c':r"A "+str(optSolutions[1])+r" and B "+str(optSolutions[0])+r"", 
                                        'd': r"A "+str(optSolutions[1])+r" and B "+str(optSolutions[1])+r""}))
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return jsonResponse
    except Exception as er:
        return er

def expectedVarianceProblem():
    try:
        m=random.randint(100,150)
        p= random.randint(200,1000)
        s=random.randint(100,200)
        sol1 = round(s/(m**(1/2)),4)
        sol2 = round((s/(m**(1/2)))*((p-m)/(p-1)),4)
        solution=r"a) "+str(sol1)+r", b) "+str(sol2)+r""
        question=r'If you make a sample of size '+str(m)+r' from a population with \sigma = '+str(s)+r' a) find the standard error of mean if population size is infinite (or it is a sample with replacement) b) standard error of mean if population size is '+str(p)+r': '
        alternatives = coursesFunctionsBll.multipleOptions([sol1, sol2],5)
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
#https://www.math.arizona.edu/~rsims/ma464/standardnormaltable.pdf link to normal distribution table
#http://onlinestatbook.com/2/calculators/normal_dist.html normal distribution calculator
def normalDistributionProblem():
    try:
        x=random.randint(14,20)
        m=x
        while m==x:
            m= random.randint(14,20)
        v=random.randint(4,10)
        sol = round(coursesFunctionsBll.normalDistributionAprox(x,m,v)*100,4)
        solution=r""+str(sol)+r"\%"
        question=r'The average salary in google is '+str(m)+' thousand dollars, with a variance of \$'+str(v)+' thousand. If distribution follows a normal distribution, which percentage of google employeers get a salary below \$'+str(x)+' thousand. Choose the option closer to the right solution: '
        alternatives = coursesFunctionsBll.arithmeticPercentageOptions([sol],5, 5)
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

#https://www.math.arizona.edu/~rsims/ma464/standardnormaltable.pdf link to normal distribution table
def normalSampleInfiniteProblem():
    try:
        n = random.randint(5,10)
        x=random.randint(144,150)
        m=x
        while m==x:
            m= random.randint(144,150)
        v=random.randint(40,50)
        v1=v/n
        sol = round((1-coursesFunctionsBll.normalDistributionAprox(x,m,v1))*100,4)
        solution=r""+str(sol)+r"\%"
        question=r'Average height for school students in New York is '+str(m)+r' cms, with a variance of '+str(v)+r' cms. For a sample of '+str(n)+' students, find the probability that sample average height is above '+str(x)+r' cms. Choose the option closer to the right solution: '
        alternatives = coursesFunctionsBll.arithmeticPercentageOptions([sol],5, 5)
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

#https://www.math.arizona.edu/~rsims/ma464/standardnormaltable.pdf link to normal distribution table
def normalSampleFiniteProblem():
    try:
        nn = random.randint(50,100)
        n = random.randint(5,10)
        m= random.randint(100,110)
        d =random.randint(1,6)
        x=m-d
        v=random.randint(50,60)
        v1=(v/n)*((nn-n)/(nn-1))
        sol = round((1-(2*coursesFunctionsBll.normalDistributionAprox(x,m,v1)))*100,4)
        solution=r""+str(sol)+r"\%"
        question=r'In a little village with '+str(nn)+r' houses,  the average size of a house is '+str(m)+r' mts^{2}, with a variance of '+str(v)+r' mts^{2}. For a sample of '+str(n)+' different houses, find the probability that sample average size is between '+str(m-d)+r' mts^{2} and '+str(m+d)+r' mts^{2}. Choose the option closer to the right solution: '
        alternatives = coursesFunctionsBll.arithmeticPercentageOptions([sol],5, 5)
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

def errorProportionProblem():
    try:
        m=random.randint(100,150)
        p= random.randint(200,1000)
        a=random.randint(10,90)/100
        sol1 = round(((a*(1-a))/(m))**(1/2),4)
        sol2 = round((((a*(1-a))/(m))*((p-m)/(p-1)))**(1/2),4)
        solution=r"a) "+str(sol1)+r", b) "+str(sol2)+r""
        question=r'In a car factory the '+str(round(a*100))+r'\% of productions has mechanical problems. If you make a sample of '+str(m)+r' cars a) find the standard error of proportion supposing factory made infinite cars (or it is a sample with replacement) b) standard error of proportion if total cars made are '+str(p)+r': '
        alternatives = coursesFunctionsBll.multipleOptions([sol1, sol2],5)
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

def sampleProportionProblem():
    try:
        a = random.randint(10,90)/100
        x=a+(random.randint(1,5)/100*((random.randint(0,1)*2)-1))
        n=random.randint(25,50)
        v=(a*(1-a))/n
        sol = round((1-coursesFunctionsBll.normalProportionAprox(x,a,v))*100,4)
        solution=r""+str(sol)+r"\%"
        question=r'In Colombia '+str(round(a*100))+r'\% of citizens think that president is doing a great job. If you make a sample of '+str(n)+r' citizens a) which is the probability that more than '+str(round(x*100))+r'\% of sample thinks the same way (choose the closest option): '
        alternatives = coursesFunctionsBll.arithmeticPercentageOptions([sol],5, 5)
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

#https://www.math.arizona.edu/~rsims/ma464/standardnormaltable.pdf link to normal distribution table
def proportionFiniteProblem():
    try:
        nn = random.randint(500,1000)
        n = random.randint(50,100)
        m= random.randint(10,90)/100
        d =random.randint(1,5)/100
        x=m-d
        v=((m*(1-m))/n)*((nn-n)/(nn-1))
        sol = round((2*coursesFunctionsBll.normalProportionAprox(x,m,v))*100,4)
        solution=r""+str(sol)+r"\%"
        question=r'In Mexico City the '+str(round(m*100))+r'\% hospitals report losses last year. If this city have a total of '+str(nn)+r' hospitals and a research study make a sample of '+str(n)+' different hospitals, find the probability that the percentage of hospitals in the sample which report losses last year is not between '+str(round((m-d)*100))+r'\% and '+str(round((m+d)*100))+r'\%. Choose the option closer to the right solution: '
        alternatives = coursesFunctionsBll.arithmeticPercentageOptions([sol],5, 5)
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

#https://www.math.arizona.edu/~rsims/ma464/standardnormaltable.pdf link to normal distribution table
def averageComparisonProblem():
    try:
        x = random.randint(70,90)
        y = x+(random.randint(1,5)*((random.randint(0,1)*2)-1))
        sx = random.randint(5,10)
        sy = random.randint(5,10)
        nx = random.randint(35,40)
        ny = nx+(random.randint(1,5)*((random.randint(0,1)*2)-1))
        d =random.randint(1,10)/10
        v=((sx**2)/nx)+((sy**2)/ny)
        sol = round((1-coursesFunctionsBll.normalDistributionAprox(d,(x-y),v))*100,4)
        solution=r""+str(sol)+r"\%"
        question=r'The average argentine lives '+str(x)+r' years, with standard deviation of '+str(sx)+r' years, while the average chilean lives '+str(y)+r' years, with standard deviation of '+str(sy)+r' years. If we make a sample of '+str(nx)+r' argentines and another samples whith '+str(ny)+r' chileans, which is the probability that argentine sample in average lives at least '+str(d)+r' years more than chilean sample? choose closest option: '
        alternatives = coursesFunctionsBll.arithmeticPercentageOptions([sol],5, 5)
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


#https://www.math.arizona.edu/~rsims/ma464/standardnormaltable.pdf link to normal distribution table
def proportionComparisonProblem():
    try:
        x = random.randint(40,60)/100
        y = x+((random.randint(1,5)*((random.randint(0,1)*2)-1))/100)
        nx = random.randint(35,40)
        ny = nx+(random.randint(1,5)*((random.randint(0,1)*2)-1))
        d =random.randint(1,5)/100
        v=((x*(1-x))/nx)+((y*(1-y))/ny)
        sol = round((coursesFunctionsBll.normalProportionAprox(d,(x-y),v))*100,4)
        solution=r""+str(sol)+r"\%"
        question=r'The '+str(round(x*100))+r'\% of ferrari cars are red color, while '+str(round(y*100))+r'\% of williams cars are red. For a sample of '+str(nx)+r' ferrari cars and a sample of '+str(ny)+r' williams cars, which is the probability that ferrari sample percentage of red cars is not more than '+str(round(d*100))+r'\% above the percentage of red cars in williams sample. Choose closest option: '
        alternatives = coursesFunctionsBll.arithmeticPercentageOptions([sol],5, 5)
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

#https://www.math.arizona.edu/~rsims/ma464/standardnormaltable.pdf link to normal distribution table
def sampleSizeProblem():
    try:
        p = random.randint(500,1000)
        s = random.randint(100,150)
        e = random.randint(5,10)
        a = random.randint(1,10)/100
        z = coursesFunctionsBll.normalDistributionAprox(1-(a/2),0,1)
        sol = round((z**2)*(s**2)*p/(((p-1)*(e**2))+((z**2)*(s**2))))
        solution=r""+str(sol)+r""
        question=r'A bank wants to know the average saving per client. A previous study shows the standard deviation on clients saving is \$'+str(s)+r'. The bank has '+str(p)+r' clients. What should be the size of the sample for an error limit of '+str(e)+r' and a significance level of '+str(a)+r'\%. Choose the closest answer: '
        alternatives = coursesFunctionsBll.positiveArithmeticOptions([sol],5, 3)
        tempAlternatives =[]
        for ta in range(5):
            tempAlternatives.append(r""+str(alternatives[ta][0])+r"")
        options =json.loads(json.dumps({'a':tempAlternatives[0],
                                        'b':tempAlternatives[1], 
                                        'c': tempAlternatives[2], 
                                        'd': tempAlternatives[3], 
                                        'e': tempAlternatives[4]}))
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return jsonResponse
    except Exception as er:
        return er

exam1 = [uniformDistributionProblem, continuousVarianceProblem, uniformVarianceProblem, categoricalQuantitativeProblem, samplingProblem, plotBoxOutlierProblem, chebyshevProblem, linearRegressionProblem, coefficientDeterminationProblem, correlationRulesProblem, statisticsConceptProblem, expectedVarianceProblem]
exam2 = [
    normalDistributionProblem, 
    normalSampleInfiniteProblem, 
    normalSampleFiniteProblem,
    errorProportionProblem,
    sampleProportionProblem,
    proportionFiniteProblem,
    averageComparisonProblem,
    proportionComparisonProblem,
    sampleSizeProblem]
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