
# object 是所有类的基类（父类）可写可不写
class Person(object):  # 相当于 Person 继承了所有 object 的方法和属性
    def __init__(self, name, age):
        print("will show when creating a new person")
        self.name = name
        self.age = age

    def eat(self):
        print("Person eats.")

    def drink(self):
        print("Person drinks.")


# create an instance of Person
p = Person('zhang3', 23)

# instance call methods
p.eat()
p.drink()
