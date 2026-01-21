# 1. Create a Pandas Series using a list of 5 random numbers and custom index names.
#     Then print the series and its data type

import pandas as pd

data = [10, 20, 30, 40, 50]
series = pd.Series(data, index=['A', 'B', 'C', 'D', 'E'])

print("Series Example:")
print(series)


# 2. Create a DataFrame with columns: "Student_Name", "Maths", "Science", "English".
#     Fill it with 5 sample student records and display the top 3 rows using head().

data = {
    "Student_Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Maths": [85, 78, 92, 70, 88],
    "Science": [90, 82, 89, 75, 91],
    "English": [88, 80, 94, 72, 86]
}

df = pd.DataFrame(data)

df.head(3)

# 3. Import a CSV file (use any sample dataset) into a DataFrame.
#     Display the number of rows and columns using shape, and print column names.

data = {
    "ID": [1, 2, 3, 4, 5],
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Age": [23, 28, 25, 30, 27],
    "Department": ["IT", "HR", "Finance", "Marketing", "IT"],
    "Salary": [50000, 45000, 48000, 52000, 51000]
}

df = pd.DataFrame(data)

df.to_csv("sample_data.csv", index=False)

df = pd.read_csv("sample_data.csv")

print("Shape of the DataFrame:", df.shape)

print("Column Names:")
print(df.columns)

# 4. Add a new column named "Total_Marks" that sums all three subject scores.
#     Then create another column "Average" by dividing Total_Marks by 3.
data = {
    "Student_Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Maths": [85, 78, 92, 70, 88],
    "Science": [90, 82, 89, 75, 91],
    "English": [88, 80, 94, 72, 86]
}

df = pd.DataFrame(data)

df["Total_Marks"] = df["Maths"] + df["Science"] + df["English"]

df["Average"] = df["Total_Marks"] / 3

print(df)

# 5. Introduce a missing value (NaN) in the "Science" column and then:
#     (a) Identify missing values using isnull()
#     (b) Replace the missing value with the column mean using fillna().

import numpy as np

data = {
    "Student_Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Maths": [85, 78, 92, 70, 88],
    "Science": [90, 82, 89, 75, 91],
    "English": [88, 80, 94, 72, 86]
}

df = pd.DataFrame(data)

df.loc[2, "Science"] = np.nan   

print("Missing values in the DataFrame:")
print(df.isnull())

science_mean = df["Science"].mean()
df["Science"] = df["Science"].fillna(science_mean)
print(df)

 #6. Filter and display all students whose "Average" score is greater than 75.

data = {
    "Student_Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Maths": [85, 78, 92, 70, 88],
    "Science": [90, 82, 89, 75, 91],
    "English": [88, 80, 94, 72, 86]
}

df = pd.DataFrame(data)

df["Total_Marks"] = df["Maths"] + df["Science"] + df["English"]
df["Average"] = df["Total_Marks"] / 3

filtered_students = df[df["Average"] > 75]

print(filtered_students)

# 7. Sort the DataFrame by "Total_Marks" in descending order and show the top 3 performers.

data = {
    "Student_Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Maths": [85, 78, 92, 70, 88],
    "Science": [90, 82, 89, 75, 91],
    "English": [88, 80, 94, 72, 86]
}

df = pd.DataFrame(data)

df["Total_Marks"] = df["Maths"] + df["Science"] + df["English"]
df["Average"] = df["Total_Marks"] / 3

sorted_df = df.sort_values(by="Total_Marks", ascending=False)

top_3 = sorted_df.head(3)

print(top_3)

# 8. Group students based on their "English" score range (like above or below 70)
#     and find the mean of "Maths" and "Science" marks for each group.

data = {
    "Student_Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Maths": [85, 78, 92, 70, 88],
    "Science": [90, 82, 89, 75, 91],
    "English": [88, 80, 94, 68, 86]
}

df = pd.DataFrame(data)

df["English_Range"] = df["English"].apply(
    lambda x: "Below 70" if x < 70 else "70 and Above"
)
grouped_result = df.groupby("English_Range")[["Maths", "Science"]].mean()

print(grouped_result)

# 9. Merge two DataFrames:
#     (a) One with "Student_Name" and "Total_Marks"
#     (b) Another with "Student_Name" and "Sports_Score"
#     Then create a new column "Overall_Score" = Total_Marks + Sports_Score.


df_marks = pd.DataFrame({
    "Student_Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Total_Marks": [263, 240, 275, 217, 265]
})


df_sports = pd.DataFrame({
    "Student_Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Sports_Score": [20, 15, 25, 18, 22]
})

df_merged = pd.merge(df_marks, df_sports, on="Student_Name")

df_merged["Overall_Score"] = df_merged["Total_Marks"] + df_merged["Sports_Score"]

print(df_merged)

# 10. Export the final DataFrame to a CSV file on your Desktop (use os library to define path)
#     and verify if the file is successfully created using os.path.exists
import os

df_final = pd.DataFrame({
    "Student_Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Total_Marks": [263, 240, 275, 217, 265],
    "Sports_Score": [20, 15, 25, 18, 22],
    "Overall_Score": [283, 255, 300, 235, 287]
})

desktop_path = os.path.join(os.path.expanduser("~"), "Desktop", "final_student_scores.csv")

df_final.to_csv(desktop_path, index=False)

file_exists = os.path.exists(desktop_path)
print(f"File successfully created: {file_exists}")


