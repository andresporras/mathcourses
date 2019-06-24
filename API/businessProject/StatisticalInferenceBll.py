import random
import math
import json
import coursesFunctionsBll

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
        return [jsonResponse]
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
        return [jsonResponse]
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
        return [jsonResponse]
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
        return [jsonResponse]
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
        return [jsonResponse]
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
        sol = round((1-(2*(0.5-coursesFunctionsBll.normalProportionAprox(x,m,v))))*100,4)
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
        return [jsonResponse]
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
        return [jsonResponse]
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
        return [jsonResponse]
    except Exception as er:
        return er

#https://www.math.arizona.edu/~rsims/ma464/standardnormaltable.pdf link to normal distribution table
def sampleSizeProblem():
    try:
        p = random.randint(500,1000)
        s = random.randint(100,150)
        e = random.randint(20,30)
        a = random.randint(1,10)/100
        z = coursesFunctionsBll.normalDistributionInverse(1-(a/2))
        sol = round((z**2)*(s**2)*p/(((p-1)*(e**2))+((z**2)*(s**2))))
        solution=r""+str(sol)+r""
        question=r'A bank wants to know the average saving per client. A previous study shows the standard deviation on clients saving is \$'+str(s)+r'. The bank has '+str(p)+r' clients. What should be the size of the sample for an error limit of '+str(e)+r' and a significance level of '+str(round(a*100))+r'\%. Choose the closest answer: '
        alternatives = coursesFunctionsBll.positiveArithmeticOptions([sol],5, 10)
        tempAlternatives =[]
        for ta in range(5):
            tempAlternatives.append(r""+str(alternatives[ta][0])+r"")
        options =json.loads(json.dumps({'a':tempAlternatives[0],
                                        'b':tempAlternatives[1], 
                                        'c': tempAlternatives[2], 
                                        'd': tempAlternatives[3], 
                                        'e': tempAlternatives[4]}))
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return [jsonResponse]
    except Exception as er:
        return er

#https://www.math.arizona.edu/~rsims/ma464/standardnormaltable.pdf link to normal distribution table
def sampleSizeProblem2():
    try:
        s = random.randint(20,30)
        e = random.randint(5,10)
        a = random.randint(1,10)/100
        z = coursesFunctionsBll.normalDistributionInverse(1-(a/2))
        sol = round((z**2)*(s**2)/e**2)
        solution=r""+str(sol)+r""
        question=r'A research shows that average height of basketball players follows a normal distribution with standard deviation of '+str(s)+r' cms. If a research group wants to find the average size, what should be the size of the sample for an error limit of '+str(e)+r' and a significance level of '+str(round(a*100))+r'\% . Choose the closest option: '
        alternatives = coursesFunctionsBll.positiveArithmeticOptions([sol],5, 10)
        tempAlternatives =[]
        for ta in range(5):
            tempAlternatives.append(r""+str(alternatives[ta][0])+r"")
        options =json.loads(json.dumps({'a':tempAlternatives[0],
                                        'b':tempAlternatives[1], 
                                        'c': tempAlternatives[2], 
                                        'd': tempAlternatives[3], 
                                        'e': tempAlternatives[4]}))
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return [jsonResponse]
    except Exception as er:
        return er

#https://www.math.arizona.edu/~rsims/ma464/standardnormaltable.pdf link to normal distribution table
def proportionSizeProblem1():
    try:
        nn = random.randint(5000,10000)
        p = random.randint(10,90)/100
        q=1-p
        e = random.randint(5,10)/100
        a = random.randint(1,10)/100
        z = coursesFunctionsBll.normalDistributionInverse(1-(a/2))
        sol = round((((z**2)*p*q*nn)+(nn*(e**2)))/((nn*(e**2))+((z**2)*p*q)))
        solution=r""+str(sol)+r""
        question=r'In a city a previous study shows that '+str(round(p*100))+r'\% of population are fans of A team. A survey wants to comfirm this previous result. The city have '+str(nn)+r' citizens. Which should be the size of the sample for the new study for an error limit of '+str(e)+r' and a significance level of '+str(round(a*100))+r'\%. Choose the closest option: '
        alternatives = coursesFunctionsBll.positiveArithmeticOptions([sol],5, 10)
        tempAlternatives =[]
        for ta in range(5):
            tempAlternatives.append(r""+str(alternatives[ta][0])+r"")
        options =json.loads(json.dumps({'a':tempAlternatives[0],
                                        'b':tempAlternatives[1], 
                                        'c': tempAlternatives[2], 
                                        'd': tempAlternatives[3], 
                                        'e': tempAlternatives[4]}))
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return [jsonResponse]
    except Exception as er:
        return er

#https://www.math.arizona.edu/~rsims/ma464/standardnormaltable.pdf link to normal distribution table
def proportionSizeProblem2():
    try:
        p = random.randint(10,90)/100
        q=1-p
        e = random.randint(5,10)/100
        a = random.randint(1,10)/100
        z = coursesFunctionsBll.normalDistributionInverse(1-(a/2))
        sol = round(((z**2)*p*q)/(e**2))
        solution=r""+str(sol)+r""
        question=r'An international statistical service founds that '+str(round(p*100))+r'\% of population in country B lives in poverty. A new research wants to comfirm the former conclusion. Which should be the size of the sample for the new study for a error limit of '+str(e)+r' and a significance level of '+str(round(a*100))+r'\%. Choose the closest option: '
        alternatives = coursesFunctionsBll.positiveArithmeticOptions([sol],5, 10)
        tempAlternatives =[]
        for ta in range(5):
            tempAlternatives.append(r""+str(alternatives[ta][0])+r"")
        options =json.loads(json.dumps({'a':tempAlternatives[0],
                                        'b':tempAlternatives[1], 
                                        'c': tempAlternatives[2], 
                                        'd': tempAlternatives[3], 
                                        'e': tempAlternatives[4]}))
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return [jsonResponse]
    except Exception as er:
        return er
#https://stattrek.com/online-calculator/t-distribution.aspx t-student distribution calculator
#https://en.wikipedia.org/wiki/Student%27s_t-distribution link to t-student table distribution
def tStudentProblem():
    try:
        x = random.randint(5,25)
        m = random.randint(100,200)
        s = random.randint(5,10)
        pOptions = [0.2, 0.1, 0.05, 0.02, 0.01,0.005]
        p = pOptions[random.randint(0,5)]
        t=abs(coursesFunctionsBll.tStudentAprox(p/2,x-1))
        sol = round(t*s/(x**0.5),4)
        solution=r""+str(m)+r" \pm "+str(sol)+r""
        question=r'A sample of '+str(x)+r' canned tunas give an average weight of '+str(m)+r' grams and standard deviation of '+str(s)+r' grams. Find the confidence limit with a '+str(round(100*(1-p),1))+r'\% for the real weight of all the canned tunas (choose the closest option): '
        alternatives = coursesFunctionsBll.multipleOptions([sol],5)
        tempAlternatives =[]
        for ta in range(5):
            tempAlternatives.append(r""+str(m)+r" \pm "+str(alternatives[ta][0])+r"")
        options =json.loads(json.dumps({'a':tempAlternatives[0],
                                        'b':tempAlternatives[1], 
                                        'c': tempAlternatives[2], 
                                        'd': tempAlternatives[3], 
                                        'e': tempAlternatives[4]}))
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return [jsonResponse]
    except Exception as er:
        return er

#https://www.youtube.com/watch?v=6_V-bJlvR6Y how to calculate confidence interval in big samples
#https://www.math.arizona.edu/~rsims/ma464/standardnormaltable.pdf link to normal distribution table
def confidenceBigSamplesProblem():
    try:
        x = random.randint(50,100)
        m = random.randint(150,175)
        s = random.randint(5,10)
        pOptions = [0.2, 0.1, 0.05, 0.02, 0.01,0.005]
        p = pOptions[random.randint(0,5)]
        z=coursesFunctionsBll.normalDistributionInverse(1-(p/2))
        sol = round(z*s/(x**0.5),4)
        solution=r""+str(m)+r" \pm "+str(sol)+r""
        question=r'A sample of '+str(x)+r' school girls give an average height of '+str(m)+r' cms and standard deviation of '+str(s)+r' cms. Find the confidence limit with a '+str(round(100*(1-p),1))+r'\% for the real height of all the school girls (choose the closest option): '
        alternatives = coursesFunctionsBll.multipleOptions([sol],5)
        tempAlternatives =[]
        for ta in range(5):
            tempAlternatives.append(r""+str(m)+r" \pm "+str(alternatives[ta][0])+r"")
        options =json.loads(json.dumps({'a':tempAlternatives[0],
                                        'b':tempAlternatives[1], 
                                        'c': tempAlternatives[2], 
                                        'd': tempAlternatives[3], 
                                        'e': tempAlternatives[4]}))
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return [jsonResponse]
    except Exception as er:
        return er

#https://www.math.arizona.edu/~rsims/ma464/standardnormaltable.pdf link to normal distribution table
def confidenceComparisonSamplesProblem():
    try:
        n1 = random.randint(41,50)
        n2 = random.randint(31,40)
        u1 = random.randint(31,40)
        u2 = random.randint(41,50)
        s1 = random.randint(2,5)
        s2 = random.randint(6,9)
        pOptions = [0.2, 0.1, 0.05, 0.02, 0.01,0.005]
        p = pOptions[random.randint(0,5)]
        z=coursesFunctionsBll.normalDistributionInverse(1-(p/2))
        sol = round(z*((((s1**2)/n1)+((s2**2)/n2))**0.5),4)
        solution=r""+str(abs(u1-u2))+r" \pm "+str(sol)+r""
        question=r'In a software company the average age of programmers have standard deviation of '+str(s1)+r' years, and for human resources they have a standard deviation of '+str(s2)+r' years. \\ In a sample of '+str(n1)+r' programmers the average age was '+str(u1)+r' years, and in a sample of '+str(n2)+r' human resources employees the average age was '+str(u2)+r' years. \\ Find the confidence interval for the difference of height with a level of '+str(round(100*(1-p),2))+r'\%. Choose the closest option: '
        alternatives = coursesFunctionsBll.multipleOptions([sol],5)
        tempAlternatives =[]
        for ta in range(5):
            tempAlternatives.append(r""+str(abs(u1-u2))+r" \pm "+str(alternatives[ta][0])+r"")
        options =json.loads(json.dumps({'a':tempAlternatives[0],
                                        'b':tempAlternatives[1], 
                                        'c': tempAlternatives[2], 
                                        'd': tempAlternatives[3], 
                                        'e': tempAlternatives[4]}))
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return [jsonResponse]
    except Exception as er:
        return er

#https://www.math.arizona.edu/~rsims/ma464/standardnormaltable.pdf link to normal distribution table
def confidenceProportionProblem():
    try:
        n = random.randint(40,60)
        u = random.randint(20,30)
        pr = u/n
        pOptions = [0.2, 0.1, 0.05, 0.02, 0.01,0.005]
        p = pOptions[random.randint(0,5)]
        z=coursesFunctionsBll.normalDistributionInverse(1-(p/2))
        sol1=round(100*pr,4)
        sol2 = round(z*100*((pr*(1-pr)/n)**0.5),4)
        solution=r""+str(sol1)+r"\% \pm "+str(sol2)+r"\%"
        question=r'In colombia the police officers are being spied by a criminal organization, but the proportion is unknown. \\ A search founds that in a sample of  '+str(n)+r' police officers they found that '+str(u)+r' police officers are spied . \\ Find the confidence limit with a '+str(round(100*(1-p),1))+r'\% for the real proportion of police officers spied (choose the closest option): '
        alternatives = coursesFunctionsBll.percentageProportionOptions([sol1, sol2],5)
        tempAlternatives =[]
        for ta in range(5):
            tempAlternatives.append(r""+str(alternatives[ta][0])+r"\% \pm "+str(alternatives[ta][1])+r"\%")
        options =json.loads(json.dumps({'a':tempAlternatives[0],
                                        'b':tempAlternatives[1], 
                                        'c': tempAlternatives[2], 
                                        'd': tempAlternatives[3], 
                                        'e': tempAlternatives[4]}))
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return [jsonResponse]
    except Exception as er:
        return er

#http://www.stat.purdue.edu/~jtroisi/STAT350Spring2015/tables/FTable.pdf f distribution
#https://stattrek.com/online-calculator/f-distribution.aspx f distribution calculator
def fDistributionProblem():
    try:
        class sample:
            def __init__(self, size, variance):
                self.variance = variance
                self.size = size
        n1 = random.randint(2,10)
        n2 = random.randint(2,10)
        list1=[]
        list2=[]
        for x in range(n1):
            list1.append(random.randint(20,80))
        for x in range(n2):
            list2.append(random.randint(40,60))
        m1= sum(l1 for l1 in list1)/n1
        m2= sum(l2 for l2 in list2)/n2
        v1= sum((l1-m1)**2 for l1 in list1)/n1
        v2= sum((l2-m2)**2 for l2 in list2)/n2
        data = [sample(n1,v1) if v1>v2 else sample(n2,v2),
                sample(n1,v1) if v1<=v2 else sample(n2,v2),]
        pOptions = [0.2, 0.1, 0.05, 0.02, 0.01, 0.005]
        p = pOptions[random.randint(0,5)]
        f1=data[0].variance/data[1].variance
        f0 = coursesFunctionsBll.fDistributionAprox(p/2,data[0].size-1,data[1].size-1)
        f2 = coursesFunctionsBll.fDistributionAprox(1-(p/2),data[0].size-1,data[1].size-1)
        solution = r"equal" if(f0<=f1 and f1<=f2) else r"not equal"
        question=r'In order to search a new treatment for cancer, '+str(data[0].size+data[1].size)+r' mice are selected. '+str(data[0].size)+r' mice receive the treatment \\ while '+str(data[1].size)+r' mice dont receive the treatment. The first group shows a standard deviation of '+str(round(data[0].variance**0.5,4))+r' \\ while the second group shows an standard deviation of  '+str(round(data[1].variance**0.5,4))+r'. With a significance level of  '+str(round(p*100,2))+r'\%.  \\ Define if variance of both groups are equal: '
        
        options =json.loads(json.dumps({'a':r"equal",
                                        'b':r"not equal",}))
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return [jsonResponse]
    except Exception as er:
        return er

#http://www.stat.purdue.edu/~jtroisi/STAT350Spring2015/tables/FTable.pdf f distribution
#https://stattrek.com/online-calculator/f-distribution.aspx f distribution calculator
def differenceMeansProblem():
    try:
        class sample:
            def __init__(self, size, variance):
                self.variance = variance
                self.size = size
        n1 = random.randint(2,10)
        n2 = random.randint(2,10)
        list1=[]
        list2=[]
        for x in range(n1):
            list1.append(random.randint(20,80))
        for x in range(n2):
            list2.append(random.randint(40,60))
        m1= sum(l1 for l1 in list1)/n1
        m2= sum(l2 for l2 in list2)/n2
        v1= sum((l1-m1)**2 for l1 in list1)/n1
        v2= sum((l2-m2)**2 for l2 in list2)/n2
        data = [sample(n1,v1) if v1>v2 else sample(n2,v2),
                sample(n1,v1) if v1<=v2 else sample(n2,v2),]
        pOptions = [0.2, 0.1, 0.05, 0.02, 0.01, 0.005]
        p = pOptions[random.randint(0,5)]
        f1=data[0].variance/data[1].variance
        f0 = coursesFunctionsBll.fDistributionAprox(p/2,data[0].size-1,data[1].size-1)
        f2 = coursesFunctionsBll.fDistributionAprox(1-(p/2),data[0].size-1,data[1].size-1)
        solution = r"equal" if(f0<=f1 and f1<=f2) else r"not equal"
        question=r'In order to search a new treatment for cancer, '+str(data[0].size+data[1].size)+r' mice are selected. '+str(data[0].size)+r' mice receive the treatment \\ while '+str(data[1].size)+r' mice dont receive the treatment. The first group shows a standard deviation of '+str(round(data[0].variance**0.5,4))+r' \\ while the second group shows an standard deviation of  '+str(round(data[1].variance**0.5,4))+r'. With a significance level of  '+str(round(p*100,2))+r'\%.  \\ Define if variance of both groups are equal: '
        
        options =json.loads(json.dumps({'a':r"equal",
                                        'b':r"not equal",}))
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return [jsonResponse]
    except Exception as er:
        return er

exam1 = [normalDistributionProblem, 
    normalSampleInfiniteProblem, 
    normalSampleFiniteProblem,
    errorProportionProblem,
    sampleProportionProblem,
    proportionFiniteProblem,
    averageComparisonProblem,
    proportionComparisonProblem,
    sampleSizeProblem,
    sampleSizeProblem2,
    proportionSizeProblem1,
    proportionSizeProblem2,]
exam2 = [tStudentProblem, 
         confidenceBigSamplesProblem,
         confidenceComparisonSamplesProblem,
         confidenceProportionProblem,
         fDistributionProblem,]
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