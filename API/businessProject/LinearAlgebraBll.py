
import random
import math
import coursesFunctionsBll
from fractions import Fraction
from flask import jsonify
import json
from sympy import *
from copy import copy, deepcopy


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
        return jsonResponse
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
        return jsonResponse
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
        return jsonResponse
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
        return jsonResponse
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
        return jsonResponse
    except Exception as er:
        return er
#inverse = (1/det)*(trans(cof(A))) where A is the matrix
def inverse_Problem():
    try:
        matrix1=coursesFunctionsBll.randomMatrixGenerator(0, 2,2)
        matrix2=coursesFunctionsBll.randomMatrixGenerator(0, 2,2)
        det = coursesFunctionsBll.findDeterminant2x2(matrix2)
        a = random.randint(1,10) * (random.randint(0,1) * 2 - 1)
        b = random.randint(1,10) * (random.randint(0,1) * 2 - 1)
        sol=[]
        solution=""
        if det!=0:
            coMatrix = coursesFunctionsBll.findCofactorMatrix2x2(matrix2)
            adjMatrix = coursesFunctionsBll.findTransposeMatrix(coMatrix)
            inverseMatrix = coursesFunctionsBll.scalarXMatrix(adjMatrix, 1/det)
            newMatrix1 = coursesFunctionsBll.scalarXMatrix(matrix1, a)
            newMatrix2 = coursesFunctionsBll.scalarXMatrix(inverseMatrix, b)
            sol = coursesFunctionsBll.sumMatrix(newMatrix1, newMatrix2, 1)
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
        
        question = r'for A = '+str(matrixString1)+r' and B = '+str(matrixString2)+r' \\Find (A*'+str(a)+r')+({B}^{-1}*'+str(b)+r')'
        options =json.loads(json.dumps({'a':tempAlternatives[0], 
                                        'b':tempAlternatives[1], 
                                        'c': tempAlternatives[2], 
                                        'd': r"No Solution"}))
        jsonResponse = json.dumps({"question":coursesFunctionsBll.replaceSpace(question), "solution":coursesFunctionsBll.replaceSpace(solution), "options":coursesFunctionsBll.replaceOptions(options)})
        return jsonResponse
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
        return jsonResponse
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
        return jsonResponse
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
        return jsonResponse
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
        
        #numbers = list(range(0, 4))
        #listSolutions =[deepcopy(sol)]
        #for x in range(2):
        #    azar = random.randint(0,len(numbers)-1)
        #    operation = 2 if random.randint(0,1)==1 else 0.5
        #    nMatrix = deepcopy(sol)
        #    nMatrix[math.floor(numbers[azar]/3)][numbers[azar]%3]=  round(nMatrix[math.floor(numbers[azar]/3)][numbers[azar]%3]*operation,4)
        #    listSolutions.append(deepcopy(nMatrix))
        #    del numbers[azar]
        #tempAlternatives =[]
        #for x in range(3):
        #    tempAlternatives.append(coursesFunctionsBll.matrixString(listSolutions[x]))
        #random.shuffle(tempAlternatives)
        matrixString1 = coursesFunctionsBll.matrixString(matrix1)
        matrixString2 = coursesFunctionsBll.matrixString(matrix2)
        question = r'for A = '+str(matrixString1)+r' and B = '+str(matrixString2)+r' \\.If C=adj(A)+{B}^{-1}, find C'+str(a)+r''+str(b)+r':'

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
        return jsonResponse
    except Exception as er:
        return er

exam1 = [matrixProblem, matrix_k_Problem, determinant_Problem, crammer_Problem, arithmetic_Problem, inverse_Problem, cofTrans_Problem, crossProduct_Problem, dotProduct_Problem, inverseAdj_Problem]
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

#integrate ((25-x^2)^(1/2))/(x)