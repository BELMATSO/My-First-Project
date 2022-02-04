def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def divide(a, b):
    return a / b


import mod1 as md

result = md.add(10, 15)
print(result)

from mod1 import *
import sample as s

res = mul(20, 15)
print(res)

print(s.fact(5))




import sys

print(sys.path)




import datetime

print(datetime.date.today())