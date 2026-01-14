# 1 Write a program to demonstrate how a local variable inside a function works and is not accessible outside the function

# def function():
#     x = 10
#     print(x)

# function()

# print("Outside the function, x =", x)

# 3 Write a program where a global variable is updated by multiple function calls using the global keyword

# count = 0

# def incerement():
#     global count
#     count += 1
#     print("the element is increment:", count)

# def decrement():
#     global count
#     count -= 1
#     print("the element is increment:", count)   

# incerement()
# decrement()
# incerement()
# decrement()

# 4 Create two functions where both use a global variable to calculate and store cumulative total sales

# total_sales = 0

# def add_online_sales(amount):
#     global total_sales
#     total_sales += amount
#     print(f"After online sale, total sales = {total_sales}")

# def add_store_sales(amount):
#     global total_sales
#     total_sales += amount
#     print(f"After store sale, total sales = {total_sales}")

# add_online_sales(1500)
# add_store_sales(2300)
# add_online_sales(700)

# print("Final total sales =", total_sales)

# 5 Write a nested function where the inner function accesses an enclosing variable from the outer function
  
# def outer_function():
#     masse = "i am durgesh"

#     def inner_function():
#         print(masse)

#     inner_function()    

# outer_function()

# 6 Demonstrate the use of nonlocal keyword by modifying an enclosing variable inside an inner function

# def outer_function():
#     x = 10

#     def inner_function():
#         nonlocal x
#         x += 1
#         print("Inside inner function, x =", x)

#     inner_function()

# outer_function()

# 7 Create a nested function structure with three levels and print variables from local enclosing and global scopes

# g = "apple"

# def outer():
#     h = "banana"
#     def middle():
#         i = "cherry"
#         def inner():
#             j = "mango"
#             print(j)
#             print(i)
#             print(h)
        
#         inner()

#     middle()

# outer()

# 8 Write a function where local variable shadows a global variable and show both outputs

# value = 500

# def show_showdow():
#     value = 1000
#     print(value)

# print(value)
# show_showdow()

# 9 Create a program to show how Python searches variable names using the LEGB rule

# x = "Global X"  # Global Scope

# def outer():
#     x = "Enclosing X"  # Enclosing Scope

#     def inner():
#         x = "Local X"  # Local Scope
#         print("Inner Function:", x)
    
#     inner()
#     print("Outer Function:", x)

# outer()
# print("Global Scope:", x)

# 10 Write a function to show that local variables are destroyed after function execution ends
# def my_function():
#     x = 10  # Local variable
#     print("Inside function, x =", x)


# my_function()

# print(x)

# 11 Create a nested function where both inner and outer functions take arguments and print their values.
# def outer_function(x):
#     print("Outer function argument:", x)

#     def inner_function(y):
#         print("Inner function argument:", y)

#     inner_function(20)

# outer_function(10)

# 12 Write a nested function that calculates total marks using an outer function for input and an inner function for computation
# def student_marks(m1, m2, m3):
#     print("Marks entered:", m1, m2, m3)

#     def calculate_total():
#         total = m1 + m2 + m3
#         return total

#     total_marks = calculate_total()
#     print("Total marks =", total_marks)

# student_marks(75, 80, 90)

# 13 Demonstrate how enclosing variable stores the running total for a counter function using nonlocal
# def counter():
#     count = 0  # Enclosing variable

#     def increment():
#         nonlocal count
#         count += 1
#         return count

#     return increment

# my_counter = counter()

# print(my_counter())
# print(my_counter())
# print(my_counter())
# print(my_counter())

# 14 Write a closure function that generates a multiplier and demonstrate how the enclosing variable remembers state
# def multiplier(n):
#     # Enclosing variable n
#     def multiply(x):
#         return x * n
#     return multiply

# double = multiplier(2)
# triple = multiplier(3)

# print(double(5))
# print(double(10))

# print(triple(5))
# print(triple(10))

# 15 Create a function with variable positional arguments to calculate the sum of all given numbers

# def total_num(*number):
    
#     print("number data received:", number)    
#     total = sum(number)                    
#     print("Total Sales:", total)            
#     return total                            


# total_num(25000, 30000, 15000, 22000)

# 16 Write a function with variable positional arguments that finds the maximum value from all numbers passed

# def find_max(*numbers):
#     max_value = numbers[0]

#     for num in numbers:
#         if num > max_value:
#             max_value = num

#     return max_value

# print(find_max(10, 25, 5, 40, 30))
# print(find_max(3, 7, 2))

# 17 Create a function with variable keyword arguments that displays student details such as name age and grade.

# def student_info(**details):
    
#     print("\nstudent Record:")
#     for key, value in details.items():      
#         print(f"{key}: {value}")            


# student_info(Name="John", Age=29, grade="A")
# student_info(Name="yash", Age=23, grade="B")

# 18 Write a function using variable keyword arguments to print employee records with department and salary

# def employee_record(**details):
    
#     print("\nEmployee Record:")
#     for key, value in details.items():      
#         print(f"{key}: {value}")            


# employee_record(Name="John", Age=29, Department="IT", Salary=45000)
# employee_record(Name="durgesh", Age=30, Department="ENTC", Salary=55000)

# 19 Combine *args and **kwargs in a single function and print both values separately

# def student_summary(*marks, **info):
    
#     print("\nStudent Information:")
#     for key, value in info.items():         
#         print(f"{key}: {value}")
        
#     total = sum(marks)                      
#     avg = total / len(marks)                
#     print("Total Marks:", total)
#     print("Average Marks:", avg)


# student_summary(78, 85, 90, 82, Name="Alice", RollNo=102, Class="B.Tech")

# 20 Write a function that uses *args to calculate average sales for any number of branches

# def total_sales(*sales):
    
#     print("Sales data received:", sales)    
#     total = sum(sales)                      
#     print("Total Sales:", total)            
#     return total                            


# total_sales(25000, 30000, 15000, 22000)

# 21 Write a function that uses **kwargs to configure a model where parameters like learning_rate and epochs are passed dynamically

# def configure_model(**kwargs):
#     learning_rate = kwargs.get("learning_rate", 0.01)
#     epochs = kwargs.get("epochs", 10)
#     batch_size = kwargs.get("batch_size", 32)
#     optimizer = kwargs.get("optimizer", "sgd")

#     print("Model Configuration:")
#     print(f"Learning Rate: {learning_rate}")
#     print(f"Epochs: {epochs}")
#     print(f"Batch Size: {batch_size}")
#     print(f"Optimizer: {optimizer}")

# configure_model(learning_rate=0.001, epochs=50, optimizer="adam")

# 22 Create a nested function that uses *args in the inner function to calculate the total of passed values
# def outer_function():
#     print("Calculating total using inner function...")

#     def inner_function(*args):
#         total = 0
#         for num in args:
#             total += num
#         return total

#     result = inner_function(10, 20, 30, 40)
#     print("Total:", result)
# outer_function()

# 23 Write a program where an outer function accepts employee details and inner function calculates bonus based on salary
# def employee_details(name, salary):
#     print("Employee Name:", name)
#     print("Salary:", salary)

#     def calculate_bonus():
        
#         if salary >= 50000:
#             bonus = salary * 0.20
#         elif salary >= 30000:
#             bonus = salary * 0.15
#         else:
#             bonus = salary * 0.10
#         return bonus

#     bonus_amount = calculate_bonus()
#     print("Bonus:", bonus_amount)

# employee_details("Rahul", 45000)

# 24 Demonstrate how a nonlocal variable can be used to maintain the count of how many times a nested function has been called
# def outer_function():
#     count = 0   

#     def inner_function():
#         nonlocal count
#         count += 1
#         print("Inner function called", count, "time(s)")

#     inner_function()
#     inner_function()
#     inner_function()

# outer_function()

# 25 Write a program to show how global and local variables can have the same name but store different data

# x = 100   

# def show_variables():
#     x = 50   
#     print("Local x:", x)

# show_variables()

# print("Global x:", x)

# 26 Create a nested function example where inner function modifies enclosing variable to accumulate running total of expenses

# def expense_tracker():
#     total_expense = 0   # Enclosing variable

#     def add_expense(amount):
#         nonlocal total_expense
#         total_expense += amount
#         print("Added Expense:", amount)
#         print("Total Expense:", total_expense)

#     # Adding expenses
#     add_expense(500)
#     add_expense(1200)
#     add_expense(300)

# # Call the outer function
# expense_tracker()

# 27 Write a function that uses *args to concatenate multiple strings into a single string
# def concatenate_strings(*args):
#     result = ""
#     for text in args:
#         result += text
#     return result

# # Function call
# output = concatenate_strings("Hello", " ", "World", "!", " Welcome")
# print(output)

# 28 Create a function that uses **kwargs to print formatted key value pairs as system configuration parameters
# def system_config(**kwargs):
#     print("System Configuration Parameters:")
#     print("-" * 35)

#     for key, value in kwargs.items():
#         print(f"{key} : {value}")

# system_config(
#     os="Windows",
#     processor="Intel i5",
#     ram="16GB",
#     storage="512GB SSD",
#     version="10 Pro"
# )

# 29 Write a function with both *args and **kwargs to simulate order details containing items and their prices
# def order_details(*items, **prices):
#     print("Order Summary")
#     print("-" * 25)

#     total = 0
#     for item in items:
#         price = prices.get(item, 0)
#         print(f"{item} : ₹{price}")
#         total += price

#     print("-" * 25)
#     print("Total Amount : ₹", total)

# order_details(
#     "Laptop", "Mouse", "Keyboard",
#     Laptop=55000,
#     Mouse=800,
#     Keyboard=1200
# )

# 30 Design a nested function where the outer function provides base salary and the inner function adds incentives using nonlocal variable
# def salary_calculator(base_salary):
#     total_salary = base_salary   # Enclosing variable

#     def add_incentive(amount):
#         nonlocal total_salary
#         total_salary += amount
#         print("Incentive Added:", amount)
#         print("Current Total Salary:", total_salary)

#     # Adding incentives
#     add_incentive(5000)
#     add_incentive(3000)

#     print("Final Salary:", total_salary)

# # Function call
# salary_calculator(40000)

