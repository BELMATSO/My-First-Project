# STRING METHODS
# a = "".join(['m', 'a', 't', 't'])
# print(a)
# b = "MATTHEW".replace("W", "S")
# print(b)
# name = input("Name: ").strip().capitalize()
# print(name)

# len()

# NUMBERS
# import math
# math.ceil(0.1)
# math.floor(0.3)
# round(0.4)
# max(9, 13, 28, 5, 0, 15)
# min(9, 13, 28, 5, 0, 15)

# Exercise
# Calculate the circumference and area of a circle collecting an input of radius from the user
# import math
#
# radius = int(input("radius:"))
# print(f"area = {math.pi * radius * radius}")
# print(f"circumfrence = {2 * math.pi * radius}")
#
#
# length = int(input("lenght:"))
# breath = int(input("breath:"))
# print(f"perimeter = {length * breath}")

# DATA TYPES
# LISTS []
# fruits = ['mango', 'apple', 'grape']
#
#
# len(fruits)
# fruits[1]
# fruits.pop()
# fruits.append("pawpaw")
# fruits.extend(["guava", "cashew"])
# fruits.insert(2, "watermelon")
# fruits.sort()
# fruits.remove("apple")
# fruits.reverse()
# fruits[3] = "lime"
# print(fruits)

# EXERCISE
# #Collect  3 inputs and list them out in the order of ascendancy

# a = int(input("a:"))
# b = int(input("b:"))
# c = int(input("c:"))
# x1 = min(a, b, c)
# x3 = max(a, b, c)
# x2 = (a + b + c) - x1 - x3
# print("Numbers in ascending order: ", x1, x2, x3)


#
# a = int(input("a:"))
# b = int(input("b:"))
# c = int(input("c:"))
# x1 = min(a, b, c)
# x3 = max(a, b, c)
# x2 = (a + b + c) - x1 - x3
# print("Numbers in descending order: ", x3, x2, x1)

# my_list = []
# for i in range(3):
#     num = int(input("Enter Number: "))
#     my_list.append(num)
# my_list.sort()
# print(f"Ascending order: {my_list[0]}, {my_list[1]}, {my_list[2]}")

# TUPLE ()
# my_tuple = ('Tayo', 'Bashir', 'Maxwell')
# len(my_tuple)

# SET {}
# my_set = {1, 1, 2, 2, 2, 3, 4, 4, 5}
# print(my_set)

# DICTIONARY {key:value}
# my_dict = {
#     "name": "Matthew",
#     "number": 98,
#     "list": ["Me", "You"],
#     "tuple": (8, True),
#     "set": {2, 3, "Mike", False},
#     "dict": {
#         "age": 78,
#         "dob": 1998
#     }
# }
# my_dict["dict"]["age"]
# my_dict.get("dict").get("age")
# my_dict.values()
# my_dict.items()
# my_dict.keys()

# DATA TYPE CASTING
# numbers = [2, 4, 6, 1, 7, 8, 2, 4, 2, 55, 4, 5, 33, 4]
# tuple(numbers)
# set(numbers)
# list(numbers)

# IF-ELSE STATEMENTS
# num = 40
# if num < 0:
#     print("Too low")
# elif 0 < num < 7:
#     print("Close")
# elif num == 7:
#     print("Correct")
# else:
#     print("Too high")
#
# EXERCISE
# Write a program that prints a suitable message when the temperature is low, normal and hot.
# Specify the range of the temperature yourself
# while True:
#     print("press 1 to check the water temperature")
#     print("press 2 to check the atmospheric temperature")
#     option = int(input("what would you like to choose?"))
#     if option == 1:
#         normal_temp = 100
#         temp = int(input("Temp: "))
#         if temp <= 0:
#             print("IT  IS FREEZING!")
#         elif 0 < temp <= normal_temp:
#             print("THE TEMPERATURE IS NORMAL!")
#         elif temp > normal_temp:
#             print("IT  IS HOT!")
#     elif option == 2:
#         weather = int(input("Temperature: "))
#         if weather < 0:
#             print("It is freezing")
#         elif weather < 30:
#             print("Its a bit cold\nGet a warm cloth to wear")
#         elif 30 < weather < 35:
#             print("Its a good day\nHave fun!")
#         else:
#             print("Its freaking hot!!\nTake a shower")
#     else:
#         print(" PLEASE ENTER A CORRECT NUMBER!")
#
#


#
# WHILE LOOP
# count = 1
# while True:
#     print(count)
#     if count == 5:
#         break
#     else:
#         pass
#     count += 1
#
# count = 1
# while count <= 5:
#     print(count)
#     count += 1

# #FOR LOOP
# for i in range(5):
#     print(i+1)
# for character in "Matthew":
#     print(character)
# for item in [2, 4, 4]:
#     print(item)

# Print this out
# (0,0)
# (0,1)
# (0,2)
# (1,0)
# (1,1)
# (1,2)
# (2,0)
# (2,1)
# (2,2)
# for i in range(3):
#     for j in range(3):
#         print(i, j)
#
# for i in range(5):
#     if i == 2:
#         pass
#     else:
#         print(i)


#ASKS A USER FOR A NUMBER AND PRINTS ITS SQUARE LOOP(3)
for i in range(3):
    num = eval(input("ENTER A NUMBER: "))
    print("THE SQUARE OF YOUR NUMBER IS ", num*num)
print("THE LOOP IS NOW DONE.")


# print("FIND THE QUADRATIC EQUATION")
# import math
#
# val_A = int(input ("first:"))
# val_B = int(input ("second:"))
# val_C = int(input ("third:"))
# D =((val_B * val_B) - (4 * val_A * val_C))
# print(f"value of X = {(-val_B +math.sqrt(D)) / 2 * val_A}")
# print(f"value of Y = {(-val_B -math.sqrt(D))/ 2 * val_A}")

#checking what year it would be when you turn 100 yrs!
# import datetime
# current_year = datetime.date.today().year
# name = (input("NAME:"))
# age = int(input("AGE:"))
# if age < 100:
#     remaining_years = 100 - age
#     predicted_year = current_year + remaining_years
#     print(f"You will be 100yrs old in the year {predicted_year}")
#     print(f"You will be 100yrs old in the year {current_year + (100 - age)}")
# else:
#     print(age)
# #
# import datetime
# while True:
#     present_year = datetime.date.today().year
#     name = input("NAME:")
#     age = int(input("AGE:"))
#     if age <100:
#         yrs_remaining = 100 - age
#         predicted_years = present_year + yrs_remaining
#         print(f"you'll be 100 yrs on { predicted_years}")
#         break

#checking if a number if /2 is even or odd!
# for i in range(4):
#     number = int(input("NUMBER:"))
#     if number % 2 == 0:
#         print("This is an even number !")
#
#     else:
#         print("This is an odd number !")

#all the elements of the list that are less than a number
# a= [1,1,2,3,5,8,7,23,45,77,89]
# for numbers in a :
#     if numbers <5:
#         print(numbers)

#
# # printing out the list of all the divisors of a number
# digits = int(input("Enter digits:"))
# x = range(2,11)
# divisor = []
# for numbers in x:
#     if digits % numbers ==0:
#         divisor.append(numbers)
#         print(divisor)













#
#
#
#
#
# digits = int(input("enter digits:"))
# r = range(3,21)
# divisor=[]
# for numbers in r:
#     if digits % numbers == 0:
#         divisor.append(numbers )
#         print(divisor)

# a = [1, 1, 2, 3, 5, 8, 13, 21, 48, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#
# c = []
# for i in a:
#     if i not in c:
#         c.append(i)
# for j in b:
#     if j not in c:
#         c.append(j)
# print(c)

#         a.extend(b)
#         c = set(a)
#         answer = list(c)
#         print(answer)



# a = [1, 1, 2, 3, 5, 8, 13, 21, 48, 34, 55, 89]
# print(a[5:0:-1])


#
#
# # (Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)
# while True:
#     for i in range(3):
#         word = input("ENTER A WORD:")
#         word = str(word)
#         reverse =word[::-1]
#         print(reverse)
#
#         if word == reverse:
#             print("IT IS PALINDROME!!")
#             break
#         else:
#             print("IT IS NOT PALINDROME!!")



d = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b =[element for  element in d if element % 2==0]
print(b)
# if d % 2 = 0:
#     print(d.append)



# number = int(input("ENTER THE NUMBERS: "))
