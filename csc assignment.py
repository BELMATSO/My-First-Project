# print("1. AREA OF A TRIANGLE")
# a = int(input("Enter Base of Triangle (cm):"))
# h = int(input("Enter Height of Triangle (cm):"))
# area_of_triangle = 0.5 * a * h
# print(f"The area of triangle is {area_of_triangle} cm")
#
# print("2. PERIMETER OF CIRCLE")
# r = int(input("Enter Radius of Circle (cm):"))
# print(f"The Perimeter of a Circle is {perimeter_of_circle} cm")
#
# pi = 3.142
# perimeter_of_circle = 2 * pi * r
# print("3. HERON'S FORMULA")
# s = int(input("Enter semi perimeter (cm):"))
# a = int(input("Enter length of side a (cm):"))
# b = int(input("Enter length of side b (cm):"))
# c = int(input("Enter length of side c (cm):"))
# Area_of_the_triangle = (1/2*(s*(s-a)*(s-b)*(s-c)))
# print(f"The Area of the triangle is {Area_of_the_triangle} cm")









# import random
#
# for i in range(4):
#     range_no = random.randint(1, 9)
#     number = int(input("enter number: "))
#     if number != range_no:
#         print("wrong input pls try again!")
#     else:
#         print("congrats you guessed right" )
#         break

# #list overlapping
# import random
# a= random.sample(range(1,30), 12)
# b= random.sample(range(1,30), 16)
# result = [i for i in a if i in b]
# print(result)


#
#
# year = int(input("ENTER YEAR: "))
# if year % 4 != 0:
#     print("IT IS  NOT A LEAP YEAR!")
# else:
#     print("IT'S  A LEAP YEAR !")
#     if year % 100 != 0:
#         print("IT'S  A LEAP YEAR !")
#     else:
#         print("IT'S  NOT A LEAP YEAR!")
#         if year % 400 == 0:
#             print("IT IS A LEAP YEAR!")
#         else:
#             print("IT IS NOT A LEAP YEAR!")
#
#
#
#
#







# print('''please pick one : rock scissors paper''')
#
#
#
#
# ##ROCK ,PAPER ,SCISSORS ,GAME!!
# while True:
#     game_dict ={"rock":1, "scissors": 2, "paper": 3}
#     player_a = str(input("player a : "))
#     player_b = str(input("player b : "))
#     a = game_dict.get(player_a)
#     b = game_dict.get(player_b)
#     dif = a - b
#
#     if dif in [-1,  2]:
#         print("player a wins.")
#         if str(input("Do you want to play another game, yes or no?\n"))=="yes":
#             continue
#         else:
#             print("Game Over!.")
#             break
#
#     elif dif in [-2, 1]:
#         print("player b wins.")
#         if str(input("Do you want to play another game, yes or no?\n")) == "yes":
#             continue
#         else:
#             print("Game Over!.")
#             break
#     else:
#         print("Draw.. Please Continue.")
#         print(" ")


r = [ 2,6,8,9,19,17,15,30,24,100,70,45,56,79,53]
v =[ elements for elements in r if elements % 2 != 0 ]
print(v)
