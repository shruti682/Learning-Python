# geometry managers -
# 1. pack()
# 2. grid()

from tkinter import *
from tkmacosx import Button

root = Tk()

first_number = second_number = operator = None


def handle_digit(digit):
    new = str(result_label['text']) + str(digit)
    result_label.config(text=new)


def handle_clear():
    result_label.config(text='')


def handle_operator(opr):
    global first_number, operator
    first_number = int(result_label['text'])
    print(type(first_number))
    operator = opr
    handle_clear()


def handle_equal():
    global first_number, operator, second_number
    second_number = int(result_label['text'])
    if operator == '+':
        result_label.config(text=str(first_number + second_number))
    if operator == '-':
        result_label.config(text=str(first_number - second_number))
    if operator == '*':
        result_label.config(text=str(first_number * second_number))
    if operator == '/':
        if second_number == 0:
            result_label.config(text='ERROR')
        result_label.config(text=str(round((first_number / second_number), 2)))


root.title('Calculator')
root.configure(background='white')
root.geometry('300x365')
root.resizable(0, 0)
root.resizable(0, 0)  # can not resize the window

result_label = Label(root, text='', fg='grey', bg='white')
result_label.grid(row=0, column=0, columnspan=100, pady=(40, 40), sticky='w')
result_label.config(font=('Verdana', 30, 'bold'))

btn7 = Button(root, text='7', bg='#00a65a', fg='white', width=75, height=60, command=lambda: handle_digit(7))
btn7.grid(row=1, column=0)
btn7.config(font=('Verdana', 20))

btn8 = Button(root, text='8', fg='white', bg='#00a65a', width=75, height=60, command=lambda: handle_digit(8))
btn8.grid(row=1, column=1)
btn8.config(font=('Verdana', 20))

btn9 = Button(root, text='9', bg='#00a65a', fg='white', width=75, height=60, command=lambda: handle_digit(9))
btn9.grid(row=1, column=2)
btn9.config(font=('Verdana', 20))

btn_add = Button(root, text='+', bg='#00a65a', fg='white', width=75, height=60, command=lambda: handle_operator('+'))
btn_add.grid(row=1, column=3)
btn_add.config(font=('Verdana', 20))

btn4 = Button(root, text='4', bg='#00a65a', fg='white', width=75, height=60, command=lambda: handle_digit(4))
btn4.grid(row=2, column=0)
btn4.config(font=('Verdana', 20))

btn5 = Button(root, text='5', fg='white', bg='#00a65a', width=75, height=60, command=lambda: handle_digit(5))
btn5.grid(row=2, column=1)
btn5.config(font=('Verdana', 20))

btn6 = Button(root, text='6', bg='#00a65a', fg='white', width=75, height=60, command=lambda: handle_digit(6))
btn6.grid(row=2, column=2)
btn6.config(font=('Verdana', 20))

btn_sub = Button(root, text='-', bg='#00a65a', fg='white', width=75, height=60, command=lambda: handle_operator('-'))
btn_sub.grid(row=2, column=3)
btn_sub.config(font=('Verdana', 20))

btn1 = Button(root, text='1', bg='#00a65a', fg='white', width=75, height=60, command=lambda: handle_digit(1))
btn1.grid(row=3, column=0)
btn1.config(font=('Verdana', 20))

btn2 = Button(root, text='2', fg='white', bg='#00a65a', width=75, height=60, command=lambda: handle_digit(2))
btn2.grid(row=3, column=1)
btn2.config(font=('Verdana', 20))

btn3 = Button(root, text='3', bg='#00a65a', fg='white', width=75, height=60, command=lambda: handle_digit(3))
btn3.grid(row=3, column=2)
btn3.config(font=('Verdana', 20))

btn_mul = Button(root, text='*', bg='#00a65a', fg='white', width=75, height=60, command=lambda: handle_operator('*'))
btn_mul.grid(row=3, column=3)
btn_mul.config(font=('Verdana', 20))

btn0 = Button(root, text='0', bg='#00a65a', fg='white', width=75, height=60, command=lambda: handle_digit(0))
btn0.grid(row=4, column=0)
btn0.config(font=('Verdana', 20))

btn_clear = Button(root, text='c', fg='white', bg='#00a65a', width=75, height=60, command=lambda: handle_clear())
btn_clear.grid(row=4, column=1)
btn_clear.config(font=('Verdana', 20))

btn_equal = Button(root, text='=', bg='#00a65a', fg='white', width=75, height=60, command=lambda: handle_equal())
btn_equal.grid(row=4, column=2)
btn_equal.config(font=('Verdana', 20))

btn_div = Button(root, text='/', bg='#00a65a', fg='white', width=75, height=60, command=lambda: handle_operator('/'))
btn_div.grid(row=4, column=3)
btn_div.config(font=('Verdana', 20))

root.mainloop()
