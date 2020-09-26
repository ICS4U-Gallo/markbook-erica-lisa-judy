"""
Markbook Application
Group members: Erica, Lisa, Judy
"""
from typing import Dict


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
    return {}


def calculate_average_mark(student: Dict) -> float:
    """Calculates the average mark of a student"""
    return 0


student = {'First Name': "unknown", 'Last Name': "unknown"}
student['First Name'] = str(input("What is the student's first name: "))
student['Last Name'] = str(input("What is the student's last name: "))

classroom = {'Course code': 'unknown', 'Course Name': 'unknown', 'Period': 'unknown', 'Teacher': 'unknown'}
classroom['Course Code'] = str(input("What is the Course Code: "))
classroom['Course Name'] = str(input("What is the Course Name: "))
classroom['Period'] = str(input("What is the period: "))
classroom['Teacher'] = str(input("Who is the teacher: "))


print(f"The student you choose to add to {classroom['Course Name']} is {student['First Name']} {student['Last Name']}!")



def add_student_to_classroom(student: Dict, classroom: Dict):
    """Adds student to a classroom

    Args:
        student: Student dict
        classroom: The classroom to add the student to
    """

    with open('markbook.txt', 'a') as f:
      f.read()
      classroom.append(student)
      print (f"You successfully added {student['First Name']} to {classroom['Course Code']}.") 

def remove_student_from_classroom(student: Dict, classroom: Dict):
    """Removes student from classroom

    Args:
        student: The student to be removed
        classroom: the class from which the student will be removed.
    """
    with open('markbook.txt', 'a') as f:
        f.read()
        del classroom[student]
        print (f"You successfully deleted {student['First Name']} from {classroom['Course Code']}.")


def edit_student(student: Dict, **kwargs: Dict):
    """Edits the student's info with the provided key/value pairs

    Args:
        student: The student whose data needs to be udated.
        **kwargs: KeyWordARGumentS. The key/value pairs of the
            data that needs to be changed. Can come in the form
            of a dictionary.
    """
    pass
