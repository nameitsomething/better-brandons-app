from tkinter import *
from PIL import ImageTk,Image


class The_Window:
    def __init__(self, tk:Tk):
        self.tk = Tk()

        tk.title("Main Window")
        tk.geometry("1200x600")
        tk.resizable(0,0)

        self.info_frame = Frame(tk)
        self.bottom_frame = Frame(tk)
        

        self.name_label = Label(self.info_frame, text="Name:",justify= LEFT)
        self.age_label = Label(self.info_frame,text="Age:",justify = LEFT)
        self.grade_label = Label(self.info_frame,text="Grade:",justify=LEFT)
        self.present_label = Label(self.info_frame,text="Present:",justify=LEFT)

        self.picture_frame = Canvas(tk, width = 300, height = 600)
        
        self.img = ImageTk.PhotoImage(Image.open("sdiperman.png")) 
        self.picture_frame.create_image(20,20, anchor=NW, image=self.img) 

        self.name_label.pack(side =TOP, fill=X)
        self.age_label.pack(side = TOP,fill= X)
        self.grade_label.pack(side=TOP,fill=X)
        self.present_label.pack(side=TOP,fill=X)
        self.picture_frame.pack()
        

        self.info_frame.place(x=120,y=60,width=500,height=100)
        self.picture_frame.place(x=5,y=10)
        


if __name__== '__main__':
    root = Tk()
    win = The_Window(root)
    root.mainloop()