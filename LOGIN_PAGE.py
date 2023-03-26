import tkinter as tk 
from tkinter import ttk 
from PIL import ImageTk,Image
from tkinter import messagebox
import mysql.connector
from JUDI_CASE import Judiciary,ttk_frame
from Admin_Panel import ttk_window,Admin_Panel
from cryptography.fernet import Fernet

class login(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Log in')
        self.resizable(False,False)
        #self.state('zoomed')
        self.geometry('1000x700')

        #==============Background Image===========================#
        self.my_image=Image.open('cl.jpg')
        self.photo=ImageTk.PhotoImage(self.my_image)
        self.court_image=tk.Label(self,image=self.photo)
        self.court_image.image=self.photo
        self.court_image.pack(fill='both', expand='yes')
        #==========================================================
        self.username=tk.StringVar()
        self.password=tk.StringVar()

        self.main_frame=tk.Frame(self,bg="white")
        self.main_frame.place(width=700,height=500,x=200,y=70)

        self.main_heading = tk.Label(self.main_frame, text="Log in Page", font=('Impact', 35, "bold"),fg='#d77337',bg='White', bd=20,relief='flat'
                             )
        self.main_heading.place(x=80, y=30, width=300,height=75)

        self.employee_label=tk.Label(self.main_frame,text='Clerk Log in area',font=('Goudy old style', 23, "bold"),fg='#d77337',bg='White',bd=20,relief='flat',)
        self.employee_label.place(x=95,y=95)

        self.username_label=tk.Label(self.main_frame,text='Username ',font=('Goudy old style', 23, "bold"),fg='Grey',bg='White',relief='flat',)
        self.username_label.place(x=105,y=165)
      
        self.username_entry = tk.Entry(self.main_frame, highlightthickness=0,textvariable=self.username, relief='flat', bg="lightgrey", fg="#6b6a69",
                                    font=("yu gothic ui ", 12, "bold"), insertbackground = '#6b6a69')
        self.username_entry.place(x=260, y=165, width=270,height=50)

        self.password_label=tk.Label(self.main_frame,text=' Password',font=('Goudy old style', 23, "bold"),fg='Grey',bg='White',relief='flat',)
        self.password_label.place(x=105,y=250)
        
        self.password_entry = tk.Entry(self.main_frame, highlightthickness=0,textvariable=self.password, relief='flat', bg="lightgrey", fg="#6b6a69",
                                    font=("yu gothic ui ", 12, "bold"), insertbackground = '#6b6a69',show="*")
        self.password_entry.place(x=260, y=250, width=270,height=50)

        self.submit_button=tk.Button(self.main_frame,text='Submit Details',command=self.login,bg='#d77337',fg='white',width=20,pady=6,padx=2,font=('Goudy old style',18))
        self.submit_button.place(x=200,y=350)

        #================functionalities+===================#
    def login(self):
            db=mysql.connector.connect(host="localhost",
                user="root",
                password="1caleb2denzeil",
                database="Judiciary")
            cursor=db.cursor()
            username=self.username.get()
            login_password=self.password.get()
            
            try:
                cursor.execute("SELECT Pass_word, Roles,Crypto_keys FROM admin_information WHERE Username=%s",(username,))
                result=cursor.fetchone()
                if result:
                   key=result[2]
                   d_password=result[0]
                   dice=Fernet(key)
                   decrypt_pass=dice.decrypt(d_password.encode()).decode()
                   if login_password == decrypt_pass:
                      messagebox.showinfo("Success","Log in succesful")
                      if result[1] == "Admin":
                        self.destroy()
                        admin=Admin_Panel()
                        admin.mainloop() 
                      else: 
                        self.destroy()
                        Jud=Judiciary("Normal")
                        ttk_frame(Jud)
                        Jud.mainloop()
            
                   else:
                        messagebox.showerror("Error","Invalid Password")   

                else:
                    messagebox.showerror("Error","Invalid Username")
            except mysql.connector.Error as error:
                messagebox.showerror("Error",str(error))
            finally:
                cursor.close()
                db.close()  
                      

if __name__ =="__main__":
    log=login()
    log.mainloop()        

