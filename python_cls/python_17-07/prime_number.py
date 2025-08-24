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
           
           
def count_vowel(str):
      count = 0
      vowel = "aeiou"
      for char in  str:
            if char in vowel:  
                  count+=1
      print(count)
str1 = input("Enter the string:").lower()
count_vowel(str1)

def list1():
      l1 = input("Enter the numbers")
      sum = 0
      for i in l1.split():
            sum += int(i)
      print(sum)
list1()
             
def palindrome(s):
      s = s.lower()
      if s == s[::-1]:
            print("Palindrome")
      else:
            print("Not a Palindrome")
str1 = input("Enter the string:")
palindrome(str1)
      
def list_even():
      l1 = [1,2,3,4,68,1,0]
      for i in l1:
            if i%2 == 0:
                  print("even" ,i)         
list_even()

def any(*b):
      avg1 = ( ) //2
      print(avg1)    