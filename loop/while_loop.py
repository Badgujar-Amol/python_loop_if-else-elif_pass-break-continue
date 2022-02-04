# 1-10 using while loop
i = 1
while i <= 10:
    print(i)
    i += 1

# 1-100 using while loop
i = 1
while i <= 100:
    print(i)
    i  += 1

# table of 2using while loop
i = 1
n = 2
while i <= 10:
    print(n , 'x', i , '=' ,n*i)
    i  += 1

# table of any number using while loop
i = 1
n = int(input('Enter number'))
while i <= 10:
    print(n , 'x', i , '=' ,n*i)
    i  += 1


# using break statement
i = 1
while i <= 10:
    print(i)
    if i==6:
        break
    i += 1

# using continue statement
i = 1
while i <= 10:
    i += 1
    if i==6:
        continue
    print(i)