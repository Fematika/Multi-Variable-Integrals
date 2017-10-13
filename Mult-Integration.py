import numpy as np
import math

deltaX = 0.005

class Func:
    def __init__(self, function, number_of_variables):
        self.func = function
        self.n = number_of_variables
        
    def partial_derivative(self, i, x):
        h = []
        
        for j in range(0, self.n):
            if j == i:
                h.append(deltaX)
            
            else:
                h.append(0)
                
        h = np.array(h)
        print(h)
        
        deltaFunc = self.func(x + h) - self.func(x)
        print(deltaFunc)
        
        return deltaFunc / deltaX
    
    def integral(self, box):
        a = box[self.n - 1][0]
        b = box[self.n - 1][1]
        
        if self.n == 1:
            sum = 0
            
            for j in range(0, math.floor((b - a) / deltaX)):
                sum += deltaX * self.func(a + j * deltaX)
            
            return sum
        
        else:
            def new(y):
                sum = 0
                
                for j in range(0, math.floor((b - a) / deltaX)):
                    z = np.append(y, np.array([a + j * deltaX]))
                    sum += deltaX * self.func(z)
                
                return sum
            
            g = Func(new, self.n - 1)
            new_box = np.delete(box, 1, 0)
            
            return g.integral(new_box)

def f(x):
    return x[0] * x[1] * x[2]

func = Func(f, 3)

box = [[0, 1], [0, 1], [0, 1]]
print(func.integral(box))