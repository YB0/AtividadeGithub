import tkinter as tk

class calculator(tk.Tk):
    
    def __init__(self):
        
        super().__init__()

        self.calculation = ""

        self.text_result = tk.Text(self, height=2, width=16, font=("Arial", 24))
        self.text_result.grid(columnspan=5)

        self.create_buttons()
    
    def add_to_calculation(self, symbol):
        
        self.calculation += str(symbol)
        self.text_result.delete(1.0, "end")
        self.text_result.insert(1.0, self.calculation)
        
    def evaluate_calculation(self):
        
        try:
            
            self.calculation = str(eval(self.calculation))
            self.text_result.delete(1.0, "end")
            self.text_result.insert(1.0, self.calculation)
        
        except:

            self.clear_field()
            self.text_result.insert(1.0, "Error")

    def clear_field(self):
        
        self.calculation = ""
        self.text_result.delete(1.0, "end")

    def create_buttons(self):
        
        button_layout = [
    
            ("1", 2, 1, 1), ("2", 2, 2, 1), ("3", 2, 3, 1), ("+", 2, 4, 1),
            ("4", 3, 1, 1), ("5", 3, 2, 1), ("6", 3, 3, 1), ("-", 3, 4, 1),
            ("7", 4, 1, 1), ("8", 4, 2, 1), ("9", 4, 3, 1), ("*", 4, 4, 1),
            ("(", 5, 1, 1), ("0", 5, 2, 1), (")", 5, 3, 1), ("/", 5, 4, 1),
            ("C", 6, 1, 1), (".", 6, 2, 1), ("=", 6, 3, 2),

        ]

        for text, row, column, colspan in button_layout:

            if text == "C":

                button = tk.Button(self, text=text, command= self.clear_field, width=5, font=("Arial", 14))
                button.grid(row=row, column=column, columnspan=colspan)

            elif text == "=":

                button = tk.Button(self, text=text, command= self.evaluate_calculation, width=11, font=("Arial", 14))
                button.grid(row=row, column=column, columnspan=colspan)

            else:
    
                button = tk.Button(self, text=text, command=lambda t=text: self.add_to_calculation(t), width=5, font=("Arial", 14))
                button.grid(row=row, column=column, columnspan=colspan)
            
app = calculator()
app.geometry("300x275")
app.mainloop()