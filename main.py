import tkinter as tk


calculation = ''


def add_to_calculation(symbol):
    global calculation
    calculation += symbol
    text_field.delete("1.0", 'end')
    text_field.insert(1.0, calculation)


def evaluate_calculation():
    global calculation
    calculation = calculation.replace('÷', '/')
    calculation = calculation.replace(',', '.')
    calculation = calculation.replace('×', '*')
    try:
        calculation = str(eval(calculation))
        text_field.delete(1.0, 'end')
        # TODO: Trying to return intrhrt value if both  operands are integers.
        text_field.insert(1.0, calculation)
    except ZeroDivisionError:
        text_field.delete(1.0, 'end')
        text_field.insert(1.0, 'division by zero')
    except SyntaxError:
        text_field.insert('end', '*')


def clear_expression():
    global calculation
    text_field.delete(1.0, 'end')
    calculation = ''


window = tk.Tk()
window.geometry('320x190')

text_field = tk.Text(window, height=2, width=20, font=('Ubuntu Light', 20))
text_field.grid(columns=5)

btn_1 = tk.Button(window, text='7', command=lambda: add_to_calculation('7'),
                  width=4, font=('Ubuntu Light', 10))
btn_1.grid(row=2, column=0)

btn_2 = tk.Button(window, text='8', command=lambda: add_to_calculation('8'),
                  width=4, font=('Ubuntu Light', 10))
btn_2.grid(row=2, column=1)

btn_3 = tk.Button(window, text='9', command=lambda: add_to_calculation('9'),
                  width=4, font=('Ubuntu Light', 10))
btn_3.grid(row=2, column=2)

button_for_divide = tk.Button(window, text='÷',
                              command=lambda: add_to_calculation('÷'),
                              width=4, font=('Ubuntu Light', 10))
button_for_divide.grid(row=2, column=3)

button_for_clear_expression = tk.Button(
                window, text='Clear', bg='red', fg='white', width=4,
                command=clear_expression,
                font=('Ubuntu Light', 10))
button_for_clear_expression.grid(row=2, column=4)

btn_4 = tk.Button(window, text='4', command=lambda: add_to_calculation('4'),
                  width=4, font=('Ubuntu Light', 10))
btn_4.grid(row=3, column=0)

btn_5 = tk.Button(window, text='5', command=lambda: add_to_calculation('5'),
                  width=4, font=('Ubuntu Light', 10))
btn_5.grid(row=3, column=1)

btn_6 = tk.Button(window, text='6', command=lambda: add_to_calculation('6'),
                  width=4, font=('Ubuntu Light', 10))
btn_6.grid(row=3, column=2)

button_for_multiplication = tk.Button(window, text='×',
                                      command=lambda: add_to_calculation('×'),
                                      width=4, font=('Ubutnu Light', 10))
button_for_multiplication.grid(row=3, column=3)

button_for_open_parenthess = tk.Button(
                    window, text='(', command=lambda: add_to_calculation('('),
                    width=4, font=('Ubuntu Light', 10))
button_for_open_parenthess.grid(row=3, column=4)

btn_7 = tk.Button(window, text='1', command=lambda: add_to_calculation('1'),
                  width=4, font=('Ubuntu Light', 10))
btn_7.grid(row=4, column=0)

btn_10 = tk.Button(window, text='2', command=lambda: add_to_calculation('2'),
                   width=4, font=('Ubuntu Light', 10))
btn_10.grid(row=4, column=1)

btn_9 = tk.Button(window, text='3', command=lambda: add_to_calculation('3'),
                  width=4, font=('Ubuntu Light', 10))
btn_9.grid(row=4, column=2)

button_for_subtract = tk.Button(window, text='-',
                                command=lambda: add_to_calculation('-'),
                                width=4, font=('Ubuntu Light', 10))
button_for_subtract.grid(row=4, column=3)

button_for_close_parenthess = tk.Button(
                    window, text=')', command=lambda: add_to_calculation(')'),
                    width=4, font=('Ubuntu Light', 10))
button_for_close_parenthess.grid(row=4, column=4)

btn_0 = tk.Button(window, text='0', command=lambda: add_to_calculation('0'),
                  width=4, font=('Ubuntu Light', 10))
btn_0.grid(row=5, column=0)

button_for_decimal_point = tk.Button(window, text=',',
                                     command=lambda: add_to_calculation(','),
                                     width=4, font=('Ubuntu Light', 10))
button_for_decimal_point.grid(row=5, column=1)

button_for_mathematical_adding = tk.Button(
                                window, text='+',
                                command=lambda: add_to_calculation('+'),
                                width=4, font=('Ubuntu Light', 10))
button_for_mathematical_adding.grid(row=5, column=2)

button_for_equal = tk.Button(window, text='=',
                             command=lambda: evaluate_calculation(),
                             bg='blue', fg='white',
                             width=4, font=('Ubuntu Light', 10))
button_for_equal.grid(row=5, column=3, columnspan=2, sticky=tk.W+tk.E)

window.mainloop()
