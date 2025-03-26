from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def show_details(self):
        pass

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
        self.__courses = []

    def enroll_course(self, course):
        self.__courses.append(course)

    def show_courses(self):
        return ", ".join(self.__courses) if self.__courses else "No courses enrolled"

    def show_details(self):
        return f"student: {self.name}, Age: {self.age}, ID: {self.student_id}, Courses: {self.show_courses()}"


class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def show_details(self):
        return f"Teacher: {self.name}, Age: {self.age}, Subject: {self.subject}"

def display_info(person):
    print(person.show_details())

class Course:
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

    def __str__(self):
        return f"Course: {self.title}, Duration: {self.duration} months"

    def __len__(self):
        return self.duration

if __name__ == "__main__":

    student1 = Student("Alice", 20, "S1234")
    teacher1 = Teacher("Dr. Anand", 45, "Mathematics")

    student1.enroll_course("Mathematics")
    student1.enroll_course("Physics")

    display_info(student1)
    display_info(teacher1)

    course1 = Course("Python Programming", 6)
    print(course1)
    print(f"Course Duration: {len(course1)} months")