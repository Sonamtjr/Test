class Person:
    def __init__(self, name, age, cid_number):
        self.name = name
        self.age = age
        self.cid_number = cid_number

    def walk(self):
        print(f"{self.name} is walking.")

    def talk(self):
        print(f"{self.name} is talking.")

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

class Teacher(Person):
    def __init__(self, name, age, cid_number, subject, salary, department, designation):
        super().__init__(name, age, cid_number)
        self.subject = subject
        self.salary = salary
        self.department = department
        self.designation = designation

    def teach(self):
        print(f"{self.name} is teaching {self.subject}.")

    def grade_students(self):
        print(f"{self.name} is grading students.")

    def attend_meeting(self):
        print(f"{self.name} is attending a meeting.")

class Student(Person):
    def __init__(self, name, age, cid_number, student_id, course, year):
        super().__init__(name, age, cid_number)
        self.student_id = student_id
        self.course = course
        self.year = year
        self.marks = []  # assuming marks will be added later

    def study(self):
        print(f"{self.name} is studying.")

    def attend_class(self):
        print(f"{self.name} is attending class.")

    def write_exam(self):
        print(f"{self.name} is writing an exam.")

    def calculate_gpa(self):
        if not self.marks:
            return 0
        return sum(self.marks) / len(self.marks)

# Creating objects
teacher1 = Teacher("Mr. Smith", 40, "123456", "Math", 50000, "Mathematics", "Senior Teacher")
student1 = Student("Alice", 20, "789012", "S1234", "Computer Science", 2)

# Using methods
teacher1.walk()
teacher1.talk()
teacher1.teach()

student1.walk()
student1.study()
student1.write_exam()
