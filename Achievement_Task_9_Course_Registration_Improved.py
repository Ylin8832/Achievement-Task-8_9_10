# Name:                     Task 9: Course Registration-Improved
# Author:                   Yunfeng Lin (Ylin8832)
# Date Created:             March 22, 2023
# Date Last Modified:       March 24, 2023

'''
Improvement 1: Trimmed whitespaces before and after any input from the user.
Improvement 2: Created new format of a list of the four courses and wrapped this block of code in a function called "courseInformation()".
Improvement 3: Changed the format and courses names actual course names and codes.
Improvement 4: If the user didn't enter any course, then the program will prompt user either type '1' to exit or type '2' to continue.
Improvement 5: If user enters one or more invalid (not offered) course codes, notify the user about the invalid input, but the program will 
               not repeat the course selection process in this case. The valid course selection will immediately be shown in the console again 
               and at the same time prompt user to try again.
Improvement 6: Write user information and registered courses detail to the local file named "courselist.txt" and a message will be printed 
               to the console informing the user about this.
'''

print("\n{0:-^64s}".format("Welcome to course registering system".upper()))

def studentInformation():
    studentInfo = {
        "firstName":" ",
        "lastName":" ",
        "studentNumber":" "
        }
    studentInfo["firstName"] = input("\nEnter your first name: ").strip()
    studentInfo["lastName"] = input("Enter your last name: ").strip()
    studentInfo["studentNumber"] = input("Enter your student number: ").strip()
    return studentInfo
student_Info = studentInformation()

def courseInformation():
    while True:
        fourCourses = {
            "COURSE#1": "Programming Fundament-PROG1783",
            "COURSE#2": "Network Infrastructure-INFO1385",
            "COURSE#3": "Computer Systems Fundamentals-INFO1250",
            "COURSE#4": "Information Technology Documentation-INFO1145"
            }

        print("\n{0:-^48}".format("Available Course List"))
        for key, value in fourCourses.items():
            print(key, value)
        return fourCourses
confirmCourses = courseInformation()

courseErr1 = "You have not selected any course. To exit the program, type '1', to continue type '2'."
courseErr2 = "Invalid input. Please select courses from the Available Course List."

validID = ["COURSE#1", "COURSE#2", "COURSE#3","COURSE#4"]
while True: # Use the while loop to make the program keep asking user to input valid course ID.
            # Store the input data in to the variable called disiredCourse and converts all letters entered by user to upper case.
        desiredCourse = input("\nEnter the course ID you would like to register (Enter comma ',' in between course IDs): ").upper().strip()
        courseList = (desiredCourse.replace(" ", "")).split(",")
        if desiredCourse is "":
            print(courseErr1)
            option = input()
            if option == '1':
                exit()
            elif option == '2':
                courseInformation()
        elif not all(course in validID for course in courseList): # Use all() function to iterate items in the list called validID.
                print(courseErr2)                     
                courseInformation()
        else:
             break
def finalConfirmation():
# Display user information (Student name and ID) and No. of selected courses for the final confirmation to the console.
    print("\n{0:-^64s}".format("Please confirm your registeration info below"))
    print("\n{0}{1:>29} {2}\n{3}{4:>28}".format("Student Name:", student_Info["firstName"], student_Info["lastName"], "Student Number:", student_Info["studentNumber"]))
    print("Total number of registered courses:", len(courseList))
    print("\nRegistered courses: ")
# Write user information (Student name and ID) and No. of selected courses for the final confirmation to the local file named "courselist.txt".
    file.write("{0:-^64s}\n".format("Please confirm your registration info below"))
    file.write("{0}{1:>29} {2}\n{3}{4:>28}\n".format("Student Name:", student_Info["firstName"], student_Info["lastName"], "Student Number:", student_Info["studentNumber"]))
    file.write("Total number of registered courses: {}\n".format(len(courseList)))
    file.write("Registered courses:\n")
    try:
        for n in courseList:
            print("{} {}".format(n, confirmCourses[n])) # Display the registered courses detail to the console.
            file.write("{} {}\n".format(n, confirmCourses[n])) # Write the registered courses detail to the local file named "courselist.txt".
    except KeyError as keyErr:
            print(keyErr)
    except AttributeError as attErr:
            print(attErr)
    except NameError as NamErr:
            print(NamErr)
    
aNewfile = r"C:\Users\yunfe\Documents\04. PROG1783_23W\MyExercises_pyDoc\courselist.txt"
file = open(aNewfile,'a')
finalConfirmation()
print("{0:=^150s}".format("Please be informed that your information and registered course details have been written to the file with the link below."))
print(r"C:\Users\yunfe\Documents\04. PROG1783_23W\MyExercises_pyDoc\courselist.txt")

