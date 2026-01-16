# While Loop:

# 1. Write a program using while loop to print numbers from 1 to 10.
num = 1
while num <= 10:
    print("the number is:",num)
    num += 1

# 2. Use while loop to print even numbers between 1 and 50.

num1 = 1
while num1 <= 50:
    if num1 % 2 == 0:
        print(f"the {num1} is even number.")
    num1 += 1

# 3. Write a while loop to calculate the sum of first 20 natural numbers.

num2 = 1
total = 0
while num2 <= 20:
    total = total + num2
    num2 = num2 + 1

print("the sum of the first twenty number is :",total)    

# 4. Create a program using while loop to print multiplication table of 7.

i = 1
j = 7
while i <= 10:
    print(f"{j} X {i} =", i*j)
    i += 1    

# 5. Write a program to reverse a given number using while loop.
num = int(input("enter the number:"))
digits = str(num)
reverse = digits.reverse()
result = int(reverse)
print(result)

while len(digits) > 0:
    print(digits)
    num2 = digits.reverse()
    print(num2)

#6. Use while loop to count the number of digits in an integer entered by the user.

num = int(input("Enter an integer: "))


if num < 0:
    num = -num

count = 0

if num == 0:
    count = 1
else:
    while num > 0:
        count += 1
        num //= 10   

print("Number of digits:", count)


# 7. Write a program to print factorial of a number using while loop

n = int(input("enter the number:"))
i = 1
factorial = 1
while i <= n :
    factorial = factorial * i
    i += 1

print("the factorial {num} is :", factorial)    

# 8. Write a program using while loop to print the Fibonacci sequence up to 50.

F2 = 1
F1 = 0
F = 0

while F <= 50:
    print(F)
    F = F1 + F2
    F1 = F2
    F2 = F

# 9. Write a program to check whether a given number is a palindrome using while loop.

num = int(input("Enter a number: "))

original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10

if original == reverse:
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")

# 10. Write a while loop that continues taking input until the user enters 'exit'.
while True:
    user_input = input("Enter something (type 'exit' to stop): ")
    
    if user_input.lower() == "exit":
        print("Program terminated.")
        break
    else:
        print("You entered:", user_input)


# do while loop

# 1. Simulate a do-while loop to print numbers from 1 to 10.

num = 1

while True:
    print("number:",num)
    num += 1
    if num > 10:
        break

# 2. Simulate a do-while loop to take user input until a positive number is entered.

while True:
    num = int(input("Enter a number: "))

    if num > 0:
        print(f"The number {num} is positive")
        break
    else:
        print("Please enter a positive number")

# 3. Use a do-while structure to display a menu until the user selects "Quit".

while True:
    print("\nMENU")
    print("1. Start")
    print("2. Settings")
    print("3. Help")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == "4":
        print("Exiting the program...")
        break
    else:
        print("You selected option:", choice)

# 4. Simulate do-while loop to print the multiplication table of 19.

i = 1
j = 19

while True:
    print(f"the multiplication {j} X {i} is:", j*i)
    i += 1

    if i > 11:
        break

# 5. Create a do-while simulation that keeps asking for a password until it matches.

correct_password = "admin123"

while True:
    password = input("Enter the password: ")

    if password == correct_password:
        print("Access granted")
        break
    else:
        print("Incorrect password. Try again.")

# 6. Simulate do-while to find the sum of digits of a number entered by user.

num = int(input("Enter a number: "))
sum_digits = 0

while True:
    digit = num % 10
    sum_digits += digit
    num = num // 10

    if num == 0:
        break

print("Sum of digits:", sum_digits)

# 7. Simulate a do-while loop to print numbers from 10 down to 1
i = 10

while True:
    print(i)
    i -= 1

    if i == 0:
        break

# 8. Simulate do-while loop to check whether the entered number is prime or not    

num = int(input("Enter a number: "))

i = 2
is_prime = True

if num <= 1:
    is_prime = False
else:
    while True:
        if i > num // 2:
            break
        if num % i == 0:
            is_prime = False
            break
        i += 1

if is_prime:
    print("The number is Prime")
else:
    print("The number is Not Prime")

# 9. Simulate do-while loop to print all odd numbers between 1 and 30.

num = 1

while True:
    if num % 2 != 0:
        print(num)

    num += 1

    if num > 30:
        break

# 10. Simulate do-while loop to calculate the product of numbers until user enters 0.

product = 1
while True:
    num = int(input("Enter a number (0 to stop): "))
    if num == 0:
        break
    product = product * num

print("Product:", product)




# for loop
# 1. Write a for loop to print numbers from 1 to 20.
for i in range(1,21):
    print(i)

# 2. Write a for loop to print the square of numbers from 1 to 10.    
for i in range(1,11):
    print(f"the square of the {i} is :", i*i)

# 3. Use for loop to display even numbers from 2 to 40    
for i in range(2,41):
    if i % 2 == 0:
        print(i)

# 4. Write a for loop to print the multiplication table of 12.
for i in range(1, 11):
    print(f"12 x {i} = {12 * i}")

# 5. Create a for loop to calculate factorial of a given number.
n = int(input("Enter the number: "))

fact = 1
for i in range(1, n + 1):
    fact = fact * i

print(fact)

# 6. Write a for loop to print elements of a list containing 10 integers.
list1 = [1,2,3,4,5,6,7,8,9,10]

for i in list1:
    print(i)

# 7. Write a for loop to count how many vowels are in a given string.
string = input("enter the string:")
count = 0

for ch in string:
    if ch.lower() in 'aeiou':
        count += 1
    
print("Number of vowels:", count)

# 8. Use nested for loop to print a right-angled triangle pattern of stars (*).

rows = int(input("Enter the number of rows: "))

for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
        print()

# 9. Use for loop to print numbers from 100 down to 1 in reverse order.

for i in range(100, 0, -1):
    print(i)

# 10. Write a for loop to display only odd numbers from 1 to 25 and calculate their sum.
sum = 0
for i in range(1,26):
    if i % 2 != 0:
        print(i)
        sum = sum + i

print("the sum of the 1 to 20 odd number is:", sum)



    