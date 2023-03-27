import tkinter as tk 
from tkinter import ttk 
from PIL import ImageTk,Image
from tkinter import messagebox
import mysql.connector
from tkinter import END
import smtplib
from email.mime.text import MIMEText
from JUDI_CASE import Judiciary,ttk_frame
import re
from cryptography.fernet import Fernet

class ttk_window(ttk.Frame):
    def __init__(self,container):
        super().__init__(container)
        self.usertype=tk.StringVar() 
        
    def combo_type(self,container):
        self.combobox=ttk.Combobox(container,textvariable=self.usertype, font=('yu gothic ui', 16, "bold"))
        self.combobox['value']=('Clerk','Judge')
        self.combobox.current(0)
        self.combobox.grid(row=3, column=1)
    def tree_view(self,container,function2):
        self.scroll_x=ttk.Scrollbar(container,orient='horizontal')
        self.scroll_y=ttk.Scrollbar(container,orient='vertical')
        column_one=('First Name','Second Name','Work ID','User Type','Email','Contact','Username',"Users' Role",'Date Created')
        self.case_table=ttk.Treeview(container,columns=column_one,xscrollcommand=self.scroll_y.set,yscrollcommand=self.scroll_y.set)

        self.scroll_x.pack(side='bottom',fill='x')
        self.scroll_y.pack(side='right',fill='y')


        self.scroll_x=ttk.Scrollbar(command=self.case_table.xview)
        self.scroll_y=ttk.Scrollbar(command=self.case_table.yview)
        column_two=('First Name','Second Name','Work ID','User Type','Email','Contact','Username',"Users' Role",'Date Created')

        for x,y in zip(column_one,column_two):
            self.case_table.heading(x,text=y)
        for x in column_one:
            self.case_table.column(x,width=100)

        self.case_table['show']='headings'
        self.case_table.pack(fill='both',expand=1) 
        self.case_table.bind("<ButtonRelease-1>",function2)  
        self.fetch_data()

    def fetch_data(self):
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1caleb2denzeil",
            database="Judiciary"
        )
        my_cursor = db.cursor()
        sql_query="SELECT First_name,Second_name,Work_ID,User_type,Email,Contact,Username,Roles, Date_created from admin_information"
        my_cursor.execute(sql_query)
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            case_table = self.case_table
            case_table.delete(*case_table.get_children())
            for i in rows:
                case_table.insert("", END, values=i)
            db.commit()
        db.close()   
    

class Admin_Panel(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Admin Panel')
        #self.resizable(False,False)
        self.state('zoomed')
        self.geometry('1200x700')
        self.configure(bg='#FF884C')

        self.search_string=tk.StringVar()
        self.first=tk.StringVar()
        self.second=tk.StringVar()
        self.work=tk.StringVar()
        self.email_string=tk.StringVar()
        self.contact_string=tk.StringVar()
        self.password_string=tk.StringVar()
        self.repeat_string=tk.StringVar()
        self.username_string=tk.StringVar()
        self.datecreated_string=tk.StringVar()
        self.radio_string=tk.StringVar()


        #===========Frames======================#
        self.main_frame=tk.LabelFrame(self,bg="white",text='User Details',font=('yu gothic ui', 15, "bold"))
        self.main_frame.place(width=826,height=470,x=10,y=70)

        self.second_frame=tk.LabelFrame(self,bg="white",font=('yu gothic ui', 15, "bold"),text='Display Details')
        self.second_frame.place(width=330,height=470,x=1030,y=70)

        self.search_frame=tk.Frame(self,bg="white")
        self.search_frame.place(width=330,height=40,x=1030,y=10)

        self.button_frame=tk.LabelFrame(self,bg="white")
        self.button_frame.place(width=170,height=470,x=850,y=70)

        self.display_frame=tk.Frame(self,bg="grey")
        self.display_frame.place(width=1350,height=200,x=10,y=550)
        #======================================================#

        #===============Search Frame=====================#
        self.search_button=tk.Button(self.search_frame,text='Search',command=self.search_function, bg='#2C73C7',fg='white',width=10,font=('yu Gothic ui',18))
        self.search_button.place(x=1,height=40)

        self.search_entry = tk.Entry(self.search_frame, highlightthickness=0, relief='flat', textvariable=self.search_string ,bg="lightgrey", fg="#6b6a69",
                                    font=("yu gothic ui ", 23, "bold"), insertbackground = '#6b6a69')
        self.search_entry.place(x=130,height=40,width=200)
        #===============================================#
        #==============Main Frame====================#
        self.first_name=tk.Label(self.main_frame,text='First Name',font=('yu gothic ui', 16, "bold"),fg='#100A06',bg='white',relief='flat')
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
        self.my_user=ttk_window(self)
        self.my_user.combo_type(self.main_frame)

        
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
                                    font=("yu gothic ui ", 16, "bold"),show="*" ,insertbackground = '#6b6a69')
        self.password_entry.grid(row=7,column=1,pady=7)
       
        self.repeat_password=tk.Label(self.main_frame,text='Repeat Password',font=('yu gothic ui', 16, "bold"),fg='#100A06',bg='White',relief='flat',)
        self.repeat_password.grid(row=8,column=0,sticky='W',pady=7)
        self.repeat_entry= tk.Entry(self.main_frame, highlightthickness=0, relief='flat',textvariable=self.repeat_string, bg="lightgrey", fg="#6b6a69",
                                    font=("yu gothic ui ", 16, "bold"),show="*" ,insertbackground = '#6b6a69')
        self.repeat_entry.grid(row=8,column=1,pady=7)
        

        self.username=tk.Label(self.main_frame,text='Username',font=('yu gothic ui', 16, "bold"),fg='#100A06',bg='White',relief='flat',)
        self.username.grid(row=0,column=3,sticky='W',pady=7)
        self.username_entry= tk.Entry(self.main_frame, highlightthickness=0, relief='flat',textvariable=self.username_string, bg="lightgrey", fg="#6b6a69",
                                    font=("yu gothic ui ", 16, "bold"), insertbackground = '#6b6a69')
        self.username_entry.grid(row=0,column=4,pady=7)

        self.date_created=tk.Label(self.main_frame,text='Date Created',font=('yu gothic ui', 16, "bold"),fg='#100A06',bg='White',relief='flat',)
        self.date_created.grid(row=1,column=3,sticky='W',pady=7)
        self.date_entry= tk.Entry(self.main_frame, highlightthickness=0, relief='flat',textvariable=self.datecreated_string, bg="lightgrey", fg="#6b6a69",
                                    font=("yu gothic ui ", 16, "bold"), insertbackground = '#6b6a69')
        self.date_entry.grid(row=1,column=4,pady=7)

        self.radio_label=tk.Label(self.main_frame,text="Users' Role",font=('yu gothic ui', 16, "bold"),relief='flat')
        self.radio_label.grid(row=2,column=3)
        self.radiobutton_one=tk.Radiobutton(self.main_frame,font=('yu gothic ui', 14, "bold"),padx=5, pady=5 ,text='Normal User',value='Normal',variable=self.radio_string)
        self.radiobutton_one.grid(row=2,column=4)
        self.radiobutton_two=tk.Radiobutton(self.main_frame,font=('yu gothic ui', 14, "bold"),padx=5, pady=5, text='Admin User',value='Admin',variable=self.radio_string)
        self.radiobutton_two.grid(row=3,column=4)

        #=============================================================================================#
        #=======================Buttons===============================================================#
        self.txtprescription=tk.Text(self.second_frame,font=('yu gothic ui',14,"bold"),bg='#94897F',padx=5,pady=6,width=28,height=16)
        self.txtprescription.grid(row=0,column=0)

        self.details=tk.Button(self.button_frame,text='Details',command=self.user_details, bg='#d77337',fg='white',font=('Goudy old style',18))
        self.details.place(x=2,y=5,width=163)

        self.submit_details=tk.Button(self.button_frame,text='Submit Details',command=self.submit_and_function ,bg='#d77337',fg='white',font=('Goudy old style',18))
        self.submit_details.place(x=2,y=70,width=163)

        self.update_button=tk.Button(self.button_frame,text='Update Details',command=self.update_function, bg='#d77337',fg='white',font=('Goudy old style',18))
        self.update_button.place(x=2,y=140,width=163)

        self.delete_button=tk.Button(self.button_frame,text='Delete Details',command=self.delete_function,bg='#d77337',fg='white',font=('Goudy old style',18))
        self.delete_button.place(x=2,y=210,width=163)

        self.clear_button=tk.Button(self.button_frame,text='Clear',command=self.clear_entries ,bg='#d77337',fg='white',font=('Goudy old style',18))
        self.clear_button.place(x=2,y=280,width=163)

        
        self.exit_button=tk.Button(self.button_frame,text='Exit',bg='#d77337',command=self.exit,fg='white',font=('Goudy old style',18))
        self.exit_button.place(x=2,y=350,width=163)
        
        
        self.mainpage_button=tk.Button(self.button_frame,text='Main Page',bg='#d77337',command=self.main_page,fg='white',font=('Goudy old style',18))
        self.mainpage_button.place(x=2,y=420,width=163)


        #=================Display frame================#
        self.my_user.tree_view(self.display_frame,self.get_treedetails)

        #===========Functionalities====================#
    def submit(self):
             if self.password_string.get() == " " and self.repeat_string.get() ==" ":
                  messagebox.showerror("Error","All fields are required")
             else:
                   db=mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="1caleb2denzeil",
                    database="Judiciary"
                     )        
                   cursor=db.cursor()

                   try:
                        user=self.my_user.usertype.get()
                        key=Fernet.generate_key()
                        fernet=Fernet(key)
                        data=self.password_string.get().encode('utf-8')
                        encrypted_data=fernet.encrypt(data)
                        data_2=self.repeat_string.get().encode('utf-8')
                        encrypted_data_two=fernet.encrypt(data_2)
                        sql_query="INSERT INTO admin_information(First_name,Second_name,Work_ID,User_type,Email,Contact,Pass_word,Password_repeat,Username, Date_created,Roles,Crypto_keys ) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                        values=(self.first.get()
                             ,self.second.get()
                             ,self.work.get()
                             ,user
                             ,self.email_string.get()
                             ,self.contact_string.get()
                             ,encrypted_data
                             ,encrypted_data_two
                             ,self.username_string.get()
                             ,self.datecreated_string.get()
                             ,self.radio_string.get(),
                             key)
                        cursor.execute(sql_query,values)
                        db.commit()
                        messagebox.showinfo("Success","Details submitted sucessfully")
                   except mysql.connector.Error as error:
                        messagebox.showerror("Error",str(error)) 
                   finally:
                       cursor.close()
                       self.my_user.fetch_data()
                       db.close()     
    
    def get_treedetails(self,event=""):
         tree_row = self.my_user.case_table.focus()
         content = self.my_user.case_table.item(tree_row)
         user=self.my_user.usertype
         row=content['values']
         self.first.set(row[0])
         self.second.set(row[1])
         self.work.set(row[2])
         user.set(row[3])
         self.email_string.set(row[4])
         self.contact_string.set(row[5])
         self.username_string.set(row[6])
         self.radio_string.set(row[7])
         self.datecreated_string.set(row[8])
    
    def search_function(self):
         
         db=mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="1caleb2denzeil",
                    database="Judiciary"
                     )        
         cursor=db.cursor()
         try:
              search=self.search_string.get()
              user=self.my_user.usertype.get()
              sql_query="SELECT First_name,Second_name,Work_ID,User_type,Email,Contact,Pass_word,Password_repeat,Username, Date_created, Roles FROM admin_information WHERE Work_ID=%s "
              cursor.execute(sql_query,(search,))
              row=cursor.fetchone()
              
              if row is None:
                    messagebox.showinfo("No Results", "No information found for the given search query.")
              else:
                  user=self.my_user.usertype
                  self.first.set(row[0])
                  self.second.set(row[1])
                  self.work.set(row[2])
                  user.set(row[3])
                  self.email_string.set(row[4])
                  self.contact_string.set(row[5])
                  self.password_string.set(row[6])
                  self.repeat_string.set(row[7])
                  self.username_string.set(row[8])
                  self.datecreated_string.set(row[9])
                  self.radio_string.set(row[10])
                        

         except mysql.connector.Error as error:
                messagebox.showerror("Error",str(error)) 
         finally:
              cursor.close()
              db.close()

    def password_regex(self):
         password=self.password_string.get()
         repeat=self.repeat_string.get()

         if password== " " and repeat== " ":
             return messagebox.showwarning("Warning","All fields are required")
         #Check password strength
         if not re.search(r'[A-Z]',password):
              messagebox.showerror("Warning","Password must have at least one uppercase letter")
              return
         if not re.search(r'[a-z]',password):
              messagebox.showerroe("Warning","Password must have at least one lowercase letter")
              return
         if not re.search(r'\d',password):
              messagebox.showerroe("Warning","Password must have at least one number")
              return
         if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
              messagebox.showerroe("Warning","Password must have at least one special character")
              return
    
    def update_function(self):
          db=mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="1caleb2denzeil",
                    database="Judiciary"
                     )        
          cursor=db.cursor()
          try:
     
              user=self.my_user.usertype.get()
              sql_query="UPDATE admin_information SET First_name=%s,Second_name=%s, User_type=%s,Email=%s,Contact=%s,Username=%s, Date_created=%s, Roles=%s WHERE Work_ID=%s "
              values=(        self.first.get()
                             ,self.second.get()
                             ,user
                             ,self.email_string.get()
                             ,self.contact_string.get()
                             ,self.username_string.get()
                             ,self.datecreated_string.get()
                             ,self.radio_string.get()
                             ,self.work.get())
              cursor.execute(sql_query,values)

              #update_workID="UPDATE admin_information SET Work_ID=%s WHERE First_name=%s"
              #workid_values=(self.work.get(),self.first.get())
              #cursor.execute(update_workID,workid_values)

              db.commit()
              messagebox.showinfo("Success","User Details Updated Succesfully")
          except mysql.connector.Error as error:
                messagebox.showerror("Error",str(error)) 
          finally:
              cursor.close()
              self.my_user.fetch_data()
              db.close()
    def user_details(self):
         
         user=self.my_user.usertype.get()
         self.txtprescription.insert(END,"First Name:\t" + self.first.get() + "\n")
         self.txtprescription.insert(END,"Second Name:\t" + self.second.get() + "\n")
         self.txtprescription.insert(END,"Work ID:\t" + self.work.get() + "\n")
         self.txtprescription.insert(END,"User Type:\t" + user + "\n")
         self.txtprescription.insert(END,"Email:\t" + self.email_string.get() + "\n")
         self.txtprescription.insert(END,"Contact:\t" + self.contact_string.get() + "\n")
         self.txtprescription.insert(END,"Password:\t" + self.password_string.get() + "\n")
         self.txtprescription.insert(END,"Repeat Password:\t" + self.repeat_entry.get() + "\n")
         self.txtprescription.insert(END,"Username:\t" + self.username_string.get() + "\n")
         self.txtprescription.insert(END,"Date created:\t" + self.datecreated_string.get() + "\n")
         self.txtprescription.insert(END,"Users' Role:\t" + self.radio_string.get() + "\n")

    def submit_and_function(self):
         self.password_regex()
         self.submit()
         self.user_details()  
         self.send_email() 

    def delete_function(self):
          db=mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="1caleb2denzeil",
                    database="Judiciary"
                     )        
          cursor=db.cursor()

          try:
            
            sql_query="DELETE FROM admin_information where WORK_ID=%s"
            worker=self.work.get()
            values=(worker)
            cursor.execute(sql_query,(values,))
            db.commit()
            messagebox.showinfo("Success","User details deleted sucessfully")

          except mysql.connector.Error as error:
                        messagebox.showerror("Error",str(error)) 

          finally:
                       cursor.close()
                       self.my_user.fetch_data()
                       db.close()  

    def clear_entries(self):
         user=self.my_user.usertype
         self.first.set(" ")
         self.second.set(" ")
         self.work.set(" ")
         user.set(" ")
         self.email_string.set(" ")
         self.contact_string.set(" ")
         self.password_string.set(" ")
         self.repeat_string.set(" ")
         self.username_string.set(" ")
         self.datecreated_string.set(" ")
         self.radio_string.set(" ")

    def exit(self):
         exited=messagebox.askyesno("Judiciary Case Management System","Would you like to exit?") 
         if exited>0:
              self.destroy()   

    def send_email(self):
         password=self.password_string.get()
         first=self.first.get()
         second=self.second.get()
         user=self.username_string.get() 
         email=self.email_string.get()  

         
         msg=MIMEText(F"Hello {first} {second}, your username and password are: {user} {password}")
         msg['From']='shiksdenzeil@gmail.com'
         msg['To']=email
         msg['Subject']='Log in details'

         #create smtp
         try: 
                smtp_server = 'smtp.gmail.com'
                smtp_port = 587
                smtp_username = 'shiksdenzeil@gmail.com'
                smtp_password = 'prtrudinlebhhdhe'
                smtp_session = smtplib.SMTP(smtp_server, smtp_port)
                smtp_session.starttls()
                smtp_session.login(smtp_username, smtp_password)
        
                # send mail
                smtp_session.sendmail(smtp_username, email, msg.as_string())
                messagebox.showinfo("Success", "Email sent successfully!")
         except Exception as e:
               messagebox.showerror("Error", str(e))
         finally:
              smtp_session.quit()    

    def main_page(self):
         self.destroy()
         Jud=Judiciary(user_admin_normal="Admin")
         ttk_frame(Jud)
         Jud.mainloop()
            
                    
if __name__ == "__main__":
    admin=Admin_Panel()
    admin.mainloop()        