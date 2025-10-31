# high_income = True
# good_credit = False
# student = True

# if not student:
#     print("Eligible")
# else:
#     print("Not Eligible")

# age = 22 
# if 18 <= age < 65:
#     print("Eligible")

# For Loop

# for number in range(1, 4):
#     print("Attempt", number, number * ".")

# For else 

successful = False
for number in range(1, 4):
    print("Attempt")
    if successful:
        print("Successful")
        break
else:
    print("Attempted 3 times and failed")