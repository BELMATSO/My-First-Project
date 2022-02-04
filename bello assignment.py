# NAME : BELLO MATTHEW ENIOLA
# DEPARTMENT: COMPUTER SCIENCE
# MATRIC NUMBER: DU/2020/10/02/O230

# write a program to check if an integer is positive or negative
digits = int(input("ENTER DIGITS : "))
if digits < 0:
    print("THIS IS A NEGATIVE INTEGER .")
elif digits > 0:
    print("THIS IS A POSITIVE INTEGER .")
else:
    print("DIGIT ENTERED IS INVALID !!")


# write a program to check if a number entered is a perfect square number or not
num = int(input("ENTER NUMBER: "))
root = round(num ** 1/2)
result = root ** 2
if result == num:
    print("THIS  NUMBER IS A PERFECT SQUARE")
else:
    print("THIS NUMBER IS NOT A PERFECT SQUARE ")


# write a program to determine if a year is leap or not
year = int(input("ENTER YEAR: "))
if (year % 4 != 0 and year % 100!= 0) or year % 400 != 0:
    print("YEAR ENTERED IS NOT A LEAP YEAR !")
else:
    print("YEAR ENTERED IS A LEAP YEAR !")


#write a program to compute the roots of a quadratic equation
import math
A = float(input("FRIST NUMBER: "))
B = float(input("SECOND NUMBER: "))
C = float(input("THIRD NUMBER: "))
D = ((B*B) - (4 * A *C))
if D < 0:
    print("INVALID ROOTS !")
else:
    print(f"value of X1 = {(-B + math.sqrt(D)) / 2 * A}")
    print(f"value of X2 = {(-B - math.sqrt(D)) / 2 * A}")














