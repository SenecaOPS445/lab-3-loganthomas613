#!/usr/bin/env python3
'''Lab 3 Inv 2 function operate '''
# Author ID: 132731225

def operate(number1, number2, operator):
    if operator == 'add':
        add = number1 + number2
        return add
    elif operator == 'subtract':
        sub = number1 - number2
        return sub
    elif operator == 'multiply':
        mul = number1 * number2
        return mul
    else:
        error = ('Error: function operator can be "add", "subtract", or "multiply"')
        return(error)


if __name__ == '__main__':
    print(operate(10, 5, 'add'))
    print(operate(10, 5, 'subtract'))
    print(operate(10, 5, 'multiply'))
    print(operate(10, 5, 'divide'))