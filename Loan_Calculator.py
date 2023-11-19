# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from tkinter import*
from tkinter import messagebox
#Staring function
def choose():
    loan_calc = Tk()
#geometry of dialog box
    loan_calc.geometry =("500 x 500")
    loan_calc.minsize=("900,800")
    loan_calc.maxsize=("1500,1200")
    loan_calc.title("LOAN CALCULATOR USING TKINTER")
    loan_calc.config(bg = "Light Yellow")
#Label of Heading
    loan_calc1 = Label(loan_calc,text = "Loan Calculator",bg = "Black",fg = "White",font = ("Copperplate Gothic Bold",20),borderwidth = 3)
    loan_calc1.grid(row= 0, column = 5)
#User Entry Form
    #Label of User Entry
    lca = Label(loan_calc, text="Loan Amount")
    tmd = Label(loan_calc, text="Time Duration",bg = "Light Blue")
    dwp = Label(loan_calc, text="Down Payment")
    ira = Label(loan_calc, text="Interest Rate %",bg = "Light Blue")

    lca.grid(row = 2,column = 1)
    tmd.grid(row = 3,column = 1)
    dwp.grid(row = 4,column = 1)
    ira.grid(row = 5,column = 1)
#Storing Input
    Loan_amt = StringVar()
    Time_Dur = StringVar()
    Down_Pay = StringVar()
    Int_Rat  = StringVar()
#Entry Filling Area
    La = Entry(loan_calc,textvariable = Loan_amt)
    Tm = Entry(loan_calc, textvariable=Time_Dur)
    Dp = Entry(loan_calc,textvariable = Down_Pay)
    Ir = Entry(loan_calc,textvariable = Int_Rat)

    La.grid(row = 2,column = 3)
    Tm.grid(row = 3,column = 3)
    Dp.grid(row = 4,column = 3)
    Ir.grid(row = 5,column = 3)
#Drop Down List
    types_of_loans = ["Car Loan - 7.5%", "Education Loan - 8.65%", "Gold Loan - 12%", "Home Loan - 6.70%",
                      "Personal Loan - 11%", "Others - 20%"]
    var = StringVar(loan_calc)
    var.set("Varieties of Loans")
    drop = OptionMenu(loan_calc, var, *types_of_loans)
    drop.grid(row = 1,column = 3)
    drop.config(bg= "Orange")

    choice = Label(loan_calc,text = "Types of Loans",background = "Grey")
    choice.grid(row = 1,column = 1)
#Calculating & Showing Result
    def answer():
        lm=float(Loan_amt.get())
        td=float(Time_Dur.get())
        dp=float(Down_Pay.get())
        inr=float(Int_Rat.get())
        r=inr/(12*100)
        if (inr > 20.0):
                msg1 = messagebox.showwarning("Warning","Invalid Intrest Rate") #Showing messagebox
        else:
            Dpt = (lm * 0.3)
            FA = lm - dp
            if (Dpt < dp):
                msg2 = messagebox.showwarning("Warning","Invalid Down Payment") #Showing messagebox
            else:
                EMI = (FA * r * ((1 + r) ** td) / ((1 + r) **td - 1))  #Calculating Formulae of EMI
                msg3 = messagebox.showinfo("Monthly Payment EMI",EMI)               #Showing messagebox
#Clearing Input
    def toClear():
        La.delete(0,END)
        Tm.delete(0,END)
        Dp.delete(0,END)
        Ir.delete(0,END)
#Submit Button
    B = Button(loan_calc, text="SUBMIT", command=answer,bg = "Green",fg = "White",font = ("Eras Bold ITC",10))
    B.place(x=50, y=60)
    B.grid(row = 7, column=1)
#Reset button
    B2 = Button(loan_calc, text="RESET", command=toClear,bg = "Red",fg = "White",font = ("Eras Bold ITC",10))
    B2.place(x=50, y=80)
    B2.grid(row = 7, column=3)
#this is a main loop
    loan_calc.mainloop()
#Function Calling
choose()