import tkinter as tk
from tkinter import messagebox

class MyGUI:
    def __init__(self):
        self.root = tk.Tk()

        self.menubar = tk.Menu(self.root)

        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Close", command=self.on_closing)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Close without question", command=exit)

        self.actionmenu = tk.Menu(self.menubar, tearoff=0)
        self.actionmenu.add_command(label="Show Message", command=self.show_message)
        
        self.menubar.add_cascade(menu=self.filemenu, label="File")
        self.menubar.add_cascade(menu=self.actionmenu, label="Action")

        self.root.config(menu=self.menubar)

        self.label = tk.Label(self.root, text="Standard Calc", font=("Consolas", 18))
        self.label.pack(padx=10, pady=10)

        self.textbox = tk.Text(self.root, height=5, font=('Consolas', 18))
        self.textbox.bind("<KeyPress>", self.shortcut)
        self.textbox.pack(padx=10, pady=10)

        self.check_state = tk.IntVar()

        self.check = tk.Checkbutton(self.root, text="Show Messagebox", font=('Consolas', 18), variable=self.check_state)
        self.check.pack(padx=10, pady=10)

        self.button = tk.Button(self.root, text="Show message", font=('Consolas', 18), command=self.show_message)
        self.button.pack(padx=10, pady=10)

        self.clearbtn = tk.Button(self.root, text="Clear", font=("Consolas", 18), command=self.clear)
        self.clearbtn.pack(padx=10, pady=10)

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()

    def show_message(self):
        if self.check_state.get() == 0:
            print(self.textbox.get('1.0', tk.END))
        else:
            messagebox.showinfo(title="Message", message=self.textbox.get('1.0', tk.END))
    
    def shortcut(self, event):
        if event.state == 16 and event.keysym == "Return":
            self.show_message()

    def on_closing(self):
        if messagebox.askyesno(title="Quit?", message="Do you really want to quit?"):
            self.root.destroy()

    def clear(self):
        self.textbox.delete('1.0', tk.END)

gui = MyGUI()


def main():
    
    
    root = tk.Tk()

    root.geometry("500x500")
    root.title("Calculator")

    header_frame = tk.Frame(root)
    header_frame.columnconfigure(0, weight=1)
    header_frame.columnconfigure(1, weight=1)
    header_frame.columnconfigure(2, weight=1)


    title = tk.Label(header_frame, text="Standard Calc", font=('Consolas', 18))
    title.grid(row=0, column=0, sticky='w')
    header_frame.pack(padx=20, pady=20)

    textbox = tk.Text(root, height=3, font=('Consolas', 16))
    textbox.pack(fill='x')

    buttonframe = tk.Frame(root)
    buttonframe.columnconfigure(0, weight=1)
    buttonframe.columnconfigure(1, weight=1)
    buttonframe.columnconfigure(2, weight=1)
    buttonframe.columnconfigure(3, weight=1)

    btn_lp = tk.Button(buttonframe, text='(', font=('Consolas', 18))
    btn_lp.grid(row=0, column=0, sticky='we')

    btn_rp = tk.Button(buttonframe, text=')', font=('Consolas', 18))
    btn_rp.grid(row=0, column=1, sticky='we')

    btn_expo = tk.Button(buttonframe, text='^', font=('Consolas', 18))
    btn_expo.grid(row=0, column=2, sticky='we')

    btn_div = tk.Button(buttonframe, text='/', font=('Consolas', 18))
    btn_div.grid(row=0, column=3, sticky='we')

    btn_mul = tk.Button(buttonframe, text='*', font=('Consolas', 18))
    btn_mul.grid(row=1, column=3, sticky='we')
    
    btn7 = tk.Button(buttonframe, text="7", font=('Consolas', 18))
    btn7.grid(row=1, column=0, sticky=tk.W+tk.E)

    btn8 = tk.Button(buttonframe, text="8", font=('Consolas', 18))
    btn8.grid(row=1, column=1, sticky=tk.W+tk.E)

    btn9 = tk.Button(buttonframe, text="9", font=('Consolas', 18))
    btn9.grid(row=1, column=2, sticky=tk.W+tk.E)

    btn4 = tk.Button(buttonframe, text="4", font=('Consolas', 18))
    btn4.grid(row=2, column=0, sticky=tk.W+tk.E)

    btn5 = tk.Button(buttonframe, text="5", font=('Consolas', 18))
    btn5.grid(row=2, column=1, sticky=tk.W+tk.E)

    btn6 = tk.Button(buttonframe, text="6", font=('Consolas', 18))
    btn6.grid(row=2, column=2, sticky=tk.W+tk.E)

    btn1 = tk.Button(buttonframe, text="1", font=('Consolas', 18))
    btn1.grid(row=3, column=0, sticky=tk.W+tk.E)

    btn2 = tk.Button(buttonframe, text="2", font=('Consolas', 18))
    btn2.grid(row=3, column=1, sticky=tk.W+tk.E)

    btn3 = tk.Button(buttonframe, text="3", font=('Consolas', 18))
    btn3.grid(row=3, column=2, sticky=tk.W+tk.E)

    btn0 = tk.Button(buttonframe, text="0", font=('Consolas', 18))
    btn0.grid(row=4, column=0, columnspan=2, sticky=tk.W+tk.E)

    btn_dec = tk.Button(buttonframe, text=".", font=('Consolas', 18))
    btn_dec.grid(row=4, column=2, sticky=tk.W+tk.E)

    btn_minus = tk.Button(buttonframe, text="-", font=('Consolas', 18))
    btn_minus.grid(row=2, column=3, sticky=tk.W+tk.E)

    btn_plus = tk.Button(buttonframe, text="+", font=('Consolas', 18))
    btn_plus.grid(row=3, column=3, sticky='news')

    btn_eq = tk.Button(buttonframe, text="=", font=('Consolas', 18))
    btn_eq.grid(row=4, column=3, sticky=tk.W+tk.E)


    buttonframe.pack(fill='both')

    root.mainloop()
    
    

if __name__ == '__main__':
    main()