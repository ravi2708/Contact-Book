from tkinter import *
import datetime
from mypeople import MyPeople
from addpeople import AddPeople
from aboutus import About

date = datetime.datetime.now().date()
date = str(date)

class Application(object):
    def __init__(self,master):
        self.master = master

        self.top = Frame(master, height=150, bg="white")
        self.top.pack(fill=X)

        self.bottom = Frame(master,height=500,bg="#34baeb")
        self.bottom.pack(fill=X)

        self.top_image = PhotoImage(file ="image/icon1.png")
        self.top_image_label = Label(self.top, image=self.top_image,bg="white")
        self.top_image_label.place(x=130,y=25)

        self.heading = Label(self.top, text="My Phonebook App", font="arial 15 bold",  bg="white", fg="#ebb434")
        self.heading.place(x= 260,y=50)

        self.date_lbl =Label(self.top, text="Date:"+date, font="arial 12 bold", fg="#ebb434", bg="white")
        self.date_lbl.place(x=500,y=110)

        self.viewbutton = Button(self.bottom, text="   My People   ",fg="#42bcf5",bg="white", font="Arial 12 bold", command=self.my_people)
        self.viewbutton.place(x=250,y=70)

        self.addbutton = Button(self.bottom, text="  Add People  ",fg="#42bcf5",bg="white", font="Arial 12 bold", command=self.addpeoplefunction)
        self.addbutton.place(x=250, y=130)

        self.aboutbutton = Button(self.bottom, text="    About Us    ",fg="#42bcf5",bg="white", font="Arial 12 bold", command = self.about_us)
        self.aboutbutton.place(x=250, y=190)



    def my_people(self):
        people = MyPeople()

    def addpeoplefunction(self):
        addpeoplewindow = AddPeople()

    def about_us(self):
        aboutpage = About()




def main():
    root = Tk()
    app = Application(root)
    root.title("Phonebook App")
    root.geometry("650x550+350+200")
    root.resizable(False, False)
    root.mainloop()


if __name__ == "__main__":
    main()
