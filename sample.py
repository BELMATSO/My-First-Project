

def fact(num):

    if num == 1:
        return num
    else:
        return num * fact(num - 1)


    def pal(x):
        x1 = x[::-1]
        if x1 == x:
            return "palindrome"
        else:
            return "not palindrome"


#built-in functions
import mod1

print(dir(mod1))