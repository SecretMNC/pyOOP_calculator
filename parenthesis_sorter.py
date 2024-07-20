from typing import Union

class ParenthesisSorter:
    '''Identifies grouped terms and counts nested term depth from an expression.
    Returns up to 3 grouped terms, # of () pairs and depth count per group.'''

    def __init__(self, expression: str):
        self.expr = expression
        self.num_of_terms = 0
        self.terms = []

    def __new__(self, expression: str) -> tuple[str, int]:
        self.expr = expression
        self.num_of_terms = 0
        self.terms = []

        self.find_grouped_terms(self)
        print(self.terms, "hello from PC")
        return tuple(self.terms)

    def find_grouped_terms(self) -> None: #||This function needs to be broken up||#
        '''Parses through expression string to find grouped terms.
        Tracks the number of grouped terms, # of () pairs,
        max depth of each grouped term, and in-between operators.
        Passes this info to instance variables.'''

        ops = '+-*/^' # Operator symbols for reference
        zeros = lambda x: [0 for _ in range(x)] # Sets variables to 0
        lp_, rp_, first_lp, last_rp, depth_count, op = zeros(6) # Initialize

        for pos, char in enumerate(self.expr): # Parses through expression
            if char in ops and lp_ == 0 and rp_ == 0: # Finds in-between ops
                op = char
            if char == '(': 
                if lp_ == 0: # Finds beginning of grouped term
                    first_lp = pos # Grabs position of first '(' in grouped term
                lp_ += 1
                if lp_ - rp_ > depth_count: # Detects parenthesis depth level
                    depth_count = lp_ - rp_ # Updates depth count if higher
            elif char == ')':
                rp_ += 1
            if lp_ != 0 and rp_ != 0 and lp_ == rp_: # If grouped term is complete:...
                last_rp = pos # Grabs position of last ')' in grouped term
                term = self.expr[first_lp:last_rp+1] # Grabs grouped term out of expr
                self.terms.append((term, op, lp_, depth_count)) # Appends term, # of () pairs, depth count, and op
                self.num_of_terms += 1 # Updates number of terms
                lp_, rp_, depth_count, op = zeros(4) # Resets trackers to zero

    @classmethod
    def find_inner_parenth(cls, term):
        '''Recursively finds innermost parenthesis term and returns it.'''
        lp_ = term.find('(')
        rp_ = term.rfind(')')
        return term[lp_+1:rp_]

