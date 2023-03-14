#Import the necessary libraries 
from tkinter import ttk 
import tkinter as tk
import random 
import time 
import datetime
from tkinter import messagebox
import mysql.connector
from tkinter import END

class ttk_frame(ttk.Frame):
    def __init__(self,container):
        super().__init__(container)

        self.casestatus_string = tk.StringVar()
        self.judgename_string = tk.StringVar()
    
    def combo_box(self, container):
        
        self.combobox=ttk.Combobox(container,textvariable=self.casestatus_string, font=('arial bold',12), width=33)
        self.combobox['value']=('Active','pending')
        self.combobox.current(0)
        self.combobox.grid(row=7, column=1)
    
    def judge(self,container):
        
        self.combo_j=ttk.Combobox(container,textvariable=self.judgename_string, font=('arial bold',12), width=33)
        self.combo_j['value']=('Justice George Njenga','Justice Jane Kuria')
        self.combo_j.current(0)
        self.combo_j.grid(row=0, column=3)
    
    def scrollbar(self,container):
       
        column_one = ('Case_ID', 'Client_name', 'Lawyer_name', 'Judge', 'Case_Type', 'Date_filed', 'Appearances', 'Billing_info', 'Hearing_date', 'Next_hearing')
        column_two = ('Case ID', 'Client Name', 'Judge', 'Case Type', 'Date filed', 'Appearances', 'Billing info', 'Hearing date', 'Next Hearing')
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
        self.fetch_data()
    
    def fetch_data(self):
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1caleb2denzeil",
            database="Judiciary"
        )
        my_cursor = db.cursor()
        sql_query = "SELECT client_information.Case_ID, client_information.Client_name, judge_information.Judge_name AS Judge, client_information.Case_type, client_information.Date_filed, client_information.Appearances, client_information.Billing_ksh AS Billing_info, client_information.Hearing_date, client_information.Next_hearing FROM client_information JOIN judge_information ON client_information.Judge_ID = judge_information.Judge_ID "
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
    def __init__(self):
        super().__init__()

        self.title('Judiciary Case Mangement System')
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
       
        self.label1=tk.Label(self,bd=13,relief="ridge",text="JUDICIARY CASE MANAGEMENT SYSTEM",fg="blue",bg="white",font=("times new roman bold",38))
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

        self.search_button=tk.Button(self.search_frame,text='Search',bg='#B4123D',fg='white',font=('arial bold',12))
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
         
        #Dataframe right
        self.txtprescription=tk.Text(self.DataFrameRight,font=('arial bold',12),fg='white',bg='#3A88AA',padx=2,pady=6,width=36,height=17)
        self.txtprescription.grid(row=0,column=0)
 
        self.Showdetails=tk.Button(self.ButtonFrame,text='Submit Details',command=self.submit, bg='#B4123D',fg='white',width=22,pady=6,padx=2,font=('arial bold',12))
        self.Showdetails.grid(row=0,column=1,ipady=1)

        self.case_detailsbutton=tk.Button(self.ButtonFrame,text='Case Details',bg='#B4123D',fg='white',width=22,pady=6,padx=2,font=('arial bold',12))
        self.case_detailsbutton.grid(row=0,column=2,ipady=1)
        
        self.update_button=tk.Button(self.ButtonFrame,text='Update',bg='#B4123D',fg='white',width=22,pady=6,padx=2,font=('arial bold',12))
        self.update_button.grid(row=0,column=3,ipady=1)
        
        self.delete_button=tk.Button(self.ButtonFrame,text='Delete',bg='#B4123D',fg='white',width=22,pady=6,padx=2,font=('arial bold',12))
        self.delete_button.grid(row=0,column=4,ipady=1)

        self.clear_button=tk.Button(self.ButtonFrame,text='Clear',bg='#B4123D',fg='white',width=22,pady=6,padx=2,font=('arial bold',12))
        self.clear_button.grid(row=0,column=5,ipady=1)
        
        
        self.exit_button=tk.Button(self.ButtonFrame,text='Exit',bg='#B4123D',fg='white',width=22,pady=6,padx=2,font=('arial bold',12))
        self.exit_button.grid(row=0,column=6,ipady=1)

        # ==================================Scrollbar========================
        self.my_object.scrollbar(self.DetailsFrame)

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

                        judge_tables="INSERT INTO judge_information(Judge_ID,Judge_name,Judge_email,Judge_contact) VALUES (%s,%s,%s,%s)"
                        judge_values=(self.judge_stringid.get(),judgename,self.judgeemail_string.get(),self.judgecontact_string.get())
                        cursor.execute(judge_tables,judge_values)


                        sql_tables="INSERT INTO client_information(Case_ID,Client_name,Client_Contact,Case_type,Case_status, Appearances, Billing_ksh, Judge_ID, Hearing_date, Next_hearing, Laywer_name, Laywer_contact,Date_filed) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                        client_values=(self.caseid_string.get(),self.clientname_string.get(),self.clientcontact_string.get(),self.casetype_string.get(), casestatus ,self.appearances_string.get(),self.billing_string.get()
                                      ,self.judge_stringid.get(),self.hearingdate_string.get(),self.nexthearing_string.get() ,
                                      self.lawyername_string.get(), self.lawyercontact_string.get(),self.datefiled_string.get())
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
        


if __name__ == "__main__":        
    Jud=Judiciary()
    ttk_frame(Jud)
    Jud.mainloop()
