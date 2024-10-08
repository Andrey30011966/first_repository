import tkinter as tk


def get_values():
    num1 = int(number1_entry.get())
    num2 = int(number2_entry.get())
    return num1, num2


def insert_velues(velue):
    answer_entry.delete(0, 'end')
    answer_entry.insert(0, str(velue))


def add():
    num1, num2 = get_values()
    res = num1 + num2
    insert_velues(res)


def sub():
    num1, num2 = get_values()
    res = num1 - num2
    insert_velues(res)


def div():
    num1, num2 = get_values()
    res = num1 / num2
    insert_velues(res)


def mul():
    num1, num2 = get_values()
    res = num1 * num2
    insert_velues(res)


window = tk.Tk()
window.title('Калькулятор')
window.geometry('350x550')
window.resizable(False, False)
button_add = tk.Button(window, text='+', width=2, height=2, command=add)
button_add.place(x=100, y=170)
button_sub = tk.Button(window, text='-', width=2, height=2, command=sub)
button_sub.place(x=150, y=170)
button_mul = tk.Button(window, text='*', width=2, height=2, command=mul)
button_mul.place(x=200, y=170)
button_div = tk.Button(window, text='/', width=2, height=2, command=div)
button_div.place(x=250, y=170)
number1_entry = tk.Entry(window, width=24)
number1_entry.place(x=100, y=75)
number2_entry = tk.Entry(window, width=24)
number2_entry.place(x=100, y=130)
answer_entry = tk.Entry(window, width=24)
answer_entry.place(x=100, y=300)
number1 = tk.Label(window, text='Введите первое число: ')
number1.place(x=100, y=55)
number2 = tk.Label(window, text='Введите второе число: ')
number2.place(x=100, y=110)
answer = tk.Label(window, text='Ответ : ')
answer.place(x=100, y=280)
window.mainloop()