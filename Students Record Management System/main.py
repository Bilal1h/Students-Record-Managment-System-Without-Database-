from tkinter import *
import tkinter.messagebox as tmsg
import os
import pyautogui as pg
def ok():
    # global recordpath
    nameval = nameent.get()
    dobval = dobent.get()
    numval = nument.get()
    addval = addressent.get()
    if nameval == '' and dobval == '' and addval == '' and numval == '':
        a = tmsg.askokcancel("Error","Please Enter the Required Fields")
        if a:
            enter()
        else:
            pass
    else:
        name_entry.destroy()
        recordpath = os.getcwd()
        with open(f'{recordpath}/Records/{nameval}.txt','w') as f:
            f.write(str(f"Name : {nameval}\n"))
            f.write(str(f"Date Of Birth : {dobval}\n"))
            f.write(str(f"Phone Number : {numval}\n "))
            f.write(str(f"Adderess : {addval}\n"))
        
def enter():
    global name_entry
    global nameent
    global dobent
    global nument
    global addressent
    # pg.prompt("Enter Student Name")
    name_entry = Toplevel(root)
    name_entry.title("Enter Student Details")
    name_entry.geometry("700x400")
    name_entry.config(bg="#F4F6E1")
    Label(name_entry,text="Name : ",font="Roboto 25",bg="#F4F6E1").place(y=10,x=20)
    Label(name_entry,text="DOB : ",font="Roboto 25",bg="#F4F6E1").place(y=80,x=20)
    Label(name_entry,text="Phone No. : ",font="Roboto 25",bg="#F4F6E1").place(y=150,x=20)
    Label(name_entry,text="Adderess : ",font="Roboto 25",bg="#F4F6E1").place(y=220,x=20)
    nameent = Entry(name_entry,font="Roboto 25",bg="#BAD4AD",fg="white")
    nameent.place(y=10,x=250)
    dobent = Entry(name_entry,font="Roboto 25",bg="#BAD4AD",fg="white")
    dobent.place(y=80,x=250)
    nument = Entry(name_entry,font="Roboto 25",bg="#BAD4AD",fg="white")
    nument.place(y=150,x=250)
    addressent = Entry(name_entry,font="Roboto 25",bg="#BAD4AD",fg="white")
    addressent.place(y=220,x=250)
    okbut = Button(name_entry,text="Ok",font="Roboto 25 bold",bg="#DEEED8",relief=RIDGE,width=5,command=ok)
    okbut.pack(side=BOTTOM,pady=30,anchor=SE,padx=215)
    name_entry.mainloop()
def check():
    global recordpath
    global name
    global check_name
    name = pg.prompt("Enter Student Name")
    check_name = Toplevel(root)
    check_name.geometry("900x400")
    check_name.resizable(True,False)
    check_name.config(bg="#F4F6E1")
    recordpath = os.getcwd()
    if (not os.path.exists(f'{recordpath}/Records/{name}.txt')):
        check_name.destroy()
        tmsg.showinfo("Error",f"Unfortunately! There is no {name} named student in our list.")
    else:
        img = Label(check_name,text="Unfortunately Image\nNot Available",bg="grey",fg="white",font="nexa 15",height=6,width=20)
        img.pack()
        with open(f'{recordpath}/Records/{name}.txt','r') as f:
            details = f.read()
            # print(details)
            Label(check_name,text=details,font="Roboto 25 bold",bg="#AAD3C1",fg="white").pack(pady=20,fill=BOTH,expand=True)



    check_name.mainloop()
def delstu():
    name_del = pg.prompt("Enter Student Name")
    recordpath = os.getcwd()
    if (not os.path.exists(f'{recordpath}/Records/{name_del}.txt')):
        tmsg.showinfo("Error",f"Unfortunately! There is no {name_del} named student in our list.")
    else:
        global sure
        sure = tmsg.askyesno("Delete Record","Are You Sure! This action cannot be undone")
        if sure:
            os.remove(f'{recordpath}/Records/{name_del}.txt')
        else:
            pass
def exits():
    root.destroy()
global root
root = Tk()
root.title("Students Record Managment System")
root.state("zoomed")
root.resizable(False,False)
root.config(bg="#F4F6E1")
dawn = Label(root,text="Dawn Public School",font="Roboto 25",fg="white",bg="#BAD4AD",height=2)
dawn.pack(fill=X)
Label(root,text=f"Welcome to the \n Students Record Management System",font="Roboto 25",bg="#F4F6E1",borderwidth=5,relief=FLAT).pack(side=TOP)
student_name = Button(root,text="Enter Student Name",font="Roboto 15 bold",borderwidth="10",relief=FLAT,bg="#8CE78C",fg="white",command=enter)
student_name.pack(pady=20)
check_student = Button(root,text="Check Student Details",font="Roboto 15 bold",borderwidth="10",bg="#8CE78C",fg="white",relief=FLAT,command=check)
check_student.pack(pady=20)
del_student = Button(root,text="Delete Student Record",font="Roboto 15 bold",borderwidth="10",relief=FLAT,bg="#8CE78C",fg="white",command=delstu)
del_student.pack(pady=20)
exit_button = Button(root,text="Exit",font="Roboto 15 bold",relief=FLAT,bg="#8CE78C",fg="white",borderwidth="10",command=exits)
exit_button.pack(pady=20)
root.mainloop()