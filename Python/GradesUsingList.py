# ---------------------------------------------------------------------------------------
"""Create a reportcard. It must contain the name of five subjects along with marks obtained in them out of 100.
Then calculate the total marks obtained, percentage, grade.
Grade must be calculated as per below criteria :-
Percentage           Grade
>=                    A+
85-75                 A
75-65                 B
65-55                 C
55-50                 D
<50                   Fail"""

# Create blank list of subjects and marks
report_card=[]
total=0
# Enter marks to the corresponding subject
print("--------------------------------------------------------------------")
print("Enter the name of subject and corresponding marks out of 100: ")
for x in range(5):
    print("Enter the subject name: ", end="")
    subject = input()
    print("Enter the corresponding marks: ", end="")
    mark = int(input())
    report_card.append([subject, mark])
    # report_card[1].append(mark)
    total += mark
# Finding the percentage of the marks
percentage = total * 100 / 500
# Initialize the grade with empty string
grade=""
# Calculating the grade according to the question
for i in range(len(report_card[0])):
    if percentage >= 80:
        grade = "A+"
    elif percentage >= 75:
        grade = "A"
    elif percentage >= 65:
        grade = "B"
    elif percentage >= 55:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "Fail"
print("-------------------------------------------------------------------")
print("List of subjects along with their marks : ")
# Printing the marks of the list along with their subjects
for index in range(len(report_card)):
    print(report_card[index][0], "\t\t\t\t : \t\t\t\t", report_card[index][1])
# Printing the grade ot the student
print("-------------------------------------------------------------------")
print("Total marks : ", total)
print("Percentage : ", percentage)
print("Grade of the student : ", grade)