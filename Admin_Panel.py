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
        self.configure(bg='#FF884C')

        #===========Frames======================#
        self.main_frame=tk.LabelFrame(self,bg="white",text='User Details',font=('yu gothic ui', 15, "bold"))
        self.main_frame.place(width=826,height=470,x=10,y=70)

        self.second_frame=tk.LabelFrame(self,bg="white",font=('yu gothic ui', 15, "bold"),text='Display Details')
        self.second_frame.place(width=330,height=470,x=1030,y=70)

        self.search_frame=tk.Frame(self,bg="white")
        self.search_frame.place(width=330,height=40,x=1030,y=10)

        self.button_frame=tk.Frame(self,bg="white")
        self.button_frame.place(width=170,height=470,x=850,y=70)

        self.display_frame=tk.Frame(self,bg="white")
        self.display_frame.place(width=1350,height=200,x=10,y=550)
        #======================================================#

        #===============Search Frame=====================#
        self.search_label=tk.Label(self.search_frame,text='Search',font=('yu gothic ui', 23, "bold"),fg='#100A06',bg='#2C73C7',bd=20,relief='flat')
        self.search_label.place(x=1,height=40)

        self.search_entry = tk.Entry(self.search_frame, highlightthickness=0, relief='flat', bg="lightgrey", fg="#6b6a69",
                                    font=("yu gothic ui ", 23, "bold"), insertbackground = '#6b6a69')
        self.search_entry.place(x=130,height=40,width=200)
        #===============================================#
        #==============Main Frame====================#
        self.first_name=tk.Label(self.main_frame,text='First Name',font=('yu gothic ui', 16, "bold"),fg='#100A06',bg='White',relief='flat',)
        self.first_name.grid(row=0,column=0,sticky='W')
        self.first_entry = tk.Entry(self.main_frame, highlightthickness=0, relief='flat', bg="lightgrey", fg="#6b6a69",
                                    font=("yu gothic ui ", 16, "bold"), insertbackground = '#6b6a69')
        self.first_entry.grid(row=0,column=1)

        self.second_name=tk.Label(self.main_frame,text='Second Name',font=('yu gothic ui', 16, "bold"),fg='#100A06',bg='White',relief='flat',)
        self.second_name.grid(row=1,column=0,sticky='W',pady=7)
        self.second_entry = tk.Entry(self.main_frame, highlightthickness=0, relief='flat', bg="lightgrey", fg="#6b6a69",
                                    font=("yu gothic ui ", 16, "bold"), insertbackground = '#6b6a69')
        self.second_entry.grid(row=1,column=1,pady=7)
        
        self.work_id=tk.Label(self.main_frame,text='Work ID',font=('yu gothic ui', 16, "bold"),fg='#100A06',bg='White',relief='flat',)
        self.work_id.grid(row=2,column=0,sticky='W',pady=7)
        self.workid_entry = tk.Entry(self.main_frame, highlightthickness=0, relief='flat', bg="lightgrey", fg="#6b6a69",
                                    font=("yu gothic ui ", 16, "bold"), insertbackground = '#6b6a69')
        self.workid_entry.grid(row=2,column=1,pady=7)
        
        self.work_id=tk.Label(self.main_frame,text='Work ID',font=('yu gothic ui', 16, "bold"),fg='#100A06',bg='White',relief='flat',)
        self.work_id.grid(row=2,column=0,sticky='W',pady=7)
        self.workid_entry = tk.Entry(self.main_frame, highlightthickness=0, relief='flat', bg="lightgrey", fg="#6b6a69",
                                    font=("yu gothic ui ", 16, "bold"), insertbackground = '#6b6a69')
        self.workid_entry.grid(row=2,column=1,pady=7)
        
        


if __name__ == "__main__":
    admin=Admin_Panel()
    admin.mainloop()        