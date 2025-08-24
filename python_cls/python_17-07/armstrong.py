# Armstrong Number
def check_Armstrong():
     num1 = int(input("Enter the number:"))
     original_num = num1
     no_of_digits = len(str(original_num))
     sum = 0
     while num1 > 0:
          rem = num1 % 10
          sum += rem ** no_of_digits 
          num1 = num1 // 10
     print(sum)
     if sum == original_num:
         print("Armstrong Number")
     else:
         print("Not an Armstrong number")
check_Armstrong()


input1 = int(input("Enter the start range:"))
input2 = int(input("Enter the end range:"))
for num in range(input1 , input2 + 1):
        no_of_digits = len(str(num))
        sum = 0
        num1 = num
        while num1 > 0:
             rem = num1 % 10
             sum += rem ** no_of_digits 
             num1 = num1 // 10     
        if sum == num:  
             print(num)
       