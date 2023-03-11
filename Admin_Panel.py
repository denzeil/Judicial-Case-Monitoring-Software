import tkinter as tk 
from tkinter import ttk 
from PIL import ImageTk,Image
from tkinter import messagebox
import _mysql_connector

class Admin_Panel(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Admin Panel')
        #self.resizable(False,False)
        self.state('zoomed')
        self.geometry('1200x700')
        self.configure(bg='#17319B')

        #===========Frames======================#
        self.main_frame=tk.Frame(self,bg="white")
        self.main_frame.place(width=900,height=470,x=10,y=70)

        self.second_frame=tk.Frame(self,bg="white")
        self.second_frame.place(width=260,height=470,x=1100,y=70)

        self.search_frame=tk.Frame(self,bg="white")
        self.search_frame.place(width=260,height=50,x=1100,y=10)

        self.button_frame=tk.Frame(self,bg="white")
        self.button_frame.place(width=170,height=470,x=920,y=70)

        self.display_frame=tk.Frame(self,bg="white")
        self.display_frame.place(width=1350,height=200,x=10,y=550)
        #======================================================#



if __name__ == "__main__":
    admin=Admin_Panel()
    admin.mainloop()        