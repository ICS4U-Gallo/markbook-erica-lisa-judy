"""
Markbook Application
Group members: Erica, Lisa, Judy
"""
from typing import Dict

name_student = input("What is the student's full name? \n")
student_email = input("Enter the student's email: ")
student_phone_number = input("Enter the student's phone number: ")
student_grade = input("Enter the student's grade: ")
 
student_info = { 
    "Student's Full Name" : name_student , 
    "Student's Email" : student_email , 
    "Student's Phone Number" : student_phone_number , 
    "Student's Grade" : student_grade 
    }


def create_assignment(name: str, due: str, points: int) -> Dict:
    """Creates an assignment represented as a dictionary
    
    Args:
        name = "" the name of the assignment.
        due = "" the due date for the assignment.
        points = "" what the assignment is out of (denominator).
    Returns:
        Assignment as a dictionary.
    """
    return {}


def create_classroom(course_code: str, course_name: str, period: int, teacher: str) -> Dict:
    """Creates a classroom dictionary"""

course_code = input("Enter course code: ")
course_name = input("Enter course name: ")
period_nmb = int(input("Enter the period: "))
teacher_name = input("Enter the teacher's name: ")

classroom = { 
    "Course code" : course_code , 
    "Course name" : course_name , 
    "Period" : period_nmb , 
    "Teacher's name" : teacher_name 
    }
print(classroom)


def calculate_average_mark(student: Dict) -> float:
    """Calculates the average mark of a student"""


no_of_grds = int(input("How many grades are being inputted? \n"))
total_sum = 0

for n in range(no_of_grds) :
    grades = float(input("Enter mark: "))
    total_sum += grades

avg = total_sum/no_of_grds

print(name_student , "'s average mark is" , avg)


def add_student_to_classroom(student: Dict, classroom: Dict):
    """Adds student to a classroom

    Args:
        student: Student dict
        classroom: The classroom to add the student to
    """

    classroom.append(student_info)
    return classroom
    
def remove_student_from_classroom(student: Dict, classroom: Dict):
    """Removes student from classroom

    Args:
        student: The student to be removed
        classroom: the class from which the student will be removed.
    """
    with open('markbook.txt', 'a') as f:
        f.read()
        del classroom[student_info]
    
    return (f"You successfully deleted {name_student} from {classroom['Course code']}.")


def edit_student(student: Dict, **kwargs: Dict):
    """Edits the student's info with the provided key/value pairs

    Args:
        student: The student whose data needs to be udated.
        **kwargs: KeyWordARGumentS. The key/value pairs of the
            data that needs to be changed. Can come in the form
            of a dictionary.
    """
    pass
