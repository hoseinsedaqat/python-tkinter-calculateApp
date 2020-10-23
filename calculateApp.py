from tkinter import *
import tkinter.messagebox


# ============================= Settings Tkinter ===========================
root = Tk()
root.geometry('400x200')
root.title('calculateApp')
root.resizable(width=False, height=False)
color = '#ddd'
root.configure(bg=color)
# ============================= variables ==================================
num1 = StringVar()
num2 = StringVar()
resultValue = StringVar()

# ============================= Frames =====================================
top_first = Frame(root, width=400, height=50, bg=color)
top_first.pack(side=TOP)

top_second = Frame(root, width=400, height=50, bg=color)
top_second.pack(side=TOP)

top_third = Frame(root, width=400, height=50, bg=color)
top_third.pack(side=TOP)

top_forth = Frame(root, width=400, height=50, bg=color)
top_forth.pack(side=TOP)
# ============================= functions ==============================


def errorMsg(msg):
    if msg == 'Error':
        tkinter.messagebox.showerror('Error', 'Something is Wrong !!!')
    elif msg == 'divide 0 base Error':
        tkinter.messagebox.showerror('Division Error', 'Can Not Divide by 0')


def plus():
    try:
        value = float(num1.get()) + float(num2.get())
        resultValue.set(value)
    except:
        errorMsg('Error')


def minus():
    try:
        value = float(num1.get()) - float(num2.get())
        resultValue.set(value)
    except:
        errorMsg('Enter')


def mul():
    try:
        value = float(num1.get()) * float(num2.get())
        resultValue.set(value)
    except:
        errorMsg('Error')


def div():
    if num2.get() == '0':
        errorMsg('divide 0 base Error')
    elif num2.get() != '0':
        try:
            value = float(num1.get()) / float(num2.get())
            resultValue.set(value)
        except:
            errorMsg('Error')


# ============================= Button =====================================
btn_plus = Button(top_third, text='+', width=10,
                  highlightbackground=color, command=lambda: plus())
btn_plus.pack(side=LEFT, padx=10, pady=10)

btn_minus = Button(top_third, text='-', width=10,
                   highlightbackground=color, command=lambda: minus())
btn_minus.pack(side=LEFT, padx=10, pady=10)

btn_mul = Button(top_third, text='*', width=10,
                 highlightbackground=color, command=lambda: mul())
btn_mul.pack(side=LEFT, padx=10, pady=10)

btn_div = Button(top_third, text='/', width=10,
                 highlightbackground=color, command=lambda: div())
btn_div.pack(side=LEFT, padx=10, pady=10)

# ============================= Entries & Labels =============================

# Entries & Labels for Number 1
labelFirstNum = Label(top_first, text="Input Number 1: ", bg=color)
labelFirstNum.pack(side=LEFT, pady=10)

entriesFirstNum = Entry(
    top_first, highlightbackground=color, textvariable=num1)
entriesFirstNum.pack(side=LEFT, padx=10)

# Entries & Labels for Number 2
labelSecondNum = Label(top_second, text="Input Number 2: ", bg=color)
labelSecondNum.pack(side=LEFT, pady=10)

entriesSecondNum = Entry(
    top_second, highlightbackground=color, textvariable=num2)
entriesSecondNum.pack(side=LEFT, padx=10)

# Entries & Labels for Results
labelResultNum = Label(top_forth, text="Result : ", bg=color)
labelResultNum.pack(side=LEFT)

entriesResultNum = Entry(
    top_forth, width=40, highlightbackground=color, textvariable=resultValue)
entriesResultNum.pack(side=LEFT)

root.mainloop()
