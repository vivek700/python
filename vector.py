class vector:
    
    def __init__(self,vec):
        self.vec = vec

    def __str__(self):
        s = ""
        j = 0
        for i in self .vec:
            s += f" {i}a{j} +"
            j +=1
        return s[:-1]

    def __add__(self,v2):
        n = []        
        for i in range(len(self.vec)):
            n.append(self.vec[i]+v2.vec[i])
        return vector(n)
    
    def __mul__(self,v2):
        s= 0   
        for i in range(len(self.vec)):
            s += (self.vec[i]*v2.vec[i])
        return s

v = vector([1,2,3])
v2 = vector([2,4,5]) 
print(v+v2)
print(v*v2)
# print(v)       