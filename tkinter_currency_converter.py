from tkinter import *
class MyGui:
    def __init__(self):
        self.window = Tk()
        self.window.title("Currency Converter")
        self.window.geometry('500x250')
        self.i = IntVar()
        self.e = IntVar()
        self.a = IntVar()
        self.s = IntVar()
        self.g = IntVar()
        self.label = Label(self.window, text="Enter currency in Dollars $ ", font=('Arial', 14)).grid(row=1)
        self.e1 = Entry(self.window, font=('Arial', 15))
        self.e1.grid(row=1, column=1)
        self.e1.focus()
        self.bt = Button(self.window, text="Convert", bg='black',
        fg="white",
        command=lambda: (self.calculate_inr(),
        self.calculate_aed(), self.calculate_eur(),
        self.calculate_gbp(),
        self.calculate_sar()), font=('Arial', 12)).grid(row=2,
        column=1)
        # INR
        self.label2 = Label(self.window, text="Currency in (INR) ", font=('Arial', 14, 'italic')).grid(row=3)
        self.e2 = Entry(self.window, textvariable=self.i,
        font=('Arial', 15, 'italic')).grid(row=3, column=1)
        # EUR
        self.label3 = Label(self.window, text="Currency in (EUR) ", font=('Arial', 14, 'italic')).grid(row=4)
        self.e3 = Entry(self.window, textvariable=self.e,
        font=('Arial', 15, 'italic')).grid(row=4, column=1)
        # AED
        self.label4 = Label(self.window, text="Currency in (AED) ", font=('Arial', 14, 'italic')).grid(row=5)
        self.e4 = Entry(self.window, textvariable=self.a,
        font=('Arial', 15, 'italic')).grid(row=5, column=1)
        # SAR
        self.label5 = Label(self.window, text="Currency in (SAR) ", font=('Arial', 14, 'italic')).grid(row=6)
        self.e5 = Entry(self.window, textvariable=self.s,
        font=('Arial', 15, 'italic')).grid(row=6, column=1)
        # GBP
        self.label6 = Label(self.window, text="Currency in (GBP) ", font=('Arial', 14, 'italic')).grid(row=7)
        self.e6 = Entry(self.window, textvariable=self.g,
        font=('Arial', 15, 'italic')).grid(row=7, column=1)
        mainloop()
    def calculate_inr(self):
        self.i.set(round(float(self.e1.get()) * 71.53, 2))
    def calculate_eur(self):
        self.e.set(round(float(self.e1.get()) * 0.92, 2))
    def calculate_aed(self):
        self.a.set(round(float(self.e1.get()) * 3.67, 2))
    def calculate_sar(self):
        self.s.set(round(float(self.e1.get()) * 3.75, 2))
    def calculate_gbp(self):
        self.g.set(round(float(self.e1.get()) * 0.77, 2))

my_gui = MyGui()
