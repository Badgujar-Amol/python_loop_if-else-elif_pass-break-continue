# if-elif else ladder
i = 50
if i == 30:
    print("i is 30")
elif i == 40:
    print("i is 40")
elif i == 50:
    print("i is 50")
else:
    print("not present")

# another example
marks = int(input("Enter the marks:"))
if marks > 85 and marks <= 100:
    print("Congrats ! you scored grade A ")
elif marks > 60 and marks <= 85:
    print("You scored grade B + ")
elif marks > 40 and marks <= 60:
    print("You scored grade B ")
elif marks > 30 and marks <= 40:
    print("You scored grade C ")
else:
    print("Sorry you are FAIL")