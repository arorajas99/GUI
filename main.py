
import tkinter as tk

login_info = {'arorajas99': '4321', 'acbd': '7894', 'hackerboii': '5648'}


def main():
    win = tk.Tk()
    win.geometry('500x500')
    win.title('OUR APPLICATION')
    win.minsize(500, 500)
    win.maxsize(500, 500)
    win.configure(bg='#F1BBB0')
    btn1 = tk.Button(win, text='Sign In', bg='black', fg='white', font='Courier 15 bold italic', command=login)
    btn1.place(x=100, y=350)

    btn2 = tk.Button(win, text='Sign Up', bg='red', font='Courier 15 bold italic', command=signup)
    btn2.place(x=300, y=350)

    win.mainloop()


def login():
    win_login = tk.Tk()
    username = tk.StringVar()
    password = tk.StringVar()

    def check():
        if field.get() in list(login_info.keys()):
            print('True')
            if field2.get() == login_info[field.get()]:
                print("HURRAY")
            else:
                print('Incorrect Password')
        else:
            print('false')

    win_login.geometry('500x500')
    win_login.title('TITLE')
    label = tk.Label(win_login, text='LOGIN PAGE')
    label.pack()

    label2 = tk.Label(win_login, text='Username')
    label2.pack()

    field = tk.Entry(win_login)
    field.pack()

    label3 = tk.Label(win_login, text='Password')
    label3.pack()

    field2 = tk.Entry(win_login)
    field2.pack()

    btn = tk.Button(win_login, text='Sign In', command=check)
    btn.pack()

    win_login.mainloop()


def signup():
    siup = tk.Tk()
    siup.geometry('500x500')
    label1 = tk.Label(siup, text='Enter your Email id')
    label1.pack()
    entry1 = tk.Entry(siup)
    entry1.pack()
    label2 = tk.Label(siup, text='Enter your password')
    label2.pack()
    entry2 = tk.Entry(siup)
    entry2.pack()
    button1 = tk.Button(siup, text='Sign UP')
    button1.pack


main()
