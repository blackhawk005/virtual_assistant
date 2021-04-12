def calc():
    x = input('type first number:'.title())
    a = float(x)
    array = ['+', '-', '/', '*', 'p', '=']
    print(
        "enter * for multipliation, / for division, + for addition or - for subtraction or p for a to the power of b:".title())
    choice = input('Input operation:'.title())
    while True:
        if choice not in array:
            print('Invalid operation input'.upper())
            choice = input('Input operation:')
        else:
            break
    y = input('type second number:'.title())
    b = float(y)
    choice_1 = "0"

    # functions
    def multiply(a, b):
        return (a * b)

    def divide(a, b):
        return (a / b)

    def add(a, b):
        return (a + b)

    def sub(a, b):
        return (a - b)

    def power(a, b):
        return (a ** b)

    if choice == '*':
        c = multiply(a, b)
    elif choice == '/':
        c = divide(a, b)
    elif choice == '+':
        c = add(a, b)
    elif choice == '-':
        c = sub(a, b)
    elif choice == 'p':
        c = power(a, b)
    else:
        print('invalid operation input'.upper())

    while True:
        choice_1 = input('Input operation:')
        while True:
            if choice_1 not in array:
                print('Invalid operation input'.upper())
                choice_1 = input('Input operation:')
            else:
                break
        if choice_1 == '=':
            break
        z = input('Enter next number:')
        d = float(z)
        if choice_1 == '*':
            c = multiply(c, d)
        elif choice_1 == '/':
            c = divide(c, d)
        elif choice_1 == '+':
            c = add(c, d)
        elif choice_1 == '-':
            c = sub(c, d)
        elif choice_1 == 'p':
            c = power(c, d)
        else:
            print('invalid operation input'.upper())
    print("Final answer:", c)
calc()