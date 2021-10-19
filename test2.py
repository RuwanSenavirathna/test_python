class CreateClass(type):
    pass


class Person:
    def __init__(self, name) -> None:
        self.name = name


def person_init(self, name):
    self.name = name

def say_name(self, age):
    return f"I am {self.name}, {age} years old." 

# p = Person("Ruwan")

# print(type(p))
# print(type(Person))

# new_class = type("Person", (), {"__init__": person_init, "say_name" : say_name})
new_class = CreateClass("Person", (), {"__init__": person_init, "say_name" : say_name})


x = new_class("Ruwan Chamara")
print(x.say_name(34))