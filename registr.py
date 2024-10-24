from tkinter import *

root = Tk()
root.geometry("700x400")

def getvals():
    print("Welcome!")

Label(root, text="Student Management System", font="ar 15 bold").grid(row=0, column=3)

name = Label(root, text="Full name")
mail = Label(root, text="Mail")

name.grid(row=1, column=2)
mail.grid(row=2, column=2)

namevalue = StringVar
mailvalue = StringVar
checkvalue = IntVar

#creating an empty field:

nameentry = Entry(root, textvariable =namevalue)
mailentry = Entry(root, textvariable =mailvalue)


#packing empty fields:
nameentry.grid (row = 1, column=3)
nameentry.grid (row = 2, column=3)



#creating remember button:
checkbutton= Checkbutton(text="Remember me?" ,variable= checkvalue)
checkbutton.grid(row=3 , column=3)

#creating submit button:
Button(text="submit",command=getvals).grid(row=4,column=3)

root.mainloop()
