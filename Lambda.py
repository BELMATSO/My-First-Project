# lambda arguments expressions
x = lambda a: a * a
print(x(3))


# lambda within user-defined functions
def A(x):
    return (lambda y: x + y)


t = A(4)
print(t(8))

##lambda within filter()
my_list = [1, 2, 3, 4, 5, 6]
newlist = list(filter(lambda a: (a / 3 == 2), my_list))  # SYNTAX: filter(function, interables)
print(newlist)

##lambda within map()
my_list = [1, 2, 3, 4, 5, 6]
p = list(map(lambda a: (a / 3 != 2), my_list))  # SYNTAX: map(function, interables)
print(p)

##lambda within reduce()
from functools import reduce

reduce(lambda a, b: a + b, [23, 56, 43, 98, 1])  # SYNTAX: reduce(function, sequence) (it adds up the whole value)

##LAMBDA FOR ALGEBRAIC EXPRESSIONS
# linear expressions
s = lambda a: a * a
s(4)
print(s)

#3X+4Y
r = lambda X,Y: 3*X+4*Y
print(r(4,7))


#quadratic equation
#(a+b)^2
x=lambda a,b:(a+b)**2
print(x(3,4))




