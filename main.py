print('Hi, this is lesson 3, give me 2 numbers >= 0')
print('We will be adding and substracting')
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
            summ=a+b
            sub=a-b
            print(f'Summ={summ}')
            print(f'Substraction={sub}')
        except Exception as e:
            print('You messed up')
            print('e')
        else:
            print('Thank you!')
            break