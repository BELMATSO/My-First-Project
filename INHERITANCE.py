#SINGLE CLASS INHERITANCE


class Parent:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def view(self):
        print(self.name, self.age)


class Child(Parent):

    def __init__(self, name, age):
        super().__init__(name, age)
        self.name = name
        self.age = age

    def get_age(self):
        print(self.age)


ob = Child("python", 24)
ob.get_age()
ob.view()



















#MULTI-LEVEL CLASS INHERITANCE
class parent:
    def func1(self):
        print("this is option 1")

class parent2(parent):
    def func3(self):
        print("this is option 3")

class Child(parent2):
    def func2(self):
        print("this is option 2")



ob = Child()
ob.func1()
ob.func3()





















#HIERARCHIAL CLASS INHERITANCE
class parent:
    def func1(self):
        print("this is option 1")

class parent2(parent):
    def func3(self):
        print("this is option 3")

class Child(parent):
    def func2(self):
        print("this is option 2")



ob = Child()
ob1 = parent2()
ob.func1()
ob1.func1()










#HYBRID CLASS INHERITANCE
class parent:
    def func1(self):
        print("this is option 1")

class parent2(parent):
    def func3(self):
        print("this is option 3")
class parent3:
    def func4(self):
        print("this is function 4")

class Child(parent, parent3):
    def func2(self):
        print("this is option 2")



ob = Child()
ob.func1()
ob.func4()











# PYTHON SUPER FUNCTON
class parent:
    def func5(self):
        print("hello function 5")


class Child(parent):
    def func6(self):
        super().func5()
        print("hello function 6")


ob = Child()
ob.func6()








#METHOD OVERRIDING
class parent:
    def func5(self):
        print("hello function 5")


class Child(parent):
    def func5(self):
        print("hello function 6")


ob = Child()
ob.func5()
