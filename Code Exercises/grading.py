grade = int(input("Enter your grade (0-100):"))

if grade == 100 or grade >= 95:
    print("A+")
elif grade >= 90 or grade >= 94:
    print("A")
elif grade >= 85 or grade >= 89:
    print("B+")
elif grade >= 80 or grade >= 84:
    print("B")
elif grade >= 75 or grade >= 79:
    print("C+")
elif grade >= 70 or grade >= 74:
    print("C")
elif grade >= 65 or grade >= 69:
    print("D+")
elif grade >= 60 or grade >= 64:
    print("D")
else:
    print("F")
