import calculator
def again():
    calc_again = input('''
Do you want to calculate again?
Please type Y for YES or N for NO.
''')

    if calc_again.upper() == 'Y':
        calculator.calculator()
    elif calc_again.upper() == 'N':
        print('Thank You!')
    else:
        again()
