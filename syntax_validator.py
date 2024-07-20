from typing import Union
from parenthesis_sorter import ParenthesisSorter

class InvalidSyntaxError(Exception):
    '''Custom exception for user-created syntax issues.'''

    def __init__(self, value: str) -> None:
        self.value = value

class SyntaxValidator:
    '''Validates a user expression for legal syntax and operations.'''

    def __init__(self, expression: str) -> None:


        self.expr = expression
        self.terms: list[str] = []
        
    def __new__(self, expression: str) -> Union[str, bool, list[str]]:
        '''Automatically excecutes all validation checks upon the class being called.
        Returns an error message if any check fails.
        Returns 'False' and all individual grouped terms of expression if all checks pass.'''

        self.expr = expression
        self.terms: list[str] = []

        check_0 = self.div_by_zero_check(self)
        if check_0:
            return check_0, True
        check_1 = self.missing_parenth_check(self)
        if check_1:
            return check_1, True
        check_2 = self.close_open_parenth_check(self)
        if check_2:
            return check_2, True
        check_3 = self.invalid_ops_check(self)
        if check_3:
            return check_3, True
        else:
            return self.terms, False

    def div_by_zero_check(self) -> Union[str, bool]:
        '''Checks if expression has a bare term that divides by zero.
        Returns 'False' if no term directly divides by zero.
        Handles DivideByZeroError and returns error message if division by zero is found.'''

        zero_num = '1' # Variable to change if conditions below are met
        for pos, char in enumerate(self.expr):
            try:
                if char == '0' and self.expr[pos-1] == '/':
                    zero_num = self.grab_zero_num(pos)
                if float(zero_num) == 0:
                    raise ZeroDivisionError("Div By Zero err")
            except ZeroDivisionError as zde:
                return zde

        return False

    def grab_zero_num(self, index):
        '''Parses through the expression and returns the specified number.'''

        numeric = '0123456789.'
        num_list = []
        leng = len(self.expr)
        for char in range(index, leng):
            if self.expr[char] in numeric:
                num_list.append(self.expr[char])
            else:
                return "".join(num_list)
        

    def missing_parenth_check(self) -> Union[str, bool]:
        '''Checks if the expression has an equal number of '(' and ')'.
        Returns 'False' if both open and close parenthesis are equal.
        Handles custom error and returns error message if they're not equal.'''

        lp_ = self.expr.count('(')
        rp_ = self.expr.count(')')
        try:
            if lp_ > rp_:
                raise InvalidSyntaxError("STXerr: ')' Missing")
            elif lp_ < rp_:
                raise InvalidSyntaxError("STXerr: '(' Missing")
        except InvalidSyntaxError as ise:
            return ise
        else:
            return False

    def close_open_parenth_check(self) -> Union[str, bool]:
        '''Checks if expression has a leading ')' or trailing '('.
        Returns 'False' if there are no illegally placed parenthesis.
        Handles syntax error and returns error message if one exists.'''

        parsed_expr = ParenthesisSorter(self.expr) #(("(3*(4-2))", 2, 2), ("((7-3)/4)", 2, 2))
        print(parsed_expr, "Hello from SV")
        for term in parsed_expr:
            #print(pos, term)
            try:
                if term[0][0] == ')':
                    #print(term[pos][0][0])
                    raise InvalidSyntaxError("STXerr: Leading ')'")
                elif term[0][-1] == '(':
                    #print(term[pos][-1], "hello from SV")
                    raise InvalidSyntaxError("STXerr: Trailing '('")
            except InvalidSyntaxError as ise:
                return ise
            else:
                self.terms.append(term[0])
        
        return False

    def invalid_ops_check(self) -> Union[str, bool]:
        '''Checks if expression has any illegally placed operations.
        Returns 'False' if there are no illegal operations or characters.
        Handles syntax error and returns error message if one exists.'''

        ops = '+-*/^'               # All arithmatic operations
        never_after_lp = '+*/^'     # All arithmatic operations except minus
        never_after_ops = '+-*/^)'  # All arithmatic operations and )
        valid_symbols = '+-*/^().'  # All valid non-numeric symbols
        
        for pos, char in enumerate(self.expr):
            try:
                if char == '(' and self.expr[pos+1] in never_after_lp:
                    raise InvalidSyntaxError("STXerr: Invalid Op")
                elif char in ops and self.expr[pos+1] in never_after_ops:
                    raise InvalidSyntaxError("STXerr: Invalid Op")
                elif not char.isnumeric() and char not in valid_symbols:
                    raise InvalidSyntaxError("STXerr: Invalid Character")
            except InvalidSyntaxError as ise:
                return ise
            
        return False



            



