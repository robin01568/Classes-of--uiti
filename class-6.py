##02/09/23

# sum, max, min
""" x = [3, 5, 6, 7, 8, 9, 10]

list = sum(x)
print(list)

maximum = max(x)
print(maximum)

minimum = min(x)
print(minimum) """

# new list with unique item
""" y = [2, 2, 4, 5, 7, 6, 1, 7 ,8, 4, 8, 9]

li = []

for a in y:

    if a not in li:
        li.append(a)

print(li)

c = y.count(7)
print(c) """

# how many item in list 
""" x = [3, 5, 6, 7, 8, 9, 10]
b = 0
for a in x:
    b += 1  
print(b) """
    

## loop control statement
# break use in loop
""" nums = [3, 5, 6, 7, 8, 9, 10]

for y in nums:
    if y == 8:
        break
    print(y)

print('End of the loop.') """

# continue use in loop
""" nums = [3, 5, 6, 7, 8, 9, 10]

for y in nums:
    if y == 10:
        continue
    print(y)

print('End of the loop.') """

# pass use in loop
""" nums = [3, 5, 6, 7, 8, 9, 10]

for y in nums:
    if y == 8:
        pass
    print(y)

print('End of the loop.') """

### functional programing
## function
# function structure 1
""" def function_name():
    
    print('Hello Mottin')

function_name()         #function calling """

# function structure 2
""" def function_name(variable1, variable2):
    
    print(variable1, variable2)

function_name(3, 5) """

# function addition
""" def addition(a, b):
    sum = a + b
    print(sum)
num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
addition(num1, num2) """

# function divition
""" def divition(a, b):
    div = a / b
    print(div)

divition(6, 2) """
