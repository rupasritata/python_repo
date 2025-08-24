def array_num():
    a1 = [20,30,40,50,60,10,70]
    a1.sort(reverse=True)                   
    print(a1)
    for i in a1:
        if a1[1] == i:
            print("second largest num is :",i)
array_num()
 
 
#   captial 

def captoFront(s):
    capitals = ""
    smalls = ""
    for i in s:
        if i.isupper():
           capitals+=i
    for i in s:
        if i.islower():
            smalls+=i
    return capitals +smalls
print(captoFront("HApPy"))
print(captoFront("moveMENT"))
print(captoFront("shOrtCAKE"))

