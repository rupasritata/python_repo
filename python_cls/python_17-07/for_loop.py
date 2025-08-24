#1.WAP take a list add the that number
numbers_input = input("Enter numbers separated by spaces or commas: ")
numbers = [int(num) for num in numbers_input.split()]
total_sum = 0
for num in numbers:
    total_sum += num
print("Sum of the numbers is:", total_sum)

# 2.WAP take a list find even number
l1=[1,2,6,44,78,99,23,4,56,11]
for i in l1:
    if i%2==0:
        print(i ,"even")

#3. WAP PRINT COUNT THE EVEN ODD NUMBERS 1 TO 10
even_count = 0  
odd_count = 0  
for i in range(1,11):
    if i%2==0:
        even_count+=1
        
    else:
        odd_count+=1
print(odd_count)
print(even_count)    

 #4.SUM OF DIGITS OF A NUMBER EXAMPLE 12322 OUTPUT=10

num =int(input("Enter the number:"))
digits_sum=0
while num>0:
     digit = num%10
     digits_sum+=digit
     num//=10
print(digits_sum)

# 5.PRODUCT OF DIGITS OF A NUMBER EXAMPLE 123 OUTPUT=6
num =int(input("Enter the number:"))
digits_product = 1
while num>0:
      digit = num%10
      digits_product*=digit
      num//=10
print(digits_product)
      

