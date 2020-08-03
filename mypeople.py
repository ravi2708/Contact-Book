from tkinter import *
from tkinter import messagebox
from addpeople import AddPeople
from updatepeople import Update
from display import Display

import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="", database="addressbook")
cursor = mydb.cursor()

class MyPeople(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)

        self.geometry("650x650+600+200")
        self.title("My People")
        self.resizable(False,False)

        self.top = Frame(self, height=150, bg="white")
        self.top.pack(fill=X)

        self.bottom = Frame(self, height=500, bg="#ebb134")
        self.bottom.pack(fill=X)

        self.top_image = PhotoImage(file="image/icon1.png")
        self.top_image_label = Label(self.top, image=self.top_image, bg="white")
        self.top_image_label.place(x=130, y=25)

        self.heading = Label(self.top, text="My People", font="arial 15 bold", bg="white", fg="#ebb434")
        self.heading.place(x=260, y=50)

        self.scrollbar = Scrollbar(self.bottom, orient=VERTICAL)
        self.scrollbar.grid(row=0, column=1, sticky=N+S)

        self.listbox = Listbox(self.bottom, width=60, height=27)
        self.listbox.grid(row=0, column=0, padx=(40,0))
        self.scrollbar.config(command=self.listbox.yview)
        self.listbox.config(yscrollcommand=self.scrollbar.set)

        sql="SELECT * FROM information"
        cursor.execute(sql)
        persons = cursor.fetchall()
        count=0
        for i in persons:
            self.listbox.insert(count, str(i[0])+". "+i[1]+" "+i[2])
            count +=1
        #the things that are static can be done without using the self

        btnadd = Button(self.bottom, text="Add", width=12, font="sans 12 bold", command=self.add_people)
        btnadd.grid(row=0,column=2, padx=20, pady=10 , sticky=N)

        btnupdate = Button(self.bottom, text="Update", width=12, font="sans 12 bold", command=self.update_function)
        btnupdate.grid(row=0, column=2, padx=20, pady=50, sticky=N)

        btndisplay = Button(self.bottom, text="Display", width=12, font="sans 12 bold", command=self.display_function)
        btndisplay.grid(row=0, column=2, padx=20, pady=90, sticky=N)

        btndelete = Button(self.bottom, text="Delete", width=12, font="sans 12 bold", command=self.delete_function)
        btndelete.grid(row=0, column=2, padx=20, pady=130, sticky=N)


    def add_people(self):
        add_page = AddPeople()
        self.destroy()

    def update_function(self):
        selected_item = self.listbox.curselection()
        person = self.listbox.get(selected_item)
        person_id = person.split(".")[0]
        updatepage = Update(person_id)
        self.destroy()

    def display_function(self):
        selected_item = self.listbox.curselection()
        person = self.listbox.get(selected_item)
        person_id = person.split(".")[0]

        displaypage = Display(person_id)

    def delete_function(self):
        selected_item = self.listbox.curselection()
        person = self.listbox.get(selected_item)
        person_id = person.split(".")[0]

        sql="DELETE FROM information where person_id={}".format(person_id)
        answer = messagebox.askquestion("Warning", "Are you sure you want to delete?")
        if answer == "yes":
            try:
                cursor.execute(sql)
                mydb.commit()
                messagebox.showinfo("Success","Deleted")
                self.destroy()

            except EXCEPTION as e:
                messagebox.showinfo("Info",str(e))