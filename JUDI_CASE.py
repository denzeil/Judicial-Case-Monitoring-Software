#Import the necessary libraries 
from tkinter import ttk 
import tkinter as tk
import random 
import time 
import datetime
from tkinter import messagebox
import _mysql_connector

class ttk_frame(ttk.Frame):
    def __init__(self,container):
        super().__init__(container)
        
    
    def combo_box(self, container):
        self.casestatus_string=tk.StringVar()
        self.combobox=ttk.Combobox(container,textvariable=self.casestatus_string, font=('arial bold',12), width=33)
        self.combobox['value']=('Active','pending')
        self.combobox.current(0)
        self.combobox.grid(row=7, column=1)
       

    def judge(self,container):
        self.judgename_string=tk.StringVar()
        self.combo_j=ttk.Combobox(container,textvariable=self.judgename_string, font=('arial bold',12), width=33)
        self.combo_j['value']=('Justice George Njenga','Justice Jane Kuria')
        self.combo_j.current(0)
        self.combo_j.grid(row=0, column=3)
    
    def scrollbar(self,container):
        self.scroll_x=ttk.Scrollbar(container,orient='horizontal')
        self.scroll_y=ttk.Scrollbar(container,orient='vertical')
        column_one=('Case_ID','Client_name','Lawyer_name','Judge','Case_Type','Date_filed','Appearances','Billing_info',
                            'Hearing_date','Next_hearing')
        self.case_table=ttk.Treeview(container,columns=column_one,xscrollcommand=self.scroll_y.set,yscrollcommand=self.scroll_y.set)

        self.scroll_x.pack(side='bottom',fill='x')
        self.scroll_y.pack(side='right',fill='y')


        self.scroll_x=ttk.Scrollbar(command=self.case_table.xview)
        self.scroll_y=ttk.Scrollbar(command=self.case_table.yview)
        column_two=('Case ID','Client Name','Judge','Case Type','Date filed','Appearances','Billing info','Hearing date',
                  'Next Hearing')

        for x,y in zip(column_one,column_two):
            self.case_table.heading(x,text=y)
        for x in column_one:
            self.case_table.column(x,width=100)

        self.case_table['show']='headings'
        self.case_table.pack(fill='both',expand=1)    
        
         
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
       
        self.label1=tk.Label(self,bd=20,relief="ridge",text="JUDICIARY CASE MANAGEMENT SYSTEM",fg="blue",bg="white",font=("times new roman bold",40))
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

        #Left Dataframe details
        self.case_Id=tk.Label(self.DataFrameLeft,text='Case ID',font=('arial bold',12),padx=2,pady=6)
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
        self.lawyer_entry=tk.Entry(self.DataFrameLeft,textvariable=self.lawyercontact_string,font=('arial bold',12),width=35)
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
        my_object = ttk_frame(self)  # create an instance of ttk_frame
        my_object.combo_box(self.DataFrameLeft) # add combobox to DataFrameLeft container

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
        my_object.judge(self.DataFrameLeft)

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
        self.txtprescription=tk.Text(self.DataFrameRight,font=('arial bold',12),fg='white',bg='#3A88AA',padx=2,pady=6,width=45,height=16)
        self.txtprescription.grid(row=0,column=0)
 
        self.Showdetails=tk.Button(self.ButtonFrame,text='Details',bg='#B4123D',fg='white',width=26,pady=6,padx=2,font=('arial bold',12))
        self.Showdetails.grid(row=0,column=1,ipady=1)

        self.case_detailsbutton=tk.Button(self.ButtonFrame,text='Case Details',bg='#B4123D',fg='white',width=26,pady=6,padx=2,font=('arial bold',12))
        self.case_detailsbutton.grid(row=0,column=2,ipady=1)
        
        self.update_button=tk.Button(self.ButtonFrame,text='Update',bg='#B4123D',fg='white',width=26,pady=6,padx=2,font=('arial bold',12))
        self.update_button.grid(row=0,column=3,ipady=1)
        
        self.delete_button=tk.Button(self.ButtonFrame,text='Delete',bg='#B4123D',fg='white',width=26,pady=6,padx=2,font=('arial bold',12))
        self.delete_button.grid(row=0,column=4,ipady=1)
        
        self.exit_button=tk.Button(self.ButtonFrame,text='Exit',bg='#B4123D',fg='white',width=26,pady=6,padx=2,font=('arial bold',12))
        self.exit_button.grid(row=0,column=5,ipady=1)

        # ==================================Scrollbar========================
        my_object.scrollbar(self.DetailsFrame)
        

if __name__ == "__main__":        
    Jud=Judiciary()
    Jud.mainloop()
