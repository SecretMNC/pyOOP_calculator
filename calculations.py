from itertools import takewhile

class Calculations:
    def __init__(self, express):
        self.express = express

    def calculate(self, term=None):
        '''Recursive function intended to handle an aribrary number of terms.
        Follows Order of Operations (referenced as ooo).
        Returns result back to the screen in CalcGUI of calculator.py.'''
        if not term:
            term = self.express
            
            
        total_ops = self.count_ops()
        #print(total_ops)
        #ooo_tuple = self.find_ops() # (exp, div, mul, sub, add) indexes of ops in self.express
        
        if '(' in term and ')' in term:
            term = self.paranthesis_calc(term)
            total_ops = self.count_ops(term)
        if total_ops > 1:
            ooo_tuple = self.find_ops(term)
            term = self.multi_op_calc(term, ooo_tuple)
        elif total_ops == 1:
            self.single_op_calc(term)
        elif total_ops == 0:
            subtotal = float(term)
            if subtotal % 1 == 0:
                total = int(subtotal)
                return str(total)
            else:
                return str(subtotal)
            
    @staticmethod
    def find_term(term, inclusive=True):
        '''Finds locations of outermost paranthesis.
        Returns expression inside the outermost paranthesis.'''
        outer_lp = term.find('(')
        outer_rp = term.rfind(')')
        if inclusive:
            return term[outer_lp+1:outer_rp]
        else:
            return term[outer_lp:outer_rp+1]

    def paranthesis_calc(self, term):
        '''Recursively finds innermost parenthesis term.
        Solves term, replaces old term with the result of the term.
        Returns updated expression.'''
        if '(' in term and ')' in term:
            inner_term = self.find_term(term)
            self.paranthesis_calc(inner_term)
        elif self.find_ops(term) > 1:
            result = self.multi_op_calc(inner_term)
            old_term = self.find_term(self.express, False)
            return self.express.replace(old_term, result)
    
    def multi_op_calc(self, term, ooo):
        exp, div, mul, sub, add = ooo
        if '^' in term:
            left, right, left_index, right_index = self.find_consts(self.express, exp)
            return self.calculate(self.express[0:left_index] + \
                                  str(float(left) ** float(right)) + \
                                  self.express[right_index:-1])
        elif '/' in term and div < mul:
            left, right, left_index, right_index = self.find_consts(self.express, div)
            return self.calculate(self.express[0:left_index] + \
                                  str(float(left) / float(right)) + \
                                  self.express[right_index:-1])
        elif '*' in term:
            left, right, left_index, right_index = self.find_consts(self.express, mul)
            return self.calculate(self.express[0:left_index] + \
                                  str(float(left) * float(right)) + \
                                  self.express[right_index:-1])
        elif '-' in term and sub < add:
            left, right, left_index, right_index = self.find_consts(self.express, sub)
            return self.calculate(self.express[0:left_index] + \
                                  str(float(left) - float(right)) + \
                                  self.express[right_index:-1])
        elif '+' in term:
            left, right, left_index, right_index = self.find_consts(self.express, add)
            print(self.express[0:left_index])
            print(self.express[right_index:-1])
            print(str(float(left) + float(right)))
            
            return self.calculate(self.express[0:left_index] + \
                                  str(float(left) + float(right)) + \
                                  self.express[right_index:-1])
        
    def single_op_calc(self, term):
        if '^' in term:
            tuple_term = term.partition('^')
            subtotal = float(tuple_term[0]) ^ float(tuple_term[2])
        elif '/' in term:
            tuple_term = term.partition('/')
            subtotal = float(tuple_term[0]) / float(tuple_term[2])
        elif '*' in term:
            tuple_term = term.partition('*')
            subtotal = float(tuple_term[0]) * float(tuple_term[2])
        elif '-' in term:
            tuple_term = term.partition('-')
            subtotal = float(tuple_term[0]) - float(tuple_term[2])
        elif '+' in term:
            tuple_term = term.partition('+')
            subtotal = float(tuple_term[0]) + float(tuple_term[2])
            print(subtotal, 'is a', type(subtotal))
        if subtotal % 1 == 0:
            return self.calculate(int(subtotal))
        else:
            return self.calculate(subtotal)

    def find_ops(self, term=None):
        if not term:
            exp = self.express.find('^')
            div = self.express.find('/')
            mul = self.express.find('*')
            sub = self.express.find('-')
            add = self.express.find('+')
            return exp, div, mul, sub, add
        else:
            exp = term.find('^')
            div = term.find('/')
            mul = term.find('*')
            sub = term.find('-')
            add = term.find('+')
            return exp, div, mul, sub, add
    
    def count_ops(self, term=None):
        if not term:
            return self.express.count('^') + \
                    self.express.count('/') + \
                    self.express.count('*') + \
                    self.express.count('-') + \
                    self.express.count('+')
        else:
            return term.count('^') + \
                    term.count('/') + \
                    term.count('*') + \
                    term.count('-') + \
                    term.count('+')
            
    @staticmethod
    def find_consts(expression, op_index):
        left_const_leng = 0
        right_const_leng = 0
        for char in expression[op_index::-1]:
            if char.isnumeric() or char == '.':
                left_const_leng += 1
        for char in expression[op_index+1::]:
            if char.isnumeric() or char == '.':
                right_const_leng += 1

        leftmost_index = op_index - left_const_leng
        rightmost_index = op_index + 1 + right_const_leng

        left_const = expression[leftmost_index:op_index]
        right_const = expression[op_index+1:rightmost_index]
        
        return left_const, right_const, leftmost_index, rightmost_index