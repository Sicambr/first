""" This program is a simple calculator. You can use basic math operations
such as: + (addition), - (subtraction),  / (division), * (multiplication);
and additional math operations such as: ^ (exponentiation) and sqrt (square root).
You can assign variables and get the solutions of your equations.
"""

import mistakes
import token_M

# Introduction for user
print('-*- SIMPLE CALCULATOR v1.0 -*- '.center(70))
print(' Type :h if you need help '.center(70,'*'))
print('\nEnter your equation below:')

# Main code
Eq = "rsd=15+19+sqrt(5/(15-5.5))"

list_mist={}
list_val={}
operators=('+','-','*', '/', '^', '=', '(', ')')
sp_func=('sqrt','gr')

tok=token_M.Token(Eq,sp_func,operators)
print(tok.tok_M())
           

print(mistakes.mis(Eq,list_mist,sp_func,operators,tok))
