
import random
import math
import coursesFunctionsBll
from fractions import Fraction
from flask import jsonify
import json
from sympy import *
from copy import copy, deepcopy
#below a really good book of linear algebra
#https://books.google.com.co/books?id=DrXiBQAAQBAJ&pg=PA19&lpg=PA19&dq=direction+cosines+linear+algebra&source=bl&ots=ShIsqN8LbO&sig=ACfU3U07qvCiTsVjGDMZPDEnWhJjW49wyA&hl=en&sa=X&ved=2ahUKEwi3sOOKhtfgAhXQwFkKHbAOCS04FBDoATAIegQIAxAB#v=onepage&q=direction%20cosines%20linear%20algebra&f=false

def matrixProblem():
    try:
        #below temp random solutions
        x1= round(random.randint(1,10) * (random.randint(0,1) * 2 - 1)/random.randint(1,10) * (random.randint(0,1) * 2 - 1),4)
        y1= round(random.randint(1,10) * (random.randint(0,1) * 2 - 1)/random.randint(1,10) * (random.randint(0,1) * 2 - 1),4)
        z1= round(random.randint(1,10) * (random.randint(0,1) * 2 - 1)/random.randint(1,10) * (random.randint(0,1) * 2 - 1),4)

        matrix = [[random.randint(1,10) * (random.randint(0,1) * 2 - 1),
                   random.randint(1,10) * (random.randint(0,1) * 2 - 1),
                   random.randint(1,10) * (random.randint(0,1) * 2 - 1),
                   random.randint(1,10) * (random.randint(0,1) * 2 - 1)],
                  [random.randint(1,10) * (random.randint(0,1) * 2 - 1),
                   random.randint(1,10) * (random.randint(0,1) * 2 - 1),
                   random.randint(1,10) * (random.randint(0,1) * 2 - 1),
                   random.randint(1,10) * (random.randint(0,1) * 2 - 1)],
                   [random.randint(1,10) * (random.randint(0,1) * 2 - 1),
                      random.randint(1,10) * (random.randint(0,1) * 2 - 1),
                      random.randint(1,10) * (random.randint(0,1) * 2 - 1),
                      random.randint(1,10) * (random.randint(0,1) * 2 - 1)]]
        Det= (matrix[0][0]*((matrix[1][1]*matrix[2][2])-(matrix[1][2]*matrix[2][1])))-(matrix[0][1]*((matrix[1][0]*matrix[2][2])-(matrix[1][2]*matrix[2][0])))+(matrix[0][2]*((matrix[1][0]*matrix[2][1])-(matrix[1][1]*matrix[2][0])))

        Detx = (matrix[0][3]*((matrix[1][1]*matrix[2][2])-(matrix[1][2]*matrix[2][1])))-(matrix[0][1]*((matrix[1][3]*matrix[2][2])-(matrix[1][2]*matrix[2][3])))+(matrix[0][2]*((matrix[1][3]*matrix[2][1])-(matrix[1][1]*matrix[2][3])))

        Dety= (matrix[0][0]*((matrix[1][3]*matrix[2][2])-(matrix[1][2]*matrix[2][3])))-(matrix[0][3]*((matrix[1][0]*matrix[2][2])-(matrix[1][2]*matrix[2][0])))+(matrix[0][2]*((matrix[1][0]*matrix[2][3])-(matrix[1][3]*matrix[2][0])))

        Detz= (matrix[0][0]*((matrix[1][1]*matrix[2][3])-(matrix[1][3]*matrix[2][1])))-(matrix[0][1]*((matrix[1][0]*matrix[2][3])-(matrix[1][3]*matrix[2][0])))+(matrix[0][3]*((matrix[1][0]*matrix[2][1])-(matrix[1][1]*matrix[2][0])))
        solution=""
        if Det==0:
            if Detx==0 and Dety==0 and Detz==0:
                solution="dependent system"
            else:
                solution= "inconsistent system"
        else:
            x1=round(Detx/Det,4)
            y1=round(Dety/Det,4)
            z1=round(Detz/Det,4)
            solution=r"x="+str(x1)+r", y="+str(y1)+r", z="+str(z1)
        matrix_=""
        matrix_sol=""
        for row in range(len(matrix)):
            for col in range(len(matrix[row])-1):
                matrix_=matrix_+r""+str(matrix[row][col])+(r" & " if (len(matrix[row])-2)!=col else r"")
            matrix_=matrix_+(r"\\" if (len(matrix)-1)!=row else r"")
            matrix_sol=matrix_sol+r""+str(matrix[row][len(matrix[row])-1])+(r"\\" if (len(matrix)-1)!=row else r"")

        question = r'find the x, y and z in the matrix \begin{bmatrix} '+str(matrix_)+r' \end{bmatrix} = \begin{bmatrix} '+str(matrix_sol)+r' \end{bmatrix}'
        alternatives = coursesFunctionsBll.multipleOptions([x1,y1,z1],3)
        tempAlternatives =[]
        for opt in range(3):
            tempAlternatives.append(r"x="+str(alternatives[opt][0])+r", y="+str(alternatives[opt][1])+r", z="+str(alternatives[opt][2]))
        options =json.loads(json.dumps({'a':tempAlternatives[0], 
                                        'b':tempAlternatives[1], 
                                        'c': tempAlternatives[2], 
                                        'd': "dependent system", 
                                        'e': "inconsistent system"}))
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return [jsonResponse]
    except Exception as er:
        return er

def matrix_k_Problem():
    try:
        #below temp random solutions
        matrix = [[random.randint(1,10) * (random.randint(0,1) * 2 - 1),
                   (random.randint(1,10) * (random.randint(0,1) * 2 - 1))/(random.randint(1,10) * (random.randint(0,1) * 2 - 1)),
                   random.randint(1,10) * (random.randint(0,1) * 2 - 1)],
                  [random.randint(1,10) * (random.randint(0,1) * 2 - 1),
                   random.randint(1,10) * (random.randint(0,1) * 2 - 1),
                   random.randint(1,10) * (random.randint(0,1) * 2 - 1)],
                   [random.randint(1,10) * (random.randint(0,1) * 2 - 1),
                      random.randint(1,10) * (random.randint(0,1) * 2 - 1),
                      random.randint(1,10) * (random.randint(0,1) * 2 - 1)]]
        solution=""
        if ((matrix[1][0]*matrix[2][2])-(matrix[1][2]*matrix[2][0]))==0:
            solution="none"
        else:
            matrix[0][1]= round(((matrix[0][0]*((matrix[1][1]*matrix[2][2])-(matrix[1][2]*matrix[2][1])))+(matrix[0][2]*((matrix[1][0]*matrix[2][1])-(matrix[1][1]*matrix[2][0]))))/((matrix[1][0]*matrix[2][2])-(matrix[1][2]*matrix[2][0])),4)
            solution=r"k="+str(matrix[0][1])
        matrix_=""
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                comp1="k" if (row==0 and col==1) else str(matrix[row][col])
                matrix_=matrix_+r""+comp1+(r" & " if (len(matrix[row])-1)!=col else r"")
            matrix_=matrix_+(r"\\" if (len(matrix)-1)!=row else r"")

        question = r'find the value of k which make the matrix have not only one solution \begin{bmatrix} '+str(matrix_)+r' \end{bmatrix}'
        alternatives = coursesFunctionsBll.multipleOptions([matrix[0][1]],4)
        tempAlternatives =[]
        for opt in range(4):
            tempAlternatives.append(r"k="+str(alternatives[opt][0]))
        options =json.loads(json.dumps({'a':tempAlternatives[0], 
                                        'b':tempAlternatives[1], 
                                        'c': tempAlternatives[2], 
                                        'd': tempAlternatives[3], 
                                        'e': "none"}))
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return [jsonResponse]
    except Exception as er:
        return er

def determinant_Problem():
    try:
        #below temp random solutions
        matrix=[]
        for n in range(4):
            matrix.append([])
            for m in range(4):
                matrix[n].append(random.randint(1,10) * (random.randint(0,1) * 2 - 1))
        det=round(coursesFunctionsBll.findDeterminant4x4(matrix),4)
        solution=r"Det="+str(det)
        matrix_ = coursesFunctionsBll.matrixString(matrix)
        question = r'find the determinant of the matrix '+str(matrix_)+r''
        alternatives = coursesFunctionsBll.multipleOptions([(det if det!=0 else (random.randint(1,10) * (random.randint(0,1) * 2 - 1))/(random.randint(1,10) * (random.randint(0,1) * 2 - 1)))],4)
        tempAlternatives =[]
        for opt in range(4):
            tempAlternatives.append(r"Det="+str(alternatives[opt][0]))
        options =json.loads(json.dumps({'a':tempAlternatives[0], 
                                        'b':tempAlternatives[1], 
                                        'c': tempAlternatives[2], 
                                        'd': tempAlternatives[3], 
                                        'e': r"Det=0"}))
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return [jsonResponse]
    except Exception as er:
        return er

def crammer_Problem():
    try:
        #below temp random solutions
        matrix=[]
        for n in range(3):
            matrix.append([])
            for m in range(4):
                matrix[n].append(random.randint(1,10) * (random.randint(0,1) * 2 - 1))
        det=round(coursesFunctionsBll.findDeterminant(matrix))
        Detz= (matrix[0][0]*((matrix[1][1]*matrix[2][3])-(matrix[1][3]*matrix[2][1])))-(matrix[0][1]*((matrix[1][0]*matrix[2][3])-(matrix[1][3]*matrix[2][0])))+(matrix[0][3]*((matrix[1][0]*matrix[2][1])-(matrix[1][1]*matrix[2][0])))
        solution=r"A=column, B=DETx/DET, C="+str(round(Detz,4))
        fakeDetz = 0 if Detz!=0 else round(random.randint(1,10) * (random.randint(0,1) * 2 - 1)*random.randint(1,10) * (random.randint(0,1) * 2 - 1),4)
        opts =[r"A=row, B=DETx/DET, C="+str(round(Detz,4)),r"A=column, B=DET/DETx, C="+str(round(Detz,4)),r"A=row, B=DET/DETx, C="+str(round(Detz,4)),r"A=row, B=DETx/DET, C="+str(fakeDetz),r"A=column, B=DET/DETx, C="+str(fakeDetz),r"A=row, B=DET/DETx, C="+str(fakeDetz),r"A=column, B=DETx/DET, C="+str(fakeDetz)]
        tempAlternatives=[r"A=column, B=DETx/DET, C="+str(round(Detz,4))]
        for i in range(4):
            rValue = random.randint(0,len(opts)-1)
            tempAlternatives.append(opts[rValue])
            del opts[rValue]
        random.shuffle(tempAlternatives)
        matrixes = coursesFunctionsBll.matrixStringAndSolution(matrix)
        question = r'to find the solution for the matrix (by using the cramer law)\\ '+str(matrixes[0])+r' = '+str(matrixes[1])+r' \\Find the determinant of the quadratic matrix (which we will call DET), then replace the first A \\for the solution column and find the determinant of this new matrix, this will be DETx\\Now repeat the process for the second A, replace it with column solution and find the determinant\\\mbox{which will be DETy. Repeat for last column. Finally we have that x=B, do the same for y and z.}\\Then the value of DETz=C'
        options =json.loads(json.dumps({'a':tempAlternatives[0], 
                                        'b':tempAlternatives[1], 
                                        'c': tempAlternatives[2], 
                                        'd': tempAlternatives[3], 
                                        'e': tempAlternatives[4]}))
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return [jsonResponse]
    except Exception as er:
        return er

def arithmetic_Problem():
    try:
        matrix1=[]
        for n in range(3):
            matrix1.append([])
            for m in range(2):
                matrix1[n].append(random.randint(1,10) * (random.randint(0,1) * 2 - 1))
        matrix2=[]
        for n in range(2):
            matrix2.append([])
            for m in range(3):
                matrix2[n].append(random.randint(1,10) * (random.randint(0,1) * 2 - 1))
        a = random.randint(1,10) * (random.randint(0,1) * 2 - 1)
        b = random.randint(1,10) * (random.randint(0,1) * 2 - 1)
        matrixSolution=[]
        for n in range(3):
            matrixSolution.append([])
            for m in range(3):
                matrixSolution[n].append(round((matrix1[n][0]*a)*(matrix2[0][m]/b) + (matrix1[n][1]*a)*(matrix2[1][m]/b),4))
        numbers = list(range(0, 9))
        listSolutions =[deepcopy(matrixSolution)]
        for x in range(3):
            azar = random.randint(0,len(numbers)-1)
            operation = 2 if random.randint(0,1)==1 else 0.5
            nMatrix = deepcopy(matrixSolution)
            nMatrix[math.floor(numbers[azar]/3)][numbers[azar]%3]=  round(nMatrix[math.floor(numbers[azar]/3)][numbers[azar]%3]*operation,4)
            listSolutions.append(deepcopy(nMatrix))
            del numbers[azar]
        tempAlternatives =[]
        for x in range(4):
            tempAlternatives.append(coursesFunctionsBll.matrixString(listSolutions[x]))
        random.shuffle(tempAlternatives)
        matrixString1 = coursesFunctionsBll.matrixString(matrix1)
        matrixString2 = coursesFunctionsBll.matrixString(matrix2)
        solution = coursesFunctionsBll.matrixString(matrixSolution)
        question = r'for A = '+str(matrixString1)+r' and B = '+str(matrixString2)+r' \\Find (A*'+str(a)+r')*(B/'+str(b)+r')'
        options =json.loads(json.dumps({'a':tempAlternatives[0], 
                                        'b':tempAlternatives[1], 
                                        'c': tempAlternatives[2], 
                                        'd': tempAlternatives[3]}))
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return [jsonResponse]
    except Exception as er:
        return er
#inverse = (1/det)*(trans(cof(A))) where A is the matrix
def inverse_Problem():
    try:
        matrix1=coursesFunctionsBll.randomMatrixGenerator(0, 2,2)
        matrix2=coursesFunctionsBll.randomMatrixGenerator(0, 2,2)
        det = coursesFunctionsBll.findDeterminant2x2(matrix2)
        a = random.randint(0,1)
        b = random.randint(1,10) * (random.randint(0,1) * 2 - 1)
        sol=[]
        solution=""
        if det!=0:
            coMatrix = coursesFunctionsBll.findCofactorMatrix2x2(matrix2)
            adjMatrix = coursesFunctionsBll.findTransposeMatrix(coMatrix)
            inverseMatrix = coursesFunctionsBll.scalarXMatrix(adjMatrix, 1/det)
            sumaMatrix = coursesFunctionsBll.sumMatrix(inverseMatrix, matrix1, 1)
            #newMatrix1 = coursesFunctionsBll.scalarXMatrix(matrix1, a)
            #newMatrix2 = coursesFunctionsBll.scalarXMatrix(inverseMatrix, b)
            sol = coursesFunctionsBll.scalarXMatrix(sumaMatrix, (b if a==0 else 1/b))
            solution = coursesFunctionsBll.matrixString(sol)
        else:
            sol=coursesFunctionsBll.randomMatrixGenerator(1, 2,2)
            solution=r"No Solution"
        numbers = list(range(0, 4))
        listSolutions =[deepcopy(sol)]
        for x in range(2):
            azar = random.randint(0,len(numbers)-1)
            operation = 2 if random.randint(0,1)==1 else 0.5
            nMatrix = deepcopy(sol)
            nMatrix[math.floor(numbers[azar]/2)][numbers[azar]%2]=  round(nMatrix[math.floor(numbers[azar]/2)][numbers[azar]%2]*operation,4)
            listSolutions.append(deepcopy(nMatrix))
            del numbers[azar]
        tempAlternatives =[]
        for x in range(3):
            tempAlternatives.append(coursesFunctionsBll.matrixString(listSolutions[x]))
        random.shuffle(tempAlternatives)
        matrixString1 = coursesFunctionsBll.matrixString(matrix1)
        matrixString2 = coursesFunctionsBll.matrixString(matrix2)
        
        question = r'for A = '+str(matrixString1)+r' and B = '+str(matrixString2)+r' \\Find (A+{B}^{-1})'+('*' if a==0 else '/')+r'('+str(b)+r'):'
        options =json.loads(json.dumps({'a':tempAlternatives[0], 
                                        'b':tempAlternatives[1], 
                                        'c': tempAlternatives[2], 
                                        'd': r"No Solution"}))
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return [jsonResponse]
    except Exception as er:
        return er

#both to practice cofactor matrix and transpose matrix
def cofTrans_Problem():
    try:
        matrix1=coursesFunctionsBll.randomMatrixGenerator(0, 3,3)
        matrix2=coursesFunctionsBll.randomMatrixGenerator(0, 3,3)
        transMatrix = coursesFunctionsBll.findTransposeMatrix(matrix1)
        coMatrix = coursesFunctionsBll.findCofactorMatrix(matrix2)
        sol = coursesFunctionsBll.sumMatrix(transMatrix, coMatrix, -1) #last param, 1 for sum, -1 for substract
        solution = coursesFunctionsBll.matrixString(sol)
        
        numbers = list(range(0, 4))
        listSolutions =[deepcopy(sol)]
        for x in range(3):
            azar = random.randint(0,len(numbers)-1)
            operation = 2 if random.randint(0,1)==1 else 0.5
            nMatrix = deepcopy(sol)
            nMatrix[math.floor(numbers[azar]/2)][numbers[azar]%2]=  round(nMatrix[math.floor(numbers[azar]/2)][numbers[azar]%2]*operation,4)
            listSolutions.append(deepcopy(nMatrix))
            del numbers[azar]
        tempAlternatives =[]
        for x in range(4):
            tempAlternatives.append(coursesFunctionsBll.matrixString(listSolutions[x]))
        random.shuffle(tempAlternatives)
        matrixString1 = coursesFunctionsBll.matrixString(matrix1)
        matrixString2 = coursesFunctionsBll.matrixString(matrix2)
        
        question = r'for A = '+str(matrixString1)+r' and B = '+str(matrixString2)+r' \\Find {A}^{T}-cof(B):'
        options =json.loads(json.dumps({'a':tempAlternatives[0], 
                                        'b':tempAlternatives[1], 
                                        'c': tempAlternatives[2], 
                                        'd': tempAlternatives[3]}))
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return [jsonResponse]
    except Exception as er:
        return er

#both to practice cofactor matrix and transpose matrix
def crossProduct_Problem():
    try:
        matrix=coursesFunctionsBll.randomMatrixGenerator(-1, 2,3)
        area = round((((matrix[0][0]*matrix[1][1])-(matrix[0][1]*matrix[1][0]))**2+((matrix[0][0]*matrix[1][2])-(matrix[0][2]*matrix[1][0]))**2+((matrix[0][1]*matrix[1][2])-(matrix[1][1]*matrix[0][2]))**2)**(0.5),4)
        mag1 = (matrix[0][0]**2+matrix[0][1]**2+matrix[0][2]**2)**(0.5)
        mag2 = (matrix[1][0]**2+matrix[1][1]**2+matrix[1][2]**2)**(0.5)
        angle = round(math.degrees(math.asin(area/(mag1*mag2))),4)
        solution= r"area="+str(area)+r", angle="+str(angle)+r"°"
        question=r"A paralelogram adjacent sides are defined by the origin and the points P=("+str(matrix[0][0])+r","+str(matrix[0][1])+r","+str(matrix[0][2])+r") Q=("+str(matrix[1][0])+r","+str(matrix[1][1])+r","+str(matrix[1][2])+r"). Finds the paralelogram area and the angle (in degrees) between P and Q: "
        alternatives = coursesFunctionsBll.multipleOptions([area, angle],5)
        tempAlternatives =[]
        for y1 in range(5):
            tempAlternatives.append(r"area="+str(alternatives[y1][0])+r", angle="+str(alternatives[y1][1])+r"°")
        options =json.loads(json.dumps({'a':tempAlternatives[0], 
                                        'b':tempAlternatives[1], 
                                        'c': tempAlternatives[2], 
                                        'd': tempAlternatives[3], 
                                        'e': tempAlternatives[4]}))
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return [jsonResponse]
    except Exception as er:
        return er

#both to practice cofactor matrix and transpose matrix
def dotProduct_Problem():
    try:
        matrix=coursesFunctionsBll.randomMatrixGenerator(-1, 2,3)
        mag1 = (matrix[0][0]**2+matrix[0][1]**2+matrix[0][2]**2)**(0.5)
        mag2 = (matrix[1][0]**2+matrix[1][1]**2+matrix[1][2]**2)**(0.5)
        dotProduct = ((matrix[0][0]*matrix[1][0])+(matrix[0][1]*matrix[1][1])+(matrix[0][2]*matrix[1][2]))
        projection=round(dotProduct/mag2,4)
        angle = round(math.degrees(math.acos(dotProduct/(mag1*mag2))),4)
        solution= r"projection="+str(projection)+r", angle="+str(angle)+r"°"
        question=r"Two vectors on a tridimensional space connect the origin and the points A=("+str(matrix[0][0])+r","+str(matrix[0][1])+r","+str(matrix[0][2])+r") B=("+str(matrix[1][0])+r","+str(matrix[1][1])+r","+str(matrix[1][2])+r") respectively. Finds the projection of A over B and the angle between the two vectors: "
        alternatives = coursesFunctionsBll.multipleOptions([projection, angle],5)
        tempAlternatives =[]
        for y1 in range(5):
            tempAlternatives.append(r"projection="+str(alternatives[y1][0])+r", angle="+str(alternatives[y1][1])+r"°")
        options =json.loads(json.dumps({'a':tempAlternatives[0], 
                                        'b':tempAlternatives[1], 
                                        'c': tempAlternatives[2], 
                                        'd': tempAlternatives[3], 
                                        'e': tempAlternatives[4]}))
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return [jsonResponse]
    except Exception as er:
        return er

#adj(A)=(trans(cof(A))) where A is the matrix
def inverseAdj_Problem():
    try:
        matrix1=coursesFunctionsBll.randomMatrixGenerator(0, 3,3)
        matrix2=coursesFunctionsBll.randomMatrixGenerator(0, 3,3)
        det = coursesFunctionsBll.findDeterminant(matrix2)
        a= random.randint(0,2)
        b= random.randint(0,2)
        sol=[]
        solution=""
        if det!=0:
            coMatrix0 = coursesFunctionsBll.findCofactorMatrix(matrix1)
            adjMatrix0 = coursesFunctionsBll.findTransposeMatrix(coMatrix0)
            coMatrix = coursesFunctionsBll.findCofactorMatrix(matrix2)
            adjMatrix = coursesFunctionsBll.findTransposeMatrix(coMatrix)
            inverseMatrix = coursesFunctionsBll.scalarXMatrix(adjMatrix, 1/det)
            sol = round(coursesFunctionsBll.sumMatrix(adjMatrix0, inverseMatrix, 1)[a][b],4)
            solution = str(sol)
        else:
            sol=round(coursesFunctionsBll.randomMatrixGenerator(1, 2,2)[a][b],4)
            solution=r"No Solution"
        matrixString1 = coursesFunctionsBll.matrixString(matrix1)
        matrixString2 = coursesFunctionsBll.matrixString(matrix2)
        question = r'for A = '+str(matrixString1)+r' and B = '+str(matrixString2)+r' \\.If C=adj(A)+{B}^{-1}, find C_{'+str(a)+r''+str(b)+r'}:'

        alternatives = coursesFunctionsBll.multipleOptions([sol],4)
        tempAlternatives =[]
        for y1 in range(4):
            tempAlternatives.append(str(alternatives[y1][0]))
        options =json.loads(json.dumps({'a':tempAlternatives[0], 
                                        'b':tempAlternatives[1], 
                                        'c': tempAlternatives[2], 
                                        'd': tempAlternatives[3], 
                                        'e': r"No Solution"}))
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return [jsonResponse]
    except Exception as er:
        return er

#adj(A)=(trans(cof(A))) where A is the matrix
#https://www.youtube.com/watch?v=AfTAn-Ijswk 
def span_Problem():
    try:
        matrix1=coursesFunctionsBll.randomMatrixGenerator(0, 2,2)
        matrix2=coursesFunctionsBll.randomMatrixGenerator(0, 2,1)
        matrix3=coursesFunctionsBll.randomMatrixGenerator(0, 1,2)
        det = coursesFunctionsBll.findDeterminant2x2(matrix1)
        a= random.randint(0,2)
        b= random.randint(0,2)
        sol=0
        solution=""
        if det!=0:
            coMatrix0 = coursesFunctionsBll.findCofactorMatrix2x2(matrix1)
            adjMatrix0 = coursesFunctionsBll.findTransposeMatrix(coMatrix0)
            inverseMatrix = coursesFunctionsBll.scalarXMatrix(adjMatrix0, 1/det)
            matrixSolution = coursesFunctionsBll.productMatrix(inverseMatrix,matrix2)
            sol = round((matrix3[0][0]*matrixSolution[0][0])+(matrix3[0][1]*matrixSolution[1][0]),4)
            solution = str(sol)
        else:
            sol=round((random.randint(1,10) * (random.randint(0,1) * 2 - 1))/(random.randint(1,10) * (random.randint(0,1) * 2 - 1)),4)
            solution=r"No Solution"
        question = r"For the vector ("+str(matrix2[0][0])+r","+str(matrix2[1][0])+r",k) find which value of k makes this vector part of the span (linear combinations) of vectors ("+str(matrix1[0][0])+r","+str(matrix1[1][0])+r","+str(matrix3[0][0])+r") and ("+str(matrix1[0][1])+r","+str(matrix1[1][1])+r","+str(matrix3[0][1])+r"): "
        alternatives = coursesFunctionsBll.multipleOptions([sol],4)
        tempAlternatives =[]
        for y1 in range(4):
            tempAlternatives.append(str(alternatives[y1][0]))
        options =json.loads(json.dumps({'a':tempAlternatives[0], 
                                        'b':tempAlternatives[1], 
                                        'c': tempAlternatives[2], 
                                        'd': tempAlternatives[3], 
                                        'e': r"No Solution"}))
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return [jsonResponse]
    except Exception as er:
        return er

#adj(A)=(trans(cof(A))) where A is the matrix
def directionCos_Problem():
    try:
        vectors = coursesFunctionsBll.randomMatrixGenerator(-1, 2,3)
        operation = (random.randint(0,1) * 2 - 1)
        vector=[[(vectors[0][0]-vectors[1][0])*operation,(vectors[0][1]-vectors[1][1])*operation,((vectors[0][2]-vectors[1][2])*operation)]]
        hipotenuse = ((vector[0][0]**2)+(vector[0][1]**2)+(vector[0][2]**2))**(1/2)
        xCos = round(vector[0][0]/hipotenuse,4)
        yCos = round(vector[0][1]/hipotenuse,4)
        zCos = round(vector[0][2]/hipotenuse,4)
        solution=r"cos(x)="+str(xCos)+r", cos(y)="+str(yCos)+r", cos(z)="+str(zCos)+r"."
        question = r"\mbox{A is the vector (i, j, k) which connects vectors ("+str(vectors[0][0])+r","+str(vectors[0][1])+r","+str(vectors[0][2])+r") and ("+str(vectors[1][0])+r","+str(vectors[1][1])+r","+str(vectors[1][2])+r") and i="+str((vectors[0][0]-vectors[1][0])*operation)+r".} \\ Lets set vectors A tail in the origin, find its directional cosines (unit vector):"
        alternatives = coursesFunctionsBll.multipleOptions([xCos, yCos, zCos],5)
        tempAlternatives =[]
        for y1 in range(5):
            tempAlternatives.append(r"cos(x)="+str(alternatives[y1][0])+r", cos(y)="+str(alternatives[y1][1])+r", cos(z)="+str(alternatives[y1][2])+r".")
        options =json.loads(json.dumps({'a':tempAlternatives[0],
                                        'b':tempAlternatives[1], 
                                        'c': tempAlternatives[2], 
                                        'd': tempAlternatives[3], 
                                        'e': tempAlternatives[4]}))
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return [jsonResponse]
    except Exception as er:
        return er

#adj(A)=(trans(cof(A))) where A is the matrix
def vectorialEquationProblem():
    try:
        matrix1 = coursesFunctionsBll.randomMatrixGenerator(-1, 3,3)
        matrix2 = coursesFunctionsBll.randomMatrixGenerator(-1, 3,1)
        vectorSolution = coursesFunctionsBll.randomMatrixGenerator(-1, 3,1)
        vectorSolution[0][0]=0
        det = coursesFunctionsBll.findDeterminant(matrix1)
        matrixSolution=[]
        sol=0
        solution=""
        if det!=0:
            coMatrix0 = coursesFunctionsBll.findCofactorMatrix(matrix1)
            adjMatrix0 = coursesFunctionsBll.findTransposeMatrix(coMatrix0)
            inverseMatrix = coursesFunctionsBll.scalarXMatrix(adjMatrix0, 1/det)
            matrixSolution = coursesFunctionsBll.productMatrix(inverseMatrix,vectorSolution)
            solution =r"("+str(round(matrixSolution[0][0],4))+r","+str(round(matrixSolution[1][0],4))+r","+str(round(matrixSolution[2][0],4))+r")+k("+str(matrix2[0][0])+r","+str(matrix2[1][0])+r","+str(matrix2[2][0])+r")"
        else:
            matrixSolution = coursesFunctionsBll.randomMatrixGenerator(1, 3,1)
            solution=r"No unique solution"
        question = r"A line has a directional vector (a_{0},a_{1},a_{2}) and it is perpendicular to the line which directional vector is ("+str(matrix1[0][0])+r","+str(matrix1[0][1])+r","+str(matrix1[0][2])+r")}, both lines pass through the point ("+str(matrix2[0][0])+r","+str(matrix2[1][0])+r","+str(matrix2[2][0])+r") \\\mbox{Besides we know that "+str(matrix1[1][0])+r"a_{0}+"+str(matrix1[1][1])+r"a_{1}+"+str(matrix1[1][2])+r"a_{2}="+str(vectorSolution[1][0])+" and "+str(matrix1[2][0])+r"a_{0}+"+str(matrix1[2][1])+r"a_{1}+"+str(matrix1[2][2])+r"a_{2}="+str(vectorSolution[2][0])+". Express line A as vectorial equation:}"
        alternatives = coursesFunctionsBll.multipleOptions([round(matrixSolution[0][0],4),round(matrixSolution[1][0],4),round(matrixSolution[2][0],4),matrix2[0][0],matrix2[1][0],matrix2[2][0]],4)
        tempAlternatives =[]
        for y1 in range(4):
            tempAlternatives.append(r"("+str(alternatives[y1][0])+r","+str(alternatives[y1][1])+r","+str(alternatives[y1][2])+r")+k("+str(alternatives[y1][3])+r","+str(alternatives[y1][4])+r","+str(alternatives[y1][5])+r")")
        options =json.loads(json.dumps({'a':tempAlternatives[0],
                                        'b':tempAlternatives[1], 
                                        'c': tempAlternatives[2], 
                                        'd': tempAlternatives[3], 
                                        'e': r"No unique solution"}))
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return [jsonResponse]
    except Exception as er:
        return er

#adj(A)=(trans(cof(A))) where A is the matrix
def parametricEquationProblem():
    try:
        matrix1 = coursesFunctionsBll.randomMatrixGenerator(-1, 2,3)
        tx= matrix1[1][0]-matrix1[0][0]
        ty= matrix1[1][1]-matrix1[0][1]
        tz= matrix1[1][2]-matrix1[0][2]
        solution=r"x="+str(matrix1[0][0])+r"+("+str(tx)+"t), y="+str(matrix1[0][1])+r"+("+str(ty)+"t), z="+str(matrix1[0][2])+r"+("+str(tz)+"t)"
        question = r"From below options choose the right one who represents the parametric function which connect to points ("+str(matrix1[0][0])+r","+str(matrix1[0][1])+r","+str(matrix1[0][2])+r") and ("+str(matrix1[1][0])+r","+str(matrix1[1][1])+r","+str(matrix1[1][2])+r")"
        alternatives = coursesFunctionsBll.multipleOptions([tx,ty,tz],5)
        tempAlternatives =[]
        for y1 in range(5):
            tempAlternatives.append(r"x="+str(matrix1[0][0])+r"+("+str(alternatives[y1][0])+"t), y="+str(matrix1[0][1])+r"+("+str(alternatives[y1][1])+"t), z="+str(matrix1[0][2])+r"+("+str(alternatives[y1][2])+"t)")
        options =json.loads(json.dumps({'a':tempAlternatives[0],
                                        'b':tempAlternatives[1], 
                                        'c': tempAlternatives[2], 
                                        'd': tempAlternatives[3], 
                                        'e': tempAlternatives[4]}))
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return [jsonResponse]
    except Exception as er:
        return er

def symmetricEquationProblem():
    try:
        point1 = coursesFunctionsBll.randomMatrixGenerator(-1, 1,3)
        point2 = coursesFunctionsBll.randomMatrixGenerator(-1, 1,3)
        direction1 = coursesFunctionsBll.randomMatrixGenerator(-1, 1,3)
        product = (random.randint(2,10) * (random.randint(0,1) * 2 - 1))/(random.randint(2,10) * (random.randint(0,1) * 2 - 1))
        direction2 = [[]]
        #coursesFunctionsBll.productMatrix(direction1,product)
        directionOptions = []
        for x1 in range(3):
            direction2[0].append(round(direction1[0][x1]*product,4))
        opts = [[0.5,1,1],[1,0.5,1],[1,1,0.5],[2,1,1],[1,2,1],[1,1,2]]
        for y1 in range(4):
            chosen = random.randint(0,len(opts)-1)
            nDirection = [[]]
            for z1 in range(3):
                nDirection[0].append(round(direction2[0][z1]*opts[chosen][z1],4))
            del opts[chosen]
            directionOptions.append(nDirection[0])
        directionOptions.append(direction2[0])
        random.shuffle(directionOptions)
        question ='The line A pass through the point ('+str(point2[0][0])+r','+str(point2[0][1])+r','+str(point2[0][2])+r') and is parallel to the line ('+str(point1[0][0])+r','+str(point1[0][1])+r','+str(point1[0][2])+r') +K('+str(direction1[0][0])+r','+str(direction1[0][1])+r','+str(direction1[0][2])+r'). From below options choose the one which represent line A:'
        tempAlternatives=[]
        solution = r'\frac{x-('+str(point2[0][0])+r')}{'+str(direction2[0][0])+r'} = \frac{y-('+str(point2[0][1])+r')}{'+str(direction2[0][1])+r'} = \frac{z-('+str(point2[0][2])+r')}{'+str(direction2[0][2])+r'}'
        for y1 in range(5):
            tempAlternatives.append(r'\frac{x-('+str(point2[0][0])+r')}{'+str(directionOptions[y1][0])+r'} = \frac{y-('+str(point2[0][1])+r')}{'+str(directionOptions[y1][1])+r'} = \frac{z-('+str(point2[0][2])+r')}{'+str(directionOptions[y1][2])+r'}')
        options =json.loads(json.dumps({'a':tempAlternatives[0],
                                        'b':tempAlternatives[1], 
                                        'c':tempAlternatives[2], 
                                        'd':tempAlternatives[3], 
                                        'e':tempAlternatives[4]}))

        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return [jsonResponse]
    except Exception as er:
        return er

def intersectProblem():
    try:
        point1 = coursesFunctionsBll.randomMatrixGenerator(-1, 2,3)
        point2 = coursesFunctionsBll.randomMatrixGenerator(-1, 2,3)
        matrix=[]
        solution=""
        for i in range(3):
            matrix.append([point1[1][i],(point1[0][i]-point2[0][i]),point2[1][i]])
        if (((matrix[1][1]*matrix[2][2])-(matrix[2][1]*matrix[1][2]))==0):
            solution=r"no solution"
        else:
            matrix[0][0]=round((-(matrix[0][1]*(((matrix[1][0]*matrix[2][2])-(matrix[1][2]*matrix[2][0]))))+(matrix[0][2]*(((matrix[1][0]*matrix[2][1])-(matrix[1][1]*matrix[2][0])))))/(-((matrix[1][1]*matrix[2][2])-(matrix[2][1]*matrix[1][2]))),4)
            solution = str(matrix[0][0])
        question = r"having two lines ("+str(point1[0][0])+r","+str(point1[0][1])+r","+str(point1[0][2])+r")+k(A,"+str(point1[1][1])+r","+str(point1[1][2])+r") and ("+str(point2[0][0])+r","+str(point2[0][1])+r","+str(point2[0][2])+r")+k("+str(point2[1][0])+r","+str(point2[1][1])+r","+str(point2[1][2])+r"), find which value of A makes the lines intersect each other: "
        alternatives = coursesFunctionsBll.multipleOptions([matrix[0][0]],4)
        tempAlternatives =[]
        for y1 in range(4):
            tempAlternatives.append(str(alternatives[y1][0]))
        options =json.loads(json.dumps({'a':tempAlternatives[0],
                                        'b':tempAlternatives[1], 
                                        'c': tempAlternatives[2], 
                                        'd': tempAlternatives[3], 
                                        'e': r"no solution"}))
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return [jsonResponse]
    except Exception as er:
        return er

def planeIntersectProblem():
    try:
        planes = coursesFunctionsBll.randomMatrixGenerator(-1, 2,3)
        pSolution1 = (random.randint(2,10) * (random.randint(0,1) * 2 - 1))
        pSolution2 = (random.randint(2,10) * (random.randint(0,1) * 2 - 1))

        x=round((random.randint(2,10) * (random.randint(0,1) * 2 - 1)),4)
        y=round((random.randint(2,10) * (random.randint(0,1) * 2 - 1)),4)
        z=round((random.randint(2,10) * (random.randint(0,1) * 2 - 1)),4)
        x0=round((random.randint(2,10) * (random.randint(0,1) * 2 - 1))/(random.randint(2,10) * (random.randint(0,1) * 2 - 1)),4)
        y0=round((random.randint(2,10) * (random.randint(0,1) * 2 - 1))/(random.randint(2,10) * (random.randint(0,1) * 2 - 1)),4)
        if (planes[0][0]/planes[1][0])==(planes[0][1]/planes[1][1]) and (planes[0][1]/planes[1][1])==(planes[0][2]/planes[1][2]):
            solution = r'No solution'
        else:
            x = (planes[0][1]*planes[1][2])-(planes[1][1]*planes[0][2])
            y = ((planes[0][0]*planes[1][2])-(planes[1][0]*planes[0][2]))*(-1)
            z = (planes[0][0]*planes[1][1])-(planes[0][1]*planes[1][0])
            
            y0=round(((pSolution1-planes[0][2])/(planes[0][0])-(pSolution2-planes[1][2])/(planes[1][0]))/((planes[0][1]/planes[0][0])-(planes[1][1]/planes[1][0])),4)
            x0= round((pSolution1-planes[0][2]-(planes[0][1]*y0))/(planes[0][0]),4)
            z0=1
            solution = r'\frac{x-('+str(x0)+r')}{'+str(x)+r'}=\frac{y-('+str(y0)+r')}{'+str(y)+r'}=\frac{z-('+str(z0)+r')}{'+str(z)+r'}'
        question = r"Find the symetric equation for the line of planes intersection between "+str(planes[0][0])+r"x+"+str(planes[0][1])+r"y+"+str(planes[0][2])+r"z="+str(pSolution1)+" and "+str(planes[1][0])+r"x+"+str(planes[1][1])+r"y+"+str(planes[1][2])+r"z="+str(pSolution2)+": "
        alternatives = coursesFunctionsBll.multipleOptions([x0, x,y0, y,z],4)
        tempAlternatives =[]
        for y1 in range(4):
            tempAlternatives.append(r'\frac{x-('+str(alternatives[y1][0])+r')}{'+str(alternatives[y1][1])+r'}=\frac{y-('+str(alternatives[y1][2])+r')}{'+str(alternatives[y1][3])+r'}=\frac{z-('+str(z0)+r')}{'+str(alternatives[y1][4])+r'}') 
        options =json.loads(json.dumps({'a':tempAlternatives[0],
                                        'b':tempAlternatives[1], 
                                        'c': tempAlternatives[2], 
                                        'd': tempAlternatives[3], 
                                        'e': r"no solution"}))
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return [jsonResponse]
    except Exception as er:
        return er

def skewProblem():
    try:
        point1 = coursesFunctionsBll.randomMatrixGenerator(-1, 2,3) #first row is the dot, second row is the directional vector
        point2 = coursesFunctionsBll.randomMatrixGenerator(-1, 2,3)
        editPoint2 = random.randint(0,2)
        if(editPoint2==0): #parallel
            multiply = random.randint(1,10)*(random.randint(0,1)*2-1)
            point2[1]=[point1[1][0]*multiply,point1[1][1]*multiply,point1[1][2]*multiply]
            rotate = random.randint(0,1)
            if rotate==1:
                temp=point1[1].copy()
                point1[1]=point2[1]
                point2[1]=temp
        elif(editPoint2==1):
            multiply = random.randint(1,10)*(random.randint(0,1)*2-1)
            point2[0]=[point1[0][0]+(point1[1][0]*multiply),point1[0][1]+(point1[1][1]*multiply),point1[0][2]+(point1[1][2]*multiply)]

        matrix=[]
        solution=r"skew"
        if (point1[1][0]/point2[1][0])==(point1[1][1]/point2[1][1]) and (point1[1][1]/point2[1][1])==(point1[1][2]/point2[1][2]):
            solution=r"parallel"
        else:
            for i in range(3):
                matrix.append([point1[1][i],(point1[0][i]-point2[0][i]),-1*point2[1][i]])
            det = coursesFunctionsBll.findDeterminant(matrix)
            if det==0:
                solution=r"intersect"
        question = r"having two lines ("+str(point1[0][0])+r","+str(point1[0][1])+r","+str(point1[0][2])+r")+k("+str(point1[1][0])+r","+str(point1[1][1])+r","+str(point1[1][2])+r") and ("+str(point2[0][0])+r","+str(point2[0][1])+r","+str(point2[0][2])+r")+k("+str(point2[1][0])+r","+str(point2[1][1])+r","+str(point2[1][2])+r"), define if the line are parallels, they intersect or skew: "
        
        options =json.loads(json.dumps({'a':r"parallel",
                                        'b':r"intersect", 
                                        'c': r"skew"}))
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return [jsonResponse]
    except Exception as er:
        return er
#https://www.youtube.com/watch?v=0qYJfKG-3l8  how to find plane that contains three points
def twoLinesProblem():
    try:
        point1 = coursesFunctionsBll.randomMatrixGenerator(-1, 2,3) #first row is the dot, second row is the directional vector
        point2 = coursesFunctionsBll.randomMatrixGenerator(-1, 2,3)
        editPoint2 = random.randint(0,1)
        if(editPoint2==0): #parallel
            multiply = random.randint(1,10)*(random.randint(0,1)*2-1)
            point2[1]=[point1[1][0]*multiply,point1[1][1]*multiply,point1[1][2]*multiply]
            rotate = random.randint(0,1)
            if rotate==1:
                temp=point1[1].copy()
                point1[1]=point2[1]
                point2[1]=temp
        else:
            multiply = random.randint(1,10)*(random.randint(0,1)*2-1)
            point2[0]=[point1[0][0]+(point1[1][0]*multiply),point1[0][1]+(point1[1][1]*multiply),point1[0][2]+(point1[1][2]*multiply)]
        dots = [[point1[0][0],point1[0][1],point1[0][2]],
                [point2[0][0],point2[0][1],point2[0][2]],
                [point2[0][0]+point2[1][0],point2[0][1]+point2[1][1],point2[0][2]+point2[1][2]]]
        director1 = [dots[0][0]-dots[1][0],dots[0][1]-dots[1][1],dots[0][2]-dots[1][2]]
        director2 = [dots[0][0]-dots[2][0],dots[0][1]-dots[2][1],dots[0][2]-dots[2][2]]
        x = (director1[1]*director2[2])-(director1[2]*director2[1])
        y = -1*((director1[0]*director2[2])-(director1[2]*director2[0]))
        z = (director1[0]*director2[1])-(director1[1]*director2[0])
        if x==0 and y==0 and z==0:
            solution=r"No solution"
            x = random.randint(1,10)*(random.randint(0,1)*2-1)
            y = random.randint(1,10)*(random.randint(0,1)*2-1)
            z = random.randint(1,10)*(random.randint(0,1)*2-1)
            d = (x*dots[0][0])+(y*dots[0][1])+(z*dots[0][2])
        else:
            d = (x*dots[0][0])+(y*dots[0][1])+(z*dots[0][2])
            solution = r"("+str(x)+r"x)+("+str(y)+r"y)+("+str(z)+r"z)="+str(d)+r":"
        
        solution = r"("+str(x)+r"x)+("+str(y)+r"y)+("+str(z)+r"z)="+str(d)+r":"
        question = r"Find the plane that contains the lines ("+str(point1[0][0])+r","+str(point1[0][1])+r","+str(point1[0][2])+r")+k("+str(point1[1][0])+r","+str(point1[1][1])+r","+str(point1[1][2])+r") and ("+str(point2[0][0])+r","+str(point2[0][1])+r","+str(point2[0][2])+r")+k("+str(point2[1][0])+r","+str(point2[1][1])+r","+str(point2[1][2])+r"): "
        alternatives = coursesFunctionsBll.multipleOptions([x,y,z,d],4)
        tempAlternatives =[]
        for y1 in range(4):
            tempAlternatives.append(r"("+str(alternatives[y1][0])+r"x)+("+str(alternatives[y1][1])+r"y)+("+str(alternatives[y1][2])+r"z)="+str(alternatives[y1][3])+r":") 
        options =json.loads(json.dumps({'a':tempAlternatives[0],
                                        'b':tempAlternatives[1], 
                                        'c': tempAlternatives[2], 
                                        'd': tempAlternatives[3], 
                                        'e': r"No solution"}))
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return [jsonResponse]
    except Exception as er:
        return er

def threeDotsProblem():
    try:
        dots = coursesFunctionsBll.randomMatrixGenerator(-1, 3,3)
        solution=r""
        det = coursesFunctionsBll.findDeterminant(dots)
        if (det==0):
            solution=r"No solution"
        else:
            director1 = [dots[0][0]-dots[1][0],dots[0][1]-dots[1][1],dots[0][2]-dots[1][2]]
            director2 = [dots[0][0]-dots[2][0],dots[0][1]-dots[2][1],dots[0][2]-dots[2][2]]
            x = (director1[1]*director2[2])-(director1[2]*director2[1])
            y = -1*((director1[0]*director2[2])-(director1[2]*director2[0]))
            z = (director1[0]*director2[1])-(director1[1]*director2[0])
            d = (x*dots[0][0])+(y*dots[0][1])+(z*dots[0][2])
            if x*y*z*d==0: #if some of those 4 values is 0 the solution will no work, becuase of solution generator
                return threeDotsProblem()
            solution = r"("+str(x)+r"x)+("+str(y)+r"y)+("+str(z)+r"z)="+str(d)+r""
        question = r"Find the plane that contains the points ("+str(dots[0][0])+r","+str(dots[0][1])+r","+str(dots[0][2])+r"), ("+str(dots[1][0])+r","+str(dots[1][1])+r","+str(dots[1][2])+r") and ("+str(dots[2][0])+r","+str(dots[2][1])+r","+str(dots[2][2])+r")"
        alternatives = coursesFunctionsBll.multipleOptions([x,y,z,d],4)
        tempAlternatives =[]
        for y1 in range(4):
            tempAlternatives.append(r"("+str(alternatives[y1][0])+r"x)+("+str(alternatives[y1][1])+r"y)+("+str(alternatives[y1][2])+r"z)="+str(alternatives[y1][3])+r"") 
        options =json.loads(json.dumps({'a':tempAlternatives[0],
                                        'b':tempAlternatives[1], 
                                        'c': tempAlternatives[2], 
                                        'd': tempAlternatives[3], 
                                        'e': r"No solution"}))
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return [jsonResponse]
    except Exception as er:
        return er


def normalVectorProblem():
    try:
        dots = coursesFunctionsBll.randomMatrixGenerator(-1, 3,3)
        director1 = [dots[0][0]-dots[1][0],dots[0][1]-dots[1][1],dots[0][2]-dots[1][2]]
        director2 = [dots[0][0]-dots[2][0],dots[0][1]-dots[2][1],dots[0][2]-dots[2][2]]
        det = coursesFunctionsBll.findDeterminant(dots)
        solution=r""
        if (det==0):
            solution=r"No solution"
        else:
            x = (director1[1]*director2[2])-(director1[2]*director2[1])
            y = -1*((director1[0]*director2[2])-(director1[2]*director2[0]))
            z = (director1[0]*director2[1])-(director1[1]*director2[0])
            solution = r"("+str(x)+r","+str(y)+r","+str(z)+r")"
        
        question = r"Find the normal vector to the plane that contains the line ("+str(dots[0][0])+r","+str(dots[0][1])+r","+str(dots[0][2])+r") + k("+str(director1[0])+r","+str(director1[1])+r","+str(director1[2])+r")  and pass through the point ("+str(dots[2][0])+r","+str(dots[2][1])+r","+str(dots[2][2])+r")"
        alternatives = coursesFunctionsBll.multipleOptions([x,y,z],4)
        tempAlternatives =[]
        for y1 in range(4):
            tempAlternatives.append(r"("+str(alternatives[y1][0])+r","+str(alternatives[y1][1])+r","+str(alternatives[y1][2])+r")") 
        options =json.loads(json.dumps({'a':tempAlternatives[0],
                                        'b':tempAlternatives[1], 
                                        'c': tempAlternatives[2], 
                                        'd': tempAlternatives[3], 
                                        'e': r"No solution"}))
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return [jsonResponse]
    except Exception as er:
        return er

def parallelepipedProblem():
    try:
        dots = coursesFunctionsBll.randomMatrixGenerator(-1, 3,3)
        superDots=[]
        #below loop to find if the three points and the origin can be in the same plane, if thats the case the problem has no solution (or solution is 0)
        for i in range(4):
            superDots.append([])
            for j in range(4):
                if i==0 or j==3:
                    superDots[i].append(0)
                else:
                    superDots[i].append(dots[i-1][j])

        det = coursesFunctionsBll.findDeterminant4x4(superDots)
        solution=r""
        sol=0
        if det==0:
            solution=r"No solution"
            sol = random.randint(2,100)
        else:
            x= (dots[0][1]*dots[1][2])-(dots[0][2]*dots[1][1])
            y= -1*((dots[0][0]*dots[1][2])-(dots[0][2]*dots[1][0]))
            z= (dots[0][0]*dots[1][1])-(dots[0][1]*dots[1][0])
            sol = round(abs((dots[2][0]*x)+(dots[2][1]*y)+(dots[2][2]*z)),4)
            solution=r""+str(sol)
        question = r"Find the volume of the parallelepiped defined by the origin and the vectors ("+str(dots[0][0])+r","+str(dots[0][1])+r","+str(dots[0][2])+r"), ("+str(dots[1][0])+r","+str(dots[1][1])+r","+str(dots[1][2])+r") and ("+str(dots[2][0])+r","+str(dots[2][1])+r","+str(dots[2][2])+r"): "
        alternatives = coursesFunctionsBll.multipleOptions([sol],4)
        tempAlternatives =[]
        for y1 in range(4):
            tempAlternatives.append(r""+str(alternatives[y1][0])) 
        options =json.loads(json.dumps({'a':tempAlternatives[0],
                                        'b':tempAlternatives[1], 
                                        'c': tempAlternatives[2], 
                                        'd': tempAlternatives[3], 
                                        'e': r"No solution"}))
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return [jsonResponse]
    except Exception as er:
        return er

#link of matrix algebra laws: https://stattrek.com/matrix-algebra/matrix-theorems.aspx?Tutorial=matrix
def matrixLawsProblem():
    try:
        exercises = [['A+B','B+A','(A+B)A^{-1}'],
                     ['A + B + C ','A + ( B + C ) = ( A + B ) + C','(A + B + C)^{T}'],
                     ['ABC','A( BC ) = ( AB )C','CAB = BCA'],
                     ['A( B + C )','AB + AC','BA + CA'],
                     ['x( A + B )','xA + xB','xAB = xBA'],
                     ['( A^{T} )^{T}','A','A^{T}'],
                     ['( A + B )^{T}','A^{T} + B^{T}','( A + B )^{-1}'],
                     ['( AB )^{T}','B^{T}A^{T}','A^{T}B^{T}'],
                     ['( ABC )^{T}','C^{T}B^{T}A^{T}','A^{T}B^{T}C^{T}'],
                     ['AI','IA = A','A^{-1}'],
                      ['AA^{-1}','A^{-1}A = I','A^{-1}A = A'],
                     ['(A^{-1})^{-1}','A','I'],
                     ['( AB )^{-1} ','B^{-1}A^{-1}','A^{-1}B^{-1}'],
                     ['( ABC )^{-1} ','C^{-1}B^{-1}A^{-1}','A^{-1}B^{-1}C^{-1}'],
                     ['( A^{T} )^{-1}','( A^{-1} )^{T}','A']
                     ]
        a = random.randint(0,14)
        b = random.randint(0,14)
        while a==b:
            b = random.randint(0,14)
        solution=r""+str(exercises[a][0])+r"="+str(exercises[a][1])+r", "+str(exercises[b][0])+r"="+str(exercises[b][1])
        tempAlternatives = [solution,
                        r""+str(exercises[a][0])+r"="+str(exercises[a][2])+r", "+str(exercises[b][0])+r"="+str(exercises[b][1]),
                        r""+str(exercises[a][0])+r"="+str(exercises[a][1])+r", "+str(exercises[b][0])+r"="+str(exercises[b][2]),
                        r""+str(exercises[a][0])+r"="+str(exercises[a][2])+r", "+str(exercises[b][0])+r"="+str(exercises[b][2])]
        random.shuffle(tempAlternatives)
        question = r"Find the right pair of matrices algebra laws from the options below: "
        options =json.loads(json.dumps({'a':tempAlternatives[0],
                                        'b':tempAlternatives[1], 
                                        'c': tempAlternatives[2], 
                                        'd': tempAlternatives[3]}))
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return [jsonResponse]
    except Exception as er:
        return er

def matrixApplicationProblem():
    try:
        matrix1 = coursesFunctionsBll.randomMatrixGenerator(0, 2,3)
        strings1 = ["","jeans","shirts","shoes","store A","store B"]
        matrix2 = coursesFunctionsBll.randomMatrixGenerator(0, 3,2)
        strings2 = ["","Bogota","Medellin","jeans","shirts","shoes"]
        stringMatrix1 = coursesFunctionsBll.matrixStringRowColumnTitles(strings1, matrix1)
        stringMatrix2 = coursesFunctionsBll.matrixStringRowColumnTitles(strings2, matrix2)
        solMatrix = coursesFunctionsBll.productMatrix(matrix1, matrix2)
        strings3 = ["","Bogota","Medellin","store A","store B"]
        alternatives = coursesFunctionsBll.multipleOptions([solMatrix[0][0],solMatrix[0][1],solMatrix[1][0],solMatrix[1][1]],5)
        solution=coursesFunctionsBll.matrixStringRowColumnTitles(strings3,solMatrix)
        question = r" the next matrix show the average number of clothings sells for A and B stores during the last months: "+stringMatrix1+r" and the next show the average price of the clothes, sells by this two stores, per city: "+stringMatrix2+r" from the options below choose which matrix represent the average sells, of each store, by city"
        alternatives = coursesFunctionsBll.multipleOptions([solMatrix[0][0],solMatrix[0][1],solMatrix[1][0],solMatrix[1][1]],5)
        tempAlternatives =[]
        for y1 in range(5):
            tempAlternatives.append(coursesFunctionsBll.matrixStringRowColumnTitles(strings3, [[alternatives[y1][0],alternatives[y1][1]],[alternatives[y1][2],alternatives[y1][3]]])) 
        options =json.loads(json.dumps({'a':tempAlternatives[0],
                                        'b':tempAlternatives[1], 
                                        'c': tempAlternatives[2], 
                                        'd': tempAlternatives[3], 
                                        'e': tempAlternatives[4]}))
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return [jsonResponse]
    except Exception as er:
        return er

exam1 = [matrixProblem, matrix_k_Problem, determinant_Problem, crammer_Problem, arithmetic_Problem, inverse_Problem, cofTrans_Problem, crossProduct_Problem, dotProduct_Problem, inverseAdj_Problem, span_Problem, directionCos_Problem]
exam2 = [vectorialEquationProblem, parametricEquationProblem, symmetricEquationProblem, intersectProblem, planeIntersectProblem, skewProblem, twoLinesProblem, threeDotsProblem, normalVectorProblem, parallelepipedProblem, matrixLawsProblem, matrixApplicationProblem]
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

#integrate ((25-x^2)^(1/2))/(x)