class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, v):
        # Addition with another vector.
        
        return Vector(self.x + v.x, self.y + v.y)
    def __mul__(self, v):
        # Multiplication with a vector.
            
        return Vector(self.x * v.x,self.y * v.y)
    def __rmul__(self, s):
        # Multiplication with a scalar.
        return Vector(self.x * s, self.y * s)
    #def __str__(self):
        #return '  '.join(map(str,self.x,self.y))
    def __repr__(self):
       return '<Vector (%f, %f)>' % (self.x, self.y )
a = Vector(3, 5)
b = Vector(2, 7)
print(a+b)
print(a*b)
print(6*a)