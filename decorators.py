# using a first class object
def func1(name):
    return f"HELLO{name}"


def func2(name):
    return f"{name}, how are you doing?"


def func3(func4):
    return func4("Dear Learner")


print(func3(func1))
print(func3(func2))


# inner functions
def func():
    print("first function")

    def func1():
        print("first child function")

    def func2():
        print("second child function")

    func2()
    func1()


func()


def function1(function):
    def wrapper():
        print("HELLO")
        function()
        print("WELCOME TO MY PYTHON DECORATOR CLASS")

    return wrapper


@function1
def function2():
    print("PYTHONISTA")


function2()


# decorator with argument
def function1(function):
    def wrapper(*args, **kwargs):
        print("WELCOME TO MY PYTHON TUTORIAL")

    return wrapper


@function1
def function2(name):
    print(f"{name}")


function2("wassem")


# fancy decorators in python
# class decorators
class square:
    def __init__(self, side):
        self._side = side

    @property
    def side(self):
        return self._side

    @side.setter
    def side(self, value):
        if value >= 0:
            self._side = value
        else:
            print("error")

    @property
    def area(self):
        return self._side ** 2

    @classmethod
    def unit_square(cls):
        return cls(1)


s = square(5)
print(s.side)
print(s.area)










#stateful decorators
#singleton class
import functools
def singleton(cls):
    @functools.wraps(cls)
    def wrapper(*args,**kwargs):
        if not wrapper.instance:
            wrapper.instance = cls(*args, *kwargs)
        return wrapper.instance
    wrapper.instance = None
    return wrapper

@singleton
class one:
    pass


#3nested docorators




#arguments in a decorator
import functools

def repeat(num):
    def decorators_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num):
                value = func(*args, **kwargs)
            return value
        return wrapper
    return decorators_repeat

@repeat(num=5)
def function(name):
    print(f"{name}")

function("python")






