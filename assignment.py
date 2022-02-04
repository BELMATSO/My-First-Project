# print("WELCOME TO MAT CREAM STORE.")
# quantity_of_product = int(input("quantity_of_product:"))
# product_price = 200
# gross_pay_before_discount = product_price * quantity_of_product
# discount = 20 / 100 * 200
# discount_acquired = 20 / 100 * 200 + gross_pay_before_discount
# net_pay= gross_pay_before_discount - discount
# if quantity_of_product >= 5:
#     print(gross_pay_before_discount)
#     print(discount)
#     print(net_pay)
#
# else:
#     print(gross_pay_before_discount)
# print("PAYROLL FOR CLASS NIG.LTD")
# grade_level = int(input("grade_level:"))
# number_of_years = int(input("number_of_years:"))
# basic_salary = 3000
# monthly_meal_allowance = 500
# housing_allowance = 10 / 100 * basic_salary
# transport_allowance = 7.5 / 100 * basic_salary
# entertainment_allowance = 2 / 100 * basic_salary
# long_serving_allowance = 1.5 / 100 * basic_salary
# if grade_level > 7:
#     print(f"entertainment_allowance = {entertainment_allowance}")
#     print(f"housing_allowance = {housing_allowance}")
#     print(f"transport_allowance = {transport_allowance}")
#     print(f"monthly_meal_allowance = {monthly_meal_allowance}")
# else:
#     print(f"housing_allowance = {housing_allowance}")
#     print(f"transport_allowance = {transport_allowance}")
#     print(f"monthly_meal_allowance = {monthly_meal_allowance}")
# if number_of_years >= 10:
#     print(f"long_serving_allowance = {long_serving_allowance}")
#     print(f"monthly_meal_allowance = {monthly_meal_allowance}")


#
# basic_salary = 50000
# meal_allowance = 500
# housing_allowance = 10 / 100 * basic_salary
# transport_allowance = 7.5 / 100 * basic_salary
# entertainment_allowance = 0
# long_serving_allowance = 0
# name = input("Name: ")
# grade_level = int(input("Grade Level: "))
# year_of_service = int(input("Year Of Service: "))
# if grade_level > 7:
#     entertainment_allowance = 2 / 100 * basic_salary
# if year_of_service >= 10:
#     long_serving_allowance = 1.5 / 100 * basic_salary
#
# total_salary = basic_salary + meal_allowance + housing_allowance + transport_allowance + entertainment_allowance + \
#                long_serving_allowance
#
# message = f"{'*' * 50}\n" \
#           f"Payroll Of {name.capitalize()}\n" \
#           f"{'*' * 50}\n" \
#           f"Grade Level: {grade_level}\n" \
#           f"Year Of Service: {year_of_service}\n" \
#           f"Basic Salary: #{basic_salary}\n" \
#           f"Housing Allowance: #{housing_allowance}\n" \
#           f"Transport Allowance: #{transport_allowance}\n" \
#           f"Entertainment Allowance: #{entertainment_allowance}\n" \
#           f"Long Serving Allowance: #{long_serving_allowance}\n" \
#           f"Meal Allowance: #{meal_allowance}\n" \
#           f"Total Salary: #{total_salary}\n" \
#           f"{'*' * 50}"
#
# print(message)


y = int(input("ENTER_NUMBER:"))
f = 1
for i in range(1,y+1):
    f = f * i

print(f"THE FACTORIAL OF THE NUMBER IS {f}")

# while True:
#     quantity_of_product = int(input("QUANTITY OF PRODUCT:"))
#     product_price = 5000
#     gross_pay_before_discount = quantity_of_product * product_price
#     if quantity_of_product <= 0:
#         print(f"Invalid input")
#
#     elif quantity_of_product <= 5:
#         print(f"GROSS_PAY_BEFORE_DISCOUNT = {gross_pay_before_discount:}")
#         discount = 2 / 100 * gross_pay_before_discount
#         print(f"DISCOUNT= {discount}")
#         net_pay = gross_pay_before_discount - discount
#         print(f"NET_PAY= {net_pay}")
#         break
#
#     elif quantity_of_product <=10:
#         print(f"GROSS_PAY_BEFORE_DISCOUNT = {gross_pay_before_discount}")
#         discount = 4/100 * gross_pay_before_discount
#         print(f"DISCOUNT= {discount}")
#         net_pay = gross_pay_before_discount - discount
#         print(f"NET_PAY= {net_pay}")
#         break
#
#     else:
#         print(f"GROSS_PAY_BEFORE_DISCOUNT = {gross_pay_before_discount}")
#         discount = 10/ 100 * gross_pay_before_discount
#         print(f"DISCOUNT= {discount}")
#         net_pay = gross_pay_before_discount - discount
#         print(f"NET_PAY= {net_pay}")
#         break
#

#
#
# digits = int(input("ENTER DIGITS:"))
# w= range(1,15)
# divisor =[]
# for numbers in w:
#     if digits % numbers ==0:
#         divisor.append(numbers)
#         print(divisor)

