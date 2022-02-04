# Build a game where the computer randomly generates a secret number and the user has 3 guesses to guess the right thing
import random


# print("WELCOME TO MATTHEW GUESSING STREAK")
#
# random = random.Random()
# secret_number = random.randint(0, 9)
# chances = 3
# guess = 0
# while chances > 0:
#     guess = int(input("New number: "))
#     if guess >= 0:
#         if guess > secret_number:
#             print("Number too large")
#         elif guess < secret_number:
#             print("Number too small! Don't give up....")
#             if chances == 0:
#                 print("oops no more tries!")
#         elif guess == secret_number:
#             print("Congratulations. You made it!")
#             break
#     else:
#         print("Guess cannot be less than 0!")
#         break
#     chances -= 1
# else:
#     print(f"Secret number: {secret_number}")

#
# random = random.Random()
# secret_number = 7
# count = 1
# while True:
#     guess = random.randint(1, 9)
#     if guess == secret_number:
#         print("You finally guessed right!")
#         break
#     count += 1
# print(f"You guessed {count} times")
#
