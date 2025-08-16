def check_prime(num1):
     if num1<=1:
           return False
          
     for i in range(2, num1 // 2 + 1):
            if num1 %i==0:
               return False
     return  True

ip1 = int(input("Enter the number:"))
ip2 = int(input("Enter the number:"))

for i in range(ip1,ip2 + 1):
     if check_prime(i):
           print(i)
          