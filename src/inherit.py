# inherit

class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print("Person eats.")


class Student(Person):  # Student inherit from Person
    pass  # 占位符，避免报错


s1 = Student('Student', 23)
print(s1.name)
print(s1.age)
s1.eat()
