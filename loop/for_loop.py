#  string using for loop
str = "python"
for i in str:
    print(i)

# another example
list1 = [1, 2, 3, 4, 5, 6]
for i in list1:
    print(i)

#  using range() function

for i in range(1, 15):
    print(i, end=" ")

# another example
for i in range(1, 21, 2):
    print(i)

# User input for number of rows
rows = int(input("Enter the rows:"))
for i in range(0, rows + 1):   # Outer loop will print number of rows
    for j in range(i):         # Inner loop will print number of *
         print("*", end='')
    print()

# using else statement
for i in range(0,5):
    print(i)
else:
    print("for loop completely exhausted, since there is no break.")