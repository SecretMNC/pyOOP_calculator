from syntax_validator import SyntaxValidator
from parenthesis_sorter import ParenthesisSorter

class Calculate:
    '''Evaluates user expression based on Order of Operations.'''

    def __init__(self, expression: str) -> tuple:
        self.expr = expression
        self.terms, self.invalid = SyntaxValidator(self.expr)
        self.leng = len(self.terms)
        
    def __new__(self, expression):
        self.expr = expression
        self.terms, self.invalid = SyntaxValidator(self.expr)
        self.leng = len(self.terms)

        if self.invalid:
            return self.terms
        else:
            self.expo(self)
    
    def evaluate_terms(self):
        '''Views each grouped term one at a time and sends it through the OoO.'''
        simpl_expr = []
        for val in self.terms:
            strip_term = val[0].strip('(').rstrip(')')
            simpl_term = self.order_of_operations(strip_term)
            simpl_expr.append(val[1]) ; simpl_expr.append(simpl_term)

    def order_of_operations(self, term):
        
        if '(' in term:
            inner_term = ParenthesisSorter.find_inner_parenth(term)

            

    def expo(self):
        pass