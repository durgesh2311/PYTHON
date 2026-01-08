#1.create a set containing five different country name and print it

set1 = {'USA','india','japan','finland','france'}
print(set1)

#2.create a set with duplicate number and print it to see how duplicate are handled

set2 = {10,10,20,30,70,80,40,30,50}
print(set2)

#3.use a set() constructur to create a set from fruit a list of fruit

fruits = ['apple','banana','cherry','mango']
fruits = set(fruits)
print(fruits)

#4. add a new element innto an exiting set using add() method.

fruits.add('orange')
fruits.add('banana')
print(fruits)

# 5.add multiple element into a set using update() method

fruits.update(['pineapple','grapes'])
print(fruits)

#6.try adding a duplicate elements to the set and check if changes

fruits.add('apple')
fruits.add('cherry')
print(fruits)

#7.remove an element from a set  using remove() method.
fruits.remove('apple')
fruits.remove('banana')
print(fruits)

#8.remove an safely using discard without raising an error.
fruits.discard('pear')
print(fruits)

#9.remove a random element using pop() and print both removed and remaining elements.

popped_iteam = fruits.pop()
print(fruits)
print(popped_iteam)

#10.clear all element from a set using clear() and print it.
fruits.clear()
print(fruits)

#11.create two set of number and perform union operation.
num1 = {1,2,3,4,5}
num2 = {3,4,5,6,7}

print("union of the two set is:", num1 | num2)

#12.perform intersection between two sets to find comman elements from the first set
print("intersection of the two set is:", num1 & num2)

#13.perform difference between two set to find unique element from the first set.
print("difference of the two set is:", num1 - num2)

#14.perform symmentric differnce between two set and print the result.
print("symentric differnce of the two set is:", num1 ^ num2)

#15.check if one set is a subset of another using issubset() method.
num3 = {1,2,3,4}
num4 = {1,2,3,4,5,6,7}
print(num3.issubset(num4))

#16.check if one set is a subset of another using issuperset() method.
print(num4.issuperset(num3))

#17.check if two set have no comman element using disjoint() method.
print(num3.isdisjoint(num4))

#18.use in keyword to check if a particular element exits in a set.
fruits = ['apple','banana','cherry','mango']
print("'apple' is present in the set:", 'apple' in fruits )

#19.use not in keyword to check if an element does not exiest in a set.
print('banana' not in fruits)

#20.find the total number of element in a set using len()
var = len(fruits)
print("the lenght of the fruits:",var)

#21.find the maximum and minimum element from a numeric set using max() and min()
data = {44,32,21,34,23,55}
print(min(data))
print(max(data))

#22.find the sum of  element from numeric set using sum().
print("the sum of the element is :", sum(data))

#23.convert a set into a sorted list in ascending order using sorted().
var1 = {23,11,23,45,12,34,67,56}
sorted_data = sorted(var1)
print(sorted_data)

#24.sort a set in descending order using sorted() with reserve=true
number = {23,11,23,45,12,34,67,56}
des = sorted(number,reverse=True)
print(des)

#25.use any() to check if at least one true value exiest in a boolean set.
binary_set = {1,0,1}

print(any(binary_set))

#26.use all() to check if all value in a boolean are true

binary_set = {1,0,1}

print(all(binary_set))

#27.copy a set using copy() and varify both set are independant.
duplicate = fruits.copy()
print(duplicate)

#28.delete a set completely using del keyword and observe the ressult
fruits = {'apple','cherry'}
del fruits
# print(fruits)

#29.convert a list with duplicate value into a set to remove duplicate
list = [23,22,32,23]
set1 = set(list)
print(set1)

#30.create two sets of student name(from two different classe) and find
student1 = {'yash','bob','david'}
student2 = {'bob','durgesh'}

#intersection
print(student1 & student2)

#student only in class A(difference)
print(student1 - student2)

#all unique student (union)
print(student1 | student2)