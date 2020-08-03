from tkinter import *
from tkinter import messagebox
import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="", database="addressbook")
cursor = mydb.cursor()

class Update(Toplevel):
    def __init__(self,person_id):
        Toplevel.__init__(self)

        self.geometry("650x650+600+200")
        self.title("Update Person")
        self.resizable(False, False)

        print("person id =",person_id)

        sql = "SELECT * FROM information where person_id = '{}'".format(person_id)
        cursor.execute(sql)
        result = cursor.fetchone()
        print(result)

        self.person_id = person_id

        person_name = result[1]
        person_surname = result[2]
        person_email = result[3]
        person_phone = result[4]
        person_address = result[5]
        print("person name",person_name)

        self.top = Frame(self, height=150, bg="white")
        self.top.pack(fill=X)

        self.bottom = Frame(self, height=500, bg="#34baeb")
        self.bottom.pack(fill=X)

        self.top_image = PhotoImage(file="image/icon1.png")
        self.top_image_label = Label(self.top, image=self.top_image, bg="white")
        self.top_image_label.place(x=130, y=25)

        self.heading = Label(self.top, text="Update Person", font="arial 15 bold", bg="white", fg="#ebb134")
        self.heading.place(x=260, y=50)

        # name
        self.label_name = Label(self.bottom, text="Name", font="Arial 15 bold", fg="white", bg="#fcc324")
        self.label_name.place(x=40, y=40)

        self.entry_name = Entry(self.bottom, width=30, bd=4)
        self.entry_name.insert(0, person_name)
        self.entry_name.place(x=150, y=40)

        # surname
        self.label_surname = Label(self.bottom, text="Surname", font="Arial 15 bold", fg="white", bg="#fcc324")
        self.label_surname.place(x=40, y=80)

        self.entry_surname = Entry(self.bottom, width=30, bd=4)
        self.entry_surname.insert(0, person_surname)
        self.entry_surname.place(x=150, y=80)

        # email
        self.label_email = Label(self.bottom, text="Email Id", font="Arial 15 bold", fg="white", bg="#fcc324")
        self.label_email.place(x=40, y=120)

        self.entry_email = Entry(self.bottom, width=30, bd=4)
        self.entry_email.insert(0, person_email)
        self.entry_email.place(x=150, y=120)

        # phone number
        self.label_phone = Label(self.bottom, text="Phone", font="Arial 15 bold", fg="white", bg="#fcc324")
        self.label_phone.place(x=40, y=160)

        self.entry_phone = Entry(self.bottom, width=30, bd=4)
        self.entry_phone.insert(0, person_phone)
        self.entry_phone.place(x=150, y=160)

        # address
        self.label_address = Label(self.bottom, text="Address", font="Arial 15 bold", fg="white", bg="#fcc324")
        self.label_address.place(x=40, y=200)

        self.entry_address = Text(self.bottom, width=23, height=10)
        self.entry_address.insert(1.0, person_address)
        self.entry_address.place(x=150, y=200)

        # button
        button = Button(self.bottom, text="Update person", command=self.update_people)
        button.place(x=250, y=400)

    def update_people(self):
        person_id = self.person_id
        name = self.entry_name.get()
        surname = self.entry_surname.get()
        email = self.entry_email.get()
        phone = self.entry_phone.get()
        address = self.entry_address.get(1.0, 'end-1c')

        sql = "UPDATE information set person_name = %s, person_surname = %s, person_email = %s, person_phone = %s, person_address = %s where person_id = %s"
        val =(name,surname,email,phone,address,str(person_id))

        try:
            cursor.execute(sql,val)
            mydb.commit()
            messagebox.showinfo("Success","Data updated")
            self.destroy()

        except EXCEPTION as e:
            print(e)

