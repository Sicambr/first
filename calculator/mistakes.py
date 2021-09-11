""" Definition mis finds common mistakes you can type in
    your equation
"""

class mis:
    def __init__(self, equation, expr, sp_f, dop_e, list_v,variables):
        self.equation = equation
        self.expr = expr
        self.sp_f = sp_f
        self.dop_e = dop_e
        self.list_v = list_v
        self.variables = variables
    

    # Check syntax of parentheses    
    def mis_par(self):
        if self.equation.count('(') != self.equation.count(')'):
            self.expr['mistakes'] += 1
            self.expr['mistake' + str(self.expr['mistakes'])] = " ".join('Not \
            all parentheses are closed'.split())
        i=self.equation.count('(')
        new_equation = self.equation
        while i>0:
            if ((new_equation.partition('(')[0].endswith(self.dop_e) == False) and
                (new_equation.partition('(')[0]!='') and
                (new_equation.partition('(')[0].endswith(self.sp_f) == False)):
                self.expr['mistakes']+=1
                self.expr['mistake'+str(self.expr['mistakes'])] = " ".join('Missed \
                math operation before ('.split())
            new_equation=new_equation.partition('(')[2]
            i -= 1
        i = 0
        while i < len(self.list_v):
            if (')' in self.list_v[i].values() and
                'oper' in self.list_v[i] and i > 0): 
                if list(self.list_v[i-1].values())[0] in "-*/+^":
                    self.expr['mistakes']+=1
                    self.expr['mistake'+str(self.expr['mistakes'])] = " ".join('Missed \
                    mean between ) and math operation'.split())
                elif list(self.list_v[i-1].values())[0] in "(":
                    self.expr['mistakes']+=1
                    self.expr['mistake'+str(self.expr['mistakes'])] = " ".join('Empty \
                    parentheses'.split())
            i += 1
        return self.expr


    # Check syntax of special math functions
    def mis_oper(self):
        i = 0
        while i < len(self.list_v):
            if ('cert_oper' in self.list_v[i] and
                i >= 1 and 'oper' not in self.list_v[i-1]):
                self.expr['mistakes']+=1
                self.expr['mistake' + str(self.expr['mistakes'])] = " ".join("Missed\
                math operation before additional operation".split())
            elif ('cert_oper' in self.list_v[i] and
                i >= 1 and 'oper' in self.list_v[i-1] and
                self.list_v[i-1]['oper']==')'):
                self.expr['mistakes']+=1
                self.expr['mistake' + str(self.expr['mistakes'])] = " ".join("Missed\
                math operation before additional operation".split())
            if ('cert_oper' in self.list_v[i] and
                i < len(self.list_v)-1):
                if ('oper' not in self.list_v[i+1] or
                    'oper' in self.list_v[i+1] and
                    self.list_v[i+1]['oper'] != '('):
                    self.expr['mistakes']+=1
                    self.expr['mistake' + str(self.expr['mistakes'])] = " ".join("Missed\
                    parentheses after additional operation".split())
            if ('cert_oper' in self.list_v[i] and
                  i==len(self.list_v)-1):
                    self.expr['mistakes']+=1
                    self.expr['mistake' + str(self.expr['mistakes'])] = " ".join("Missed\
                    parentheses after additional operation".split())                
            i = i + 1
        return self.expr


    # Check correct names of variables
    def mis_var(self):    
        if self.equation.count('=')>1:
            self.expr['mistakes'] += 1
            self.expr['mistake' + str(self.expr['mistakes'])] = " ".join("You\
            can use the sign '=' only once in your equation".split())
        elif self.equation.count('=')==1:
            if self.equation.partition('=')[0].isdigit():
                self.expr['mistakes']+=1
                self.expr['mistake'+str(self.expr['mistakes'])] = " ".join("The\
                    name of your variable must include Latin letters \
                    (A-Z), not only numbers (0-9)".split())
            elif self.equation.partition('=')[0].isalnum()==False:
                self.expr['mistakes']+=1
                self.expr['mistake'+str(self.expr['mistakes'])] = " ".join(" \
                    Incorrect initialization of your variable".split())
            if self.equation.partition('=')[0].endswith(self.sp_f):
                self.expr['mistakes'] += 1
                self.expr['mistake' + str(self.expr['mistakes'])] = " ".join("The\
                    name of your variable is incorrect. This operation \
                    is for special commands.".split())
        for i in self.list_v:
            if ('variable' in i) and (i['variable'].isalnum()==False):
                self.expr['mistakes']+=1
                self.expr['mistake'+str(self.expr['mistakes'])] = " ".join("You\
                    can only use Latin letters (A-Z) and numbers \
                    (0-9) for the name of your variable".split())
        return self.expr


    #Chek right order simple operatons
    def mis_order(self):
        i = 0
        while i<(len(self.list_v)-1):
            if ('oper' in self.list_v[i] and            
                'oper' in self.list_v[i+1]):
                if self.list_v[i]['oper'] in "*/^" and self.list_v[i+1]['oper'] in "*/^":
                    self.expr['mistakes'] += 1
                    self.expr['mistake' + str(self.expr['mistakes'])] = " ".join("Missed\
                        mean between math operations".split())
                elif self.list_v[i+1]['oper'] in "/*^" and self.list_v[i]['oper'] in "=(":
                    self.expr['mistakes'] += 1
                    self.expr['mistake' + str(self.expr['mistakes'])] = " ".join("Missed\
                        mean before math operation".split())
                elif self.list_v[i]['oper'] in "*/^" and self.list_v[i+1]['oper'] in ")":
                    self.expr['mistakes'] += 1
                    self.expr['mistake' + str(self.expr['mistakes'])] = " ".join("Missed\
                        mean after math operations".split())
            i = i+1
            if (i == len(self.list_v)-1 and 'oper' in self.list_v[i] and
                self.list_v[i]['oper'] in "*+-/^"):
                self.expr['mistakes'] += 1
                self.expr['mistake' + str(self.expr['mistakes'])] = " ".join("Missed\
                mean after math operations".split())
        return self.expr

    
    #Check safe variables and correct numbers
    def mis_means(self):
        i = 0
        if (len(self.list_v)>=2 and 'variable' in self.list_v[0] and
            'oper' in self.list_v[1] and self.list_v[1]['oper'] == '='):
            i = 1
        while i<len(self.list_v):
            if ('variable' in self.list_v[i] and            
                self.list_v[i]['variable'] not in self.variables):
                self.expr['mistakes'] += 1
                self.expr['mistake' + str(self.expr['mistakes'])] = " ".join("Unkown\
                    name of variable. Type :v to check safed names in memory".split())
            if ('variable' in self.list_v[i] and
                i != 0 and self.list_v[i-1].get('oper',False) not in "/*+-^=("):
                self.expr['mistakes'] += 1
                self.expr['mistake' + str(self.expr['mistakes'])] = " ".join("Missed\
                    operation before variable".split())
            if ('num' in self.list_v[i] and
                self.list_v[i]['num'].replace(',','.').count('.')>1):
                self.expr['mistakes'] += 1
                self.expr['mistake' + str(self.expr['mistakes'])] = " ".join("There\
                    is too many points in number".split())
            i = i+1
        return self.expr
