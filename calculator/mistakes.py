""" Definition mis finds common mistakes you can type in
    your equation
"""

def mis(equation, expr, sp_f, dop_e, list_v):

    # Clear mistakes from the first list
    equation.replace(',', '.')
    expr.clear()
    expr['mistakes'] = 0

    # Check syntax of parentheses
    if equation.count('(') != equation.count(')'):
        expr['mistakes'] += 1
        expr['mistake' + str(expr['mistakes'])] = 'Not all parentheses \
        are closed'
    i=equation.count('(')
    new_equation = equation

    while i>0:
        if ((new_equation.partition('(')[0].endswith(dop_e) == False) and
            (new_equation.partition('(')[0]!='') and
            (new_equation.partition('(')[0].endswith(sp_f) == False)):
            expr['mistakes']+=1
            expr['mistake'+str(expr['mistakes'])] = 'Missed math operation \
            before ('
        new_equation=new_equation.partition('(')[2]
        i-=1

    # Check syntax of special math functions
    for x in sp_f:
        i = equation.count(x)
        new_equation = equation
        while i > 0:
            if ((new_equation.partition(x)[0].endswith(dop_e) == False) and
                (new_equation.partition(x)[0] != '')):
                expr['mistakes']+=1
                expr['mistake'+str(expr['mistakes'])] = \
                    f'Missed math operation before { x } additional operation'

            if not new_equation.partition(x)[2].startswith('('):
                expr['mistakes'] += 1
                expr['mistake'+str(expr['mistakes'])] = \
                    f'Missed parenthesis ( after { x } additional operation'

            new_equation = new_equation.partition(x)[2]
            i -= 1

    # Check correct names of variables
    if equation.count('=')>1:
        expr['mistakes'] += 1
        expr['mistake' + str(expr['mistakes'])] = "You can use the \
        sign '=' only once in your equation"
    elif equation.count('=')==1:
        if not (equation.partition('=')[0].isalnum()):
            expr['mistakes']+=1
            expr['mistake'+str(expr['mistakes'])] = \
                "You can only use Latin letters (A-Z) and numbers \
                (0-9) for the name of your variable"

        if equation.partition('=')[0].isdigit():
            expr['mistakes']+=1
            expr['mistake'+str(expr['mistakes'])] = \
                "The name of your variable must include Latin letters \
                (A-Z), not only numbers (0-9)"

        if equation.partition('=')[0].endswith(sp_f):
            Our_ex['mistakes'] += 1
            Our_ex['mistake' + str(Our_ex['mistakes'])] = \
                "The name of your variable is incorrect. This operation \
                is for special commands."

    return expr

