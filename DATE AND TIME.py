# import time
#
# print(time.time())
#
# print(time.ctime(1634821304.0442784))
# help(time.time)
# print(time.localtime())
# a=time.localtime()
# b=time.mktime(a)
# print(b)
# c=time.asctime(a)
# print(c)
# help(time.strftime)
# x=time.strftime("%m/%d/%Y")
# print(x)
# y="08 August 2018"
# s=time.strptime(y, "%d %B %Y")
# print(s)



#DATETIME
import datetime

# print(datetime.datetime(2021,7,16,9,30,47,861))

u=print(datetime.datetime.today())
# print(u.year)
# print(u.month)
# print(u.hour)










#
# def multiplication(num1, num2):
#     return num1 * num2
#
#
# def addition(num1, num2):
#     return num1 * num2
#
#
# def subtraction(num1, num2):
#     return num1 - num2
#
#
# def division(num1, num2):
#     return num1 / num2
#
#
# num1 = int(input("ENTER FIRST NUMBER: "))
# num2 = int(input("ENTER SECOND NUMBER: "))
#
# print("choose operation 1-MULTIPLICATION, 2-ADDITION, 3-SUBTRACTION, 4-DIVISION")
# operation = int(input("choose operation 1/2/3/4:  "))
# if operation == 1:
#     print(num1, "*", num2, "=", multiplication(num1, num2))
#
# elif operation == 2:
#     print(num1, "+", num2, "=", addition(num1, num2))
#
# elif operation == 3:
#     print(num1, "-", num2, "=", subtraction(num1, num2))
#
# elif operation == 4:
#     print(num1, "/", num2, "=", division(num1, num2))
#
# else:
#     print("ENTER THE CORRECT OPTION!!")
