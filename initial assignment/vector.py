class Vector:
    def __init__(self, numbers):
        self.numbers = numbers
    
    def __str__(self):
        return  ','.join(map(str,self.numbers))
    
    def __add__(self,others):
        results=[]
        for a, b in zip(self.numbers, others.numbers):
                results.append(a+b)
        return Vector(results)
        
    def dotProduct(self,other):
         mul=[]
         for x,y in zip(self.numbers,other.numbers):
              mul.append(x*y)
         return sum(mul)
    
    @staticmethod
    def scalarVector(vector,scalar):
        x1 = []
        for item in vector:
            x1.append(item * scalar)
        return x1
        

vec1= Vector([1,2,3])
vec2=Vector([4,5,6])
print("Addition of 2 vectors:",vec1+vec2)
print("Dot Product of 2 vectors:",vec1.dotProduct(vec2))
print("Vector and Scalar Multiplication:",Vector.scalarVector([3,4,5],6))
