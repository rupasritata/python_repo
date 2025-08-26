
# String inbuilt func:
# To get char to ascii - ord(char) 
# to change ascii to char -chr(ascii value)

str = "Hello"
print(ord("e"))
print(chr(101))


# Case convertion builtin methods only works for Alphabets.
# upper() : to convert the lowercase to upper case
# lower() : to convert the uppercase to lowercase 

str1 = "Programming"
print(str1.lower())
print(str1.upper())

# islower() : To check whether lower or not
# isupper() :  To check whether upper or not

s = "flower"
print(s.islower())
print(s.isupper())

# swapcase() : converts the chars from if they are small then it converts into upper and viceversa.
# len() : To find the lengthe of the string
# count() : To count the number of occurances of a subsrting in the given string
# index() : I t returns the lowest index of the substiring if found in the given string. if not found it raises a value error

s1 = 'Good MoRniNg'
print(s1.swapcase())
print(len(s1))
print(s1.count('o'))
print(s1.index('M'))


# title() : It is used to Capitalize the first letter in the each word 
# capitalize : only converts the first char in the word .

s2 = "this is the title method"
print(s2.title())
print(s2.capitalize())

# strip() :  to remove the excess spaces in the start and end .  we need to reassigned the value again for its operations
# lstrip() : To remove the excess space in the starting
# rstrip() : To remove the excess space in the Ending

s = " hi Hello  "
s.lstrip()
s.rstrip()
s = s.strip()
print(s)

# Replace("old" , "new") : to replace old val to new value

S1 = "The captial of AP is kadapa"
s1 = S1.replace("kadapa" , "Amaravathi")
print(S1)

# string -find,split,join,startswith,endswith
# find : it returns the lowest index of the substring if it is found in given string. if not found then returns -1

str1 = "Good Morning"
print(str1.find("Good"))

# startswith :  it returns true if the string starts with the specified value otherwise false

print(str1.startswith("Goo"))
print(str1.startswith("morn"))

# endswith : it returns true if the string ends with the specified values otherwise false

print(str1.endswith("ing"))
print(str1.endswith("mor"))

# split : it splits the string at the specified separator and returns a list

input_nums = input("Enter all the numbers in csv format:")
for i in input_nums.split(","):
    print(i)
    # num1,num2 = input("Enter two numbers in csv format:").split()


# map()
# The map() function applies a given function to every item in an iterable (like a list), returning a map object (which can be converted to a list).
# Great for transforming, converting, or processing lists without a loop.

a = [1, 2, 3]
b = [4, 5, 6]
products = list(map(lambda x, y: x * y, a, b))
print(products)                  

numbers = ['1', '2', '3', '4']
ints = list(map(int, numbers))   # Convert strings to integers
print(ints)          

# join : it joins the elements of an iterable to the end of the string ,we can use any delimeter to seperate the list elements into strings

list1 = ["1",'2','3','hi']
encoded_str = ','.join(list1)
print(encoded_str)

# set methods:
# add(element)remove(element),discard(element),pop(),clear(),union(other_set),intersection(other_set),difference(other_set),symmetric_difference(other_set)
# isdisjooint(other_set),issuperset(other_set)

set1 = {10,20,30,40,50}
print(set1.add(60))
print(set1.remove(30))
print(set1.discard(70))
print(set1.pop())
print(set1.clear())

set2 = {5,6,7,89,90,10}
print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))
print(set1.symmetric_difference(set2))

s3 = {1,2,3,4,5}
print(s3.isdisjoint(set2))
print(s3.issuperset(set2))



