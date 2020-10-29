from tkinter import *
from PIL import ImageTk, Image #pillow
from tkinter import messagebox #messagebox
import pymysql  # pip install pymysql
from tkinter import ttk
from tkinter.ttk import Treeview # treeview


root = Tk()

root.maxsize(840, 710)
root.minsize(840, 710)

root.wm_iconbitmap("1.ico")

root.title("Online Gas Booking GUI")


#  DB connection window


def connect_db():
    global input_value, input_hvalue, input_password
    log = Toplevel(root)
    log.title("Database Login Panel")
    log.wm_iconbitmap("1.ico")

    log.minsize(520, 550)
    log.maxsize(520, 550)

    Label(log, text="Connect Database !", font="consolas 33 bold", fg="white", bg="red", pady=15).pack(fill=X)

    input_value = StringVar()
    input_value.set("")

    input_hvalue = StringVar()
    input_hvalue.set("")

    input_password = StringVar()
    input_password.set("")

    Label(log, text="Hostname :", font="consolas 20 bold", bd=5).place(x=50, y=130)
    Entry(log, textvariable=input_hvalue, font="consolas 15 bold", bd=5).place(x=210, y=135, )

    Label(log, text="Username :", font="consolas 20 bold", bd=5).place(x=50, y=230)
    Entry(log, textvariable=input_value, font="consolas 15 bold", bd=5).place(x=210, y=235, )

    Label(log, text="Password :", font="consolas 20 bold").place(x=50, y=330)
    Entry(log, textvariable=input_password, font="consolas 15 bold", show='*', bd=5).place(x=210, y=335)

    Button(log, text="Sign in", font="consolas 20 bold", bd=5, command=connect).place(x=190, y=430)

    log.grab_set()

    log.mainloop()


#  DB Connecting function

def connect():
    global connection, my_cursor, VERIFY_DB
    hostname = input_hvalue.get()
    username = input_value.get()
    password = input_password.get()
    try:
        connection = pymysql.connect(hostname, username, password)
        my_cursor = connection.cursor()
        messagebox.showinfo("Notification", "Db Successfully Connected")
        try:
            sql = "CREATE DATABASE lpg_user"
            my_cursor.execute(sql)
            sql = "USE lpg_user"
            my_cursor.execute(sql)
            sql = "CREATE table lpg_user(id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,fname varchar(20) NOT NULL,email varchar(20) NOT NULL,mobile varchar(20) NOT NULL,password varchar(20) NOT NULL)"
            my_cursor.execute(sql)
            connection.commit()
            VERIFY_DB = 1
        except:
            sql = "USE lpg_user"
            my_cursor.execute(sql)
            connection.commit()
            VERIFY_DB = 1
    except:
        messagebox.showerror('Error', 'Something went wrong Please Retry !')


#   Booking Window


def file_book():
    global VERIFY_DB, my_cursor, connection
    copy_num = book_pass.get()
    aadhar = book_card.get()
    mobile = book_mobile.get()
    address = book_addr.get()

    try:
        try:
            sql = "USE lpg_user"
            my_cursor.execute(sql)
            sql = "CREATE table book_user(id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,copy_num varchar(20) NOT NULL,aadhar varchar(20) NOT NULL,mobile varchar(20) NOT NULL,address varchar(20) NOT NULL)"
            my_cursor.execute(sql)
            connection.commit()
            VERIFY_DB = 1
            try:
                sql = "INSERT INTO book_user(id,copy_num,aadhar,mobile,address) values(%s,%s,%s,%s,%s)"
                values = ('', copy_num, aadhar, mobile, address)
                my_cursor.execute(sql, values)
                connection.commit()
                messagebox.showinfo('Congrats', f"Congrats! {input_lvalue.get()} Your Cylinder Booked Successfully")
            except:
                messagebox.showerror('Oops!', 'Not Booked, Try Again!')
        except:
            sql = "USE lpg_user"
            my_cursor.execute(sql)
            connection.commit()
            VERIFY_DB = 1
            try:
                sql = "INSERT INTO book_user(id,copy_num,aadhar,mobile,address) values(%s,%s,%s,%s,%s)"
                values = ('', copy_num, aadhar, mobile, address)
                my_cursor.execute(sql, values)
                connection.commit()
                messagebox.showinfo('Congrats', f"Congrats! {input_lvalue.get()} Your Cylinder Booked Successfully")
            except:
                messagebox.showerror('Oops!', 'Not Booked, Try Again!')
    except:
        messagebox.showerror('Oops', 'Something Went Wrong, Try again!')


def booking():
    log = Toplevel(root)
    log.title("Booking Panel")
    log.wm_iconbitmap("1.ico")
    log.maxsize(700, 730)
    log.minsize(700, 730)

    Label(log, text=f"Book Your Cylinder", font="lucida 33 bold", fg="white", bg="red", pady=15).pack(fill=X)

    global book_pass, book_card, book_addr, book_mobile

    book_pass = StringVar()
    book_pass.set("")
    book_card = StringVar()
    book_card.set("")
    book_addr = StringVar()
    book_addr.set("")
    book_mobile = StringVar()
    book_mobile.set("")

    Label(log, text="Unique ID. :", font="consolas 20 bold", bd=5).place(x=100, y=130)
    Entry(log, textvariable=book_pass, font="consolas 15 bold", bd=5).place(x=290, y=135, )

    Label(log, text="Aadhar   :", font="consolas 20 bold", bd=5).place(x=100, y=230)
    Entry(log, textvariable=book_card, font="consolas 15 bold", bd=5).place(x=290, y=235, )

    Label(log, text="Mobile   :", font="consolas 20 bold", bd=5).place(x=100, y=330)
    Entry(log, textvariable=book_mobile, font="consolas 15 bold", bd=5).place(x=290, y=335, )

    Label(log, text="Address  :", font="consolas 20 bold").place(x=100, y=430)
    Entry(log, textvariable=book_addr, font="consolas 15 bold", bd=5).place(x=290, y=435)

    Button(log, text="Submit", font="consolas 20 bold", bd=5, command=file_book).place(x=270, y=530)

    log.grab_set()

    log.mainloop()


#   Status Window

def status():

    log = Toplevel(root)
    log.title("Status Panel")
    log.wm_iconbitmap("1.ico")
    log.geometry('500x500+200+30')
    log.maxsize(500, 500)
    log.minsize(500, 500)

    mwrightframe = Frame(log, borderwidth="3", bg="snow3", relief=GROOVE)
    mwrightframe.place(x=0, y=0, height=500, width=500)
    style = ttk.Style()
    style.configure('Treeview.Heading', font=('arial', 14, 'bold'), foreground='black')
    style.configure('Treeview', font=('arial', 13, 'bold'), rowheight=50, rowwidth=300, foreground='blue',
                    bg='powder blue')

    mwscrollrightframe_x = Scrollbar(mwrightframe, orient=HORIZONTAL)
    mwscrollrightframe_y = Scrollbar(mwrightframe, orient=VERTICAL)

    table = Treeview(mwrightframe, columns=(
            'Id', 'user', 'Copy No', 'Status'), yscrollcommand=mwscrollrightframe_y,  xscrollcommand=mwscrollrightframe_x)

    global VERIFY_DB, my_cursor, connection

    sql = "USE lpg_user"
    my_cursor.execute(sql)
    connection.commit()
    VERIFY_DB = 1

    sql = "SELECT * FROM book_user"
    my_cursor.execute(sql)
    connection.commit()
    VERIFY_DB = 1
    result = my_cursor.fetchall()
    mwscrollrightframe_x.pack(side=BOTTOM, fill=X)
    mwscrollrightframe_y.pack(side=RIGHT, fill=Y)
    mwscrollrightframe_x.config(command=table.xview)
    mwscrollrightframe_y.config(command=table.yview)
    table.heading('Id', text='Sr no.')
    table.heading('user', text='Copy no.')
    table.heading('Copy No', text='Address')
    table.heading('Status', text='Status')
    table['show'] = 'headings'
    for data in result:
        table.insert('', 'end', values=(data[0], data[1], data[4], 'Booked'))
    table.pack(fill=BOTH, expand=1)

    log.grab_set()

    log.mainloop()


#  Dashboard After Login Panel

def welcome():
    log = Toplevel(root)
    log.title("Dashboard Panel")
    log.wm_iconbitmap("1.ico")
    log.maxsize(750, 670)
    log.minsize(750, 670)

    Label(log, text=f"Welcome , {input_lvalue.get()}", font="lucida 33 bold", fg="white", bg="red", pady=15).pack(
        fill=X)
    f0 = Frame(log)

    book_btn = Button(f0, text=" Book  ", padx=30, pady=30, bg="blue", fg="white", font="arial 20 bold", bd=5,
                      command=booking)
    book_btn.pack(side=LEFT, anchor="n", padx=20)

    status_btn = Button(f0, text="Status", padx=30, pady=30, bg="blue", fg="white", font="arial 20 bold", bd=5,
                        command=status)
    status_btn.pack(side=LEFT, anchor="n", padx=20)

    f0.pack(padx=0)

    load = Image.open("l2.png")

    render = ImageTk.PhotoImage(load)

    img = Label(log, image=render, padx=30, pady=20)
    img.image = render
    img.place(x=-70, y=210)

    log.grab_set()

    log.mainloop()


#  Team Window


def team():
    log = Toplevel(root)
    log.title("Team Panel")
    log.wm_iconbitmap("1.ico")
    log.maxsize(700, 770)
    log.minsize(700, 770)

    Label(log, text="Our Developer Team", font="lucida 33 bold", fg="white", bg="red", pady=15).pack(fill=X)

    photo = PhotoImage(file=r"3.png")
    Label(log, text="Akash Kashyap\n Reg No. 11904396", font="consolas 25 bold").place(x=300, y=150)
    Label(log, image=photo).place(x=50, y=120)

    photo1 = PhotoImage(file=r"2.png")
    Label(log, text="Reet Gupta\n Reg No. 11904993", font="consolas 25 bold").place(x=30, y=370)
    Label(log, image=photo1).place(x=400, y=320)

    photo2 = PhotoImage(file=r"4.png")
    Label(log, text="Sachin Verma\n Reg No. 11902043", font="consolas 25 bold").place(x=300, y=590)
    Label(log, image=photo2).place(x=50, y=550)

    log.grab_set()

    log.mainloop()


#  Login Validation

def log_lpg():
    global connection, my_cursor
    u_email = input_lvalue.get()
    u_pass = input_lpassword.get()

    try:
        # sql = ("Select *from lpg_user where email=%s and password=%s", (u_email, u_pass))

        my_cursor.execute('Select * from lpg_user where email=%s and password=%s', (u_email, u_pass))
        connection.commit()
        records = my_cursor.fetchall()
        if records:
            welcome()

        else:
            messagebox.showerror('Oops!', 'User / Password not exist')

    except:
        messagebox.showerror('Oops', 'Check your Inputs')


#  Login Window


def login():
    log = Toplevel(root)
    log.title("Log In Panel")
    log.wm_iconbitmap("1.ico")

    log.minsize(520, 550)
    log.maxsize(520, 550)

    Label(log, text="Welcome Back !", font="consolas 33 bold", fg="white", bg="red", pady=15).pack(fill=X)

    global input_lvalue, input_lpassword

    input_lvalue = StringVar()
    input_lvalue.set("")

    input_lpassword = StringVar()
    input_lpassword.set("")

    Label(log, text="Username :", font="consolas 20 bold", bd=5).place(x=50, y=130)
    Entry(log, textvariable=input_lvalue, font="consolas 15 bold", bd=5).place(x=210, y=135, )

    Label(log, text="Password :", font="consolas 20 bold").place(x=50, y=230)
    Entry(log, textvariable=input_lpassword, font="consolas 15 bold", show='*', bd=5).place(x=210, y=235)

    Button(log, text="Sign in", font="consolas 20 bold", bd=5, command=log_lpg).place(x=190, y=330)

    log.grab_set() # Hold the present window

    log.mainloop()


#  Register User in DB

def reg_lpg():
    name = input_name.get()
    email = input_email.get()
    mobile = input_mobile.get()
    password = input_rpassword.get()


    try:
        sql = "INSERT INTO lpg_user(id,fname,email,mobile,password) values(%s,%s,%s,%s,%s)"
        values = ('', name, email, mobile, password)
        my_cursor.execute(sql, values)
        connection.commit()
        messagebox.showinfo('Congrats', f"Congrats {email},You are Registered Successfully")
    except:
        messagebox.showerror('Oops!', 'Failed! Try Again')


#  Register window

def register():
    log = Toplevel(root)
    log.title("Register Panel")
    log.wm_iconbitmap("1.ico")
    log.maxsize(600, 600)
    log.minsize(600, 600)

    Label(log, text="Register User !", font="consolas 33 bold", fg="white", bg="red", pady=15).pack(fill=X)
    global input_name, input_email, input_mobile, input_rpassword
    input_name = StringVar()
    input_name.set("")
    input_email = StringVar()
    input_email.set("")
    input_mobile = StringVar()
    input_mobile.set("")
    input_rpassword = StringVar()
    input_rpassword.set("")

    Label(log, text="Full Name :", font="consolas 20 bold", bd=5).place(x=100, y=130)
    Entry(log, textvariable=input_name, font="consolas 15 bold", bd=5).place(x=260, y=135, )

    Label(log, text="Username :", font="consolas 20 bold", bd=5).place(x=100, y=230)
    Entry(log, textvariable=input_email, font="consolas 15 bold", bd=5).place(x=260, y=235, )

    Label(log, text="Mobile No. :", font="consolas 20 bold", bd=5).place(x=100, y=330)
    Entry(log, textvariable=input_mobile, font="consolas 15 bold", bd=5).place(x=260, y=335, )

    Label(log, text="Password :", font="consolas 20 bold").place(x=100, y=430)
    Entry(log, textvariable=input_rpassword, font="consolas 15 bold", bd=5).place(x=260, y=435)

    Button(log, text="Submit", font="consolas 20 bold", bd=5, command=reg_lpg).place(x=220, y=530)

    log.grab_set()

    log.mainloop()


Label(root, text="Online Gas Booking Management System", bg="red", fg="white", height=2, bd=5,
      font="arial 30 bold").pack(fill=X)
f0 = Frame(root)

b_login = Button(f0, text=" Log In ", padx=30, pady=30, bg="blue", fg="white", font="arial 20 bold", bd=5,
                 command=login)
b_login.pack(side=LEFT, anchor="n")

b_register = Button(f0, text="Register", padx=30, pady=30, bg="blue", fg="white", font="arial 20 bold", bd=5,
                    command=register)
b_register.pack(side=LEFT, anchor="n")

b_register = Button(f0, text="Connect\nDatabase", padx=30, pady=14, bg="blue", fg="white", font="arial 20 bold", bd=5,
                    command=connect_db)
b_register.pack(side=LEFT, anchor="n")

b_team = Button(f0, text=" Team ", padx=30, pady=30, bg="blue", fg="white", font="arial 20 bold", bd=5,
                command=team)
b_team.pack(side=LEFT, anchor="n")

f0.pack(padx=0)

#  Main Image

load = Image.open("l2.png")

render = ImageTk.PhotoImage(load)

img = Label(root, image=render)
img.image = render
img.place(x=0, y=230)

root.mainloop()