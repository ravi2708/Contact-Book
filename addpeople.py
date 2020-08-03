from tkinter import *
from tkinter import messagebox
import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="", database="addressbook")
cursor = mydb.cursor()


class AddPeople(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)

        self.geometry("650x650+600+200")
        self.title("Add New Person")
        self.resizable(False,False)

        self.top = Frame(self, height=150, bg="white")
        self.top.pack(fill=X)

        self.bottom = Frame(self, height=500, bg="#34baeb")
        self.bottom.pack(fill=X)

        self.top_image = PhotoImage(file="image/icon1.png")
        self.top_image_label = Label(self.top, image=self.top_image, bg="white")
        self.top_image_label.place(x=130, y=25)

        self.heading = Label(self.top, text="Add New Person", font="arial 15 bold", bg="white", fg="#ebb134")
        self.heading.place(x=260, y=50)

        #name
        self.label_name = Label(self.bottom, text="Name", font="Arial 15 bold", fg="white", bg="#fcc324")
        self.label_name.place(x=40, y=40)

        self.entry_name = Entry(self.bottom, width=30, bd=4)
        self.entry_name.insert(0,"Enter Name")
        self.entry_name.place(x=150, y=40)

        #surname
        self.label_surname = Label(self.bottom, text="Surname", font="Arial 15 bold", fg="white", bg="#fcc324")
        self.label_surname.place(x=40, y=80)

        self.entry_surname = Entry(self.bottom, width=30, bd=4)
        self.entry_surname.insert(0, "Enter Surname")
        self.entry_surname.place(x=150, y=80)

        #email
        self.label_email = Label(self.bottom, text="Email Id", font="Arial 15 bold", fg="white", bg="#fcc324")
        self.label_email.place(x=40, y=120)

        self.entry_email = Entry(self.bottom, width=30, bd=4)
        self.entry_email.insert(0, "Enter Email Id")
        self.entry_email.place(x=150, y=120)

        #phone number
        self.label_phone = Label(self.bottom, text="Phone", font="Arial 15 bold", fg="white", bg="#fcc324")
        self.label_phone.place(x=40, y=160)

        self.entry_phone = Entry(self.bottom, width=30, bd=4)
        self.entry_phone.insert(0, "Enter Phone Number")
        self.entry_phone.place(x=150, y=160)

        #address
        self.label_address = Label(self.bottom, text="Address", font="Arial 15 bold", fg="white", bg="#fcc324")
        self.label_address.place(x=40, y=200)

        self.entry_address = Text(self.bottom, width=23, height=10)
        self.entry_address.place(x=150, y=200)

        #button
        button = Button(self.bottom, text="Add person", command=self.insert_person)
        button.place(x=250, y=400)


    def insert_person(self):
        name = self.entry_name.get()
        surname = self.entry_surname.get()
        email = self.entry_email.get()
        phone = self.entry_phone.get()
        address = self.entry_address.get(1.0, 'end-1c')

        if name and surname and email and phone and address !="":
            sql = "INSERT INTO information( person_name, person_surname, person_email, person_phone, person_address) VALUES(%s, %s, %s, %s, %s)"
            val= (name, surname, email, phone, address)
            cursor.execute(sql,val)
            mydb.commit()
            messagebox._show("Success","Person Added")
            self.destroy()

        else:
            messagebox.showerror("Error", "fill all the fields", icon="warning")








