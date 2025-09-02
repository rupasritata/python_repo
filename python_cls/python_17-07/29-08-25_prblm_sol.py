# Product of all elements in a matrix
list1 = [[1,2,3],[5,6,7],[10,12,8]]
product = 1
for i in list1:
    for j in i:
        product *= j
print(product) 

# Find even digits in a number. 
num1 = int(input("Enter the number:"))
num1_str = str(num1)
for i in num1_str:
    if int(i) % 2 == 0:
        print(i)
        
# Find prime digits in a number.

num = int(input("Enter the number:"))
num_str = str(num)
primes = ['2','3','5','7']
for i in num_str:
    if i in primes:
        print(i)
          