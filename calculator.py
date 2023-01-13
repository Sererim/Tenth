from tkinter import *
import math
import tkinter.messagebox as message
from datetime import datetime as date

root = Tk()
root.geometry("312x324+450+90")
root.resizable(width=False, height=False)
root.title("Калькулятор")
root.configure(background='misty rose')


expression = ""
input_text = StringVar()


def button_click(item) -> None:
    global expression
    expression = expression + str(item)
    input_text.set(expression)


def button_clear() -> None:
    global expression
    expression = ""
    input_text.set("")


def button_equal() -> None:
    global expression
    save = expression
    result = compile(expression, "<string>", "eval")
    result = str(eval(result))
    input_text.set(result)
    expression = ""
    if result != "":
        save = f"{save} = {result}"
        archive(save)


def button_func(item: str) -> None:
    global expression
    expression = f"math.{item}({expression})"
    input_text.set(expression[5:])


def button_braces() -> None:
    global expression
    expression = f"({expression})"
    input_text.set(expression)

def button_plot() -> None:
    pass


def archive(save: str) -> None:
    with open("calc_log.csv", 'a') as f:
        f.write(f"\n{date.now()} : {save}")
        f.close()


input_frame = Frame(root, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black",
                    highlightthickness=2)
input_frame.pack(side=TOP)


input_field = Entry(input_frame, font=('Calibri', 20, 'bold'), textvariable=input_text, width=50, bg="#FBFDFE", bd=0,
                    justify=RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)


buttons_frame = Frame(root, width=312, height=272.5, bg="black")
buttons_frame.pack()


clear = Button(buttons_frame, text="C", fg="black", width=32, height=3, bd=0, bg="#fff", cursor="hand2",
               command=lambda: button_clear()).grid(row=0, column=0, columnspan=3, padx=1, pady=1)

divide = Button(buttons_frame, text="/", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                command=lambda: button_click("/")).grid(row=0, column=3, padx=1, pady=1)

seven = Button(buttons_frame, text="7", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
               command=lambda: button_click(7)).grid(row=1, column=0, padx=1, pady=1)

eight = Button(buttons_frame, text="8", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
               command=lambda: button_click(8)).grid(row=1, column=1, padx=1, pady=1)

nine = Button(buttons_frame, text="9", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
              command=lambda: button_click(9)).grid(row=1, column=2, padx=1, pady=1)

multiply = Button(buttons_frame, text="*", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                  command=lambda: button_click("*")).grid(row=1, column=3, padx=1, pady=1)

four = Button(buttons_frame, text="4", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
              command=lambda: button_click(4)).grid(row=2, column=0, padx=1, pady=1)

five = Button(buttons_frame, text="5", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
              command=lambda: button_click(5)).grid(row=2, column=1, padx=1, pady=1)

six = Button(buttons_frame, text="6", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
             command=lambda: button_click(6)).grid(row=2, column=2, padx=1, pady=1)

minus = Button(buttons_frame, text="-", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
               command=lambda: button_click("-")).grid(row=2, column=3, padx=1, pady=1)

one = Button(buttons_frame, text="1", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
             command=lambda: button_click(1)).grid(row=3, column=0, padx=1, pady=1)

two = Button(buttons_frame, text="2", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
             command=lambda: button_click(2)).grid(row=3, column=1, padx=1, pady=1)

three = Button(buttons_frame, text="3", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
               command=lambda: button_click(3)).grid(row=3, column=2, padx=1, pady=1)

plus = Button(buttons_frame, text="+", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
              command=lambda: button_click("+")).grid(row=3, column=3, padx=1, pady=1)

zero = Button(buttons_frame, text="0", fg="black", width=21, height=3, bd=0, bg="#fff", cursor="hand2",
              command=lambda: button_click(0)).grid(row=4, column=0, columnspan=2, padx=1, pady=1)

point = Button(buttons_frame, text=".", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
               command=lambda: button_click(".")).grid(row=4, column=2, padx=1, pady=1)

equals = Button(buttons_frame, text="=", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                command=lambda: button_equal()).grid(row=4, column=3, padx=1, pady=1)

sin = Button(buttons_frame, text="sin", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                command=lambda: button_func("sin")).grid(row=5, column=0, padx=1, pady=1)

cos = Button(buttons_frame, text="cos", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                command=lambda: button_func("cos")).grid(row=5, column=1, padx=1, pady=1)

tan = Button(buttons_frame, text="tan", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                command=lambda: button_func("tan")).grid(row=5, column=2, padx=1, pady=1)

exp = Button(buttons_frame, text="exp", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                command=lambda: button_func("exp")).grid(row=5, column=3, padx=1, pady=1)

log = Button(buttons_frame, text="log", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                command=lambda: button_func("log2")).grid(row=6, column=0, padx=1, pady=1)

ln = Button(buttons_frame, text="ln", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                command=lambda: button_func("log")).grid(row=6, column=1, padx=1, pady=1)

lg = Button(buttons_frame, text="lg", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                command=lambda: button_func("log10")).grid(row=6, column=2, padx=1, pady=1)

sqrt = Button(buttons_frame, text="sqrt", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                command=lambda: button_func("sqrt")).grid(row=6, column=3, padx=1, pady=1)

j = Button(buttons_frame, text="j", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                command=lambda: button_click("j")).grid(row=7, column=0, padx=1, pady=1)

cosh = Button(buttons_frame, text="cosh", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                command=lambda: button_func("cosh")).grid(row=7, column=1, padx=1, pady=1)

sinh = Button(buttons_frame, text="sinh", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                command=lambda: button_func("sinh")).grid(row=7, column=2, padx=1, pady=1)

braces = Button(buttons_frame, text="()", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                command=lambda: button_braces()).grid(row=7, column=3, padx=1, pady=1)




def exit():
    iexit = message.askyesno("Калькулятор", "Завершить работу ?")
    if iexit > 0:
        root.destroy()
        return


def more_functions():
    root.resizable(width=False, height=False)
    root.geometry("312x490+0+0")


def standart():
    root.resizable(width=False, height=False)
    root.geometry("312x324+0+0")


menubar = Menu(root)


filemenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Файл', menu=filemenu)
filemenu.add_command(label="Обычный", command=standart)
filemenu.add_command(label="Дополнительные функции и график", command=more_functions)
filemenu.add_separator()
filemenu.add_command(label = "Закрыть", command = exit)

editmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Изменить', menu=editmenu)
editmenu.add_command(label="Вырезать")
editmenu.add_command(label="Копировать")
editmenu.add_separator()
editmenu.add_command(label="Вставить")

root.config(menu=menubar)


root.mainloop()
