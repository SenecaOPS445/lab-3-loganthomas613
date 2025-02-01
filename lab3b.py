#!/usr/bin/env python3
'''Lab 3 Part 1 script - functions'''
# Author ID: 132731225

def sum_numbers(number1, number2):
    addnumber = (number1 + number2)
    return addnumber

def subtract_numbers(number1, number2):
    subnumber = (number1 - number2)
    return subnumber
def multiply_numbers(number1, number2):
    mulnumber = (number1 * number2)
    return mulnumber
    

if __name__ == '__main__':
    print(sum_numbers(10, 5))
    print(subtract_numbers(10, 5))
    print(multiply_numbers(10, 5))