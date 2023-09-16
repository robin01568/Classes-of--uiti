#09/09/23

# Python exception handling
# 1. try..except
""" try:
    x = 10
    y = 0
    z = x/y

except ZeroDivisionError as e:
    print(e) """

""" try:
    num = [2, 3, 4]
    print(num[3])

except IndexError as e:
    print(e)
except ZeroDivisionError as e:
    print('It can not be divided by zero.')

# or 
except (ZeroDivisionError, IndexError):
    print('Error') """


# 2. try..except..else
""" try:
    num = int(input('Enter a number: '))
    assert num % 2 == 0                     #assert means True or False detection

except:
    print('Not an even number!')

else:
    reciprocal = 1/num
    print(reciprocal) """

""" try:
    num = int(input('Enter a number: '))
    assert num % 2 == 0

except AssertionError:
    print('Not an even number!')

else:
    try:
        half = 1/num
        print(half)
    
    except ZeroDivisionError:
        print(f'Can not be divide by {num}.') """

# 3. try..finally
""" try:
    numerator = 10
    denominator = 0

    result = numerator/denominator

    print(result)

except ZeroDivisionError:
    print('Error: Demoniator cannot be 0.')

finally:
    print('This is finally block.') """
