# print("Welcome to Polaris Bank ATM")
# restart = "Y"
# chances = 3
# balance = 7000.58
# while chances >= 0:
#     pin = int(input("Please Enter Your 4 Digits Pin: "))
#     if pin == 0000:
#         print("You entered your pin correctly\n")
#         while restart not in ("n", "NO", "no", "N"):
#             print("Please Press 1 for Your Balance\n")
#             print("Please Press 2 To Make A Withdrawal\n")
#             print("Please Press 3 To Pay in\n")
#             print("Please Press 4 To Return Card\n")
#             option = int(input("What Would You Like To Choose?"))
#             if option == 1:
#                 print("Your Balance is X#", balance, "\n")
#                 restart = input("Would You Like To Go Back? ")
#
#                 if restart in ("n", "NO", "no", "N"):
#                     print("THANK YOU ")
#                     break
#             elif option == 2:
#                 option2 = "y"
#                 withdrawal = float(input("How Much Would You Like To Withdraw?\nX#200/X#500/X#1000/X#5000?"))
#                 if withdrawal in [200, 500, 1000, 5000]:
#                     balance = balance - withdrawal
#                     print("\nYour Balance Is Now X#", balance)
#                     restart = input("Would You Would Like To Go Back? ")
#                     if restart in ("n", "NO", "no", "N"):
#                         print("THANK YOU ")
#                         break
#                 elif withdrawal != [200, 500, 1000, 5000]:
#                     print("Invalid Amount, Please Try Again\n")
#                     restart = "y"
#                 elif withdrawal == 1:
#                     withdrawal = float(input("Please Enter Your Desired Amount: "))
#
#             elif option == 3:
#                 pay_in = float(input("How Much Would You Like To Deposit? "))
#                 balance = balance + pay_in
#                 print("\nYour  Balance Is Now X#", balance)
#                 restart = input("Would You Like To Go Back? ")
#                 if restart in ("n", "NO", "no", "N"):
#                     print("THANK YOU ")
#                     break
#             elif option == 4:
#                 print("Please Wait While Your Card Is Returned....\n")
#                 print("Thank You For Your Service ")
#                 break
#             else:
#                 print("Please Enter A Correct Number. \n")
#                 restart = "y"
#     elif pin != 0000:
#         print("Incorrect Password ")
#         chances = chances - 1
#         if chances == 0:
#             print("\nNo More Tries")
#             break
#
#
#
#
#
