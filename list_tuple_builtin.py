

# Inbuilt methods
# Adding the elements 
#List :  using append() we can only add the element to the end of the list1
# and also we can  concatinate by ading a list to another list and also append will only take one argument ,we cannot add the numbers by using indexing

list1 = [1,2,3,4,5,6]
list1.append(12)
print(list1)

# Extend() can overcome the shortcoming of append()
list1.extend([71,22,73,74])
print(list1)

# insert(index,element)
list1.insert(0,9)
print(list1)

# # Removing the elements
# # clear():clears everything in the list

list1.clear()
print(list1)

# pop():we can give the index to the pop() so that we can remove that element and without giving indexing the last value in the list will pop out

list1 = [1,2,2,2,3,4,5,[5,7]]
elem = list1.pop(4)
print(elem)

# remove(elem):only one occurance will be removed if the element has occured many times in the list . using the count and for loop we remove the all freq elements in the list.

freq = list1.count(2)
for i in range(freq):
     list1.remove(2)
print(list1)

list2 = [1,2,3,4]
list2.remove(3)
print(list2)

# searching the elements

# Index : 
list1 = [1,2,2,2,3,4,5,[5,7]]
print(list1.index(2,1,4))

# Reverse()
list1.reverse()
print(list1)

# # sort () : sorts all the elements from ascending order by default ,if wee write reverse = True it can reverse the list from descending order.

list3 = ['ball','bat','apple']
list3.sort(key = len)
print(list3)

list1 = [1,4,3,2,'apple' ,'egg','ball']
list1.sort()
print(list1)

l1 = [[1,2,3],[0.3,1,2,4],[-4,3,2,-1]]
l1.sort(key = lambda x : x[0])
print(l1)


l1 = [[1,2,3],[0.3,1,2,4],[1,3,2,-1]]
l1.sort(key = lambda x : (x[0],x[2]))
print(l1)

#  copy(): 
#  shallow copy :
l1= [1,2,3,4,2,2]
count = 0
for i in l1:
     if  i == 2:
        count+=1
print(count)


# copy():to copy anything initially

l = [1,2,3,4,2,2]
b = l.copy()
print(l,b)

# shallow copy and deepcopy:

list1 = [1,2,3,[4,5]]
list2 = list1.copy()
list2[3][1] = 13
print(list1)
print(list2)

# deepcopy:

import copy
list1 = [1,2,3,[4,5]]
list3  = copy.deepcopy(list1)
list1[3][1] = 12
print(list1)
print(list3)

# Drawbacks
# if we do not use copy() then the list will change along with the original list.

# Tuple: Immutable order with heterogenous elements.
# Index same as usage in the tuple
# we cannot use the sort()  in tuple because it is immutable .
# Tuple Inbuilt Func: Index() ,Count(), len()

tuple1 = (1,2,3,4)
tuple1.index(2)
print(tuple1)
print(tuple1.count(2))
print(len(tuple1))


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
print(s3.issubset(set2))


s1 = {1,2,3}
s2 = {1,2,3}
print(s1.issubset(s2))
print(s2.issubset(s1))
print(s1.issuperset(s2))
print(s2.issuperset(s1))
