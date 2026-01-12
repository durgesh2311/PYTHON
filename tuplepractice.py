#1. create a tuple named fruits contaning five fruit name and print it.

fruit = ('apple','cherry','banan','orange','mango')
print(fruit)

#2.
tuple2 = (23,45.6,'apple',True)
print(tuple2[0])
print(tuple2[1])
print(tuple2[2])
print(tuple2[3])

#3.

tuple1 = ('india',('up','maha','mp','jk'),'usa',('california','texax'))
print(tuple1)

#4.access the last element
print(tuple2[-1])

#5.slice and access first three element
print(tuple2[ : 3])

#6.use len() method
student = ('dvid','yash','bob','marli','yug')
print('the total number student in the tuple:', len(student))

#7.use max() and min() function
num1 = (1,2,3,4,5,6,7,8,9)
print(max(num1))
print(min(num1))

#8.sum()
print(sum(num1))

#9.sorting in the ascending

num2 = (90,34,56,78,12,34,33)

asce = tuple(sorted(num2))
print(asce)

#10.sorting in the descending order

descen = tuple(sorted(num2,reverse=True))
print(descen)

#11.
var1 = num2.count(34)
print('the total number of the time the number 34 is repited is:', var1)

#12.index method
var2 = num2.index(34)
print(var2)

#13.use of the in keyword

prog = ('python','cpp','java','javascript','c')
print("'python' is present on the tuple:", 'python' in prog)

#14.
print('cpp' not in prog)

#15.
num3 = tuple(range(1,11))
print(num3)

#16.
var2 = ('True','True','True')
print(any(var2))

#17.
print(all(var2))

#18.
tup1 = ('durgesh','yash','david')
tup2 = ('harsule','bora','jackson')

combined = tuple(zip(tup1,tup2))
print(combined)

#19.
t = ('ai', 'ml')
result = t * 3
print(result)

#20.
name = ('alce','bob','yash')
score = (90,80,70)

combined = tuple(zip(score,name))
print(combined)

#21.
tup3 = ('japan','usa','finland')
list1 = list(tup3)

list1.reverse()
print(list1)

tup4 = tuple(list1)
print(tup4)

#22.
var3 = ('p','y','t','h','o','n')
print(min(var3))
print(max(var3))

#23.
my_tuple = (10, 20, 30)

a, b, c = my_tuple

print(a)
print(b)
print(c)

#24.
number = (10,20,30)

print("original tuple:",number)

# number[0] = 99

# print(number)

#25.
import sys
elements_list = [1, 2, 3, 4, 5]
elements_tuple = (1, 2, 3, 4, 5)

print("List size (bytes):", sys.getsizeof(elements_list))
print("Tuple size (bytes):", sys.getsizeof(elements_tuple))
 
#26.
num4 = (10,20,30,40,50,60,70,80,90,100)
print(sum(num4)/len(num4))

#27.

cities = ("New York", "London", "Paris", "Tokyo", "Sydney")
print(cities[::-1])

#28.
tup5 = ('c','p','p')
list2 = list(tup5)
print(list2)

list2.append('a')
list2.append('y')
print(list2)

tup6 = tuple(list2)
print(tup6)

#29.
employee = ("john",34,'wed')

print(employee)

name , age , dep = employee

print('name:', name)
print('age:', age)
print('department:', dep)

#30.
product_name = ("Laptop", "Mobile", "Tablet", "Headphones", "Smartwatch")
price = (75000, 30000, 25000, 3000, 15000)

combined = list(zip(product_name, price))



