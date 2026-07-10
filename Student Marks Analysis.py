import numpy as np 

print ("="  *60)
print ("     STUDENT MARKS ANALYSIS SYSTEM")
print ("="  *60)

#Students Name
students_name = np.array([
    "Kami",
    "Saleem",
    "ALI",
    "Adeel",
    "Hasseeb",
    "Faizan",
    "Nida",
    "Ayesha",
    "Hira",
    "Zohib",
    "Usman",
    "Hamza",
    "Aqib",
    "Aqeel",
    "Moksh"

])
marks = np.array([99, 87, 78, 67, 56, 64, 67, 45, 60, 78, 34, 56, 87, 90, 63])

print("\nStudents Marks")
print ("-" *60)


for name, mark in zip(students_name, marks):
    print (f"{name} : {mark}")

print ("\n"+ "=" * 60)

print ("STATISTICS")
print ("=" *60)


print (f"Average Marks :{np.mean(marks)}")
print (f"Median Marks :{np.median(marks)}")
print (f"Highest Marks : {np.max(marks)}")
print (f"Lowest Marks : {np.min(marks)}")
print (f"Standard Deviation : {np.std(marks):.2f}")


# Topper
topper_index = np.argmax(marks)

print ("\nTopper")
print ("-" * 60)

print (f"Name :{students_name[topper_index]}")
print (f"Marks :{marks[topper_index]}")


# Pass / Fail
passing = np.where(marks >= 50)[0]
failing = np.where(marks < 50)[0]

print ("\nPassing Studenst")
print ("-" * 60)
for i in passing :
    print (f"{students_name[i]}: {marks[i]}")

print ("\nFail Students")
print ("-" *60)
for i  in failing:
    print (f"{students_name[i]}: {marks[i]}")


print ("\nTotal Passing Students :",len(passing))
print ("Total Failing students :",len(failing))
print (f"Pass Percentage : {(len(passing) / len(marks)) *100:.2f}%")


# Grading
grades = np.where(
    marks >=90, 'A+',
    np.where(
        marks >=80, 'A',
        np.where(
            marks >=70, 'B',
            np.where(
                marks >=60, 'C',
                np.where(
                    marks >=50, 'D', 'F'
                )
            )
        )
    )
)

print ("\nGrades")
print ("-" * 60)


for name, mark, grade in zip(students_name, marks, grades):
    print (f"{name : <10} {mark : <5} Grade : {grade}")


print ("=" * 60)
print ("Analysis Completed Successfully!")
print ("=" * 60)
