print('Hi, this is lesson 3')
#inputtin 2 numbers and doing dirty stuff
try:
    print('Give me number "a"')
    a=int(input())
    print('Give me number "b"')
    b=int(input())
    #operations
    try:
        summ=a+b
        diff=a-b
        print('Summ={}',summ)
        print('Difference={}', diff)
    except Exception as e:
        print('You messed up')
        print('e')

except ValueError:
    print('I asked for numbers, man!')

else:
    print('All good, thanks for playing')

finally:
    print('Whatevs')
