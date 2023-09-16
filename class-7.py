## 04/09/23

## dictionary into dictionary data retrive and avg

# dictionary into dictionary iterete and avg values
""" def average():

    batch_2 = {
        'student_1':{
            'name' : 'Robin',
            'age' : 7,
            'session' : 'A',
            'marks' : {
                'bangla' : 50,
                'engkish' : 50,
                'math' : 50,
                'scince' : 50,
            },
            'roll' : 2,
        },
        'student_2':{
            'name' : 'Rayhan',
            'age' : 8,
            'session' : 'B',
            'marks' : {
                'bangla' : 55,
                'engkish' : 55,
                'math' : 55,
                'scince' : 55,
            },
            'roll' : 1,
        },
    }


    sum = 0
    length = 0

    student1_name = batch_2['student_1']['name']
    for x in batch_2['student_1']['marks'].values():
        sum += x
        length += 1

        avg1 = sum / length

    print(f'{student1_name} marks sum is',sum)
    print(f'{student1_name} marks length is',length)
    print(f'{student1_name} marks average is',avg1)
    print()
    
    
    student2_name = batch_2['student_2']['name']
    for x in batch_2['student_2']['marks'].values():
        sum += x
        length += 1

        avg2 = sum / length

    print(f'{student2_name} marks sum is',sum)
    print(f'{student2_name} marks length is',length)
    print(f'{student2_name} marks average is',avg2)
    print()

average() """

# 1.required positional argument (x, y)
""" def addition(x, y):
    pass


addition() """

# 2.default argument (x, y=0)
""" def addition(x, y=0):
    pass


addition(3) """

# 3.none key worded or variable length argument (*args) return as tuple
""" def addition(*args):
    sum = 0
    for x in args:
        sum += x
        
    print(sum)

addition(2, 434, 5, 6, 5.6, 0) """

# 4.key worded argument (**kwargs)  return as dictionary
""" def addition(**kwargs):
    
    print(kwargs)


addition(name='mottin',roll=12) """
