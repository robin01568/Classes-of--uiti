##23/08/23

##STRING

# forward slice
"""x = "hello"
y = "hello"
print(x[2]) """

# forward index slice
"""x = "hello"
y = "hello"
print(y[1:4]) """

# backward index slice
"""x = "hello"
print(x[-5: -1]) """

# insert in string
"""x = "hello world"
print(x[0:5] + " " + "python") """

# string concatenation
"""x = "Hello"
y = "World"
z = x + " " + y
print(z) """

# repetation operator
"""x = "Hello" + " "
z = x * 3
print(z) """

# not in
"""x = "Hello" + " "
print('o' not in x) """

# string formating using format method
"""amount = int(input("Enter your amount: "))
message = "Your current balance is {} taka".format(amount)
print(message) """

# string formating using modulas opearator
"""amount = int(input("Enter your amount: "))
message = "Your current balance is %d taka"%(amount)
print(message) """

# string formating using f-string method
"""amount = int(input("Enter your amount: "))
message = f"Your current balance is {amount} taka"
print(message) """

# for count character length function
"""user_input = input("Enter any character: ")
x = (len(user_input))
if x >= 8:
    print("Welcome")
else:
    print("Invalid username") """

# lowercase method
"""user_input = input("Enter any character: ")
print(user_input.lower()) """

# uppercase method
"""user_input = input("Enter any character: ")
print(user_input.upper()) """

# swapcase method
"""user_input = input("Enter any character: ")
print(user_input.swapcase()) """

# capitalize method
"""user_input = input("Enter any character: ")
print(user_input.capitalize()) """

# splite method (reture as list)
"""user_input = input("Enter any character: ")
x = user_input.split()
print(x) """

# splite method length
"""user_input = input("Enter any character: ")
x = user_input.split()
print(len(x)) """