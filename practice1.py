#1
list = [1,2,34,55,66,77,34,90,89,90]
print(list)

#2.
list1 = ['apple',78,44.44,True,90]
print(list1)
print(type(list1[0]))
print(type(list1[1]))
print(type(list1[2]))
print(type(list1[3]))

#3.
print(list1[0])
print(len(list1)/2)
print(list1[-1])

#4
print(list1[0:3])
print(list1[1:4])

#5 
list1[1] = "banana"
print(list1)

#6
list1.append("USA")
print(list1)

#7
list1.insert(2,"mumbai")
print(list1)

#8 
list2 = ["india ", "pak"]
list1.extend(list2)
print(list1)

#9
list1.remove("mumbai")
print(list1)

#10
removed_iteam = list1.pop(3)
print("after pop(3):", list1)

#11
del list1[0]
print(list1)

#12
list1.clear()
print(list1)

#13
list4 = ['apple','banana','mango','pineapple','apple']
print("is apple in list4:" ,"banana" in list4)

#14
print(list4.index('apple'))

#15
count = list4.count('apple')
print(count)

#16
list5 = [34,12,45,34,67,43]
list5.sort()
print(list5)

#17
list5.sort(reverse=True)
print("sorted list", list5)

#18
list5.reverse()
print(list5)

#20

new_list = list5 + list4
print(new_list)



