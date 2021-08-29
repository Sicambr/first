""" This program is a simple calculator. You can use basic math operations
such as: + (addition), - (subtraction),  / (division), * (multiplication);
and additional math operations such as: ^ (exponentiation) and sqrt (square root).
You can assign variables and get the solutions of your equations.
"""

import check_my_mistakes

class SyntaxChecker:

    def __init__(self):
        self._current_pos = 0

    # checks given expr correction
    def check(self, expr):
        self._current_pos += 1
        return False


# Introduction for user
print('-*- SIMPLE CALCULATOR v1.0 -*- '.center(70))
print(' Type :h if you need help '.center(70,'*'))
print('\nEnter your equation below:')

# Main code
Eq="rsd =15 + 19 + sqrt(5/(15-5))"

list_mist={}
list_val={}
dop_ex=('+','-','/','*','^','(','=')
sp_func=('sqrt','gr')

print(check_my_mistakes.e_mistakes(Eq,list_mist,sp_func,dop_ex,list_val))

