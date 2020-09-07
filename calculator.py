import tkinter as tk
import random as rand

#Steps to making calculator
#1. Display Keyboard on the Screen
#2. Let buttons map to numbers
#3. Build an expression with buttons
#4. Use the = to evaluate expression
           

window = tk.Tk()
window.title("Calculator")

e = tk.Entry(window,width=35,borderwidth=5)
e.grid(row=0,column=0,columnspan=4,padx=10,pady=10)


def button_click(number):
        current = e.get()
        e.delete(0,tk.END)
        e.insert(0,str(current) + str(number))

def button_clear():
        e.delete(0,tk.END)

def button_add():
        try:
                first_number = e.get()
        except:
                first_number = 0
        global f_num
        global math
        math = "addition"
        try:
                f_num = int(first_number)
        except:
                f_num = float(first_number)
        e.delete(0,tk.END)

def button_equals():
        global math
        if math == "none":
                return
        
        second_number = e.get()
        e.delete(0,tk.END)
        
        try:
                second_number = int(second_number)
        except:
                second_number = float(second_number)

        if math == "addition":
                e.insert(0, f_num+second_number)
                math = "none"
        elif math == "subtraction":
                e.insert(0, f_num-second_number)
                math = "none"
        elif math == "multiplication":
                e.insert(0, f_num*second_number)
                math = "none"
        elif math == "division":
                try:
                        if(f_num%int(second_number) == 0):
                                e.insert(0,f_num//second_number)
                        else:
                                e.insert(0, f_num/second_number)
                        math = "none"
                except:
                        e.insert(0,"Cannot divide by 0")
                        math = "none"
def button_subtract():
        try:
                first_number = e.get()
        except:
                first_number = 0
        global f_num
        global math
        math = "subtraction"
        try:
                f_num = int(first_number)
        except:
                f_num = float(first_number)
        e.delete(0,tk.END)

def button_multiply():
        try:
                first_number = e.get()
        except:
                first_number = 0
        global f_num
        global math
        math = "multiplication"
        try:
                f_num = int(first_number)
        except:
                f_num = float(first_number)
        e.delete(0,tk.END)

def button_divide():
        try:
                first_number = e.get()
        except:
                first_number = 0
        global f_num
        global math
        math = "division"
        try:
                f_num = int(first_number)
        except:
                f_num = float(first_number)
        e.delete(0,tk.END)
#Define Buttons

button_1 = tk.Button(window,text="1",padx=40,pady=20,command=lambda: button_click(1))
button_2 = tk.Button(window,text="2",padx=40,pady=20,command=lambda: button_click(2))
button_3 = tk.Button(window,text="3",padx=40,pady=20,command=lambda: button_click(3))
button_4 = tk.Button(window,text="4",padx=40,pady=20,command=lambda: button_click(4))
button_5 = tk.Button(window,text="5",padx=40,pady=20,command=lambda: button_click(5))
button_6 = tk.Button(window,text="6",padx=40,pady=20,command=lambda: button_click(6))
button_7 = tk.Button(window,text="7",padx=40,pady=20,command=lambda: button_click(7))
button_8 = tk.Button(window,text="8",padx=40,pady=20,command=lambda: button_click(8))
button_9 = tk.Button(window,text="9",padx=40,pady=20,command=lambda: button_click(9))
button_0 = tk.Button(window,text="0",padx=40,pady=20,command=lambda: button_click(0))
button_dot = tk.Button(window,text=".",padx=42,pady=20,command=lambda: button_click('.'))
button_add= tk.Button(window,text="+",padx=40,pady=20,command=button_add)
button_subtract = tk.Button(window,text="-",padx=40,pady=20,command=button_subtract)
button_multiply = tk.Button(window,text="*",padx=40,pady=20,command=button_multiply)
button_divide = tk.Button(window,text="/",padx=40,pady=20,command=button_divide)

button_equal = tk.Button(window,text="=",padx=39,pady=20,command=button_equals)
button_clear = tk.Button(window,text="ON/C",padx=27,pady=20,command=button_clear)


#Place buttons on screen

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)
button_clear.grid(row=1,column=3)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)
button_divide.grid(row=2,column=3)

button_3.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_1.grid(row=3,column=2)
button_multiply.grid(row=3,column=3)

button_0.grid(row=4,column=0)
button_dot.grid(row=4,column=1)
button_equal.grid(row=4,column=2)
button_subtract.grid(row=4,column=3)

button_add.grid(row=5,column=3)






window.mainloop()
