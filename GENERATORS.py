def ex():
    n = 3
    yield n
    n = n * n
    yield n


v = ex()
for x in v:
    print(x)

# GENERATOR EXPRESSIONS
f = range(6)
print("list comp", end=":")
q = [x + 2 for x in f]
print(q)
print("gen exp", end=":")
r = (x + 2 for x in f)
print(r)

for x in r:
    print(x)

    print("gen exp", end=":")
    r = (x + 2 for x in f)
    print(r)
    print(min(r))


# FIBONACCI SERIES
def fib():
    f, s = 0, 1
    while True:
        yield f
        f, s = s, f + s


for x in fib():
    if x > 50:
        break
    print(x, end=" ")

# NUMBER STREAM
a = range(100)
b = (x for x in a)
print(b)
for y in b:
    print(y)

    # STREAM OF EVEN NUMBERS
    a = range(2, 100, 2)
    b = (x for x in a)
    print(b)
    for y in b:
        print(y)

        # STREAM OF ODD NUMBERS
        a = range(1, 100, 2)
        b = (x for x in a)
        print(b)
        for y in b:
            print(y)

##SINE WAVE
# USING THE NORMAL FUNCTION
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sb


def s(flip=2):
    x = np.linspace(0, 14, 100)
    for i in range(1, 5):
        plt.plot(x, np.sin(x + i * .5) * (7 - i) * flip)


sb.set()
s()
plt.show()
