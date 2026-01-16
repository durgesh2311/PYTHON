# case study1: employee skill tracker

employees = {}
n = int(input("Enter number of employees: "))
for i in range(n):
    name = input("\nEnter employee name: ")
    skills = set(input("Enter skills (comma separated): ").split(","))
    
    employees[name] = skills

print("\nEmployees who know both Python and SQL:")
required_skills = {"Python", "SQL"}

for name, skill_set in employees.items():
    if required_skills.issubset(skill_set):
        print(name)

all_skills = set()

for skill_set in employees.values():
    all_skills = all_skills | skill_set  
print("\nUnique skills available across all employees:")
print(all_skills)

emp_name = input("\nEnter employee name to compare skills: ")

if emp_name in employees:
    target_skills = employees[emp_name]
    count = 0

    for name, skill_set in employees.items():
        if name != emp_name:
            if target_skills & skill_set:   
                count += 1

    print(f"\nNumber of employees sharing at least one skill with {emp_name}: {count}")
else:
    print("Employee not found.")


#Case Study B: Product Inventory Analyzer (Warehouse Comparison)

def input_warehouse_data(warehouse_name):
    products = {}
    n = int(input(f"\nEnter number of products in {warehouse_name}: "))

    for i in range(n):
        print(f"\nProduct {i + 1}:")
        product_id = input("Enter Product ID: ")
        product_name = input("Enter Product Name: ").strip().lower()
        quantity = int(input("Enter Quantity: "))

        # Store quantity by product name
        products[product_name] = {
            "product_id": product_id,
            "quantity": quantity
        }

    return products


# Input data
warehouse_a = input_warehouse_data("Warehouse A")
warehouse_b = input_warehouse_data("Warehouse B")

# 1. Common products
common_products = set(warehouse_a.keys()) & set(warehouse_b.keys())

print("\n--- Common Products in Both Warehouses ---")
if common_products:
    for product in common_products:
        print(product.title())
else:
    print("No common products found.")

# 2. Unique products
unique_products = set(warehouse_a.keys()) ^ set(warehouse_b.keys())

print("\n--- Unique Products Across Both Warehouses ---")
if unique_products:
    for product in unique_products:
        print(product.title())
else:
    print("No unique products found.")

# 3. Combine inventories
combined_inventory = {}

for product, details in warehouse_a.items():
    combined_inventory[product] = details["quantity"]

for product, details in warehouse_b.items():
    if product in combined_inventory:
        combined_inventory[product] += details["quantity"]
    else:
        combined_inventory[product] = details["quantity"]


sorted_inventory = sorted(
    combined_inventory.items(),
    key=lambda x: x[1],
    reverse=True
)

print("\n--- Combined Inventory (Sorted by Quantity Descending) ---")
for product, quantity in sorted_inventory:
    print(f"{product.title()} : {quantity}")


#Case Study C: University Course Registration System

# Accept student course registrations
registrations = []

n = int(input("Enter number of registrations: "))

for i in range(n):
    print(f"\nRegistration {i + 1}:")
    student = input("Enter Student Name: ").strip()
    course = input("Enter Course Name: ").strip()
    registrations.append((student, course))

# ---------------------------------------
# 1. Students enrolled in both Data Science and AI
# ---------------------------------------

student_courses = {}

for record in registrations:
    student = record[0]
    course = record[1]

    if student not in student_courses:
        student_courses[student] = set()

    student_courses[student].add(course)

students_in_both = []

for student in student_courses:
    courses = student_courses[student]
    if "Data Science" in courses and "AI" in courses:
        students_in_both.append(student)

print("\n--- Students enrolled in BOTH Data Science and AI ---")
if students_in_both:
    for student in students_in_both:
        print(student)
else:
    print("No student enrolled in both courses.")

# ---------------------------------------
# 2. Total number of unique courses
# ---------------------------------------

unique_courses = set()

for record in registrations:
    course = record[1]
    unique_courses.add(course)

print("\n--- Total Number of Unique Courses Offered ---")
print(len(unique_courses))

# ---------------------------------------
# 3. Courses that no student has repeated
# ---------------------------------------

course_count = {}

for record in registrations:
    course = record[1]
    if course in course_count:
        course_count[course] += 1
    else:
        course_count[course] = 1

non_repeated_courses = []

for course in course_count:
    if course_count[course] == 1:
        non_repeated_courses.append(course)

print("\n--- Courses That No Student Has Repeated ---")
if non_repeated_courses:
    for course in non_repeated_courses:
        print(course)
else:
    print("All courses are repeated by at least one student.")

#Case Study D: Customer Purchase Insights (E-commerce Scenario)

# Accept customer purchase details
purchases = []

n = int(input("Enter number of customers: "))

for i in range(n):
    print(f"\nCustomer {i + 1}:")
    name = input("Enter Customer Name: ").strip()

    product_count = int(input("Enter number of products purchased: "))
    product_list = []

    for j in range(product_count):
        product = input(f"Enter product {j + 1}: ").strip()
        product_list.append(product)

    purchases.append((name, product_list))

# ---------------------------------------
# 1. Total number of unique products
# ---------------------------------------

unique_products = set()

for record in purchases:
    products = record[1]
    for product in products:
        unique_products.add(product)

print("\n--- Total Number of Unique Products Bought ---")
print(len(unique_products))

# ---------------------------------------
# 2. Customers who purchased both Laptop and Headphones
# ---------------------------------------

print("\n--- Customers who purchased BOTH Laptop and Headphones ---")

found = False
for record in purchases:
    customer = record[0]
    products = record[1]

    if "Laptop" in products and "Headphones" in products:
        print(customer)
        found = True

if not found:
    print("No customer purchased both Laptop and Headphones.")

# ---------------------------------------
# 3. Most frequently purchased product(s)
# ---------------------------------------

product_count = {}

for record in purchases:
    products = record[1]
    for product in products:
        if product in product_count:
            product_count[product] += 1
        else:
            product_count[product] = 1

max_count = max(product_count.values())

print("\n--- Most Frequently Purchased Product(s) ---")
for product in product_count:
    if product_count[product] == max_count:
        print(product)

#Case Study E: Travel Planner (Data Deduplication Challenge)

# Accept travel booking details
bookings = []

n = int(input("Enter number of booking records: "))

for i in range(n):
    print(f"\nBooking {i + 1}:")
    name = input("Enter Traveler Name: ").strip()
    destination = input("Enter Destination: ").strip()
    date = input("Enter Date: ").strip()

    bookings.append((name, destination, date))

# ---------------------------------------
# 1. Remove duplicate records using set
# ---------------------------------------

unique_bookings = set(bookings)

print("\n--- Unique Booking Records ---")
for record in unique_bookings:
    print(record)

# ---------------------------------------
# 2. Display all unique destinations
# ---------------------------------------

unique_destinations = set()

for record in unique_bookings:
    destination = record[1]
    unique_destinations.add(destination)

print("\n--- Unique Destinations ---")
for destination in unique_destinations:
    print(destination)

# ---------------------------------------
# 3. Top 3 most visited destinations
# ---------------------------------------

destination_count = {}

for record in unique_bookings:
    destination = record[1]
    if destination in destination_count:
        destination_count[destination] += 1
    else:
        destination_count[destination] = 1

# Sort destinations by frequency (descending)
sorted_destinations = sorted(
    destination_count.items(),
    key=lambda item: item[1],
    reverse=True
)

print("\n--- Top 3 Most Visited Destinations ---")
count = 0
for item in sorted_destinations:
    if count < 3:
        print(item[0], ":", item[1], "visits")
        count += 1
#Case Study F: Student Attendance Analyzer

# Store attendance for 5 days
attendance = []

for day in range(1, 6):
    print(f"\nDay {day} Attendance")
    count = int(input("Enter number of students present: "))
    day_set = set()

    for i in range(count):
        name = input(f"Enter student name {i + 1}: ").strip()
        day_set.add(name)

    attendance.append(day_set)

# ---------------------------------------
# 1. Students present every day
# ---------------------------------------

present_every_day = attendance[0]

for i in range(1, 5):
    present_every_day = present_every_day.intersection(attendance[i])

print("\n--- Students Present Every Day ---")
if present_every_day:
    for student in present_every_day:
        print(student)
else:
    print("No student was present every day.")

# ---------------------------------------
# 2. Students absent on at least one day
# ---------------------------------------

all_students = set()

for day_set in attendance:
    for student in day_set:
        all_students.add(student)

absent_at_least_one_day = all_students - present_every_day

print("\n--- Students Absent on At Least One Day ---")
if absent_at_least_one_day:
    for student in absent_at_least_one_day:
        print(student)
else:
    print("All students were present every day.")

# ---------------------------------------
# 3. Total unique students across all days
# ---------------------------------------

print("\n--- Total Unique Students Across All Five Days ---")
print(len(all_students))


 #Case Study G: Movie Recommendation Tracker

# Accept user movie preferences
users = {}

n = int(input("Enter number of users: "))

for i in range(n):
    print(f"\nUser {i + 1}:")
    name = input("Enter user name: ").strip()

    movie_count = int(input("Enter number of favorite movies: "))
    movie_list = []

    for j in range(movie_count):
        movie = input(f"Enter movie {j + 1}: ").strip()
        movie_list.append(movie)

    users[name] = tuple(movie_list)

# ---------------------------------------
# 1. Users sharing at least two movies in common
# ---------------------------------------

print("\n--- Users Sharing At Least Two Movies ---")
found = False

user_names = list(users.keys())

for i in range(len(user_names)):
    for j in range(i + 1, len(user_names)):
        user1 = user_names[i]
        user2 = user_names[j]

        movies1 = set(users[user1])
        movies2 = set(users[user2])

        common_movies = movies1.intersection(movies2)

        if len(common_movies) >= 2:
            print(user1, "and", user2, "share", common_movies)
            found = True

if not found:
    print("No users share at least two movies.")

# ---------------------------------------
# 2. Display all unique movies
# ---------------------------------------

unique_movies = set()

for name in users:
    for movie in users[name]:
        unique_movies.add(movie)

print("\n--- All Unique Movies in Database ---")
for movie in unique_movies:
    print(movie)

# ---------------------------------------
# 3. Movies marked as favorite by only one user
# ---------------------------------------

movie_count = {}

for name in users:
    for movie in users[name]:
        if movie in movie_count:
            movie_count[movie] += 1
        else:
            movie_count[movie] = 1

print("\n--- Movies Favorited by Only One User ---")
found = False
for movie in movie_count:
    if movie_count[movie] == 1:
        print(movie)
        found = True

if not found:
    print("No movie is unique to a single user.")

 #Case Study H: Sports Event Participation Summary

 # Accept participant details
participants = []

n = int(input("Enter number of participants: "))

for i in range(n):
    print(f"\nParticipant {i + 1}:")
    name = input("Enter participant name: ").strip()

    sport_count = int(input("Enter number of sports registered: "))
    sport_list = []

    for j in range(sport_count):
        sport = input(f"Enter sport {j + 1}: ").strip()
        sport_list.append(sport)

    participants.append((name, sport_list))

# ---------------------------------------
# 1. Participants in both Cricket and Football
# ---------------------------------------

print("\n--- Participants in BOTH Cricket and Football ---")
found = False

for record in participants:
    name = record[0]
    sports = record[1]

    if "Cricket" in sports and "Football" in sports:
        print(name)
        found = True

if not found:
    print("No participant plays both Cricket and Football.")

# ---------------------------------------
# 2. Total number of unique sports
# ---------------------------------------

unique_sports = set()

for record in participants:
    sports = record[1]
    for sport in sports:
        unique_sports.add(sport)

print("\n--- Total Number of Unique Sports ---")
print(len(unique_sports))

# ---------------------------------------
# 3. Sports with highest participation count
# ---------------------------------------

sport_count_dict = {}

for record in participants:
    sports = record[1]
    for sport in sports:
        if sport in sport_count_dict:
            sport_count_dict[sport] += 1
        else:
            sport_count_dict[sport] = 1

highest_count = max(sport_count_dict.values())

top_sports = []

for sport in sport_count_dict:
    if sport_count_dict[sport] == highest_count:
        top_sports.append(sport)

top_sports_tuple = tuple(top_sports)

print("\n--- Sports with Highest Participation ---")
print(top_sports_tuple)
