from tkinter import *
root = Tk()
root.title('Calculator')

answer=0
num_list = []
num = ''
def num_click(number):
    global num
    num += str(number)
    field.delete(0, END)
    field.insert(0, num)

def operator_click(op):
    global operation
    global num_list
    global num
    if op == 'add':
        operation = 'add'
        if num:
            num_list.append(num)
            field.delete(0, END)
            num = ''
    elif op == 'sub':
        operation = 'sub'
        if num:
            num_list.append(num)
            field.delete(0, END)
            num = ''
    elif op == 'mul':
        operation = 'mul'
        if num:
            num_list.append(num)
            field.delete(0, END)
            num = ''
    else:
        operation = 'div'
        if num:
            num_list.append(num)
            field.delete(0, END)
            num = ''

def equals():
    global num_list
    global answer
    global num_list
    global num
    num_list.append(num)
    if operation == 'add':
        answer = float(num_list[0]) + float(num_list[-1])
    elif operation == 'sub':
        answer = float(num_list[0]) - float(num_list[-1])
    elif operation == 'mul':
        answer = float(num_list[0]) * float(num_list[-1])
    else:
        if float(num_list[-1]) != 0:
            answer = float(num_list[0]) / float(num_list[-1])
        else:
            answer = '---__(**)__---'
    field.delete(0, END)
    #field.insert(0,int(answer) if answer == int(answer) else answer)
    field.insert(0,answer)
    num_list = []
    num_list.append(answer)

def clear_all():
    global num_list
    global num
    num_list = []
    num = ''
    field.delete(0, END)


field = Entry(root, width=35, borderwidth=5)
field.grid(row=0, column=0, columnspan=4)

button_7 = Button(root, text=7, width=3, height=2, command=lambda: num_click(7)).grid(row=1, column=0)
button_8 = Button(root, text=8, width=3, height=2, command=lambda: num_click(8)).grid(row=1, column=1)
button_9 = Button(root, text=9, width=3, height=2, command=lambda: num_click(9)).grid(row=1, column=2)
button_plus = Button(root, text='+', width=3, height=2, command=lambda: operator_click('add')).grid(row=1, column=4)

button_4 = Button(root, text=4, width=3, height=2, command=lambda: num_click(4)).grid(row=2, column=0)
button_5 = Button(root, text=5, width=3, height=2, command=lambda: num_click(5)).grid(row=2, column=1)
button_6 = Button(root, text=6, width=3, height=2, command=lambda: num_click(6)).grid(row=2, column=2)
button_minus = Button(root, text='-', width=3, height=2, command=lambda: operator_click('sub')).grid(row=2, column=4)

button_1 = Button(root, text=1, width=3, height=2, command=lambda: num_click(1)).grid(row=3, column=0)
button_2 = Button(root, text=2, width=3, height=2, command=lambda: num_click(2)).grid(row=3, column=1)
button_3 = Button(root, text=3, width=3, height=2, command=lambda: num_click(3)).grid(row=3, column=2)
button_times = Button(root, text='x', width=3, height=2, command=lambda: operator_click('mul')).grid(row=3, column=4)

button_0 = Button(root, text=0, width=3, height=2, command=lambda: num_click(0)).grid(row=4, column=1)
button_dot = Button(root, text='.', width=3, height=2, command=lambda: num_click('.')).grid(row=4, column=2)
button_divide = Button(root, text='/', width=3, height=2, command=lambda: operator_click('div')).grid(row=4, column=4)

button_equals = Button(root, text='=', width=12, height=2, command=equals).grid(row=5, column=0, columnspan=2)
button_clear = Button(root, text='Clear All', width=12, height=2, command=clear_all).grid(row=5, column=3, columnspan=2)

root.mainloop()
