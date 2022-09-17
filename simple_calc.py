from tkinter import *
root = Tk()
root.title('Calculator')
root.configure(background='#dfdfdf')

answer=0
exp = ''
def any_click(number):
    operators = ['+', '-', '*', '/']
    global exp
    if len(exp):
        if exp[-1] in operators and number in operators:
            exp = exp[:-1]
            exp += str(number)
        else:
            exp += str(number)
    else:
        exp += str(number)
    field.delete(0, END)
    field.insert(0, exp)

def equals(event):
    global exp
    to_eval = field.get()
    try:
        answer = eval(to_eval)
    except ZeroDivisionError:
        answer = '--__(**)__--'
    except:
        answer = 'Are you Krazie'

    exp = str(answer)
    field.delete(0, END)
    field.insert(0,answer)

def clear_all():
    global exp
    exp = ''
    field.delete(0, END)

root.bind('<Return>', equals)
root.bind('<KP_Enter>', equals)


field = Entry(root, width=35, borderwidth=0, bg='#cacaca' )
field.grid(row=0, column=0, columnspan=4)

# field = Entry(root, width=35, borderwidth=10).grid(row=0, column=0, columnspan=4) # This does not work -_-

button_7 = Button(root, text=7, height=2,width=7, bg='#cfe7f4',activebackground='#b9dff4', fg='#416276', activeforeground='#295299', borderwidth=0,  command=lambda: any_click(7)).grid(row=1, column=0)
button_8 = Button(root, text=8, height=2,width=7, bg='#cfe7f4',activebackground='#b9dff4', fg='#416276', activeforeground='#295299', borderwidth=0,  command=lambda: any_click(8)).grid(row=1, column=1)
button_9 = Button(root, text=9, height=2,width=7, bg='#cfe7f4',activebackground='#b9dff4', fg='#416276', activeforeground='#295299', borderwidth=0,  command=lambda: any_click(9)).grid(row=1, column=2)
button_plus = Button(root, text='+', height=2,width=7, borderwidth=0, bg='#f4f4b6',activebackground='#f3f49a', fg='#76763e', activeforeground='#76763e',  command=lambda: any_click('+')).grid(row=1, column=3)

button_4 = Button(root, text=4, height=2,width=7, bg='#cfe7f4',activebackground='#b9dff4', fg='#416276', activeforeground='#295299', borderwidth=0,  command=lambda: any_click(4)).grid(row=2, column=0)
button_5 = Button(root, text=5, height=2,width=7, bg='#cfe7f4',activebackground='#b9dff4', fg='#416276', activeforeground='#295299', borderwidth=0,  command=lambda: any_click(5)).grid(row=2, column=1)
button_6 = Button(root, text=6, height=2,width=7, bg='#cfe7f4',activebackground='#b9dff4', fg='#416276', activeforeground='#295299', borderwidth=0,  command=lambda: any_click(6)).grid(row=2, column=2)
button_minus = Button(root, text='-', height=2,width=7, borderwidth=0, bg='#f4f4b6',activebackground='#f3f49a', fg='#76763e', activeforeground='#76763e',  command=lambda: any_click('-')).grid(row=2, column=3)

button_1 = Button(root, text=1, height=2,width=7, bg='#cfe7f4',activebackground='#b9dff4', fg='#416276', activeforeground='#295299', borderwidth=0,  command=lambda: any_click(1)).grid(row=3, column=0)
button_2 = Button(root, text=2, height=2,width=7, bg='#cfe7f4',activebackground='#b9dff4', fg='#416276', activeforeground='#295299', borderwidth=0,  command=lambda: any_click(2)).grid(row=3, column=1)
button_3 = Button(root, text=3, height=2,width=7, bg='#cfe7f4',activebackground='#b9dff4', fg='#416276', activeforeground='#295299', borderwidth=0,  command=lambda: any_click(3)).grid(row=3, column=2)
button_times = Button(root, text='x', width=7, height=2, borderwidth=0, bg='#f4f4b6',activebackground='#f3f49a', fg='#76763e', activeforeground='#76763e',  command=lambda: any_click('*')).grid(row=3, column=3)

button_0 = Button(root, text=0, height=2,width=7, bg='#cfe7f4',activebackground='#b9dff4', fg='#416276', activeforeground='#295299', borderwidth=0,  command=lambda: any_click(0)).grid(row=4, column=1)
button_dot = Button(root, text='.', height=2,width=7, bg='#cfe7f4',activebackground='#b9dff4', fg='#416276', activeforeground='#295299', borderwidth=0, font=('UbuntuMono Nerd Font', 12, 'bold'), command=lambda: any_click('.')).grid(row=4, column=2)
button_divide = Button(root, text='/', height=2,width=7, borderwidth=0, bg='#f4f4b6',activebackground='#f3f49a', fg='#76763e', activeforeground='#76763e',  command=lambda: any_click('/')).grid(row=4, column=3)

button_equals = Button(root, text='=', height=2,width=14, borderwidth=0, bg='#9bf4ad',activebackground='#74f48d', fg='#459153', activeforeground='#459153',  command=lambda: equals('<Return>')).grid(row=5, column=0, columnspan=2)
button_clear = Button(root, text='Clear All', height=2,width=14, borderwidth=0, bg='#f4a0a1',activebackground='#f48183', fg='#914647', activeforeground='#914647',  command=clear_all).grid(row=5, column=2, columnspan=2)

field.focus_set()
root.mainloop()
