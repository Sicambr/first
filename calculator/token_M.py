""" This programm get tokents from your equation"""

class Token:
    def __init__(self,equation,sp_f,oper):
        self.eq = equation
        self.tokens = []
        self.operators = oper
        self.numbers = ".,0123456789"
        self.certain_op = sp_f
        


    def tok_M (self):
        string = ""
        type_str=''
        for i in self.eq:
            if i in self.numbers:
                if  type_str == 'variable':
                    self.tokens.append({type_str:string})
                    string = ""  
                string = string+i
                type_str = 'num'
            elif (i == ' ' or i in self.operators):
                if (string != ""):
                    self.tokens.append({type_str:string})
                    string = ""
                type_str = 'oper'
                self.tokens.append({type_str:i})
            else:
                if (string != "")and(type_str != 'variable'):
                    self.tokens.append({type_str:string})
                    string = ""
                string = string+i
                type_str = 'variable'
        if (string != ""):
            self.tokens.append({type_str:string})
            string = ""
        self.correct_toc()
        return self.tokens


    def correct_toc (self):
        for i in range(len(self.tokens)):
            if ('variable' in self.tokens[i] and
                self.tokens[i]['variable'] in self.certain_op):
                    self.tokens[i]['cert_oper']=self.tokens[i].pop('variable')
            if (self.tokens[i].get('oper',False) == '-' and
                i-1 != -1 and
                self.tokens[i-1].get('oper',False) == '-'):
                    self.tokens[i]['oper'] = '+'
                    self.tokens[i-1]['oper'] = ' '
            elif (self.tokens[i].get('oper',False) == '-' and
                i-1 != -1 and
                self.tokens[i-1].get('oper',False) == '+'):
                    self.tokens[i-1]['oper'] = ' '
            elif (self.tokens[i].get('oper',False) == '+' and
                i-1 != -1 and
                self.tokens[i-1].get('oper',False) == '+'):
                    self.tokens[i]['oper'] = '+'
                    self.tokens[i-1]['oper'] = ' '
        i = 0
        while i<len(self.tokens):
            if self.tokens[i].get('oper',False) == ' ':
                self.tokens.pop(i)
                i=i-1
            i=i+1
        return self.tokens
            

                
            
    
