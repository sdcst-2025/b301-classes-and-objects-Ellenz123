import os

class quadratic:

    def showInstructions(self):
        os.system("clear||cls")
        print("- Quadratic Equation Calculator - ")
        print("You will enter a quadratic in standard form")
        print("          ax² + bx + c")
        print("I will ask you for the coefficients")
        print("I will then tell you several things about the quadratic")
        print("I hope you are ready, this poop is about to get real!\n")

    def getCoeffs(self):
        vars = ['a','b','c']
        for i in range(3):
            while True:
                try:
                    coeff = int(input(f"Enter coefficient {vars[i]} >"))
                    vars[i] = coeff 
                    break
                except:
                    print("invalid! It must be an integer. Try again")
        self.a, self.b, self.c=vars[0],vars[1],vars[2]   
        return self.a, self.b, self.c

    def getVertex(self):
        x = -(self.b)/(2*self.a)
        y = self.a*x**2 + self.b*x + self.c
        return (x,y)

    def getVertexForm(self,vertex):
        x = vertex[0]
        y = vertex[1]
        if x < 0:
            bracket = f"(x + {-1*x})"
        else:
            bracket = f"(x - {x})"
        if y < 0:
            constant = f"- {-1*y}"
        else:
            constant = f" + {y}"
        return f"{self.a}{bracket}² {constant}"

    def getYInt(self):
        return self.c

    def getDiscriminant(self):
        return self.b**2 - 4*self.a*self.c

    def getXInt(self):
        disc = self.getDiscriminant()
        roots = []
        if disc >= 0:
            r1 = round((-(self.b) + disc**(0.5))/(2*self.a),3)
            r2 = round((-(self.b) - disc**(0.5))/(2*self.a),3)
            roots.append(r1)
            roots.append(r2)
        else:
            roots.append('non real')
            roots.append('non real')
        return roots

    def __init__(self):
        self.a=None
        self.b=None
        self.c=None
        #show instructions
        self.showInstructions()
        #ask user for coefficients
        self.getCoeffs()
        vertex = self.getVertex()
        print(vertex)
        vertexForm = self.getVertexForm(vertex)
        print(vertexForm)
        yint = self.getYInt()
        print(yint)
        xint = self.getXInt()
        print(xint)
        #determine vertex form of parabola
        #determine directino of opening
        #determine y-intercept
        #determine x-intercepts (if they exist)

game=quadratic()