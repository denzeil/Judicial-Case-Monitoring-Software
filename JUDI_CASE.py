#Import the necessary libraries 
from tkinter import ttk 
import tkinter as tk
import random 
import time 
import datetime
from tkinter import messagebox
import mysql.connector
from tkinter import END
import smtplib
from email.mime.text import MIMEText


class ttk_frame(ttk.Frame):
    def __init__(self,container):
        super().__init__(container)
        

        self.casestatus_string = tk.StringVar()
        self.judgename_string = tk.StringVar()
        self.case_table=None
    
    def combo_box(self, container):
        
        self.combobox=ttk.Combobox(container,textvariable=self.casestatus_string, font=('arial bold',12), width=33)
        self.combobox['value']=('Active','pending','Approved','Rejected','Dismissed','Closed','In progress','On hold','Settled','Resolved','Under review','Withdrawn')
        self.combobox.current(0)
        self.combobox.grid(row=7, column=1)
    
    def judge(self,container):
        
        self.combo_j=ttk.Combobox(container,textvariable=self.judgename_string, font=('arial bold',12), width=33)
        self.combo_j['value']=('Justice George Njenga','Justice Jane Kuria')
        self.combo_j.current(0)
        self.combo_j.grid(row=0, column=3)
    
    def scrollbar(self,container,function2):
       
        column_one = ('Case_ID', 'Client_name', 'Judge', 'Case_Type','Case_Status', 'Date_filed', 'Appearances', 'Billing_info', 'Hearing_date', 'Next_hearing')
        column_two = ('Case_ID', 'Client_name', 'Judge', 'Case_Type','Case_Status', 'Date_filed', 'Appearances', 'Billing_info', 'Hearing_date', 'Next_hearing')
        self.case_table = ttk.Treeview(container, columns=column_one)

        self.scroll_y = ttk.Scrollbar(container, orient='vertical',command=self.case_table.yview)
        self.case_table.configure(yscroll=self.scroll_y.set)      
        self.scroll_y.pack(side='right', fill='y')

        self.scroll_x = ttk.Scrollbar(container, orient='horizontal',command=self.case_table.xview)
        self.case_table.configure(xscroll=self.scroll_x.set)
        self.scroll_x.pack(side='bottom', fill='x') 
        
        for x, y in zip(column_one, column_two):
            self.case_table.heading(x, text=y)
            self.case_table.column(x, width=100)

        self.case_table['show'] = 'headings'
        self.case_table.pack(fill='both', expand=1)
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
        sql_query = "SELECT client_information.Case_ID, client_information.Client_name, judge_information.Judge_name, client_information.Case_type,client_information.Case_status, client_information.Date_filed, client_information.Appearances, client_information.Billing_ksh, client_information.Hearing_date, client_information.Next_hearing FROM client_information JOIN judge_information ON client_information.Judge_ID = judge_information.Judge_ID "
        my_cursor.execute(sql_query)
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            case_table = self.case_table
            case_table.delete(*case_table.get_children())
            for i in rows:
                case_table.insert("", END, values=i)
            db.commit()
        db.close()   

#Create the class
class Judiciary(tk.Tk):
    def __init__(self,user_admin_normal):
        super().__init__()
        self.user_admin_normal=user_admin_normal
        self.title('Judicial Case Monitoring Software')
        self.geometry('2000x800+0+0')
        self.configure(bg="#3A88AA")
        
        self.caseid_string=tk.StringVar()
        self.clientname_string=tk.StringVar()
        self.clientcontact_string=tk.StringVar()
        self.lawyername_string=tk.StringVar()
        self.lawyercontact_string=tk.StringVar()
        self.casetype_string=tk.StringVar()
        self.datefiled_string=tk.StringVar()
        self.appearances_string=tk.StringVar()
        self.billing_string=tk.StringVar()
        self.judgeemail_string=tk.StringVar()
        self.hearingdate_string=tk.StringVar()
        self.nexthearing_string=tk.StringVar()
        self.judgecontact_string=tk.StringVar()
        self.judge_stringid=tk.StringVar()
        self.search_string=tk.StringVar()
       
        self.label1=tk.Label(self,bd=13,relief="ridge",text="JUDICIAL CASE MONITORING SOFTWARE",fg="blue",bg="white",font=("times new roman bold",38))
        self.label1.pack(side="top",fill="x")
    
        #Create 
        self.DataFrame=tk.Frame(self,bd=10,relief='ridge',bg="#3A88AA")
        self.DataFrame.place(x=0,y=130,width=1500,height=400)

        #create the left and Right Dataframe
        self.DataFrameLeft=tk.LabelFrame(self.DataFrame,bd=10,relief='ridge',font=("times new roman bold",12),text='CASE DETAILS ENTRY',padx=10)
        self.DataFrameLeft.place(x=0,y=5,width=980,height=380)
           
        self.DataFrameRight=tk.LabelFrame(self.DataFrame,bd=10,relief='ridge',font=("times new roman bold",12),text='CASE DETAILS',padx=10)
        self.DataFrameRight.place(x=990,y=5,width=365,height=380)

        #Create the button frame
        self.ButtonFrame=tk.Frame(self,bd=10,relief='ridge')
        self.ButtonFrame.place(x=0,y=530,width=1530,height=60)

        #DetailsFrame
        self.DetailsFrame=tk.Frame(self,bd=10,relief='ridge')
        self.DetailsFrame.place(x=0,y=600,width=1530,height=140)
        
        #search frame
        self.search_frame=tk.Frame(self,bd=6,relief='ridge',bg="white")
        self.search_frame.place(x=1015,y=79,width=347,height=52)

        self.search_button=tk.Button(self.search_frame,command=self.search_query,text='Search',bg='#B4123D',fg='white',font=('arial bold',12))
        self.search_button.place(x=0,y=0,width=148,height=40)
        self.search_entry=tk.Entry(self.search_frame,textvariable=self.search_string,bg="lightgrey",font=('arial bold',12))
        self.search_entry.place(x=150,y=0,width=190,height=40)

        #Left Dataframe details
        self.case_Id=tk.Label(self.DataFrameLeft,text='Case ID',font=('arial bold',12),padx=2,pady=6 )
        self.case_Id.grid(row=0,column=0,sticky='W')
        self.caseEntry=tk.Entry(self.DataFrameLeft,textvariable=self.caseid_string,font=('arial bold',12),width=35)
        self.caseEntry.grid(row=0,column=1)

        self.client_name=tk.Label(self.DataFrameLeft,text="Client's Name.",font=('arial bold',12),padx=2,pady=6)
        self.client_name.grid(row=1,column=0,sticky='W')
        self.client_Entry=tk.Entry(self.DataFrameLeft,textvariable=self.clientname_string ,font=('arial bold',12),width=35)
        self.client_Entry.grid(row=1,column=1)

        self.client_contact=tk.Label(self.DataFrameLeft,text="Client's Contact",font=('arial bold',12),padx=2,pady=6)
        self.client_contact.grid(row=2,column=0,sticky='W')
        self.clientcontact_entry=tk.Entry(self.DataFrameLeft,textvariable=self.clientcontact_string,font=('arial bold',12),width=35)
        self.clientcontact_entry.grid(row=2,column=1)

        self.lawyer_name=tk.Label(self.DataFrameLeft,text="Lawyer's Name.",font=('arial bold',12),padx=2,pady=6)
        self.lawyer_name.grid(row=3,column=0,sticky='W')
        self.lawyer_entry=tk.Entry(self.DataFrameLeft,textvariable=self.lawyername_string,font=('arial bold',12),width=35)
        self.lawyer_entry.grid(row=3,column=1)

        self.lawyer_contact=tk.Label(self.DataFrameLeft,text="Lawyer's Contact",font=('arial bold',12),padx=2,pady=6)
        self.lawyer_contact.grid(row=4,column=0,sticky='W')
        self.lawyer_contactentry=tk.Entry(self.DataFrameLeft,textvariable=self.lawyercontact_string, font=('arial bold',12),width=35)
        self.lawyer_contactentry.grid(row=4,column=1)

        self.case_type=tk.Label(self.DataFrameLeft,text='Case Type',font=('arial bold',12),padx=2,pady=6)
        self.case_type.grid(row=5,column=0,sticky='W')
        self.case_entry=tk.Entry(self.DataFrameLeft,textvariable=self.casetype_string ,font=('arial bold',12),width=35)
        self.case_entry.grid(row=5,column=1)
        
        self.date_filed=tk.Label(self.DataFrameLeft,text='Date Filed',font=('arial bold',12),padx=2,pady=6)
        self.date_filed.grid(row=6,column=0,sticky='W')
        self.date_entry=tk.Entry(self.DataFrameLeft,textvariable=self.datefiled_string ,font=('arial bold',12),width=35)
        self.date_entry.grid(row=6,column=1)

        self.case_status=tk.Label(self.DataFrameLeft,text="Case Status",font=('arial bold',12),padx=2,pady=6)
        self.case_status.grid(row=7,column=0,sticky='W')
        self.my_object = ttk_frame(self) # create an instance of ttk_frame
        self.my_object.combo_box(self.DataFrameLeft) # add combobox to DataFrameLeft container

        self.appearance=tk.Label(self.DataFrameLeft,text='Court Appearances',font=('arial bold',12),padx=2,pady=6)
        self.appearance.grid(row=8,column=0,sticky='W')
        self.appear=tk.Entry(self.DataFrameLeft,textvariable=self.appearances_string, font=('arial bold',12),width=35)
        self.appear.grid(row=8,column=1)

        self.billing_info=tk.Label(self.DataFrameLeft,text='Billing info.',font=('arial bold',12),padx=2,pady=6)
        self.billing_info.grid(row=9,column=0,sticky='W')
        self.bill=tk.Entry(self.DataFrameLeft,textvariable=self.billing_string ,font=('arial bold',12),width=35)
        self.bill.grid(row=9,column=1)

        self.judge_name=tk.Label(self.DataFrameLeft,text="Judge's Name",font=('arial bold',12),padx=2,pady=6)
        self.judge_name.grid(row=0,column=2,sticky='W')
        self.my_object.judge(self.DataFrameLeft)

        self.judge_email=tk.Label(self.DataFrameLeft,text="Judge's Email",font=('arial bold',12),padx=2,pady=6)
        self.judge_email.grid(row=1,column=2,sticky='W')
        self.judge_entry=tk.Entry(self.DataFrameLeft,textvariable=self.judgeemail_string,font=('arial bold',12),width=35)
        self.judge_entry.grid(row=1,column=3)
         
        self.j_contact=tk.Label(self.DataFrameLeft,text="Judge's Contact",font=('arial bold',12),padx=2,pady=6)
        self.j_contact.grid(row=2,column=2,sticky='W')
        self.j_contactentry=tk.Entry(self.DataFrameLeft,textvariable=self.judgecontact_string ,font=('arial bold',12),width=35)
        self.j_contactentry.grid(row=2,column=3)

        self.judge_id=tk.Label(self.DataFrameLeft,text="Judge ID",font=('arial bold',12),padx=2,pady=6)
        self.judge_id.grid(row=3,column=2,sticky='W')
        self.judgeid_entry=tk.Entry(self.DataFrameLeft,textvariable=self.judge_stringid ,font=('arial bold',12),width=35)
        self.judgeid_entry.grid(row=3,column=3)

         
        self.hearing_date=tk.Label(self.DataFrameLeft,text="Hearing Date",font=('arial bold',12),padx=2,pady=6)
        self.hearing_date.grid(row=4,column=2,sticky='W')
        self.hearingentry=tk.Entry(self.DataFrameLeft,textvariable=self.hearingdate_string ,font=('arial bold',12),width=35)
        self.hearingentry.grid(row=4,column=3)

         
        self.next_hearing=tk.Label(self.DataFrameLeft,text="Next hearing",font=('arial bold',12),padx=2,pady=6)
        self.next_hearing.grid(row=5,column=2,sticky='W')
        self.next_hearingentry=tk.Entry(self.DataFrameLeft,textvariable=self.nexthearing_string ,font=('arial bold',12),width=35)
        self.next_hearingentry.grid(row=5,column=3)
         
        self.description=tk.Label(self.DataFrameLeft,text="Case Description",font=('arial bold',12),padx=2,pady=6)
        self.description.grid(row=6,column=2,sticky='W')
        self.text_description=tk.Text(self.DataFrameLeft,font=('arial bold',12))
        self.text_description.grid(row=6, column=3,rowspan=5, sticky='W', padx=2, pady=6)
        self.text_description.configure(width=35,height=6.6)
        
        

        #self.text_description.rowconfigure(6,weight=5)
        #Dataframe right
        self.txtprescription=tk.Text(self.DataFrameRight,font=('arial bold',12),fg='white',bg='#3A88AA',padx=2,pady=6,width=36,height=17)
        self.txtprescription.grid(row=0,column=0)
 
        self.Showdetails=tk.Button(self.ButtonFrame,text='Submit Details',command=self.print_out, bg='#B4123D',fg='white',width=22,pady=6,padx=2,font=('arial bold',12))
        self.Showdetails.grid(row=0,column=1,ipady=1)

        self.case_detailsbutton=tk.Button(self.ButtonFrame,text='Case Details',command=self.case_details,bg='#B4123D',fg='white',width=22,pady=6,padx=2,font=('arial bold',12))
        self.case_detailsbutton.grid(row=0,column=2,ipady=1)
        
        self.update_button=tk.Button(self.ButtonFrame,text='Update',command=self.update_data, bg='#B4123D',fg='white',width=22,pady=6,padx=2,font=('arial bold',12))
        self.update_button.grid(row=0,column=3,ipady=1)
   
        if self.user_admin_normal == "Admin":
           self.delete_button=tk.Button(self.ButtonFrame,text='Delete',command=self.delete_details ,bg='#B4123D',fg='white',width=22,pady=6,padx=2,font=('arial bold',12))
           self.delete_button.grid(row=0,column=4,ipady=1)
        else:
           self.delete_button=None 

          
        self.clear_button=tk.Button(self.ButtonFrame,text='Clear',command=self.clear_details, bg='#B4123D',fg='white',width=22,pady=6,padx=2,font=('arial bold',12))
        self.clear_button.grid(row=0,column=5,ipady=1)
        
        self.exit_button=tk.Button(self.ButtonFrame,text='Exit',command=self.exit ,bg='#B4123D',fg='white',width=22,pady=6,padx=2,font=('arial bold',12))
        self.exit_button.grid(row=0,column=6,ipady=1)

        if self.delete_button is not None:
           self.delete_button.grid(row=0,column=4,ipady=1)
        
        # ==================================Scrollbar========================
        self.my_object.scrollbar(self.DetailsFrame,self.get_treedetails)

        #==================Functionalities=================================
    def submit(self):
            if self.caseid_string.get()== " " or self.appearances_string == " ":
                messagebox.showerror('Error','All fields are required')
            else:
                 #establish a connection
                    db=mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="1caleb2denzeil",
                    database="Judiciary"
                     )    
                #create a cursor
                    cursor=db.cursor()
            
                    try:
                        casestatus=self.my_object.casestatus_string.get()
                        judgename=self.my_object.judgename_string.get()
                        text=self.text_description.get("1.0","end-1c")
                        

                        judge_tables="INSERT INTO judge_information(Judge_ID,Judge_name,Judge_email,Judge_contact) VALUES (%s,%s,%s,%s)"
                        judge_values=(self.judge_stringid.get(),judgename,self.judgeemail_string.get(),self.judgecontact_string.get())
                        cursor.execute(judge_tables,judge_values)


                        sql_tables="INSERT INTO client_information(Case_ID,Client_name,Client_Contact,Case_type,Case_status, Appearances, Billing_ksh, Judge_ID, Hearing_date, Next_hearing, Laywer_name, Laywer_contact,Date_filed,case_description) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                        client_values=(self.caseid_string.get(),self.clientname_string.get(),self.clientcontact_string.get(),self.casetype_string.get(), casestatus ,self.appearances_string.get(),self.billing_string.get()
                                      ,self.judge_stringid.get(),self.hearingdate_string.get(),self.nexthearing_string.get() ,
                                      self.lawyername_string.get(), self.lawyercontact_string.get(),self.datefiled_string.get(),text)
                        cursor.execute(sql_tables,client_values)
                        
                        #Insert into judge information
                       
                        db.commit()
                        messagebox.showinfo("Success","Case Details inserted successfully")
                        
                    
                    except mysql.connector.Error as error:
                        messagebox.showerror("Error",str(error))

                           
                    finally:
                        cursor.close()
                        self.my_object.fetch_data()
                        db.close()
        
                #establish a connection
                  
        
    def get_treedetails(self,event=""):
        casestatus=self.my_object.casestatus_string
        tree_row = self.my_object.case_table.focus()
        content = self.my_object.case_table.item(tree_row)
        self.judgename = self.my_object.judgename_string
        row=content['values']
        self.caseid_string.set(row[0])
        self.clientname_string.set(row[1])
        self.judgename.set(row[2])
        self.casetype_string.set(row[3])
        casestatus.set(row[4])
        self.datefiled_string.set(row[5])
        self.appearances_string.set(row[6])
        self.billing_string.set(row[7])
        self.hearingdate_string.set(row[8])
        self.nexthearing_string.set(row[9])
        
    #def delete_hide(self):
        #self.hide_button()
        
        #self.delete_details()

    def search_query(self):
              db=mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="1caleb2denzeil",
                    database="Judiciary"
                     ) 
              try:
                 mycursor=db.cursor() 
                 search=self.search_string.get()
                 query="SELECT client_information.Case_ID, client_information.Client_name, client_information.Client_contact, client_information.Case_type, client_information.Case_status, client_information.Appearances, client_information.Billing_ksh, judge_information.Judge_ID, client_information.Hearing_date, client_information.Next_hearing, client_information.Laywer_name, client_information.Laywer_contact, client_information.Date_filed,client_information.case_description, judge_information.Judge_name, judge_information.Judge_email, judge_information.Judge_contact FROM client_information INNER JOIN judge_information ON client_information.Judge_ID = judge_information.Judge_ID WHERE client_information.Case_ID= %s"
                 mycursor.execute(query,(search,))
                 result=mycursor.fetchone()

                 if result is None:
                    messagebox.showinfo("No Results", "No information found for the given search query.")
                 else:
                    casestatus=self.my_object.casestatus_string
                    judgename=self.my_object.judgename_string
                    text=self.text_description.get("1.0","end-1c")
                    self.caseid_string.set(result[0])
                    self.clientname_string.set(result[1])
                    self.clientcontact_string.set(result[2])
                    self.casetype_string.set(result[3])
                    casestatus.set(result[4])
                    self.appearances_string.set(result[5])
                    self.billing_string.set(result[6])
                    self.judge_stringid.set(result[7]) 
                    self.hearingdate_string.set(result[8])
                    self.nexthearing_string.set(result[9])
                    self.lawyername_string.set(result[10])
                    self.lawyercontact_string.set(result[11])
                    self.datefiled_string.set(result[12])
                    self.text_description.delete('1.0', tk.END) 
                    self.text_description.insert(tk.END,result[13])
                    judgename.set(result[14])
                    self.judgeemail_string.set(result[15])
                    self.judgecontact_string.set(result[16])
                   
                  
              except mysql.connector.Error as error:
                        messagebox.showerror("Error",str(error))

                           
              finally:
                        mycursor.close()
                     
                        db.close()

    def update_data(self):
         #establish a connection
                  
                    db=mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="1caleb2denzeil",
                    database="Judiciary"
                     )    
                #create a cursor
                    cursor=db.cursor()
            
                    try:
                        casestatus=self.my_object.casestatus_string.get()
                        judgename=self.my_object.judgename_string.get()
                        text=self.text_description.get("1.0","end-1c")

                        #update the judge_query
                        judge_tables="UPDATE judge_information SET Judge_name=%s,Judge_email=%s,Judge_contact=%s WHERE Judge_ID=%s "
                        judge_values=(judgename,self.judgeemail_string.get(),self.judgecontact_string.get(),self.judge_stringid.get())
                        cursor.execute(judge_tables,judge_values)


                        sql_tables="UPDATE client_information SET Case_ID=%s, Client_name=%s ,Client_Contact=%s ,Case_type=%s, Case_status=%s, Appearances=%s, Billing_ksh=%s, Hearing_date=%s, Next_hearing=%s, Laywer_name=%s, Laywer_contact=%s,Date_filed=%s,case_description=%s WHERE Judge_ID=%s"
                        client_values=(self.caseid_string.get(),self.clientname_string.get(),self.clientcontact_string.get(),self.casetype_string.get(), casestatus ,self.appearances_string.get(),self.billing_string.get()
                                      ,self.hearingdate_string.get(),self.nexthearing_string.get() ,
                                      self.lawyername_string.get(), self.lawyercontact_string.get(),self.datefiled_string.get(),text,self.judge_stringid.get())
                        cursor.execute(sql_tables,client_values)
                        
                        #Insert into judge information
                       
                        db.commit()
                        messagebox.showinfo("Success","Case Details Updated successfully")
                        
                    
                    except mysql.connector.Error as error:
                        messagebox.showerror("Error",str(error))

                           
                    finally:
                        cursor.close()
                        self.my_object.fetch_data()
                        db.close()
    
    def case_details(self):
         casestatus=self.my_object.casestatus_string.get()
         judgename=self.my_object.judgename_string.get()
         text=self.text_description.get("1.0","end-1c")
         self.txtprescription.insert(END,"Case ID:\t\t" + self.caseid_string.get() + "\n")
         self.txtprescription.insert(END,"Client's name:\t\t" + self.clientname_string.get() + "\n")
         self.txtprescription.insert(END,"Client's contact:\t\t" + self.clientcontact_string.get() + "\n")
         self.txtprescription.insert(END,"Lawyer's name:\t\t" + self.lawyercontact_string.get() + "\n")
         self.txtprescription.insert(END,"Lawyer's Contact:\t\t" + self.lawyercontact_string.get() + "\n")
         self.txtprescription.insert(END,"Date Filed:\t\t" + self.datefiled_string.get() + "\n")
         self.txtprescription.insert(END,"Case Status:\t\t" + casestatus + "\n")
         self.txtprescription.insert(END,"Court Appearances:\t\t" + self.appearances_string.get() + "\n")
         self.txtprescription.insert(END,"Judge's name:\t\t" + judgename + "\n")
         self.txtprescription.insert(END,"Judge's email:\t\t" + self.judgeemail_string.get() + "\n")
         self.txtprescription.insert(END,"Judge's Contact:\t\t" + self.judgecontact_string.get() + "\n")
         self.txtprescription.insert(END,"Judge ID:\t\t" + self.judge_stringid.get() + "\n")
         self.txtprescription.insert(END,"Hearing Date:\t\t" + self.hearingdate_string.get() + "\n")
         self.txtprescription.insert(END,"Next Hearing:\t\t" + self.nexthearing_string.get() + "\n")
         self.txtprescription.insert(END,"Case Description:\t\t" + text + "\n")
    
    def print_out(self):
         self.submit()
         self.case_details()
         self.send_email()

    def delete_details(self):
         db=mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="1caleb2denzeil",
                    database="Judiciary" ) 
         try:
           cursor=db.cursor()   
           client_query="DELETE FROM client_information WHERE Judge_ID=%s"
           cursor.execute(client_query,(self.judge_stringid.get(),))
           
           judge_query="DELETE FROM judge_information where Judge_ID=%s"
           cursor.execute(judge_query,(self.judge_stringid.get(),))

           db.commit()
           messagebox.showinfo("Success","Case Details deleted succesfully")

         except mysql.connector.Error as error:
             messagebox.showerror("Error",str(error))  
              
         finally:
              cursor.close()
              self.my_object.fetch_data()
              db.close()
    def clear_details(self):
        casestatus=self.my_object.casestatus_string
        judgename=self.my_object.judgename_string
        
        self.caseid_string.set(" ")
        self.clientname_string.set(" ")
        self.clientcontact_string.set(" ")
        self.casetype_string.set(" ")
        casestatus.set(" ")
        self.appearances_string.set(" ")
        self.billing_string.set(" ")
        self.judge_stringid.set(" ") 
        self.hearingdate_string.set(" ")
        self.nexthearing_string.set(" ")
        self.lawyername_string.set(" ")
        self.lawyercontact_string.set(" ")
        self.datefiled_string.set(" ")
        judgename.set(" ")
        self.judgeemail_string.set(" ")
        self.judgecontact_string.set(" ")
        self.text_description.delete('1.0','end')
        
        
    def send_email(self):
         judge_name=self.my_object.judgename_string.get()
         hearingdate=self.hearingdate_string.get()
         judge_email=self.judgeemail_string.get()
         case_status=self.my_object.casestatus_string.get()
         lawyer_name=self.lawyername_string.get()
         case_type=self.casetype_string.get()
         nexthearing=self.nexthearing_string.get()
         #client_name=self.clientname_string.get()
         case_id=self.caseid_string.get()
         text=self.text_description.get("1.0","end-1c")

         msg=MIMEText(F"Hello {judge_name},I hope your doing well. On {hearingdate}, you will be required in Court for a hearing, the Case ID is {case_id} and the type of case:{case_type}. The lawyer in charge of the case is {lawyer_name}. The case is {case_status}.Case Description: {text}\nyour next hearing will be on {nexthearing}.\n Have a nice day.")
         msg['From']='calebdenzeil@gmail.com'
         msg['To']=judge_email
         msg['Subject']='Case Details'

         #create smtp
         try: 
                smtp_server = 'smtp.gmail.com'
                smtp_port = 587
                smtp_username = 'calebdenzeil@gmail.com'
                smtp_password = 'lxxwhddjbziaqeuz'
                smtp_session = smtplib.SMTP(smtp_server, smtp_port)
                smtp_session.starttls()
                smtp_session.login(smtp_username, smtp_password)
        
                # send mail
                smtp_session.sendmail(smtp_username, judge_email, msg.as_string())
                messagebox.showinfo("Success", "Email sent successfully!")
         except Exception as e:
               messagebox.showerror("Error", str(e))
         finally:
              smtp_session.quit()


    def exit(self):
         exited=messagebox.askyesno("Judiciary Case Management System","Would you like to exit?") 
         if exited>0:
              self.destroy()

if __name__ == "__main__":        
    Jud=Judiciary(user_admin_normal=False)
    ttk_frame(Jud)
    Jud.mainloop()
                    
