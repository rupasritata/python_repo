class calculator:
    def add(self,a,b):
        print(a+b)
    
    def sub(self,a,b):
        print(a-b)
        
    def mul(self,a,b):
        print(a * b )
        
    def div(self,a,b):
        if b !=0:
            print(a/b)
        else:
            print("Zero division error")
    
    def mod(self,a,b):
        if b!=0:
            print(a % b)
        else:
            print("Zero division error")
        
        
clc1 = calculator()
clc2 = calculator()

clc1.model_num = 1
clc1.made_in  = 'India'
clc2. color = 'black'
clc2.discount = '10%'

print("clc1 add:", clc1.add(2, 7))
print("clc2 sub:", clc2.sub(60, 5))
print("clc1 mult:", clc1.mul(11, 5))
print("clc2 div:", clc2.div(16, 2))
print("clc1 Mod:", clc1.mod(22 , 5))

print("model_num:", getattr(clc1, 'model_num', 'N/A'))
print("made_in:", getattr(clc1, 'made_in', 'N/A'))
print("color:", getattr(clc1,'color', 'N/A'))
print("discount:", getattr(clc1, 'discount', 'N/A'))

print("model_num:", getattr(clc2, 'model_num', 'N/A'))
print("made_in:", getattr(clc2, 'made_in', 'N/A'))
print("color:", getattr(clc2, 'color', 'N/A'))
print("discount:", getattr(clc2, 'discount', 'N/A'))

# self :

# In Python, self is a reference to the current instance of a class. It is used within class methods to access or modify the object’s own attributes and methods.
# Not a keyword: self is just a naming convention. You can technically use another name, but using self is standard and makes code readable and consistent.
# First parameter: In any instance method of a class, self must be the first parameter, so Python knows you're working with the current object's data.
# Purpose: It allows each object of a class to keep its own data and interact with its own attributes and methods separately from other objects.
# Usage: When you create an object, self inside class methods refers to that specific object—so each object can store/track its own values.
