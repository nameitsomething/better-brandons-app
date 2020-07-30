from tkinter import *
from PIL import ImageTk,Image



class The_Window:
    def __init__(self, tk:Tk):
        self.tk = Tk()

        self.size = 150,180
        self.bottom_int = 50
        self.bottom_y=320
        self.label_int = 90
        self.label_y=490

        tk.title("Main Window")
        tk.geometry("1200x600")
        tk.resizable(0,0)


        self.info_frame = Frame(tk)
        self.course_frame = Frame(tk)
        self.bottom_frame = Frame(tk)
        self.bottom_frame2 = Frame(tk)
        self.bottom_frame3 = Frame(tk)
        
        

        self.name_label = Label(self.info_frame, text="Name:",anchor=NW,justify= LEFT,font=("Helvetica",15))
        self.age_label = Label(self.info_frame,text="Age:",anchor=NW,justify = LEFT,font=("Helvetica",15))
        self.grade_label = Label(self.info_frame,text="Grade:",anchor=NW,justify=LEFT,font=("Helvetica",15))
        self.present_label = Label(self.info_frame,text="Present:",anchor=NW,justify=LEFT,font=("Helvetica",15))

        
        self.student1_label = Label(self.bottom_frame, background ="red",text="Sdiperman",justify=LEFT,font=("Helvatica",16),width=10,height=2)
        self.student2_label = Label(self.bottom_frame2, background ="red",text="Gru",justify=LEFT,font=("Helvatica",16),width=10,height=2)
        self.student3_label = Label(self.bottom_frame3, background ="red",text="Shrekowski",justify=LEFT,font=("Helvatica",16),width=10,height=2)


        self.course_label = Label(self.course_frame,text="Courses", font=("Helvetica",20,'bold','underline'))


        self.bottom_canvas1 = Canvas(tk,width= 180, height = 170)
        self.bottom_canvas2 = Canvas(tk,width=180,height=170)
        self.bottom_canvas3 = Canvas(tk,width=180,height =170)
        self.picture_frame = Canvas(tk, width = 300, height = 300)

        
        #self.img = Image.open('sdiperman.jpeg')
        self.student_1 = Image.open('sdipermanCopy.jpeg')
        self.student_2 = Image.open('gru.jpeg')
        self.student_3 = Image.open('shrekowski.jpeg')

        self.resize_1 = self.student_1.resize((self.size))
        self.resize_2 = self.student_2.resize((self.size))
        self.resize_3 = self.student_3.resize((self.size))

        self.resize_1.save('bruh2.jpeg')
        self.resize_2.save('gru2.jpeg')
        self.resize_3.save('shrekowski2.jpeg')

        self.img = ImageTk.PhotoImage(Image.open('sdiperman.jpeg'))
        self.student_1 = ImageTk.PhotoImage(Image.open('bruh2.jpeg'))
        self.student_2 = ImageTk.PhotoImage(Image.open('gru2.jpeg'))
        self.student_3 = ImageTk.PhotoImage(Image.open('shrekowski2.jpeg'))

        self.bottom_canvas1.create_image(20,20,anchor=NW,image=self.student_1) 
        self.bottom_canvas2.create_image(20,20,anchor=NW,image=self.student_2)
        self.bottom_canvas3.create_image(20,20,anchor=NW,image=self.student_3)
        self.picture_frame.create_image(20,20, anchor=NW, image=self.img) 


        self.name_label.pack(side =TOP, fill=X)
        self.age_label.pack(side = TOP,fill= X)
        self.grade_label.pack(side=TOP,fill=X)
        self.present_label.pack(side=TOP,fill=X)
        self.student1_label.pack()
        self.student2_label.pack()
        self.student3_label.pack()
        self.course_label.pack()
        self.picture_frame.pack()
        self.bottom_canvas1.pack()
        self.bottom_canvas2.pack()
        self.bottom_canvas3.pack()
        

        self.info_frame.place(x=330,y=50,width=200,height=200)
        self.course_frame.place(x=810,y=25,width= 200,height=300)
        self.picture_frame.place(x=5,y=10)
        self.bottom_frame.place(x=self.label_int,y=self.label_y)
        self.bottom_frame2.place(x=self.label_int*3+70,y=self.label_y)
        self.bottom_frame3.place(x=self.label_int*6+55,y=self.label_y)
        self.bottom_canvas1.place(x=self.bottom_int,y=self.bottom_y)
        self.bottom_canvas2.place(x=self.bottom_int*6,y=self.bottom_y)
        self.bottom_canvas3.place(x=self.bottom_int*11,y=self.bottom_y)
     

        


if __name__== '__main__':
    root = Tk()
    win = The_Window(root)
    root.mainloop()