#!/usr/bin/python3
def print_last_digit(number):
    last = number % 10 if number > 0 else (abs(number) % 10)
    print(f'{last}', end='')
    return last
