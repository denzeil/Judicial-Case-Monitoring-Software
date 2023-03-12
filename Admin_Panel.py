import tkinter as tk 
from tkinter import ttk 
from PIL import ImageTk,Image
from tkinter import messagebox
import _mysql_connector


class ttk_window(ttk.Frame):
    def __init__(self,container):
        super().__init__(container)
        
    def combo_type(self,container):
             self.user_type=tk.StringVar()
             self.combobox=ttk.Combobox(container,textvariable=self.user_type, font=('yu gothic ui', 16, "bold"))
             self.combobox['value']=('Clerk','Judge')
             self.combobox.current(0)
             self.combobox.grid(row=3, column=1)
    def tree_view(self,container):
               self.scroll_x=ttk.Scrollbar(container,orient='horizontal')
               self.scroll_y=ttk.Scrollbar(container,orient='vertical')
               column_one=('First Name','Second Name','Work ID','User Type','Email','Contact','Username')
               self.case_table=ttk.Treeview(container,columns=column_one,xscrollcommand=self.scroll_y.set,yscrollcommand=self.scroll_y.set)

               self.scroll_x.pack(side='bottom',fill='x')
               self.scroll_y.pack(side='right',fill='y')


               self.scroll_x=ttk.Scrollbar(command=self.case_table.xview)
               self.scroll_y=ttk.Scrollbar(command=self.case_table.yview)
               column_two=('First Name','Second Name','Work ID','User Type','Email','Contact','Username')

               for x,y in zip(column_one,column_two):
                 self.case_table.heading(x,text=y)
               for x in column_one:
                 self.case_table.column(x,width=100)

               self.case_table['show']='headings'
               self.case_table.pack(fill='both',expand=1)    
        

class Admin_Panel(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Admin Panel')
        #self.resizable(False,False)
        self.state('zoomed')
        self.geometry('1200x700')
        self.configure(bg='#FF884C')

        self.search=tk.StringVar()
        self.first=tk.StringVar()
        self.second=tk.StringVar()
        self.work=tk.StringVar()
        self.email_string=tk.StringVar()
        self.contact_string=tk.StringVar()
        self.password_string=tk.StringVar()
        self.repeat_string=tk.StringVar()
        self.username_string=tk.StringVar()


        #===========Frames======================#
        self.main_frame=tk.LabelFrame(self,bg="white",text='User Details',font=('yu gothic ui', 15, "bold"))
        self.main_frame.place(width=826,height=470,x=10,y=70)

        self.second_frame=tk.LabelFrame(self,bg="white",font=('yu gothic ui', 15, "bold"),text='Display Details')
        self.second_frame.place(width=330,height=470,x=1030,y=70)

        self.search_frame=tk.Frame(self,bg="white")
        self.search_frame.place(width=330,height=40,x=1030,y=10)

        self.button_frame=tk.LabelFrame(self,bg="white")
        self.button_frame.place(width=170,height=470,x=850,y=70)

        self.display_frame=tk.Frame(self,bg="white")
        self.display_frame.place(width=1350,height=200,x=10,y=550)
        #======================================================#

        #===============Search Frame=====================#
        self.search_label=tk.Button(self.search_frame,text='Search',bg='#2C73C7',fg='white',width=10,font=('yu Gothic ui',18))
        self.search_label.place(x=1,height=40)

        self.search_entry = tk.Entry(self.search_frame, highlightthickness=0, relief='flat', textvariable=self.search ,bg="lightgrey", fg="#6b6a69",
                                    font=("yu gothic ui ", 23, "bold"), insertbackground = '#6b6a69')
        self.search_entry.place(x=130,height=40,width=200)
        #===============================================#
        #==============Main Frame====================#
        self.first_name=tk.Label(self.main_frame,text='First Name',font=('yu gothic ui', 16, "bold"),fg='#100A06',bg='White',relief='flat')
        self.first_name.grid(row=0,column=0,sticky='W')
        self.first_entry = tk.Entry(self.main_frame, highlightthickness=0, relief='flat',textvariable=self.first, bg="lightgrey", fg="#6b6a69",
                                    font=("yu gothic ui ", 16, "bold"), insertbackground = '#6b6a69')
        self.first_entry.grid(row=0,column=1)

        self.second_name=tk.Label(self.main_frame,text='Second Name',font=('yu gothic ui', 16, "bold"),fg='#100A06',bg='White',relief='flat')
        self.second_name.grid(row=1,column=0,sticky='W',pady=7)
        self.second_entry = tk.Entry(self.main_frame, highlightthickness=0, relief='flat',textvariable=self.second , bg="lightgrey", fg="#6b6a69",
                                    font=("yu gothic ui ", 16, "bold"), insertbackground = '#6b6a69')
        self.second_entry.grid(row=1,column=1,pady=7)
        
        self.work_id=tk.Label(self.main_frame,text='Work ID',font=('yu gothic ui', 16, "bold"),fg='#100A06',bg='White',relief='flat',)
        self.work_id.grid(row=2,column=0,sticky='W',pady=7)
        self.workid_entry = tk.Entry(self.main_frame, highlightthickness=0,textvariable=self.work, relief='flat', bg="lightgrey", fg="#6b6a69",
                                    font=("yu gothic ui ", 16, "bold"), insertbackground = '#6b6a69')
        self.workid_entry.grid(row=2,column=1,pady=7)
        

        self.user_type=tk.Label(self.main_frame,text='User Type',font=('yu gothic ui', 16, "bold"),fg='#100A06',bg='White',relief='flat',)
        self.user_type.grid(row=3,column=0,sticky='W',pady=7)
        my_user=ttk_window(self)
        my_user.combo_type(self.main_frame)

        
        self.email=tk.Label(self.main_frame,text='Email',font=('yu gothic ui', 16, "bold"),fg='#100A06',bg='White',relief='flat',)
        self.email.grid(row=5,column=0,sticky='W',pady=7)
        self.email_entry= tk.Entry(self.main_frame, highlightthickness=0, relief='flat',textvariable=self.email_string ,bg="lightgrey", fg="#6b6a69",
                                    font=("yu gothic ui ", 16, "bold"), insertbackground = '#6b6a69')
        self.email_entry.grid(row=5,column=1,pady=7)

        self.contact=tk.Label(self.main_frame,text='Contact',font=('yu gothic ui', 16, "bold"),fg='#100A06',bg='White',relief='flat',)
        self.contact.grid(row=6,column=0,sticky='W',pady=7)
        self.contact_entry= tk.Entry(self.main_frame, highlightthickness=0, relief='flat',textvariable=self.contact_string, bg="lightgrey", fg="#6b6a69",
                                    font=("yu gothic ui ", 16, "bold"), insertbackground = '#6b6a69')
        self.contact_entry.grid(row=6,column=1,pady=7)

        self.password=tk.Label(self.main_frame,text='Password',font=('yu gothic ui', 16, "bold"),fg='#100A06',bg='White',relief='flat',)
        self.password.grid(row=7,column=0,sticky='W',pady=7)
        self.password_entry= tk.Entry(self.main_frame, highlightthickness=0, relief='flat',textvariable=self.password_string, bg="lightgrey", fg="#6b6a69",
                                    font=("yu gothic ui ", 16, "bold"), insertbackground = '#6b6a69')
        self.password_entry.grid(row=7,column=1,pady=7)
       
        self.repeat_password=tk.Label(self.main_frame,text='Repeat Password',font=('yu gothic ui', 16, "bold"),fg='#100A06',bg='White',relief='flat',)
        self.repeat_password.grid(row=8,column=0,sticky='W',pady=7)
        self.repeat_entry= tk.Entry(self.main_frame, highlightthickness=0, relief='flat',textvariable=self.repeat_string, bg="lightgrey", fg="#6b6a69",
                                    font=("yu gothic ui ", 16, "bold"), insertbackground = '#6b6a69')
        self.repeat_entry.grid(row=8,column=1,pady=7)
        

        self.username=tk.Label(self.main_frame,text='Username',font=('yu gothic ui', 16, "bold"),fg='#100A06',bg='White',relief='flat',)
        self.username.grid(row=0,column=3,sticky='W',pady=7)
        self.username_entry= tk.Entry(self.main_frame, highlightthickness=0, relief='flat',textvariable=self.username_string, bg="lightgrey", fg="#6b6a69",
                                    font=("yu gothic ui ", 16, "bold"), insertbackground = '#6b6a69')
        self.username_entry.grid(row=0,column=4,pady=7)
        #=============================================================================================#
        #=======================Buttons===============================================================#

        self.details=tk.Button(self.button_frame,text='Details',bg='#d77337',fg='white',font=('Goudy old style',18))
        self.details.place(x=2,y=5,width=163)

        self.submit_details=tk.Button(self.button_frame,text='Submit Details',bg='#d77337',fg='white',font=('Goudy old style',18))
        self.submit_details.place(x=2,y=90,width=163)

        self.update_button=tk.Button(self.button_frame,text='Update Details',bg='#d77337',fg='white',font=('Goudy old style',18))
        self.update_button.place(x=2,y=180,width=163)

        self.delete_button=tk.Button(self.button_frame,text='Delete Details',bg='#d77337',fg='white',font=('Goudy old style',18))
        self.delete_button.place(x=2,y=265,width=163)

        
        self.exit_button=tk.Button(self.button_frame,text='Exit',bg='#d77337',fg='white',font=('Goudy old style',18))
        self.exit_button.place(x=2,y=350,width=163)

        #=================Display frame================#
        my_user.tree_view(self.display_frame)

       

       
       
       
       
        
        
        


if __name__ == "__main__":
    admin=Admin_Panel()
    admin.mainloop()        