class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.gender}, {self.age} years old"

class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"Student: {self.first_name} {self.last_name}, {self.age} years old, Record Book: {self.record_book}"

class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        # Перевірка на ліміт
        if len(self.group) >= 10:
            raise ValueError("Cannot add more than 10 students to the group.")
        self.group.add(student)

    def delete_student(self, last_name):
        """Deletes a student by their last name."""
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def find_student(self, last_name):
        """Finds a student by their last name."""
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        """Returns a string representation of the group and its students."""
        all_students = "\n".join(str(student) for student in self.group)
        return f"Group: {self.number}\nStudents:\n{all_students}"

st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st3 = Student('Male', 22, 'John', 'Smith', 'AN146')
st4 = Student('Male', 24, 'Mike', 'Brown', 'AN147')
st5 = Student('Female', 23, 'Anna', 'White', 'AN148')
st6 = Student('Female', 22, 'Emma', 'Green', 'AN149')
st7 = Student('Male', 25, 'Robert', 'Lee', 'AN150')
st8 = Student('Female', 21, 'Sophia', 'Hall', 'AN151')
st9 = Student('Male', 20, 'Oliver', 'King', 'AN152')
st10 = Student('Female', 19, 'Isabella', 'Wright', 'AN153')
st11 = Student('Male', 26, 'Ethan', 'Scott', 'AN154')

gr = Group('PD1')
for student in [st1, st2, st3, st4, st5, st6, st7, st8, st9, st10]:
    gr.add_student(student)
try:
    gr.add_student(st11)
except ValueError as error_student:
    print(f"Error: {error_student}")