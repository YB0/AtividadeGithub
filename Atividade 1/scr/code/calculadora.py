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
            
app = calculator()
app.geometry("300x275")
app.mainloop()