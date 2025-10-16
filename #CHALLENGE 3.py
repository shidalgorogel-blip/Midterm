#CHALLENGE 3
import csv
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def __str__(self):
        return f"Student Name: {self.name}, Age: {self.age}, Grade: {self.grade}"
    
class School:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def save_to_csv(self, filename):
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Age", "Grade"])
            for student in self.students:
                writer.writerow([student.name, student.age, student.grade])
            
    def load_from_csv(self, filename):
        with open(filename, mode='r') as file:
            reader = csv.DictReader(file)
            self.students = []
            for row in reader:
                student = Student(row["Name"], int(row["Age"]), row["Grade"])
                self.add_student(student)
    def studentsAge(self, age):
        return [student for student in self.students if student.age == age]

    def studentsFiles(self, filename):
        try:
            with open(filename, mode='r') as file:
                reader = csv.DictReader(file)
                return [row for row in reader]
        except Exception as e:
            print(f"Error reading file: {e}")
            return []
    

###########

def print_students(self):
    for student in self.students:
        print(student)

School.print_students = print_students

school = School()
school.add_student(Student("alex", 17, "12th"))
school.add_student(Student("Dan", 15, "10th"))

school.save_to_csv("students.csv")
school.load_from_csv("students.csv")

print("All Students: ")
school.print_students()

print("\nStudents aged 14: ")
for student in school.studentsAge(14):
    print(student)

print("\nStudents from file: ")
for student in school.studentsFiles("students.csv"):
    print(student)
