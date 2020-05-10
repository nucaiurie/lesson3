print('Hi, this is lesson 3, give me 2 numbers >= 0')
print('We will be adding, substracting, multiplying and dividing (b - divider)')
#inputtin 2 numbers and doing dirty stuff
while True:
    try:
        print('Give me number "a"')
        a = input()
        if float(a) < 0:
            print('Number is negative')
            continue
        if float(a) > 0:
            break
    except ValueError:
        print('Not a number')

while True:
    try:
        print('Give me number "b"')
        b = input()
        if float(b) < 0:
            print('Number is negative')
            continue
        if float(b) > 0:
            break
    except ValueError:
        print('Not a number')

#operations
while True:
    try:
        summ = a + b
        sub = a - b
        print(f'Summ={summ}')
        print(f'Substraction={sub}')
        mul = a * b
        div = a / b
        print(f'Multiplication={mul}')
        print(f'Division={div}')

    except ZeroDivisionError:
        print('Can not divide by 0!, change "b"')

    except Exception as e:
        print('You messed up')
        print(e)
    else:
        print('Thank you!')
        break
