##30/08/23

#list, tuple, set, dictioinary

""" list item insert method 3 (new elements entry korte) """
x = [2, 3, 4, 5, 6]

# 1.append()-1 ta item entry kore data ses a entry kore
x.append(7)
print(x)

# 2.extend()- multiple item entry kore iterable 6 ti object dia work done kore
x.extend([4])
print(x)

# 3.insert()- index kore data entry kore
x.insert(0, 1)
print(x)

#update list element (i can update any thing) in square bracket i enter index value
x[0] = 'Hello'
x[5] = [3,5]
print(x)

""" list item delete korar method """
#delete list item in square bracket i enter index value
del x[0]
print(x)

#remove item exact value
x.remove('Hello')
print(x)

#pop item delete index value
x.pop(1)
print(x)

#clear list er sob item clear kore
x.clear()
print(x)

#delete hole list
del x
print(x)

##Problem:-1
#create new list and enter odd number in new list
new_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
app = []
for odd in new_list:
    if odd % 2 != 0:
        app.append(odd)
print(app)

#create new list and enter even number in new list
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_list = []
for even in num:
    if even % 2 == 0:
        new_list.append(even)
print(new_list)

##problem:-2
#check username, that the username exists or not in the list
#if usernsme exists in the list  the print "welcome to new worls!""
x = ['rahim', 'karim', 'jubayer', 'arfin']

username = input('Enter your username: ').lower()

if username in x:
    print('You are a valid user.')
else:
    print('You are not a valid user.')


""" concatanation, repetation, membership"""
#concatanation
x = [1, 2]
y = [3, 4]
z = x + y
print(z)

#repetation
a = x*2
print(a)

#membership (in, or, not)
names = ['rahim', 'karim', 'jabbar']
if 'rahim' in names:
    print('You are a valid user.')
else:
    print('You are not a valid user')


""" tuple data cannot support any kind of insert or delete but can fully clear, concate, repeat, member"""
x = (1, 2, 3, 4, 5, 6)
print(x[1])


"""dictionary data """
student = {
    'name': 'robin',
    'roll': 949,
    'semester': '5th',
    'shift': '2nd',
    'department': 'cse',
    'session': '19-20'
}

#access by key name
print(student['session'])

#replace a item value
student['registration'] = 4705
print(student)

#get method for specific item
print(student.get('shift'))

#update or add a new item
student.update({'session': '3636'})
print(student)

#pop item is work to delete last item
student.popitem()
print(student)