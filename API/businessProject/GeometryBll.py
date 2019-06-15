import random
import math
import json
import coursesFunctionsBll


#find the equation which pass through a given point and is parallel to a given
#line
def parallelProblem():
    try:
        x0 = random.randint(2,10) * (random.randint(0,1) * 2 - 1)
        y0 = random.randint(2,10) * (random.randint(0,1) * 2 - 1)
        x1 = random.randint(2,10) * (random.randint(0,1) * 2 - 1)
        y1 = random.randint(2,10) * (random.randint(0,1) * 2 - 1)
        x2 = random.randint(2,10) * (random.randint(0,1) * 2 - 1)
        y2 = random.randint(2,10) * (random.randint(0,1) * 2 - 1)
        if x2 == x1:
            return parallelProblem()
        slope = round((y2 - y1) / (x2 - x1),4)
        intersection = round(y0 - (x0 * slope),4)
        solution = "y=(" + str(slope) + "x)+(" + str(intersection) + ")"
        question = "which is the straight line which pass through the point (" + str(x0) + "," + str(y0) + ") and is parallel to the straigh line which pass through the points (" + str(x1) + "," + str(y1) + ") and (" + str(x2) + "," + str(y2) + "): "
        options = coursesFunctionsBll.parallelProblemOptions(slope, intersection)
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return jsonResponse
    except Exception as er:
        return er
#find perpendicular line which connect a given point with a given line
def perpendicularProblem():
    try:
        x0 = random.randint(2,10) * (random.randint(0,1) * 2 - 1)
        y0 = random.randint(2,10) * (random.randint(0,1) * 2 - 1)
        x1 = random.randint(2,10) * (random.randint(0,1) * 2 - 1)
        y1 = random.randint(2,10) * (random.randint(0,1) * 2 - 1)
        x2 = random.randint(2,10) * (random.randint(0,1) * 2 - 1)
        y2 = random.randint(2,10) * (random.randint(0,1) * 2 - 1)
        if x2 == x1:
            return parallelProblem()
        slope = round(-1 / ((y2 - y1) / (x2 - x1)),4)
        intersection = round(y0 - (x0 * slope),4)
        solution = "y=(" + str(slope) + "x)+(" + str(intersection) + ")"
        question = "which is the straight line which pass through the point (" + str(x0) + "," + str(y0) + ") and is perpendicular to the straigh line which pass through the points (" + str(x1) + "," + str(y1) + ") and (" + str(x2) + "," + str(y2) + "): "
        options = coursesFunctionsBll.parallelProblemOptions(slope, intersection)
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return jsonResponse
    except Exception as er:
        return er
#find circle equation having one point of the circle an its center
def circleProblem():
    try:
        x0 = random.randint(2,19) * (random.randint(0,1) * 2 - 1)
        y0 = random.randint(2,19) * (random.randint(0,1) * 2 - 1)
        x1 = random.randint(2,19) * (random.randint(0,1) * 2 - 1)
        y1 = random.randint(2,19) * (random.randint(0,1) * 2 - 1)
        r = (((x1 - x0) ** 2) + ((y1 - y0) ** 2)) ** (1 / 2)
        perimeter = round(2 * 3.1416 * r,4)
        area = round(3.1416 * r * r,4)
        solution = "Perimeter= " + str(perimeter) + " and Area=" + str(area)
        question = "Find the perimeter and area of the circle which center is (" + str(x0) + "," + str(y0) + ") and pass through the point (" + str(x1) + "," + str(y1) + "): "
        options = coursesFunctionsBll.perimeterAreaOptions(perimeter, area)
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return jsonResponse
    except Exception as er:
        return er
#find ellipse having the foci and a point of the ellipse
def ellipseProblem():
    try:
        x01 = random.randint(2,10) * (random.randint(0,1) * 2 - 1)
        x02 = random.randint(2,10) * (random.randint(0,1) * 2 - 1)
        y0 = random.randint(2,10) * (random.randint(0,1) * 2 - 1)
        x1 = random.randint(2,10) * (random.randint(0,1) * 2 - 1)
        y1 = random.randint(2,10) * (random.randint(0,1) * 2 - 1)
        x0 = (x01 + x02) / 2 #HERE IS X0
        if x01 == x02 or y0 == y1:
            return ellipseProblem()
        constant = ((((x1 - x01) ** 2) + ((y1 - y0) ** 2)) ** (1 / 2)) + ((((x1 - x02) ** 2) + ((y1 - y0) ** 2)) ** (1 / 2))
        vertice01 = (x01 + x02 - constant) / 2
        vertice02 = (x01 + x02 + constant) / 2
        xDistance = abs(vertice02 - x0)
        yDistance = ((xDistance ** 2) - ((x01 - x0) ** 2)) ** (1 / 2)
        solution = "[(x-(" + str(x0) + "))^2/" + str(round(xDistance ** 2,4)) + "]+[(y-(" + str(y0) + "))^2/" + str(round(yDistance ** 2,4)) + "]=1"
        #solutions =
        #["[(x-("+str(x0)+"))^2/"+str(xDistance**2)+"]+[(y-("+str(y0)+"))^2/"+str(yDistance**2)+"]=1",
        #"[(x-("+str(x0)+"))^2/"+str(xDistance)+"]+[(y-("+str(y0)+"))^2/"+str(yDistance)+"]=1",
        #"[(x-("+str(x0)+"))^2/"+str(xDistance**2)+"]+[(y-("+str(y0)+"))^2/"+str(yDistance**2)+"]=1",
        #"[(x-("+str(x0)+"))^2/"+str(xDistance**2)+"]+[(y-("+str(y0)+"))^2/"+str(yDistance**2)+"]=1"]
        #random.shuffle(solutions)
        #options =json.loads(json.dumps({'a':solutions[0], 'b':solutions[1],
        #'c':solutions[2], 'd':solutions[3]}))
        options = coursesFunctionsBll.ellipseProblemOptions([x0, round(xDistance ** 2,4), y0, round(yDistance ** 2,4)])
        question = "which is the canonical equation of the ellipse  which focus are (" + str(x01) + "," + str(y0) + ") (" + str(x02) + "," + str(y0) + ") and pass through the point (" + str(x1) + "," + str(y1) + "): "
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return jsonResponse
    except Exception as er:
        return er
#get parabola equation through focus and directrix
#this is how you get equation form focus and directrix:
#https://www.khanacademy.org/math/algebra2/intro-to-conics-alg2/focus-and-directrix-of-a-parabola-alg2/v/equation-for-parabola-from-focus-and-directrix
def parabolaProblem():
    try:
        focusx = random.randint(2,20) * (random.randint(0,1) * 2 - 1)
        focusy = random.randint(2,20) * (random.randint(0,1) * 2 - 1)
        directrix = (random.randint(2,20) * (random.randint(0,1) * 2 - 1))
        if(directrix >= focusy):
            parabolaProblem()
        c1 = round((focusy + directrix) / 2,4)
        c2 = round(1 / (2 * (abs(focusy - directrix))),4)
        c3 = focusx
        solution = "y-(" + str(c1) + ")=" + str(c2) + "*(x-(" + str(c3) + "))^2"
        options = coursesFunctionsBll.parabolaProblemOptions([c1, c2, c3])
        question = "which is the canonical equation of the parabola which focus (" + str(focusx) + "," + str(focusy) + ")  directrix y=" + str(directrix) + ":"
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return jsonResponse
    except Exception as er:
        return er
#given the center and one vertix find the equation of hyperbola
#review asymptotes topic in https://en.wikipedia.org/wiki/Hyperbola 
def hyperbolaProblem():
    try:
        x01 = random.randint(2,20) * (random.randint(0,1) * 2 - 1)
        x02 = random.randint(2,20) * (random.randint(0,1) * 2 - 1)
        if abs(x01 - x02) <= 2:
            return hyperbolaProblem()
        y0 = random.randint(2,20) * (random.randint(0,1) * 2 - 1)
        x0 = (x01 + x02) / 2
        vertice = x0
        while vertice == x0:
            vertice = random.randint(1,abs(x01 - x02) - 1) + (x01 if x01 < x02 else x02)
        x0 = (x01 + x02) / 2
        a = abs(vertice - x0)
        c = abs(x01 - x0)
        b = round(((c ** 2) - (a ** 2)) ** (1 / 2),4)

        solution = "[(x-(" + str(x0) + "))^2/" + str(round(a ** 2,4)) + "]-[(y-(" + str(y0) + "))^2/" + str(round(b ** 2,4)) + "]=1"
        options = coursesFunctionsBll.hyperbolaProblemOptions([x0, round(a ** 2,4), y0, round(b ** 2,4)])
        question = "which is the canonical equation of the hyperbola  which foci are (" + str(x01) + "," + str(y0) + ") (" + str(x02) + "," + str(y0) + ") and one of vertices is in (" + str(vertice) + "," + str(y0) + "): "
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return jsonResponse
    except Exception as er:
        return er
#find the diameter of the circle which a given center and a given tangent line
#use the perpendicular line between the center an the tangent line
def circleTanProblem():
    try:
        x = random.randint(2,10) * (random.randint(0,1) * 2 - 1)
        y = random.randint(2,10) * (random.randint(0,1) * 2 - 1)
        m = random.randint(2,10) * (random.randint(0,1) * 2 - 1)
        c = random.randint(2,10) * (random.randint(0,1) * 2 - 1)
        slope = -1 / m
        intersection = y - (x * slope)
        x1 = (intersection - c) / (m - slope)
        y1 = (x1 * m) + c
        distance = ((x1 - x) ** 2 + (y1 - y) ** 2) ** (1 / 2)
        diameter = round(distance * 2,4)
        solution = str(diameter)
        options = coursesFunctionsBll.generateOptions(diameter)
        question = "which is the diameter of a circle where center is in (" + str(x) + "," + str(y) + ") and is tangent to the line y=(" + str(m) + "x)+(" + str(c) + ")"
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return jsonResponse
    except Exception as er:
        return er
#find the are havinf the foci and the minor semiaxis, to do this you must find
#the major semi-axis
def ellipseAreaProblem():
    try:
        x01 = random.randint(2,10) * (random.randint(0,1) * 2 - 1)
        x02 = random.randint(2,10) * (random.randint(0,1) * 2 - 1)
        y0 = random.randint(2,10) * (random.randint(0,1) * 2 - 1)
        minor = random.randint(2,10)
        if x01 == x02:
            return ellipseProblem()
        x0 = (x01 + x02) / 2 #HERE IS X0
        major = ((x01 - x0) ** 2 + (minor) ** 2) ** (1 / 2)
        area = round(3.1416 * minor * major,4)
        solution = str(area)
        options = coursesFunctionsBll.generateOptions(area)
        question = "which is the area of ellipse which focus on (" + str(x01) + "," + str(y0) + ") (" + str(x02) + "," + str(y0) + ") and minor semiaxis equal to " + str(minor) + ""
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return jsonResponse
    except Exception as er:
        return er
#to the triangle with given three points find the area and perimeter
#find the perpendicular line between any of the three point and the line build
#with the other two points
#DO THE AREA PART BY SHOELACE FORMULA, IS FAR EASIER
#https://math.stackexchange.com/questions/516219/finding-out-the-area-of-a-triangle-if-the-coordinates-of-the-three-vertices-are
def triangleProblem():
    try:
        x1 = random.randint(2,10) * (random.randint(0,1) * 2 - 1)
        y1 = random.randint(2,10) * (random.randint(0,1) * 2 - 1)
        x2 = random.randint(2,10) * (random.randint(0,1) * 2 - 1)
        y2 = random.randint(2,10) * (random.randint(0,1) * 2 - 1)
        x3 = random.randint(2,10) * (random.randint(0,1) * 2 - 1)
        y3 = random.randint(2,10) * (random.randint(0,1) * 2 - 1)
        if x2 == (-1 * x1):
            return triangleProblem()
        area = abs(((x2 * y3) - (x3 * y2) - (x1 * y3) + (x3 * y1) + (x1 * y2) - (x2 * y1))/2)
        #m1 = (y2 - y1) / (x2 - x1)
        #b1 = y1 - (m1 * x1)
        #m2 = -1 / m1
        #b2 = y3 - (m2 * x3)
        #x4 = (b2 - b1) / (m1 - m2)
        #y4 = (m2 * x4) + b2
        base = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1 / 2)
        #height = ((x4-x3)**2+(y4-y3)**2)**(1/2)
        side2 = ((x3 - x1) ** 2 + (y3 - y1) ** 2) ** (1 / 2)
        side3 = ((x3 - x2) ** 2 + (y3 - y2) ** 2) ** (1 / 2)
        #area = round(base * height / 2,4)
        perimeter = round(base + side2 + side3,4)
        solution = "Perimeter= " + str(perimeter) + " and Area=" + str(area)
        options = coursesFunctionsBll.perimeterAreaOptions(perimeter, area)
        question = "which is the perimeter and area of triangle where vertixes are (" + str(x1) + "," + str(y1) + ") (" + str(x2) + "," + str(y2) + ") (" + str(x3) + "," + str(y3) + "):"
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return jsonResponse
    except Exception as er:
        return er
#for the triangle with the given three vertixes find if is acute, obtuse or
#right
#get the biggest line, find perpendicular line which connect biggest line with
#the lef point
#betterr do it this way: find the biggest line, find the hipotenuse for the other two sides, if biggest side is bigger than hipotenuse then is abtuse, less than hipotenuse then acute, if both are equal then right
def triangleAngleProblem():
    try:
        x1 = random.randint(2,10) * (random.randint(0,1) * 2 - 1)
        y1 = random.randint(2,10) * (random.randint(0,1) * 2 - 1)
        x2 = random.randint(2,10) * (random.randint(0,1) * 2 - 1)
        y2 = random.randint(2,10) * (random.randint(0,1) * 2 - 1)
        x3 = random.randint(2,10) * (random.randint(0,1) * 2 - 1)
        y3 = random.randint(2,10) * (random.randint(0,1) * 2 - 1)
        if x1 == x2 or x1 == x3 or x2 == x3:
            return triangleAngleProblem()
        side1 = round(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1 / 2),2)
        side2 = round(((x3 - x1) ** 2 + (y3 - y1) ** 2) ** (1 / 2),2)
        side3 = round(((x3 - x2) ** 2 + (y3 - y2) ** 2) ** (1 / 2),2)
        #line = []
        #point = []
        sides = [side1,side2, side3]
        sides.sort()
        #if side1 > side2 and side1 > side3:
        #    line = [[x1,y1],[x2,y2]]
        #    point = [x3,y3]
        #    sides = [side2,side3, side1]
        #elif side2 > side3:
        #    line = [[x1,y1],[x3,y3]]
        #    point = [x2,y2]
        #    sides = [side1,side3, side2]
        #else:
        #    line = [[x2,y2],[x3,y3]]
        #    point = [x1,y1]
        #    sides = [side1,side2, side3]
        hipotenuse  =  round(((sides[0])**2+(sides[1])**2)**(1/2),2)
        #m = (line[1][1] - line[0][1]) / (line[1][0] - line[0][0])
        #b = line[0][1] - (m * line[0][0])
        #m1 = -1 / m
        #b1 = point[1] - (m1 * point[0])
        #x4 = (b1 - b) / (m - m1)
        #y4 = (m1 * x4) + b1
        #side4 = ((x4 - point[0]) ** 2 + (y4 - point[1]) ** 2) ** (1 / 2)
        #angle1 = math.degrees(math.asin(side4 / sides[0]))
        #angle2 = math.degrees(math.asin(side4 / sides[1]))
        #maxAngle = 180 - (angle1 + angle2)
        #solution = "right" if (maxAngle > 89.99 and maxAngle < 90.01) else ("obtuse" if maxAngle >= 90.01 else "acute")
        solution = "right" if (hipotenuse==sides[2]) else ("obtuse" if sides[2] >= hipotenuse else "acute")
        options = json.loads(json.dumps({'a':'right', 'b':'obtuse', 'c':'acute'}))
        question = "which is the triangle type if vertixes are (" + str(x1) + "," + str(y1) + "), (" + str(x2) + "," + str(y2) + "), and (" + str(x3) + "," + str(y3) + "): "
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return jsonResponse
    except Exception as er:
        return er

def apothemProblem():
    try:
        s0 = random.randint(5,10) #number of sides
        l0 = random.randint(10,100) #apothem

        a0 = (s0-2)*(math.pi) #total inner angle
        a1 = a0/s0 #angle per corner
        b0 = (l0*2)/math.tan(a1/2) #base per side
        area = round((l0*b0/2)*s0,4)
        perimeter = round(b0*s0,4)

        solution=r"area= "+str(area)+r"cm^{2}, perimeter="+str(perimeter)+r"cm"
        question = r"A regular polygon of "+str(s0)+r" sides have an apothem of "+str(l0)+r" cm. Find its area and perimeter: "
        alternatives = coursesFunctionsBll.multipleOptions([area, perimeter],5)
        tempAlternatives =[]
        for ta in range(5):
            tempAlternatives.append(r"area= "+str(alternatives[ta][0])+r"cm^{2}, perimeter="+str(alternatives[ta][1])+r"cm") 
        options =json.loads(json.dumps({'a':tempAlternatives[0],
                                        'b':tempAlternatives[1], 
                                        'c': tempAlternatives[2], 
                                        'd': tempAlternatives[3], 
                                        'e': tempAlternatives[4]}))
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return jsonResponse
    except Exception as er:
        return er

def rhombusProblem():
    try:
        q1 = [random.randint(0,7), random.randint(0,1)]
        while True:
            q2 =  [random.randint(0,7), random.randint(0,1)]
            if q2[0]!=q1[0]:
                break

        questOptions = [
            ["the diagonals bisect each other","the diagonals don't bisect each other"],
            ["the diagonals are not always congruent","the diagonals are always congruent"],
            ["each diagonal bisect a pair of opposite angles","each diagonal bisect a pair of adjacent angles"],
            ["the diagonals are perpendicular","the diagonals are parallel"],
            ["the legs don't bisect each other","the legs bisect each other"],
            ["the legs are always congruent","the legs are not always congruent"],
            ["each leg consecutive internal angles are suplementary","each leg consecutive internal angles are not suplementary"],
            ["the legs are parallel","the legs are perpendicular"]
            ]
       
        optSolutions=["is true","is false"]
        solution=r"A "+str(optSolutions[q1[1]])+r" and B "+str(optSolutions[q2[1]])+r""
        question = r"for a rhombus define which of the next affirmations are true, A="+str(questOptions[q1[0]][q1[1]])+r", B="+str(questOptions[q2[0]][q2[1]])+r""
        
        options =json.loads(json.dumps({'a':r"A "+str(optSolutions[0])+r" and B "+str(optSolutions[0])+r"",
                                        'b':r"A "+str(optSolutions[0])+r" and B "+str(optSolutions[1])+r"", 
                                        'c':r"A "+str(optSolutions[1])+r" and B "+str(optSolutions[0])+r"", 
                                        'd': r"A "+str(optSolutions[1])+r" and B "+str(optSolutions[1])+r""}))
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return jsonResponse
    except Exception as er:
        return er

def orthoCenterProblem():
    try:
        
        point=[]
        while True:
            point =[
            [random.randint(1,10) * (random.randint(0,1) * 2 - 1),random.randint(1,10) * (random.randint(0,1) * 2 - 1)],
            [random.randint(1,10) * (random.randint(0,1) * 2 - 1),random.randint(1,10) * (random.randint(0,1) * 2 - 1)],
            [random.randint(1,10) * (random.randint(0,1) * 2 - 1),random.randint(1,10) * (random.randint(0,1) * 2 - 1)]
            ]
            if (point[0][0]!=point[1][0] and point[0][1]!=point[1][1]) and (point[0][0]!=point[2][0] and point[0][1]!=point[2][1]) and (point[1][0]!=point[2][0] and point[1][1]!=point[2][1]):
                if ((point[0][1]-point[1][1])/(point[0][0]-point[1][0]))!=((point[0][1]-point[2][1])/(point[0][0]-point[2][0])):
                    break
        m1= -1/((point[0][1]-point[1][1])/(point[0][0]-point[1][0]))
        c1 = point[2][1]-(m1*point[2][0])
        m2= -1/((point[0][1]-point[2][1])/(point[0][0]-point[2][0]))
        c2 = point[1][1]-(m2*point[1][0])
        x = round((c2-c1)/(m1-m2),4)
        y = round((m2*x)+c2,4)

        solution=r"("+str(x)+r","+str(y)+r")"
        question = r"Find the orthocenter of triangle with vertices at ("+str(point[0][0])+r","+str(point[0][1])+r") ("+str(point[1][0])+r","+str(point[1][1])+r") ("+str(point[2][0])+r","+str(point[2][1])+r"): "
        alternatives = coursesFunctionsBll.multipleOptions([x, y],5)
        tempAlternatives =[]
        for ta in range(5):
            tempAlternatives.append(r"("+str(alternatives[ta][0])+r","+str(alternatives[ta][1])+r")") 
        options =json.loads(json.dumps({'a':tempAlternatives[0],
                                        'b':tempAlternatives[1], 
                                        'c': tempAlternatives[2], 
                                        'd': tempAlternatives[3], 
                                        'e': tempAlternatives[4]}))
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return jsonResponse
    except Exception as er:
        return er

def tangencyPointProblem():
    try:
        d= random.randint(11,20)
        t= random.randint(21,30)
        x = ((t**2)-(d**2))/(2*d)
        sol = round(x+d,4)
        solution=r""+str(sol)
        question = r"You are walking towards a circular swimming pool. At some moment you are standing "+str(d)+r"ft from the border, while your distance to the point of tangency is "+str(t)+r"ft. How many ft are you from the center of the pool?: "
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
        return jsonResponse
    except Exception as er:
        return er

def cosineTheoremProblem():
    try:
        a= random.randint(16,20)
        b= random.randint(16,20)
        c= random.randint(21,30)

        angle_a=round(math.acos(((a**2)-(b**2)-(c**2))/(-2*b*c))*(180/math.pi),4)
        angle_b=round(math.acos(((b**2)-(a**2)-(c**2))/(-2*a*c))*(180/math.pi),4)
        angle_c=round(math.acos(((c**2)-(b**2)-(a**2))/(-2*b*a))*(180/math.pi),4)

        optQuestions=[
            [r"x",angle_a],
            [r"y",angle_b],
            [r"z",angle_c]
            ]
        quest = optQuestions[random.randint(0,2)]

        solution=r""+str(quest[1])
        question = r"a triangle have side A of length "+str(a)+r" and opposite angle x, side B of length "+str(b)+r" and opposite angle y, side C of length "+str(c)+r" and opposite angle z. Find the value (in degrees) of "+str(quest[0])+r": "
        alternatives = coursesFunctionsBll.multipleTrigonometricOptions([quest[1]],5)
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
#centroid is also known as median
def centroidTriangleProblem():
    try:
        
        point=[]
        while True:
            point =[
            [random.randint(1,10) * (random.randint(0,1) * 2 - 1),random.randint(1,10) * (random.randint(0,1) * 2 - 1)],
            [random.randint(1,10) * (random.randint(0,1) * 2 - 1),random.randint(1,10) * (random.randint(0,1) * 2 - 1)],
            [random.randint(1,10) * (random.randint(0,1) * 2 - 1),random.randint(1,10) * (random.randint(0,1) * 2 - 1)]
            ]
            if (point[0][0]!=point[1][0] and point[0][0]!=point[2][0] and point[1][0]!=point[2][0]) and ((point[0][1]!=point[1][1] and point[0][1]!=point[2][1] and point[1][1]!=point[2][1])):
                #if (((point[0][1]+point[1][1])/(point[0][0]+point[1][0]))!=((point[0][1]+point[2][1])/(point[0][0]+point[2][0]))):
                break
            
        y1 = (point[0][1]+point[1][1])/2
        x1 = (point[0][0]+point[1][0])/2
        y2 = (point[0][1]+point[2][1])/2
        x2 = (point[0][0]+point[2][0])/2
        if x1==point[2][0] or x2==point[1][0]:
            return centroidTriangleProblem()
        m1= (y1-point[2][1])/(x1-point[2][0])
        c1 = point[2][1]-(m1*point[2][0])
        m2= (y2-point[1][1])/(x2-point[1][0])
        if  m1==m2:
            return centroidTriangleProblem()
        c2 = point[1][1]-(m2*point[1][0])
        x = round((c2-c1)/(m1-m2),4)
        y = round((m2*x)+c2,4)

        solution=r"("+str(x)+r","+str(y)+r")"
        question = r"Find the centroid (median) of triangle with vertices at ("+str(point[0][0])+r","+str(point[0][1])+r") ("+str(point[1][0])+r","+str(point[1][1])+r") ("+str(point[2][0])+r","+str(point[2][1])+r"): "
        alternatives = coursesFunctionsBll.multiAritmeticOptions([x, y],5)
        tempAlternatives =[]
        for ta in range(5):
            tempAlternatives.append(r"("+str(alternatives[ta][0])+r","+str(alternatives[ta][1])+r")") 
        options =json.loads(json.dumps({'a':tempAlternatives[0],
                                        'b':tempAlternatives[1], 
                                        'c': tempAlternatives[2], 
                                        'd': tempAlternatives[3], 
                                        'e': tempAlternatives[4]}))
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return jsonResponse
    except Exception as er:
        return er

def quadrilateralProblem():
    try:
        c1 = random.randint(1,45)
        c2 = random.randint(1,45)
        a1 = random.randint(2,10)
        a2 = random.randint(2,10)
        sol = round((180-(c1+c2))/(a1+a2),4)

        solution=r""+str(sol)
        question = r"A quadrilateral incribed in a circle has inner opposite angles A and B, where A degrees are "+str(a1)+r"x+"+str(c1)+r" and B degrees are "+str(a2)+r"x+"+str(c2)+r". Which is the value of x?:"
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
        return jsonResponse
    except Exception as er:
        return er

def ellipsePointProblem():
    try:
        x = random.randint(1,20)
        y = random.randint(1,20)
        a=b=0
        while True:
            a = random.randint(1,20)
            b = random.randint(1,20)
            if a!=b:
                break
        h = random.randint(1,20)
        k = random.randint(1,20)
        sol = (((x-h)**2)/(a**2))+(((y-k)**2)/(b**2))
        solution=""
        if sol<1:
            solution=r"Inside"
        elif sol==1:
            solution=r"On the edge"
        else:
            solution=r"Outside"
        question = r"For the ellipse with equation \frac{(x-("+str(h)+r"))^{2}}{"+str(a)+r"^{2}}+\frac{(y-("+str(k)+r"))^{2}}{"+str(b)+r"^{2}}=1 find where's fall the point ("+str(x)+r","+str(y)+r"): "
        
        options =json.loads(json.dumps({'a':r"Inside",
                                        'b':r"On the edge", 
                                        'c':r"Outside"}))
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return jsonResponse
    except Exception as er:
        return er

def sinTheoremProblem():
    try:
        z = random.randint(10,20)
        a=b=90
        while True:
            a = random.randint(1,178)
            b = random.randint(1,178)
            if a+b<(180):
                break
        c=180-a-b
        constant = z/math.sin(c*math.pi/180)
        y = constant*math.sin(b*math.pi/180)
        x = constant*math.sin(a*math.pi/180)
        sol = round(x+y+z,4)
        solution=r""+str(sol)+r"cm"
        question=r"a triangle has angles A, B and C, where angle A is "+str(a)+r"°, angle B is "+str(b)+r"° and the length of side AB is "+str(z)+r"cm. Find the perimeter of the triangle: "
        alternatives = coursesFunctionsBll.multipleOptions([sol],5)
        tempAlternatives =[]
        for ta in range(5):
            tempAlternatives.append(r""+str(alternatives[ta][0])+r"cm") 
        options =json.loads(json.dumps({'a':tempAlternatives[0],
                                        'b':tempAlternatives[1], 
                                        'c': tempAlternatives[2], 
                                        'd': tempAlternatives[3], 
                                        'e': tempAlternatives[4]}))
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return jsonResponse
    except Exception as er:
        return er

def kiteSinAreaProblem():
    try:
        z = random.randint(30,150)
        a=b=0
        while True:
            a = random.randint(5,20)
            b = random.randint(5,20)
            if a!=b:
                break
        area= round(a*b*math.sin(z*math.pi/180),4)
        long = ((a**2)+(b**2)-(2*a*b*math.cos(z*math.pi/180)))**(1/2)
        short = round(2*area/long,4)
        solution=r"area: "+str(area)+r", diagonal: "+str(short)+r""
        question=r"For a kite with side A with length "+str(a)+r" and side B with length "+str(b)+r", and angle between them equals to "+str(z)+r" degrees, find the area of the kite and the length of diagonal which connects the two congruent angles of the kite: "
        alternatives = coursesFunctionsBll.multipleOptions([area, short],5)
        tempAlternatives =[]
        for ta in range(5):
            tempAlternatives.append(r"area: "+str(alternatives[ta][0])+r", diagonal: "+str(alternatives[ta][1])+r"") 
        options =json.loads(json.dumps({'a':tempAlternatives[0],
                                        'b':tempAlternatives[1], 
                                        'c': tempAlternatives[2], 
                                        'd': tempAlternatives[3], 
                                        'e': tempAlternatives[4]}))
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return jsonResponse
    except Exception as er:
        return er

def circleRegularPolygonProblem1():
    try:
        x=  random.randint(10,20)
        s = random.randint(3,10)
        angle = (s-2)*180/(s*2)
        h= (x/2)/math.cos(angle*math.pi/180)
        perimeter = round(2*math.pi*h,4)
        solution=r""+str(perimeter)
        question=r"For a regular polygon of "+str(s)+" sides, where each side have a length of "+str(x)+r", find the perimeter of the circle that inscribe this polygon: "
        alternatives = coursesFunctionsBll.multipleOptions([perimeter],5)
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

def pyramidRegularPolygonProblem():
    try:
        x=  random.randint(10,20)
        s = random.randint(3,10)
        h= random.randint(10,20)
        angle = (s-2)*180/(s*2)
        op= (x/2)*math.tan(angle*math.pi/180)
        base = op*x*s/2
        volume = round((1/3)*base*h,4)
        solution=r""+str(volume)
        question=r"For a  pyramid where base is a regular polygon of "+str(s)+" sides where each side have a length of "+str(x)+r",and the pyramid height is "+str(h)+r", find the volume of the pyramid: "
        alternatives = coursesFunctionsBll.multipleOptions([volume],5)
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

def circleRegularPolygonProblem2():
    try:
        x=  random.randint(10,20)
        s = random.randint(3,10)
        angle = (s-2)*180/(s*2)
        h= (x/2)*math.tan(angle*math.pi/180)
        area = round(math.pi*h*h,4)
        solution=r""+str(area)
        question=r"For a regular polygon of "+str(s)+" sides, where each side have a length of "+str(x)+r", find the area of the circle inscribed in this polygon: "
        alternatives = coursesFunctionsBll.multipleOptions([area],5)
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

def circleKiteProblem():
    try:
        z = random.randint(30,150)
        a=b=0
        while True:
            a = random.randint(5,20)
            b = random.randint(5,20)
            if a<b:
                break
        area= a*b*math.sin(z*math.pi/180)
        c = ((a**2)+(b**2)-(2*a*b*math.cos(z*math.pi/180)))**(1/2)
        z1=z/2
        #short = round(2*area/long,4)
        #height = short/2
        z2 = math.asin((a/c)*math.sin(z*math.pi/180))*180/math.pi
        z3 = 180-z1-z2
        b2= b*math.sin(z1*math.pi/180)/math.sin(z3*math.pi/180)
        b3 = round(math.sin(z2*math.pi/180)*b2,4)

        solution=r""+str(b3)
        question=r"For a kite with side A with length "+str(a)+r" and side B with length "+str(b)+r", and angle between them equals to "+str(z)+r" degrees, find the radio of the circle inscribed in the kite: "
        alternatives = coursesFunctionsBll.multipleOptions([b3],5)
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

exam1 = [parallelProblem, perpendicularProblem, circleProblem, ellipseProblem, parabolaProblem, hyperbolaProblem, circleTanProblem, ellipseAreaProblem, triangleProblem, triangleAngleProblem, apothemProblem, rhombusProblem]
exam2 = [orthoCenterProblem, tangencyPointProblem, cosineTheoremProblem, centroidTriangleProblem, quadrilateralProblem, ellipsePointProblem, sinTheoremProblem, kiteSinAreaProblem, circleRegularPolygonProblem1, pyramidRegularPolygonProblem, circleRegularPolygonProblem2, circleKiteProblem]
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

#IDEAS FOR GEOMETRY EXAM 3
#area of circle that inscribe a rectangular
#area of circle that inscribe a triangle
#bisector problem
#area of queadrilateral inscribed in a circle
#equation of a circle that pass through three points
#suplpementary and complementary angles
#radians to degrees
#circumcircle (and how to get it with law of sines)
#algebraic proof of pitagoras theorem
#internal rectangle triangle in a rectangle triangle
#https://www.dummies.com/education/math/trigonometry/find-the-area-of-a-triangle-using-asa/ sas, asa methods to calculate triangle area
