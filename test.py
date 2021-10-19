
class Student:

    def __init__(self, name, age, grade):
        self.name = name
        self.age = age,
        self.grade = grade # 1 - 100
        
    def get_grade(self):
        return self.grade


class Course:
    
    def __init__(self, name, max_students) -> None:
        self.name = name
        self.max_students = max_students
        self.students = []


    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
        
        return value / len(self.students)

    

s1 = Student('Ruwan', 34, 95)
s2 = Student('Bill', 35, 90)
s3 = Student('Nell', 32, 87)


course = Course('Python', 2)
course.add_student(s1)
course.add_student(s2)
# course.add_student(s3)
course.get_average_grade()


# print(course.add_student(s3))
# print(course.get_average_grade())




##....................

class Pet:
    def __init__(self, name, age):
            self.name = name
            self.age = age

    def show(self):
        print(f"I am {self.name}. and I am {self.age} years old")

    def speak(self):
        print('I am a developer')

class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print('Meow')

    def show(self):
        print(f"I am {self.name}. and I am {self.age} years old and I am {self.color}")
      
    

class Dog(Pet):

    def speak(self):
        print('Bark')


class Fish(Pet):
    pass

# p = Pet('Ruwan', 34)
# p.show()


# c = Cat('Chamara', 35, 'dark')
# c.show()
# c.speak()

# f = Fish('Tuna', 5)
# f.show()
# f.speak()


##..........................

class Person:
    number_of_people = 0

    def __init__(self, name):
        self.name = name
        Person.add_person()

    @classmethod
    def number_of_people_(cls):
        return cls.number_of_people

    @classmethod
    def  add_person(cls):
        cls.number_of_people += 1

    

# p = Person('Ruwan')
# p1 = Person('Chamara')

# print(Person.number_of_people_())
# print(Person.add_person())
# print(Person.number_of_people_())
# print("#.........")

# print(f"{p.name} and {p.number_of_people}")

# print(f"{p1.name} and {p.number_of_people}")
# print(p1.number_of_people)
# Person.number_of_people = 8

# print(p1.number_of_people)
# print(f"{p1.name} and {p.number_of_people}")

# print('####')
# p3 = Person('Chama')
# print(Person.number_of_people)
# p4 = Person('Ru')
# print(Person.number_of_people)


## ................

class Math:
    
    @staticmethod
    def add5(x):
        return x + 5
    
    @staticmethod
    def add10(x):
        return x + 10

    @staticmethod
    def pr():
        print("Run")

print(Math.add10(5))
Math.pr()