import again
def calculator():
    action = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
^ for power             
% for modulo
exp for expression
''')
    if action != 'exp':
        num1 = int(input('Please enter the first number: '))
        num2 = int(input('Please enter the second number: '))
        if action == '+':
            print('{} + {} = '.format(num1, num2))
            print(num1 + num2)
        elif action == '-':
            print('{} - {} = '.format(num1, num2))
            print(num1 - num2)
        elif action == '*':
            print('{} * {} = '.format(num1, num2))
            print(num1 * num2)
        elif action == '/':
            print('{} / {} = '.format(num1, num2))
            print(num1 / num2)   
        elif action == '^':
            print('{} ^ {} = '.format(num1, num2))
            print(num1**num2)
        elif action == '%':
            print('{} % {} ='.format(num1, num2))
            print(num1%num2)   
        else:
            print('You have not typed a valid operator, please run the program again.')
    

    else:
        calc = input("Type calculation:\n")
        print(calc + " = " + str(eval(calc)))
    # Call again() function to use calculator again
    again.again()



