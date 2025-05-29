import numpy as np

# function to initialize and store data
def initialize_data():
    subject = np.array(['English', 'Maths', 'Science', 'Social', 'History'])
    students = np.array(['Alice', 'Bob', 'Charlie', 'Dan'])
    marks = np.array([[81, 78, 80, 60, 63],
                      [50, 60, 65, 48, 55],
                      [30, 83, 97, 79, 75],
                      [99, 55, 60, 48, 30]])
    return subject, students, marks

# function that takes user input for new record
def add_record(studentArray, subjectArray, marksArray):

    # get student's name
    studentName = input('Student Name : ')

    # initialize an empty marks array of same length as subject
    marks = np.empty(len(subjectArray), dtype=int)
    
    # get inputs from the user
    for i in range(len(subjectArray)):
        marks[i] = int(input(f"Enter marks for {subjectArray[i]}: "))

    # append new student to studentArray
    studentArray = np.append(studentArray, studentName)

    # append marks of new student to studentArray
    marksArray = np.vstack((marksArray, marks))
    
    return studentArray, marksArray
    
def main():
    subject, students, marks = initialize_data()
    students, marks = add_record(students, subject, marks)
    print(subject)
    print(students)
    print(marks)

main()