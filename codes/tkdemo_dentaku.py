import tkinter as tk

current_number = 0
first_term = 0
second_term = 0
operation = None

# ウィジェット（ボタン）が押された際の操作
def key0():
    key(0)

def key1():
    key(1)

def key2():
    key(2)

def key3():
    key(3)

def key4():
    key(4)

def key5():
    key(5)

def key6():
    key(6)

def key7():
    key(7)

def key8():
    key(8)

def key9():
    key(9)

def key(n):
    global current_number
    current_number = current_number*10 + n
    show_number(current_number)

def clear():
    global current_number
    current_number = 0
    show_number(current_number)

def plus():
    global first_term
    global current_number
    global operation
    first_term = current_number
    current_number = 0
    operation = 0
    show_number(current_number)

def minus():
    global first_term
    global current_number
    global operation
    first_term = current_number
    current_number = 0
    operation = 1
    show_number(current_number)

def multiple():
    global first_term
    global current_number
    global operation
    first_term = current_number
    current_number = 0
    operation = 2
    show_number(current_number)

def division():
    global first_term
    global current_number
    global operation
    first_term = current_number
    current_number = 0
    operation = 3
    show_number(current_number)

def eq():
    global first_term
    global second_term
    global current_number
    global operation
    second_term = current_number
    if operation == 0:
        current_number = first_term + second_term
    elif operation == 1:
        current_number = first_term - second_term
    elif operation == 2:
        current_number = first_term * second_term
    elif operation == 3:
        if second_term == 0:
            show_number("error")
        current_number = first_term // second_term
    show_number(current_number)

def show_number(num):
    e.delete(0, tk.END)
    e.insert(0, str(num))

# 画面の作成
root = tk.Tk()
f = tk.Frame(root)
f.grid()

# ウィジェット（ボタン）の作成
wid = 10
height = 5
b0 = tk.Button(f, text='0', command=key0, width=wid, height=height, bg='#0000ff')
b1 = tk.Button(f, text='1', command=key1, width=wid, height=height, bg='#0000ff')
b2 = tk.Button(f, text='2', command=key2, width=wid, height=height, bg='#0000ff')
b3 = tk.Button(f, text='3', command=key3, width=wid, height=height, bg='#0000ff')
b4 = tk.Button(f, text='4', command=key4, width=wid, height=height, bg='#0000ff')
b5 = tk.Button(f, text='5', command=key5, width=wid, height=height, bg='#0000ff')
b6 = tk.Button(f, text='6', command=key6, width=wid, height=height, bg='#0000ff')
b7 = tk.Button(f, text='7', command=key7, width=wid, height=height, bg='#0000ff')
b8 = tk.Button(f, text='8', command=key8, width=wid, height=height, bg='#0000ff')
b9 = tk.Button(f, text='9', command=key9, width=wid, height=height, bg='#0000ff')
bc = tk.Button(f, text='C', command=clear, width=wid, height=height, bg='#00ff00')
b_plus = tk.Button(f, text='+', command=plus, width=wid, height=height, bg='#00ff00')
b_minus = tk.Button(f, text='-', command=minus, width=wid, height=height, bg='#00ff00')
b_multiple = tk.Button(f, text='×', command=multiple, width=wid, height=height, bg='#00ff00')
b_division = tk.Button(f, text='÷', command=division, width=wid, height=height, bg='#00ff00')
be = tk.Button(f, text='=', command=eq, width=wid, height=height, bg='#00ff00')
e = tk.Entry(f, width=50)

# ウィジェットの配置
b0.grid(row=5 ,column=0)
b1.grid(row=4 ,column=0)
b2.grid(row=4 ,column=1)
b3.grid(row=4 ,column=2)
b4.grid(row=3 ,column=0)
b5.grid(row=3 ,column=1)
b6.grid(row=3 ,column=2)
b7.grid(row=2 ,column=0)
b8.grid(row=2 ,column=1)
b9.grid(row=2 ,column=2)
bc.grid(row=1 ,column=2)
b_division.grid(row=1 ,column=3)
b_multiple.grid(row=2 ,column=3)
b_minus.grid(row=3 ,column=3)
b_plus.grid(row=4 ,column=3)
be.grid(row=5 ,column=3)
e.grid(row=0 ,column=0, columnspan=5)

# GUIのスタート
root.mainloop()
