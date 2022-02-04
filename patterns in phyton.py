# pyramid
def pattern(n):
    k = 3 * n - 3
    for i in range(0, n + 1):
        for j in range(0, k):
            print(end="  ")
        k = k - 1
        for j in range(0, i + 1):
            print("* ", end="")
        print("\r")


print(pattern(5))


# right start pattern
def pattern(n):
    for i in range(0, n):
        for j in range(0, i + 1):
            print("* ", end="")
        print("\r")
    for i in range(n, -1 + 1):
        for j in range(0, 1 + 1):
            print("* ", end="")
            print("\r")


print(pattern(7))


# left start pattern
def pattern(n):
    k = 2 * n - 2
    for i in range(0, n - 1):
        for j in range(0, k):
            print(end=" ")
        k = k - 2
        for j in range(0, i + 1):
            print("* ", end="")
        print("\r")
    k = - 1
    for i in range(n - 1, -1, -1):
        for j in range(k, -1, -1):
            print(end=" ")
        k = k + 2
        for j in range(0, i + 1):
            print("* ", end="")
        print("\r")


print(pattern(7))


# hour glass pattern
def pattern(n):
    k = 3 * n - 3
    for i in range(n, -1, -1):
        for j in range(k, 0, -1):
            print(end=" ")
        k = k + 1
        for j in range(0, i + 1):
            print("* ", end="")
        print("\r")
    k = 2 * n - 2
    for i in range(1, n + 1):
        for j in range(0, k):
            print(end="  ")
        k = k - 1
        for j in range(0, i + 1):
            print("* ", end="")
        print("\r")


print(pattern(5))


# inverse pattern
def pattern(n):
    k = n - 2
    for i in range(n, -1, -1):
        for j in range(k, 0, -1):
            print(end=" ")
        k = k + 1
        for j in range(0, i + 1):
            print("* ", end="")
        print("\r")


print(pattern(5))


# half pattern
def pattern(n):
    for i in range(0, n):
        for j in range(0, i + 1):
            print("* ", end="")
        print("\r")


print(pattern(5))

# diamond star pattern
for i in range(5):
    for j in range(5):
        if i + j == 2 or i - j == 2 or i + j == 6 or j - i == 2:
            print("*", end="")
        else:
            print(end="")
    print()


# number patterns
def pattern(n):
    x = 0
    for i in range(0, n):
        x += 1
        for j in range(0, i + 1):
            print(x, end=" ")
        print("\r")


print(pattern(7))


# pascal's triangle
def pattern(n):
    for i in range(0, n):
        for j in range(0, i + 1):
            print(function(i, j), " ", end="")
        print()


def function(n, k):
    res = 1
    if k > n - k:
        k = n - k
    for i in range(0, k):
        res = res * (n - i)
        res - res // (i + 1)
    return res


pattern(6)
