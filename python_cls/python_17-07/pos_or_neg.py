# positive or Negative
num = int(input("Enter the number:"))
if num>0:
    print(f"{num} is positive")
elif num==0:
    print(f"{num} is zero")
else:
    print(f"{num} is negative")
    
# even or odd
n = int(input("Enter the number:"))
if n%2==0:
    print(f"{n} is even")
else:
    print(f"{n} is odd")
    
#leap year

year = int(input("Enter the year:"))
if year%4==0:
    if year%100==0:
        if year%400==0:
           print(f"{year} is leap year")
        else:
            print("not a leap year")
    else:
        print(" it is a leap year")
else:
    print("Not a leap year")
    
# greatest of two numbers

num1 = float(input("Enter the number:"))
num2 = float(input("Enter the number:"))
if num1>num2:
    print(f"{num1} is greater")
    
else:
    print(f"{num2} is greater")
    
# vote eligibility    
age = int(input("Enter the age:"))
if age>=18:
    print(f"{age} is eligible to vote")
else:
    print(f"{age} is not eligible")
    
# Grade checker
marks = float(input("Enter the marks:"))
if marks>=90:
    print("Grade A")
elif marks>=75:
    print("Grade B")
elif marks>=60:
    print("Grade C")
elif marks>=40:
    print("Grade D")
else:
    print("Fail")

# Number Type Checker

number= int(input("Enter the number:"))
if number>0:
    if number%2==0:
        print("number is even")
    else:
        print("number is odd")
elif number<0:
    print("number is negative")
else:
    print("number is zero")   

#simple Calculator 

num1 =int(input("Enter the number1:"))
num2 =int(input("Enter the number2:"))
symbol =input("Enter the symbol:")
if symbol== '+':
    print(num1+num2)
elif symbol=='-':
    print(num1-num2)
elif symbol=='*':
    print(num1*num2)
elif symbol =='/':
    if num2!=0:
        print(num1/num2)
    else:
        print("divisible by zero is not possible")
else:
    print("Invalid")        