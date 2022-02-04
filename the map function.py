# map(func, iterables) SYNTAX
def new(a):
    return a * a


x = map(new, [1, 2, 3, 4])
print(x)
print(tuple(x))


# map(func, iterables) SYNTAX
def new(a, b):
    return a * b


x = map(new, [1, 2, 3, 4], [2, 3, 4, 5])
print(x)
print(tuple(x))

# using lambda functions with map functions
lst = [1, 2, 3, 4, 5]
z = list(map(lambda p: p + 3, lst))
print(z)


##FILTER FUNCTIONS
# filter(functions, iterables) SYNTAX
def new1(k):
    if k >= 3:
        return k


j = filter(new1, (1, 2, 3, 4, 5, 6, 7))
print(j)
print(tuple(j))

b = filter(lambda x: (x >= 3), (1, 2, 3, 4, 5, 6, 7))
print(list(b))

##REDUCE FUNCTION
# reduce(function,iterables)  SYNTAX
from functools import reduce


def a(x, y):
    return x + y


s = reduce(a, [1, 2, 3, 4, 5, 6, 7, 7, 8, 8])
print(s)

t = reduce(lambda q, p: q * p, [1, 2, 3, 4, 5, 6, 7, 7])
print(t)

##FILTER FUNCTION WITHIN MAP FUNCTION
c = map(lambda x: x + x, filter(lambda x: (x >= 4), [2, 3, 4, 5]))
print(tuple(c))



##MAP FUNCTION WITHIN FILTER FUNCTION
m=filter(lambda x:(x>=4),map(lambda x:x+x,[2,3,4,5,6]))
print(set(m))




##MAP() AND FILTER() WITHIN REDUCE()
o=reduce(lambda x,y:x+y, map(lambda x:x+x, filter(lambda x:(x<=4),(1,2,3,4,5,6,7))))
print(o)
