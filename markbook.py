"""
Markbook Application
Group members: Erica, Lisa, Judy
"""
from typing import Dict
import json
 
# Lisa
class markbook:
    def _init_(self):
        self.list = []

    def set_up(self):
        self.read_file()

    def close(self):
        self.write_file()

    def read_file(self):
        try:
            file = open('markbook.json', 'r')
            self.list = json.load(file.read())
            file.close()
        except:
            print("File missing")

    def write_file(self):
        file = open('markbook.json', 'w')
        file.write(json.dumps(self.list))
        file.close()
 
# Lisa
def create_assignment(self, name: str, due: str, points: int) -> dict:
    """Creates an assignment represented as a dictionary

    Args:
        name = "" the name of the assignment.
        due = "" the due date for the assignment.
        points = "" what the assignment is out of (denominator).
    Returns:
        Assignment as a dictionary.
    """

    assignment = {
        "assignment_name": name,
        "assignment_due": due,
        "assignment_points": points
    }

    return assignment

# Lisa
def assignment_details(slef, classroom: dict, assignment: dict) -> list:
    return [assignment.items()] # assuming that a classroom list is created

def add_student(self, first_name: str, last_name: str, gender: str, image: str,
                student_number: int, grade: int, email: str, comments: str, marks: list= []) -> dict:

    student = {
        "student_first_name": first_name,
        "student_last_name": last_name,
        "student_gender": gender,
        "student_image": image,
        "student_number": student_number,
        "student_grade": grade,
        "student_email": email,
        "student_marks": marks,
        "comments": comments
    }
    return student

# Lisa
def edit_student(student: Dict, **kwargs: Dict):
    """Edits the student's info with the provided key/value pairs

    Args:
        student: The student whose data needs to be udated.
        **kwargs: KeyWordARGumentS. The key/value pairs of the
            data that needs to be changed. Can come in the form
            of a dictionary.
    """

    student_info = {'first_name': "un-known", 'last_name': "un-known", 'student_gender': "un-known",
                    'student_number': "un-known", 'studnet_grade': "un-known", 'student_email': "un-known",
                    'student_marks': "un-known", 'comment': "un-known"}

    student_info['first_name'] = str(input("What is the first name of the student: "))
    student_info['last_name'] = str(input("What is the last name of the student: "))
    student_info['gender'] = str(input("What is the gender of the student: "))
    student_info['student_number'] = int(input("What is the student number: "))
    student_info['grade'] = int(input("What is the grade of the student: "))
    student_info['student_email'] = str(input("What is the email of the student: "))
    student_info['student_marks'] = int(input("What mark did the student get: "))
    student_info['comment'] = str(input("What is the comment: "))

# ERICA
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

# ERICA
def calculate_average_mark(student: Dict) -> float:
    """Calculates the average mark of a student"""

name_student = input("What is the full name of the student? \n")
no_of_grds = int(input("How many grades are being inputted? \n"))
total_sum = 0

for n in range(no_of_grds) :
    grades = float(input("Enter mark: "))
    total_sum += grades

avg = total_sum/no_of_grds

print(name_student , "'s average mark is" , avg)

# judy 

def add_student_to_classroom(student: Dict, classroom: Dict):
    """Adds student to a classroom

    Args:
        student: Student dict
        classroom: The classroom to add the student to
    """

    classroom.append(student)
    return classroom

# judy
    
def remove_student_from_classroom(student: Dict, classroom: Dict):
    """Removes student from classroom

    Args:
        student: The student to be removed
        classroom: the class from which the student will be removed.
    """
    with open('markbook.txt', 'a') as f:
        f.read()
        del classroom[student]
    
    return (f"You successfully deleted {name_student} from {classroom['Course code']}.")
