import tkinter as tk 
from tkinter import ttk 
from PIL import ImageTk,Image
from tkinter import messagebox
import _mysql_connector

class Admin_Panel(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Admin Panel')
        self.resizable(False,False)
        #self.state('zoomed')
        self.geometry('1200x700')
        self.configure(bg='#17319B')

       
        self.main_frame=tk.Frame(self,bg="white")
        self.main_frame.place(width=800,height=500,x=70,y=70)

if __name__ == "__main__":
    admin=Admin_Panel()
    admin.mainloop()        