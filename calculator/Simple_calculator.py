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
Eq = "d=56+789-(7/2.2)+(-(sqrt(6,7)))"
Eq = Eq.replace(' ','')

list_mist={}
list_val={}
variables={'pi':3.1415}
operators=('+','-','*', '/', '^', '=', '(', ')')
sp_func=('sqrt','gr')


tok=token_M.Token(Eq,sp_func,operators)
print(tok.tok_M())
list_val=tok.tok_M()

# Clear mistakes from the first list
list_mist.clear()
list_mist['mistakes'] = 0

mis_ex=mistakes.mis(Eq,list_mist,sp_func,operators,list_val,variables)
print(mis_ex.mis_par())
print(mis_ex.mis_oper())
print(mis_ex.mis_var())
print(mis_ex.mis_order())
print(mis_ex.mis_means())
