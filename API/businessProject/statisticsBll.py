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
        return [jsonResponse]
    except Exception as er:
        return er
#https://math.dartmouth.edu/archive/m60s06/public_html/Lecture17.pdf
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
            sol2 = round((product*(ran**4)/4)-(2*product*sol1*(ran**3)/3)+(product*(sol1**2)*(ran**2)/2),4) #f(x)*[(u-x)**2] where u is expected value (sol1)
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
        return [jsonResponse]
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
        return [jsonResponse]
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
        return [jsonResponse]
    except Exception as er:
        return er

# simple random: each object is equally likely to be selected.
# convenience: you make it easy, the easiest sample you can get.
# systematic: selection of every k object for your sample, where k=m/n, where m is population and n is sample size.
# cluster: population is divide in clusters and one of the clusters, randomly selected, is chosen as the sample.
# stratified: the sample is formed by choosing objects from different stratified clusters.

def samplingProblem():
    try:
        opts = ["simple random","convenience","systematic","cluster", "stratified"]
        biOpts = []
        for i in range(5):
            for j in range(5):
                biOpts.append(r"a) "+str(opts[i])+r", b) "+str(opts[j]))
        quest = [
            ["Teacher randomly choose three sheets from a bag. The bag contains 30 sheets, each one with a different student name.", 0],
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
        return [jsonResponse]
    except Exception as er:
        return er

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
        return [jsonResponse]
    except Exception as er:
        return er

#sigma is standard deviation, mu is average value
#use chebyshev inequality https://en.wikipedia.org/wiki/Chebyshev%27s_inequality
def chebyshevProblem():
    try:
        av = random.randint(41,80)
        sd = random.randint(10,20)
        ran = random.randint(21,40)
        k = ran/sd
        prob = 1-(1/(k**2))
        sol = round(prob*100,4) #equals to 1-((sd/ran)**2)
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
        return [jsonResponse]
    except Exception as er:
        return er
    #y=mx+c https://stattrek.com/regression/regression-example.aspx?Tutorial=ap
    #m=sum[(x-X)(y-Y)]/sum[(x-X)^2] where X is x media, Y is y media
    #c=Y-m*X
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
        return [jsonResponse]
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
        return [jsonResponse]
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
            ["linear correlation coefficient is que square root of the coefficient of determination","coefficient of determination is tue square root of the linear correlation coefficient"],
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
        return [jsonResponse]
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
            ["consistent is a property of an estimator that as the sample increase the measure converges to the true value","consistent is a property of estimator that the sample increase doesn't need to increase to converge to the true value"],
            ["efficiency is a property of an estimator, so efficiency is bigger when variance is lower","efficiency is a property of estimator, so efficiency is bigger when  measure converges to the true value"],
            ["bias is a property of an estimator, so estimator is unbias when mean of data is equal to estimated parameter","bias is a property of an estimator, so estimator is unbias when mode of data is equal to estimated parameter"],
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
        return [jsonResponse]
    except Exception as er:
        return er

def expectedVarianceProblem():
    try:
        m=random.randint(100,150)
        p= random.randint(200,1000)
        s=random.randint(100,200)
        sol1 = round(s/(m**(1/2)),4)
        sol2 = round((s/(m**(1/2)))*(((p-m)/(p-1))**(1/2)),4)
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
        return [jsonResponse]
    except Exception as er:
        return er
#sample standard deviation vs population standard deviation https://www.khanacademy.org/math/statistics-probability/summarizing-quantitative-data/variance-standard-deviation-sample/a/population-and-sample-standard-deviation-review
def samplePopulationDeviationProblem():
    try:
        i0= random.randint(1,5)
        ik= random.randint(15,20)
        d = random.randint(5,10)
        numbers=[]
        for i in range(d):
            numbers.append(random.randint(i0,ik))
        av =sum(s for s in numbers)/d
        sumSquares= sum((n-av)**2 for n in numbers)
        sol1= round((sumSquares/d)**0.5,4)
        sol2= round((sumSquares/(d-1))**0.5,4)
        solution=r"a) "+str(sol1)+r", b) "+str(sol2)+r""
        question=r"For a population of numbers like the next one "+", ".join(str(n) for n in numbers)+r" a) find the standard deviation of this population b) assuming this list of number are a sample from a larger population, find the standard deviation of this sample: "
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
        return [jsonResponse]
    except Exception as er:
        return er

#Box and Whisker Plot https://datavizcatalogue.com/methods/box_plot.html
#https://www.whatissixsigma.net/box-plot-diagram-to-identify-outliers/
def boxWhiskerPlotProblem():
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
        th = random.randint(0,n-1)
        solution=""
        if (listValues[th]>=q1 and listValues[th]<=q3):
            solution=r"box"
        elif (listValues[th]>=ll and listValues[th]<=ul):
            solution=r"whisker"
        else:
            solution=r"outlier"
        question=r"Use the box and whisker plot for the next list of values "+", ".join(str(x) for x in listValues)+r". Find where the "+str(th+1)+r"th value of the list falls: "
        options =json.loads(json.dumps({'a':r"box",
                                        'b':r"whisker", 
                                        'c': r"outlier"}))
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return [jsonResponse]
    except Exception as er:
        return er
#skewed right and left, and center using mean and median https://people.richland.edu/james/ictcm/2001/descriptive/helpcenter.html https://study.com/academy/lesson/skewed-distribution-examples-definition-quiz.html
def statisticsMeasuresProblem():
    try:
        q1 = [random.randint(0,8), random.randint(0,1)]
        while True:
            q2 =  [random.randint(0,8), random.randint(0,1)]
            if q2[0]!=q1[0]:
                break

        questOptions = [
            [r"If mean is bigger than median then the distribution is skewed to the left",r"If mean is bigger than median then the distribution is skewed to the right"],
            [r"If mean is lower than median then the distribution is positively skewed",r"If mean is lower than median then the distribution is negatively skewed"],
            [r"If data is skewed to one side then median is a best measure of the center than mean",r"If data is skewed to one side then mean is a best measure of the center than median"],
            [r"The median does not have to be one of the data values",r"The median is always one of the data values"],
            [r"The midrange is the midpoint between the highest and the lowest value",r"The midrange is the midpoint between the most extreme value and 0"],
            [r"The trimmed mean remove the 10\% highest and the 10\% lowest values to get the mean",r"The trimmed mean remove the 10\% most extreme values to get the mean"],
            [r"To get the quadratic mean first sum the squares of every value, then divide by the number of values and then get the square root",r"To get the quadratic mean first sum the squares of every value, then get the square root and then divide by the number of values"],
            [r"To get the geometric mean first multiply all the values and then get the n root (where n is the number of values)",r"To get the geometric mean first multiply all the values and then get the n-1 root (where n is the number of values)"],
            [r"To get the harmonic mean divide n by the sum of the multiplicative inverses of each value",r"To get the harmonic mean divide 1 by the sum of the multiplicative inverses of each value"],
            [r"A distribution is multimodal when more than one value (and less than all the values) is the most repeated value",r"A distribution is always multimodal when more than one value is the most repeated value"],
            [r"A distribution has no mode when all the values repeat the same number of times",r"if all the values repeat the same number of times, then all the values are the mode"]
            ]
       
        optSolutions=["is true","is false"]
        solution=r"A "+str(optSolutions[q1[1]])+r" and B "+str(optSolutions[q2[1]])+r""
        question = r"Which of the next affirmations are true, \\ A="+str(questOptions[q1[0]][q1[1]])+r" \\ B="+str(questOptions[q2[0]][q2[1]])+r""
        
        options =json.loads(json.dumps({'a':r"A "+str(optSolutions[0])+r" and B "+str(optSolutions[0])+r"",
                                        'b':r"A "+str(optSolutions[0])+r" and B "+str(optSolutions[1])+r"", 
                                        'c':r"A "+str(optSolutions[1])+r" and B "+str(optSolutions[0])+r"", 
                                        'd': r"A "+str(optSolutions[1])+r" and B "+str(optSolutions[1])+r""}))
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return [jsonResponse]
    except Exception as er:
        return er

#domain and range https://www.varsitytutors.com/hotmath/hotmath_help/topics/domain-and-range
def midRangeProblem():
    try:
        a = random.randint(1,10)*((random.randint(0,1)*2)-1)
        b = random.randint(1,10)*((random.randint(0,1)*2)-1)
        c = random.randint(1,10)
        d = random.randint(1,10)
        a1 = -a*c
        b1 = -2*b*c
        c1 = a*d
        x1 = (-b1+(((b1**2)-(4*a1*c1))**0.5))/(2*a1)
        x2 = (-b1-(((b1**2)-(4*a1*c1))**0.5))/(2*a1)
        y1= ((a*x1)+(b))/((c*x1*x1)+(d))
        y2= ((a*x2)+(b))/((c*x2*x2)+(d))
        sol = round((y1+y2)/2,4)
        solution=r""+str(sol)
        question=r"Find the midrange of the function \frac{"+str(a)+r"x"+(r"+" if b>=0 else r"")+str(b)+r"}{"+str(c)+r"x^{2}+"+str(d)+r"}: "
        alternatives = coursesFunctionsBll.multipleOptions([sol],5)
        tempAlternatives =[]
        for ta in range(5):
            tempAlternatives.append(r""+str(alternatives[ta][0]))
        options =json.loads(json.dumps({'a':tempAlternatives[0],
                                        'b':tempAlternatives[1], 
                                        'c': tempAlternatives[2], 
                                        'd': tempAlternatives[3], 
                                        'e': tempAlternatives[4]}))
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return [jsonResponse]
    except Exception as er:
        return er

#empirical rule of normal distribution https://www.investopedia.com/terms/e/empirical-rule.asp
def empiricalRuleProblem():
    try:
        p= random.randint(10000,20000)
        m= random.randint(80,120)
        s= random.randint(2,8)
        sol1 = round(p*0.68)
        sol2 = round((p/2)-((p/2)*0.95))
        sol3 = round((p/2)+((p/2)*0.997))
        solution=r"a) "+str(sol1)+r", b) "+str(sol2)+r", c) "+str(sol3)
        question=r"A college research make a IQ test to every single student of the college and found the data follows a normal distribution where average IQ score is "+str(m)+r" and standard deviation equal to "+str(s)+r". Having the college "+str(p)+r" students, use the empirical rule of normal distribution to answer the next quetions \\ a) How many students get a score between "+str(m-s)+r" and "+str(m+s)+r". b) how many students get have a score below "+str(m-(2*s))+r". c) how many students get a score above "+str(m-(3*s))+r". Choose the closer option: "
        alternatives = coursesFunctionsBll.positiveArithmeticOptions([sol1, sol2, sol3],5, 5)
        tempAlternatives =[]
        for ta in range(5):
            tempAlternatives.append(r"a) "+str(alternatives[ta][0])+r", b) "+str(alternatives[ta][1])+r", c) "+str(alternatives[ta][2]))
        options =json.loads(json.dumps({'a':tempAlternatives[0],
                                        'b':tempAlternatives[1], 
                                        'c': tempAlternatives[2], 
                                        'd': tempAlternatives[3], 
                                        'e': tempAlternatives[4]}))
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return [jsonResponse]
    except Exception as er:
        return er

#fiftieth percentile is the median https://www.statisticshowto.datasciencecentral.com/probability-and-statistics/percentiles-rank-range/
def percentileProblem():
    try:
        a= random.randint(2,10)
        b= random.randint(2,10)
        z= random.randint(2,10)
        w = (random.randint(10,40)+(50 if random.randint(0,1)==0 else 0))/100
        c = (b*(math.e**(z/2))/a)-(b/a)
        sol1 = round(b*math.log(((0.5*a*c)+b)/b),4) 
        sol2 = round(b*math.log(((w*a*c)+b)/b),4) 
        solution=r"a) "+str(sol1)+r" hours, b) "+str(sol2)+r" hours"
        question=r"A chemistry laboratory finds that function \frac{e^{\frac{x}{"+str(b)+r"}}}{"+str(round(a*c,4))+r"} between 0 and "+str(z)+r" describes the probability distribution of the time of life (per hours) for XA1800  bacteria. \\ a) find the minimal time of life that a XA1800 bacteria requires to be in percentile 50 (median) b) minimal time of life that a XA1800 bacteria requires to be in percentile "+str(round(w*100))+r": "
        alternatives = coursesFunctionsBll.multipleOptions([sol1, sol2],5)
        tempAlternatives =[]
        for ta in range(5):
            tempAlternatives.append(r"a) "+str(alternatives[ta][0])+r" hours, b) "+str(alternatives[ta][1])+r" hours")
        options =json.loads(json.dumps({'a':tempAlternatives[0],
                                        'b':tempAlternatives[1], 
                                        'c': tempAlternatives[2], 
                                        'd': tempAlternatives[3], 
                                        'e': tempAlternatives[4]}))
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return [jsonResponse]
    except Exception as er:
        return er

#use hyper Geometric Distribution to solve this problem
#https://math.stackexchange.com/questions/3248971/what-is-the-probability-that-at-least-one-of-the-questions-appears-in-both-exams?noredirect=1#3248971 question made by myself in stackexchange
def bothExamsProblem():
    try:
        q= random.randint(80,160)
        e1= random.randint(5,10)
        e2= random.randint(15,30)
        sol = round(100*(1-coursesFunctionsBll.binomialCoefficient(q-e1,e2)/coursesFunctionsBll.binomialCoefficient(q,e2)),4)
        solution=r""+str(sol)+r"\%"
        question=r"To make his exams, a teacher has a database with "+str(q)+r" different questions and an algorithm which chooses n different questions from the database. In the semester the teacher made two exams, the first one with "+str(e1)+r" questions, the second one with "+str(e2)+r" questions. What is the probability that at least one of the questions appears in both exams?"
        alternatives = coursesFunctionsBll.arithmeticPercentageOptions([sol],5,1)
        tempAlternatives =[]
        for ta in range(5):
            tempAlternatives.append(r""+str(alternatives[ta][0])+r"\%")
        options =json.loads(json.dumps({'a':tempAlternatives[0],
                                        'b':tempAlternatives[1], 
                                        'c': tempAlternatives[2], 
                                        'd': tempAlternatives[3], 
                                        'e': tempAlternatives[4]}))
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return [jsonResponse]
    except Exception as er:
        return er

#use z valueu of normal distribution to define who is relatively taller http://www.talkstats.com/threads/computing-z-scores.602/
def relativelyTallerProblem():
    try:
        mm= random.randint(150,190)
        mf= mm-random.randint(5,20)
        m = mm+random.randint(1,5)*((random.randint(0,1)*2)-1)
        f=mf+random.randint(1,5)*((random.randint(0,1)*2)-1)
        sm = random.randint(10,15)
        sf = random.randint(10,15)
        zm= (m-mm)/sm
        zf= (f-mf)/sf
        solution = r"the male is relatively taller" if(zm>zf) else (r"the female is relatively taller" if(zm<zf) else r"the male and the female are relatively of the same tall")
        question=r"In X city the average size of 20-29 year old man is "+str(mm)+r" cms with an standard deviation of "+str(sm)+r" cms, the average size of 20-29 year old woman is "+str(mf)+r" cms with an standards deviation of "+str(sf)+r" cms. For 25 year old male person whose size is "+str(m)+r" cms and a 27 year old female whose size is "+str(f)+r" cms. Whose is relatively taller?: "
        options =json.loads(json.dumps({'a':r"the male is relatively taller",
                                        'b':r"the female is relatively taller", 
                                        'c': r"the male and the female are relatively of the same tall"}))
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return [jsonResponse]
    except Exception as er:
        return er

#residuals https://stattrek.com/regression/residual-analysis.aspx
def residualProblem():
    try:
        patron= random.randint(0,1)
        mistake= random.randint(0,1)
        m= random.randint(100,1000)/1000
        lista=[]
        sol1=["non-linear model", "linear model"]
        sol2=["no evidence of mistake in residual data", "evidence of mistake in residual data"]
        if patron==0:
            for x in range(7):
                lista.append(m*((x-3)**2))
        else:
            for x in range(7):
                lista.append(random.randint(1,10) if x%2==0 else (random.randint(1,10)*-1))
        distance = sum(lis for lis in lista)/7
        for x in range(7):
            lista[x]=round(lista[x]-distance,2)
        
        if mistake==0:
            nDistance = sum(lis for lis in lista)
            lista[0]=round(lista[3]-nDistance,2)
        else:
            lista[0]=round(lista[0]-0.5,2) if lista[0]<lista[1] else round(lista[0]+0.5,2)
            lista[6]=round(lista[6]-0.5,2) if lista[6]<lista[5] else round(lista[6]+0.5,2)
        subPatron=random.randint(0,1)
        if subPatron==0:
            for x in range(7):
                lista[x]=round(lista[x]*-1,2)
        matrix=[["independent variable (x)","residual"]]
        for x in range(7):
            matrix.append([str(x+1), str(lista[x])])
        matrix_ = coursesFunctionsBll.tableString(matrix)
        solution = r"a) "+sol1[patron]+r", b) "+sol2[mistake]
        question=r"A linear regression model gives this table about independent variable (x) of the model and it's residuals \\ "+str(matrix_)+r" \\ find a) if residual data suggest a linear or non-linear model b) if there is evidence of a mistake in residual data: "
        options =json.loads(json.dumps({'a':r"a) linear model, b) evidence of mistake in residual data",
                                        'b':r"a) linear model, b) no evidence of mistake in residual data", 
                                        'c': r"a) non-linear model, b) evidence of mistake in residual data", 
                                        'd': r"a) non-linear model, b) no evidence of mistake in residual data"}))
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return [jsonResponse]
    except Exception as er:
        return er

exam1 = [uniformDistributionProblem, continuousVarianceProblem, uniformVarianceProblem, categoricalQuantitativeProblem, samplingProblem, plotBoxOutlierProblem, chebyshevProblem, linearRegressionProblem, coefficientDeterminationProblem, correlationRulesProblem, statisticsConceptProblem, expectedVarianceProblem]
exam2 = [
    samplePopulationDeviationProblem,
    boxWhiskerPlotProblem,
    statisticsMeasuresProblem,
    midRangeProblem,
    empiricalRuleProblem,
    percentileProblem,
    bothExamsProblem,
    relativelyTallerProblem,
    residualProblem,
    ]
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


#sample standard deviation vs population standard deviation https://www.khanacademy.org/math/statistics-probability/summarizing-quantitative-data/variance-standard-deviation-sample/a/population-and-sample-standard-deviation-review
#Box and Whisker Plot https://datavizcatalogue.com/methods/box_plot.html
#skewed right and left, and center using mean and median https://people.richland.edu/james/ictcm/2001/descriptive/helpcenter.html https://study.com/academy/lesson/skewed-distribution-examples-definition-quiz.html
#domain and range https://www.varsitytutors.com/hotmath/hotmath_help/topics/domain-and-range
#empirical rule (normal distribution) https://www.investopedia.com/terms/e/empirical-rule.asp
#fiftieth percentile is the median https://www.statisticshowto.datasciencecentral.com/probability-and-statistics/percentiles-rank-range/
#use z valueu of normal distribution to define who is relatively taller http://www.talkstats.com/threads/computing-z-scores.602/
#residuals https://stattrek.com/regression/residual-analysis.aspx


