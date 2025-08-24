for i in range(5):
     if i == 3:
         continue
     print(i)
# num1=55
# num1+=5
# print(num1)
# num1-=5
# print(num1)
# num1*=5
# print(num1)
# num1/=5
# print(num1)
# num1//=5
# print(num1)
# num1%=5
# print(num1)
# print('abs'>'b')

# print(3 in range(0,6,2))
# tup1 =(1,2,3,4,5)
# print(1 in tup1)    

# print(-2 or 3)
# print(3 or '')
# print("" or [])
# print('Truth' or 'Dare')

# print(13 << 22)

# str1 = 'Good'
# str2 = "bad"
# str3 ="Good"
# print(id(str1))
# print(id(str2))
# print(id(str3))

# n = int(input("Enter the number n:"))
# if (n>=40 and n%7==0):
#     print(f'{n} power is {n**2}')


    
# age1 =int(input("Enter the age1:"))
# age2 =int(input("Enter the age2:"))
# age3 =int(input("Enter the age3:"))
# if age1>=age2 and age1>=age3:
#     print(f"this age1  {age1} is greater")
# elif (age2>=age1 and age2>=age3):
#     print(f"this age2  {age2} greater")
# else:     
#     print(f"this age1  {age3} greater")

# n = int(input("enter the number 1 to 4:"))
# a=int(input("Enter the a:"))
# b=int(input("Enter the b:"))
# if n==1:
#     print(a+b)
# elif n==2:
#     print(a-b)
# elif n==3:
#     print(a*b)
# elif n==4:
#     print(a/b)
# else:
#     print("number is not there")
    
  
    
# num = int(input("Enter the num:"))
# if num%2==0:
#     print(f"{num} is even")
# else :
#     print(f"{num} is odd")
    

# # num = int(input("Enter the num:"))    
# # if num > 0:
# #     print(f"{num} is positive")
# # else:
# #     if num ==0:
# #         print("Zero")
# #     else:
# #         if num==-1:
# #             print("-1")
# #         else:
# #             print(f"{num} is negative")

# # num1 =int(input("Enter the number1:"))
# # num2 =int(input("Enter the number2:"))
# # symbol =input("Enter the symbol:")
# # if symbol== '+':
# #     print(num1+num2)
# # elif symbol =='/':
# #     if num2!=0:
# #         print(num1/num2)
# #     else:
# #         print("divisible by zero is not possible")
# # elif symbol =='%':
# #     if num2!=0:
# #         print(num1%num2)
# #     else:
# #         print("divisible by zero is not possible")

# # str = 'Ambica'
# # print(str[1:5:2])

# # write the code in a manner like from least possible to highest possible
# units = int(input("Enter the units:"))
# if units>=300:
#     print(units*4)
# else:
#     if units>=200:
#         print(units*3)
#     else:
#         if units>=100:
#             print(units*2)
            
#         else:
#             print(0)

# year = int(input("Enter the year:"))
# if year%4==0 and year%100!=0 or year%400==0:
#     print(f"{year} is leap year")
# else:
#     print(f"{year} not a leap year")


# for i in range(0,11):
#     print (i)
    
# for i in list(range(2,20,2)):
#     print(i)
    
# for i in range(0,11):
#     if i%2==0 :
#         print(i,"even")
#     else:
#         print(i,"odd")
# dict1 ={"ram":20,'raj':25,"hello":7}
# for i in dict1:
#     print(dict1)
    
# n=100
# for i in range(1,n):
#     if i>=40 and i<=49:
#         print (i)
#     elif(i>=70 and i<=79):
#         print(i)
# print("end the loop")
# n=int (input("Enter the num:"))
# for i in range(1,n):
#     print (17, "X " ,i ,"=",17*i)

#  n = int(input("Enter the number:"))
# i=0
# while i<=n:
#     print(i)
#     i=i+1

# n=int (input("Enter the num:"))
# i=1
# while i<=n:
#     print (17, "X " ,i ,"=",17*i) 
#     i =i+1
    
# l1=["a","e","i","o","u"]
# str1 =input("Enter any character:")
# if str1 in l1:
#     print(str1,"Vowel")
# else:
#     print(str1,"Consonant")
   
# a = float(input("Enter the a value:"))
# b =  float(input("Enter the b value:"))
# c = float(input("Enter the c value:"))
# if (a+b>c and b+c>a) and a+c>b:
#     print("Triangle is Valid")
# else:
#     print(" Triangle is Invalid")

# #all numbers from 1 to 100

# for i in range(1,100):
#     print(i)
    
#     # Print the sum of n natural numbers
# n = int(input("enter the number:"))
# sum=n*(n+1)//2
# # print(sum)

# #    # using for loop
# # n = int(input("enter the number:"))
# # sum=0
# # for i in range (1,n+1):
# #     sum+=i
# # print(sum)
 
# #  #print all the even numbers from 1 to 50 using while loop

# # i=1
# # while i<=50:
# #     if i%2==0:
# #         print(i)
# #     i+=1    

# #Write a program to display the multiplication table of a given
# #number. First 20

# # n = int(input("Enter the number:"))
# # for i in range(1,21):
# #    print(n,"X",i,"=",n*i)
    
#  #  Reverse a number using a while loop.
# #1. Also can we get the sum of all the digits. 

# # num = 0
# # while num>=0:  
# #     num = int(input("Enter the number:"))
# # print("loop ended")   

# #  password attempts
# # correct_password = 12345678
# # for attempt in range(1,4):
# #     entered_password = int(input("Enter the password:"))
# #     if entered_password == correct_password:
# #         print("login successfully")
# #         break
# #     else:
# #         print("Wrong Password",3-attempt)
# #         print("Attempt Failed")       
     

# # s = {"raj": 10,"ram":50 ,"ravi":23}
# # for i in s.items():
# #     print(i)
    
# str1 = "hello"
# count=0
# for i in str1[::-1]:
#     count+=1
#     # print(count)
# print(count)
 
# str = "Hello world"
# count = 0
# for i in str:
#     if i in ['a','e','i','o','u']:
#         count+=1
#         print(i)
# print(count)

# e_count=0
# o_count=0
# l1 = [1,2,6,4,8,66,7,9,3,55,77,99]
# for i in l1:
#     if i%2==0:
#         e_count+=1
#     else:
#         o_count+=1
# print("odd numbers count:",o_count)
# print("even numbers count:",e_count)    


# str1 = input("Enter the chars:")
# for i in str1:
#     if  "A"<=i<="Z":
#         res=ord(str1)+1
#         print(chr(res))    
#     else:
#         print(" It is Already in  lowercase")

# # s = "pYTHon"
# # count = 0 
# # for i in s:
# #     if "a"<=i<="z":
# #        count+=1
# #        print("lowercase:",chr(ord(i)))
   
# s = "pYTHon"
# count = 0 
# for i in s:
#     if "A"<=i<="Z":
#         count+=1
# print("count of chars",count)   

# # Factorial

def fact(num):
     factorial=1
     for i in range(1,num+1):
         factorial = factorial*i
     print("Fact of num :",factorial)
fact(3)

# num = int(input("Enter the num:"))
# factorial=1
# for i in range(1,num+1):
#     factorial = factorial*i
# print("Fact of num :",factorial)


# num = int(input("Enter the num:"))
# i=1
# factorial =1
# while i<=num:
#     factorial = factorial*i
#     i=i+1
# print("Fact of num :",factorial)

    
# special_char = input("Enter the char:")
# for i in special_char:
#     if  0<=ord(i)<=47 or 58<=ord(i)<=64 or 91<=ord(i)<=96 or 123<=ord(i)<=127:
#         print(i)

# i=97
# for i in range(i,122):
#     print(chr(i),end=" ")
   


# str = input("Enter the string:")
# count =0
# for i in str:
#     count+=1
# print(count)

# str = input("Enter the string:")
# count =0
# i = 1
# while i<=len(str) :
#     count+=1
#     i+=1
# print(count)

# num = int(input("Enter the num:"))
# sum=0
# for i in range(0,num+1):
#     sum+=i
# print(sum)

# num = int(input("Enter the num:"))
    
# # nested loops 
# count=0
# for i in range(1,11):
#      print(f'class {i} ')
#      for j in range(1,31):
#         if i%3==0 and  j%7==0:
#              print(f'class {i} roll {j}')
 

# for i in range(1,13):
#     print(f'table {i}')
#     for j in range(1,21):
#         print(i ,"X",j,"=",i*j)


# class_no = 1
# while class_no<=11: 
#      print("class no:" ,class_no)
#      roll_no= 1
#      while roll_no<=30:
#           print("roll no:",roll_no)
#           roll_no+=1
# #      class_no+=1

# # jump stmts
   
# for i in range(1,25):
#      print(i)
#      if i ==8:
#           continue    
#      print(i)
#      print(i)
     
for class_no in range(1,11):
     for roll_no in range(1,31):
          if roll_no ==5:
               break
          print(class_no,roll_no)
          
     
# for class_no in range(1,11):
#      for roll_no in range(1,31):
#           if class_no>5 or roll_no<16:
#                break
#           print(class_no,roll_no)     
          
          
# char = input("Enter the single char:").lower()
# if len(char) > 1 or len(char)==0:
#     print("Invalid input")
# else:
#     if char in 'a,e,i,o,u':
#         print("Vowels")
#     elif char.isalpha():
#         print("Consonants")
#     elif char.isnumeric():
#         print("Number")
#     else:
#         print("special chracters")
        
# Reverse a number using a while loop.
# 1. Also can we get the sum of all the digits.   
# num =(int(input("Enter the number:")))
# sum =0 
# reversed_num = 0
# while num>0:
#     digit = num%10
#     reversed_num = reversed_num*10 + digit
#     print(reversed_num)
#     num//=10
#     sum +=digit
# print(sum)


num = int(input("Enter the num:"))
count = 0
if num ==0:
    count=1
while num>=0 :
    num//=10
    count+=1
print(count)

        
# def calc_volume():
#     print("Claculating the volumeof sphere")       
#     print(4/3 *3.14*(10**3)) 
#     print("sphere volume")
# calc_volume()



# def simple_calculator(a,b):
#     if b != 0 :
#           print(a%b)
#           print(a/b)
#           print(a//b)
#     else:
#         print(" not divisible by Zero ")
#     print("sum:",a+b)
#     print("substraction:",a-b)
#     print("mult:",a*b)
       
# simple_calculator(10,20)
# simple_calculator(12,8)
# simple_calculator(15,5)
# simple_calculator(10,0)

# def table_of(n):
#     for i in range(1,10):
#        print(n ,"X",i,"=",n*i)
# table_of(15)
# table_of(10)


# def natural_numbers(n):
#     sum =0 
#     for i in range(1,n+1):
#         sum += i
#     print(sum)
    
# natural_numbers(3)
# natural_numbers(10)

# def check_product(n):
#     product=1 
#     for i in range(1,n+1):
#         product *= i
#     print("procuct:",product)
# check_product(5)
# check_product(15)

# def greater(a,b,c):
#     if a>b and a>c:
#         print("a is greater")
#     elif b>c and b>a:
# #         print(b, " is greater")
# #     else:
# #         print("c is greater")
# # greater(10,20,19)
# # greater(11,20,29)


# def name(a,b):
#    print( a+b)
#    print(a-b)
# name(5,10)

# def name(a,b=1):
#    print( a+b)
#    print(a-b)
# name(a=10)

# def name(a,b):
#    print( a+b)
#    print(a-b)
# name(a=2,b=3)
    
# def add(a,c,*b):
#     print(a+sum(b))
#     print(b)
# add(5)   
# add(5,6,7)
# add(5,6,7,8)   

# def numbers(num):
#     if num%2==0:
#         return "Even"
#     else:
#         return 'odd'
# r1 = numbers(22)
# print(r1)
# print(numbers(21))


# def number(n):
#     if n>0:
#         return 'Positive'
#     elif n<0:
#         return 'Negative'
#     else:
#         return 'Zero'
# res1 = print(number(23))
# res2 = print(number(-23))
# res3 = print(number(0))


# def eligible_to_vote(age):
#     return 'Eligible to vote' if age>=18  else  "Not eligible to Vote"         
# age = int(input("Enter the age:"))
# print(eligible_to_vote(age))

# def greatest_number(a,b):
#     return "a is Greater" if a>b else  "both are equal" if a==b  else 'b is greater' 
# a =int(input("Enter the number1:"))
# b =int(input("Enter the number2:"))

# print(greatest_number(a,b))

# def simple_calculator(num1,num2,op):
#      print(num1+num2)  if op in ['+',"add"] else print(num1 - num2) if op == '-' or op =='sub' else  print(num1 * num2) if  op == '*' or op=='mul' else print(num1/num2) if num2 >0  else print('Not Divisible by Zero') if op=='/' or op == 'Div'  else print('Invalid number')
# num1 = int(input("Enter the num1:"))   
# num2 = int(input("Enter the num2:"))
# op = (input("Enter the op:")).lower()
# simple_calculator(num1,num2,op)

# def greatest_of_numbers(num1,num2,num3):
#      if num1>num2 and num1>num3:
#           print(num1,"is greater")
#      elif num1==num2==num3:
#           print("All are same")
#      elif num1==num2 and num3>num1:
#           print(num3,"is greater")
#      elif num2>num3 and num2>num1:
#           print(num2,"is greater")
#      else:
#           print(num3 ,"is greater")
# num1 = int(input("Enter the num1:"))
# num2 = int(input("Enter the num2:"))
# num3 = int(input("Enter the num3:"))
# greatest_of_numbers(num1,num2,num3)

# def leap_year_or_not(year):
#      return 'Invalid Year' if year<0 else print(year," Leap year") if (year%400==0) or (year%100!=0 and year%4==0) else print(year,"Not a leap Year")
# year = int(input("Enter the Year:"))
# leap_year_or_not(year)

# def vowel_or_not(char):
#      if char in 'aeiou':
#           print ("Vowel")
#      elif char.isnumeric():
#           print("neither")
#      else:
#           print("Consonant")  
# char = input("Enter the char:").lower()  
# vowel_or_not(char)


# def student_grade(marks):
#      return "Fail"  if marks<70 else  "Grade C" if 70<=marks<=79 else "Grade B" if 80<=marks<=89 else "Grade A"
# marks = int (input("Enter the students Marks:"))
# print(student_grade(marks))   



# def check_valid_trianle(side1,side2,side3):
#      if (side1 + side2 > side3 ) and (side2+side3>side1) and(side3 +side1>side2):
#           if side1==side2==side3:
#               print("Equilateral Triangle")
#           elif side1!=side2 and side2!=side3:
#                print("Scelene Triangle")
#           else:
#                print("Isosceles Triangle") 
#           print("Triangle is Valid")            
#      else:
#           print("Triangle is invalid")
# side1 = float(input("Enter the side1 Len:"))
# side2 = float(input("Enter the side2 Len:"))
# side3 = float(input("Enter the side3 Len:"))
# check_valid_trianle(side1,side2,side3)


# def check_right_angle_triangle(s1,s2,s3):
#      if s3**2 == (s1)**2 +(s2)**2:
#           print("Right angled triangle")
#      else:
#           print("Not Right Angled")

# s1 = float(input("Enter the side1 Len:"))
# s2 = float(input("Enter the side2 Len:"))
# s3 = float(input("Enter the side3 Len:"))
# check_right_angle_triangle(s1,s2,s3)
          

# def even_numbers(n=50):
#      i = 1
#      while i<=50:
#          if i%2==0:
#               print(i,"Even")
#          i+=1
# even_numbers()

# start = 2
# while start <=50:
#      print(start)
#      start+=2
     


# while True:
#      user_input = int(input("Enter the number:"))
#      if user_input<=0:
#           print("negative number")
#           break
#      else:
#           print(user_input)
     
     
# ip_num = float(input("Enter the Positive number:"))
# if ip_num<=0:
#      print("Entered negative number")
# while ip_num>0:
#      ip_num = float(input("Enter the Positive number:"))
#      if ip_num<=0:
#           print("Entered negative number")
          

# num1 = 3456
# count = 0
# sum = 0
# while num1>0:
#      rem = num1%10
#      print(rem)
#      num1 = num1//10
#      print(num1)
#      count+=1
#      sum+=rem

# print("count:",count)
# print("sum",sum)


# method - 1 to find prime number
# num1 = int(input("Enter the number:"))
# count = 0 
# for i in range(1,num1+1):
#      if num1 % i == 0:
#           count+=1
# print(count)
# if count == 2:
#      print("prime number")
# else:
#      print("Not a Prime number")
     
     
#  method 2 
# num1 = int(input("Enter the number:"))
# Flag = True
# for i in range(2,num1):
#      if num1%i==0:
#           Flag = False
#           print("Not a prime")
#           break

# if Flag == True:
#      print("Prime number")


# def check_prime(num1):
#      if num1<=1:
#           return 'Not a prime'
     
#      for i in range(2, num1 // 2 + 1):
#           if num1%i==0:
#                return 'Not a Prime'
#      return 'Prime'
# num1 = int(input("Enter the number:"))
# print(check_prime((num1)))

# # method 4 for printing the Prime number


# def check_prime(num1):
#      if num1<=1:
#           return 'Not a prime'
     
#      for i in range(2, int(num1**0.5 )+ 1):
#           if num1%i==0:
#                return 'Not a Prime'
#      return 'Prime'
# num1 = int(input("Enter the number:"))
# print(check_prime((num1)))


# ## Factorial

# num1  = int(input("Enter the number:"))
# factorial = 1 
# i = 1
# while  i <= num1:
#      factorial = factorial * i
#      i+=1
# print(factorial)
     
# # For loop divisible by 3 and 5
# n= 100
# for i in range(1,n):
#      if i%3==0 and i%5==0:
#           print("Divisible by 3 and 5",i)
          
          
# # choose to: 
# # 1.  Find the square of a number. 
# # 2.  Find the cube of a number. 
# # 3.  Exit.

# while True:
#      print("1. square 2.cube 3. add 4.sub 5.mult 6.div 7.exit ")
#      input_op = (input("Enter the op:")).lower()
#      if input_op == '1'or input_op == 'square':
#           input_num = float(input("Enter the number to square:"))
#           print(input_num**2)
          
#      elif input_op == '2'or input_op == 'cube':
#           input_num = float(input("Enter the number to cube:"))
#           print(input_num ** 3)
          
          
#      elif input_op == '3' or input_op == 'add':
#           input_num1 = float(input("Enter the num1:"))
#           input_num2 = float(input("Enter the num2:"))
#           print(input_num1 + input_num2)
          
#      elif input_op == '4' or input_op == 'sub':
#           input_num1 = float(input("Enter the num1:"))
#           input_num2 = float(input("Enter the num2:"))
#           print(input_num1 - input_num2)
     
#      elif input_op == '5' or input_op == 'mult':
#           input_num1 = float(input("Enter the num1:"))
#           input_num2 = float(input("Enter the num2:"))
#           print(input_num1 * input_num2)
     
#      elif input_op == '6' or input_op == 'Div':
#           input_num1 = float(input("Enter the num1:"))
#           input_num2 = float(input("Enter the num2:"))
#           if input_num2<=0:
#                print("Not divisible by zero")
#           else:
#                print(input_num1/input_num2)
     
#      elif input_op == '7' or input_op == 'Exit':
#           print("exit")
#           break
          
    
# def check_prime(num1):
#      if num1<=1:
#            return False
          
#      for i in range(2, num1 // 2 + 1):
#             if num1 %i==0:
#                return False
#      return  True

# ip1 = int(input("Enter the number:"))
# ip2 = int(input("Enter the number:"))

# for i in range(ip1,ip2 + 1):
#      if check_prime(i):
#            print(i)
          
# Fibnocci series

# n = int(input("Enter the num:"))
# num1 = 0
# num2 = 1
# for i in range(0,n):
#      print(num1)
#      new_num = num1 + num2
#      num1 = num2
#      num2 = new_num     
     
# Armstrong
# def check_Armstong(num1):
#      num1 = int(input("Enter the number:"))
#      original_num = num1
#      no_of_digits = len(str(original_num))
#      sum = 0
#      while num1 > 0:
#           rem = num1 % 10
#           sum += rem ** no_of_digits 
#           num1 = num1 // 10
#      print(sum)
#      ip1 = int(input("Enter the number:"))
#      ip2 = int(input("Enter the number:"))


# Global scope

# # num1 = 10
# # print(num1)

# # if 3>2:
# #      print(num1)
     
# # for i in range(1,4):
# #      print(num1)
     
#      # loacal variable is covering the global variable then it is called as global shadowing.
# # Local scope

# # def func():
# #      num2 = "Hello"
# #      print(num2)
# # func()

# # Enclosed scope
# # # globals function
# # num1 = 10
# # def preference():
# #      num1 = 20
# #      globals()['num1'] = 50
# #      print(num1)
# # preference()
# # print(num1)
# # from functools import reduce
# # print(reduce(lambda x,y: x if x>y else y ,[1,2,5,7,11,-10]))

# def check_even(X):
#      if X%2==0:
#        return True
#      return False  
# print(check_even(7)) 

# # Inbuilt methods
# # Adding the elements 
# #List :  using append() we can only add the element to the end of the list1
# # and also we can  concatinate by ading a list to another list and also append will only take one argument ,we cannot add the numbers by using indexing

# list1 = [1,2,3,4,5,6]
# list1.append(12)
# print(list1)

# # Extend() can overcome the shortcoming of append()
# list1.extend([71,22,73,74])
# print(list1)

# # insert(index,element)
# list1.insert(0,9)
# print(list1)

# # Removing the elements
# # clear():clears everything in the list

# list1.clear()
# print(list1)

# # pop():we can give the index to the pop() so that we can remove that element and without giving indexing the last value in the list will pop out

# list1 = [1,2,2,2,3,4,5,[5,7]]
# elem = list1.pop(4)
# print(elem)

# # remove(elem):only one occurance will be removed if the element has occured many times in the list . using the count and for loop we remove the all freq elements in the list.

# freq = list1.count(2)
# for i in range(freq):
#      list1.remove(2)
# print(list1)

# list2 = [1,2,3,4]
# list2.remove(3)
# print(list2)

# # searching the elements

# # Index : 
# list1 = [1,2,2,2,3,4,5,[5,7]]
# print(list1.index(2,1,4))

# # Reverse()
# list1.reverse()
# print(list1)

# # sort () : sorts all the elements from ascending order by default ,if wee write reverse = True it can reverse the list from descending order.
# list3 = [7,8,3,5,10,12,14]
# list3.sort()
# print(list3)

# l1= [1,2,3,4,2,2]
# count = 0
# for i in l1:
#      if  i == 2:
#         count+=1
# print(count)


# copy():to copy anything initially

# l = [1,2,3,4,2,2]
# b = l.copy()
# print(l,b)

# Drawbacks
# if we do not use copy() then the list will change along with the original list.

# Tuple: Immutable order with heterogenous elements.
# Index same as usage in the tuple
# we cannot use the sort()  in tuple because it is immutable .
# Tuple Inbuilt Func: Index() ,Count(), len()

# tuple1 = (1,2,3,4)
# tuple1.index(2)
# print(tuple1)
# print(tuple1.count(2))
# print(len(tuple1))





















