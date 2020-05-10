print('Hi, this is lesson 3, give me 2 numbers >= 0')
print('CARE b will be the number by which you divide')
#inputtin 2 numbers and doing dirty stuff
while True:
    print('Give me number "a"')
    a=int(input())
    print('Give me number "b"')
    b=int(input())
    if (a*b<0):
        print('Give me numbers bigger than 0!')
    else:
        #operations
        try:
            mul=a*b
            div=a/b
            print(f'Multiplication={mul}')
            print(f'Division={div}')
        except Exception as e:
            print('You messed up')
            print('e')
        except ZeroDivisionError:
            print('Can not divide by 0!, change "b"')
        else:
            print('Thank you!')
            break
