str ="123"
num = int(str)
print(str)
print(type(num))

a= 10
b =3
print("before swapping:",a,b)
temp=a
a=b
b=temp
print(a,b)

a=10.3456
print(round(a,2))

a = input("Enter string1:")
b = input("Enter string2:")
print(a+b)

str = "Python"
print(str[0],str[-1])


str1= input("Enter the str1:")
sub_str =input("Enter the substring:")
if sub_str in str1:
    print("Substring is present")

str = "Rupa"  
print(str.lower())
print(str.upper())

l1 = [3,4,5,8,78,9,0]
print(l1.remove(l1[2]))


lst = [1, 2,"t"]
print(lst*2) 