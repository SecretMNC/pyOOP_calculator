from tkinter import *
import calculations as c

class CalcGUI:
    def __init__(self):
        
        self.root = Tk()
        self.root.title("Basic Calculator")
        self.root.geometry('600x600')
        
        self.font = ('Consolas', 32)

        self.screen = Text(self.root, height=1, font=self.font, relief='sunken')
        self.screen.bind("<KeyPress>", self.keyboard)
        self.screen.pack(pady=10, fill='x')

        self.buttonframe = Frame(self.root)
        self.buttonframe.columnconfigure(0, weight=1)
        self.buttonframe.columnconfigure(1, weight=1)
        self.buttonframe.columnconfigure(2, weight=1)
        self.buttonframe.columnconfigure(3, weight=1)
        self.buttonframe.pack(fill='both')

        self.build_grid()

        self.valid_chars = ['0','1','2','3','4','5','6','7','8','9','.','(',')']

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()

    def on_closing(self):
        self.root.destroy()
        print("Calculator has closed.")
        
    def build_grid(self):
        '''Assembles calculator buttons, places them in a grid, and prints characters to screen'''
        self.btn_bs = Button(self.buttonframe, text='⌫', font=self.font, command=self.backspace)
        self.btn_bs.grid(row=0, column=3, sticky='we')
        
        self.btn_clear = Button(self.buttonframe, text='C', font=self.font, command=self.clear)
        self.btn_clear.grid(row=0, column=2, sticky='we')
        
        # Left parenthesis
        self.btn_lp = Button(self.buttonframe, text='(', font=self.font, command=self.lp)
        self.btn_lp.grid(row=1, column=0, sticky='we')
        # Right parenthesis
        self.btn_rp = Button(self.buttonframe, text=')', font=self.font, command=self.rp)
        self.btn_rp.grid(row=1, column=1, sticky='we')
        # Carrot/raise to the power of...
        self.btn_expo = Button(self.buttonframe, text='^', font=self.font, command=self.expo)
        self.btn_expo.grid(row=1, column=2, sticky='we')
        # Forward slash
        self.btn_div = Button(self.buttonframe, text='/', font=self.font, command=self.divide)
        self.btn_div.grid(row=1, column=3, sticky='we')

        self.btn7 = Button(self.buttonframe, text='7', font=self.font, command=self.seven)
        self.btn7.grid(row=2, column=0, sticky='we')

        self.btn8 = Button(self.buttonframe, text='8', font=self.font, command=self.eight)
        self.btn8.grid(row=2, column=1, sticky='we')

        self.btn9 = Button(self.buttonframe, text='9', font=self.font, command=self.nine)
        self.btn9.grid(row=2, column=2, sticky='we')
        # Astrisk
        self.btn_mul = Button(self.buttonframe, text='*', font=self.font, command=self.multiply)
        self.btn_mul.grid(row=2, column=3, sticky='we')

        self.btn4 = Button(self.buttonframe, text='4', font=self.font, command=self.four)
        self.btn4.grid(row=3, column=0, sticky='we')

        self.btn5 = Button(self.buttonframe, text='5', font=self.font, command=self.five)
        self.btn5.grid(row=3, column=1, sticky='we')

        self.btn6 = Button(self.buttonframe, text='6', font=self.font, command=self.six)
        self.btn6.grid(row=3, column=2, sticky='we')
        # Minus/negative
        self.btn_minus = Button(self.buttonframe, text='-', font=self.font, command=self.minus)
        self.btn_minus.grid(row=3, column=3, sticky='we')

        self.btn1 = Button(self.buttonframe, text='1', font=self.font, command=self.one)
        self.btn1.grid(row=4, column=0, sticky='we')

        self.btn2 = Button(self.buttonframe, text='2', font=self.font, command=self.two)
        self.btn2.grid(row=4, column=1, sticky='we')

        self.btn3 = Button(self.buttonframe, text='3', font=self.font, command=self.three)
        self.btn3.grid(row=4, column=2, sticky='we')
        # Add
        self.btn_plus = Button(self.buttonframe, text='+', font=self.font, command=self.plus)
        self.btn_plus.grid(row=4, column=3, sticky='news')

        self.btn0 = Button(self.buttonframe, text='0', font=self.font, command=self.zero)
        self.btn0.grid(row=5, column=0, columnspan=2, sticky='we')
        # Decimal point
        self.btn_dec = Button(self.buttonframe, text='.', font=self.font, command=self.decimal)
        self.btn_dec.grid(row=5, column=2, sticky='we')
        # Return subtotalwer
        self.btn_eq = Button(self.buttonframe, text='=', font=self.font, command=self.equals)
        self.btn_eq.grid(row=5, column=3, sticky='we')

    def screen_state(self):
        cursor_pos = self.screen.index(INSERT)
        expression = self.screen.get("1.0", END)
        op_present = any((cha in '+-*/') for cha in expression)
        return cursor_pos, op_present, expression.strip()

    def keyboard(self, event):
        if event.keysym == "Return" or event.keysym == "KP_Enter":
            self.equals()

    def backspace(self):
        '''Deletes the character directly before the cursor'''
        pos, present, term = self.screen_state()
        start_pos = round((float(pos) - 0.1), 2)
        self.screen.delete(str(start_pos), pos)

    def clear(self):
        '''Completely clears the calculator screen'''
        self.screen.delete("1.0", END)

    def zero(self):
        '''Prints '0' at cursor's position'''
        pos, present, term = self.screen_state()
        self.screen.insert(pos, 0)

    def one(self):
        '''Prints '1' at cursor's position'''
        pos, present, term = self.screen_state()
        self.screen.insert(pos, 1)

    def two(self):
        '''Prints '2' at cursor's position'''
        pos, present, term = self.screen_state()
        self.screen.insert(pos, 2)

    def three(self):
        '''Prints '3' at cursor's position'''
        pos, present, term = self.screen_state()
        self.screen.insert(pos, 3)

    def four(self):
        '''Prints '4' at cursor's position'''
        pos, present, term = self.screen_state()
        self.screen.insert(pos, 4)

    def five(self):
        '''Prints '5' at cursor's position'''
        pos, present, term = self.screen_state()
        self.screen.insert(pos, 5)

    def six(self):
        '''Prints '6' at cursor's position'''
        pos, present, term = self.screen_state()
        self.screen.insert(pos, 6)

    def seven(self):
        '''Prints '7' at cursor's position'''
        pos, present, term = self.screen_state()
        self.screen.insert(pos, 7)

    def eight(self):
        '''Prints '8' at cursor's position'''
        pos, present, term = self.screen_state()
        self.screen.insert(pos, 8)

    def nine(self):
        '''Prints '9' at cursor's position'''
        pos, present, term = self.screen_state()
        self.screen.insert(pos, 9)

    def plus(self):
        '''Prints '+' at cursor's position. If op already exists, returns answer and prints op.'''
        pos, present, term = self.screen_state()
        if not present or term[-1].isnumeric():
            self.screen.insert(pos, '+')
        elif '(' in term and term[-1] == ')' and term[-2].isnumeric():
            self.screen.insert(pos, '+')
        elif present and term[-1] in self.valid_chars:
            self.screen.delete('1.0', END)
            self.screen.insert(END, (self.calculate(term),'+'))

    def minus(self):
        '''Prints '-' at cursor's position. If an op already exists, returns answer and prints op.'''
        pos, present, term = self.screen_state()
        if not present or term[-1].isnumeric():
            self.screen.insert(pos, '-')
        elif present and '(' in term and term[-1] == ')' and term[-2].isnumeric():
            self.screen.insert(pos, '-')
        elif present and term[-1] in self.valid_chars:
            self.screen.delete('1.0', END)
            self.screen.insert(END, (self.calculate(term),'-'))

    def multiply(self):
        '''Prints '*' at cursor's position. If op already exists, returns answer and prints op.'''
        pos, present, term = self.screen_state()
        if not present or term[-1].isnumeric():
            self.screen.insert(pos, '*')
        elif present and '(' in term and term[-1] == ')' and term[-2].isnumeric():
            self.screen.insert(pos, '*')
        elif present and term[-1] in self.valid_chars:
            self.screen.delete('1.0', END)
            self.screen.insert(END, (self.calculate(term),'*'))

    def divide(self):
        '''Prints '/' at cursor's position. If op already exists, returns answer and prints op.'''
        pos, present, term = self.screen_state()
        if not present or term[-1].isnumeric():
            self.screen.insert(pos, '/')
        elif present and '(' in term and term[-1] == ')' and term[-2].isnumeric():
            self.screen.insert(pos, '/')
        elif present and term[-1] in self.valid_chars:
            self.screen.delete('1.0', END)
            self.screen.insert(END, (self.calculate(term),'/'))

    def expo(self):
        '''Prints '^' at cursor's position. If op already exists, returns answer and prints op.'''
        pos, present, term = self.screen_state()
        if not present or term[-1].isnumeric():
            self.screen.insert(pos, '^')
        elif present and '(' in term and term[-1] == ')' and term[-2].isnumeric():
            self.screen.insert(pos, '^')
        elif present and term[-1] in self.valid_chars:
            self.screen.delete('1.0', END)
            self.screen.insert(END, (self.calculate(term),'^'))

    def lp(self):
        '''Prints '(' at cursor's position'''
        pos, present, term = self.screen_state()
        self.screen.insert(pos, '(')

    def rp(self):
        '''Prints ')' at cursor's position'''
        pos, present, term = self.screen_state()
        self.screen.insert(pos, ')')

    def decimal(self):
        '''Prints '.' at cursor's position'''
        pos, present, term = self.screen_state()
        self.screen.insert(pos, '.')

    def equals(self):
        '''Deletes the displayed characters and prints the answer in its place'''
        pos, is_op_present, term = self.screen_state()
        if term[-1] in self.valid_chars and is_op_present:
            self.screen.delete('1.0', END)
            calc = c.Calculations(term.rstrip('+-*/.( '))
            self.screen.insert(END, calc.calculate())

    def calculate(self, term, term2=None):
        '''Breaks term into seperate numbers and applies op. Returns result.
        If full parenthesis is present, computes that term first.'''
        print(f'Start calculation. Current term = {term}')
        try:
            if '(' and ')' in term:
                lp_ = term.find('(')
                rp_ = term.find(')')
                _z_ = term[lp_ + 1:rp_]
                x_y = term[:lp_] + term[rp_+1:]
                print(f'Inside parenthesis. z = {_z_} x_y = {x_y}')
                term = str(self.calculate(_z_))

            if '+' in term:
                x_y = term.split('+')
                subtotal = float(x_y[0]) + float(x_y[1])
            elif '-' in term[0]:
                subtotal = float(term)
            elif '-' in term:
                x_y = term.split('-')
                subtotal = float(x_y[0]) - float(x_y[1])
            elif '*' in term:
                x_y = term.split('*')
                subtotal = float(x_y[0]) * float(x_y[1])
            elif '/' in term:
                x_y = term.split('/')
                subtotal = float(x_y[0]) / float(x_y[1])
            elif '^' in term:
                x_y = term.split('^')
                subtotal = float(x_y[0]) ** float(x_y[1])
            else:
                subtotal = int(term)
        except ValueError:
            return "Only use real numbers!"
        
        # Returns answer as int if whole number, fails gracefully if input is invalid
        try:
            if subtotal % 1 == 0:
                return int(subtotal)
            else:
                return subtotal
        except TypeError:
            return "Invalid Entry!"

            
        
        


    

