##28/08/23

#Loop (for loop= definite, while loop= indefinite)

# Biggest number in 3 number.
"""a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
c = int(input("Enter 3rd number: "))
if a>b and a>c:
    print("The biggest number is", a)
elif b>c and b>a:
    print("The biggest number is", b)
else:
    print("The biggest number is", c) """

# slice and index slice
"""fruits = ["mango", "apple", "jackfruit", "pinapple"]
print(fruits[2])
print(fruits[1:3])
print(fruits[0])
print(fruits[2:4]) """

#Loop   (for loop= definite, iterate objects(set,dictionary,tuple,list,string,range)
#        while loop= indefinite)


#while loop(while condition:
#               statement
#                print()
#                increment(+)/decrement(-))

""" a = 1                              #variable
b = 50                              #variable
while a <= b:                       #while condition:
    print("Hello Mottin")            #statement
    a += 1                          #increment(+)/decrement(-) """

""" x  = 1 
while x <= 10:
    print(x)
    x +=1
else:
    print("End of the while loop") """


#for loop(for variable/counter variable in range(starting, ending value:))

# range
""" for variable in range(0, 10):
    print("Hello mottin")
for variable in range(0, 10):
    print(variable)
for variable in range(10):
    print("Hello mottin") """

# tuple
""" iterable_obj = (1, 2, 3) #tuple
for a in iterable_obj:
    print(a) """

# dictionary
""" iterable_obj = {
    "id" : "motin",
    "college" : "AMDA"
} #dictionary
for a in iterable_obj:
    print(a) """

# set
""" iterable_obj = {1, 2, 3, "Mottin"} #set
for a in iterable_obj:
    print(a) """

# list
""" iterable_obj = [1, 2, 3, 4] #list
for a in iterable_obj:
    print(a)

iterable_obj = [1, 2, 3, 4] #list
for a in iterable_obj:
    print(a)
else:
    print("End of the for loop") """