
from tkinter import *
from tkinter import ttk
import pymysql
class student:
    def __init__(self,root):
        self.root=root
        self.root.title("**Student Management System**")
        self.root.geometry("1300x600+0+0")

        title=Label(self.root,text="Student Management System",bd=6 ,relief=GROOVE, font=("times new roman",20,"bold"),bg="black",fg="cyan")
        title.pack(side=TOP,fill=X)
    

    #--------All Variables--------------
        self.Roll_No_var=StringVar()
        self.Name_var=StringVar() 
        self.Email_var=StringVar() 
        self.Gender_var=StringVar() 
        self.contact_var=StringVar() 
        self.DOB_var=StringVar() 
        self.ADD_var=StringVar()
        self.search_by=StringVar()
        self.search_txt=StringVar() 



    #--------manage frame--------
        manage_frame=Frame(self.root,bd=2,relief=RIDGE,bg="cyan")
        manage_frame.place(x=12,y=55,width=410,height=530)

        m_title=Label(manage_frame,text="Students Details",bg="cyan", font=("times new roman",20,"bold"))
        m_title.grid(row=0,columnspan=2,pady=10)

        lbl_roll=Label(manage_frame,text="Roll N0.:",bg="cyan",font=("times new roman",15,"bold"))
        lbl_roll.grid(row=1,column=0,pady=10,padx=20,sticky="W")
        txt_roll=Entry(manage_frame,textvariable=self.Roll_No_var, font=("times new roman",12,"bold"),bd=2,relief=GROOVE)
        txt_roll.grid(row=1,column=1,pady=10,padx=20,sticky="W")

        
        lbl_Name=Label(manage_frame,text="Name:",bg="cyan",font=("times new roman",15,"bold"))
        lbl_Name.grid(row=2,column=0,pady=10,padx=20,sticky="W")
        txt_Name=Entry(manage_frame,textvariable=self.Name_var, font=("times new roman",12,"bold"),bd=2,relief=GROOVE)
        txt_Name.grid(row=2,column=1,pady=10,padx=20,sticky="W")

        
        lbl_Email=Label(manage_frame,text="Email:",bg="cyan",font=("times new roman",15,"bold"))
        lbl_Email.grid(row=3,column=0,pady=10,padx=20,sticky="W")
        txt_Email=Entry(manage_frame,textvariable=self.Email_var, font=("times new roman",12,"bold"),bd=2,relief=GROOVE)
        txt_Email.grid(row=3,column=1,pady=10,padx=20,sticky="W")

        
        lbl_gender=Label(manage_frame,text="Gender:",bg="cyan",font=("times new roman",15,"bold"))
        lbl_gender.grid(row=4,column=0,pady=10,padx=20,sticky="W")
        combo_gender=ttk.Combobox(manage_frame,textvariable=self.Gender_var, font=("times new roman",10,"bold"),state='readonly')
        combo_gender['values']=("Male","Female","Other")
        combo_gender.grid(row=4,column=1,padx=20,pady=10)

        
        lbl_contact=Label(manage_frame,text="Contact No.:",bg="cyan",font=("times new roman",15,"bold"))
        lbl_contact.grid(row=5,column=0,pady=10,padx=20,sticky="W")
        txt_contact=Entry(manage_frame,textvariable=self.contact_var, font=("times new roman",12,"bold"),bd=2,relief=GROOVE)
        txt_contact.grid(row=5,column=1,pady=10,padx=20,sticky="W")

        
        lbl_DOB=Label(manage_frame,text="D.O.B",bg="cyan",font=("times new roman",15,"bold"))
        lbl_DOB.grid(row=6,column=0,pady=10,padx=20,sticky="W")
        txt_DOB=Entry(manage_frame,textvariable=self.DOB_var, font=("times new roman",12,"bold"),bd=2,relief=GROOVE)
        txt_DOB.grid(row=6,column=1,pady=10,padx=20,sticky="W")

        
        lbl_add=Label(manage_frame,text="Address:",bg="cyan",font=("times new roman",15,"bold"))
        lbl_add.grid(row=7,column=0,pady=10,padx=20,sticky="W")
        self.txt_add=Text(manage_frame,width=20,height=4)
        self.txt_add.grid(row=7,column=1,pady=10,padx=20,sticky="W")
        

    #--------Button Frame----------
        btn_frame=Frame(manage_frame,bd=0,relief=RIDGE,bg="cyan")
        btn_frame.place(x=9,y=450,width=385)

        Addbtn=Button(btn_frame,text="Add",width=10,command=self.add_students).grid(row=0,column=0,padx=10,pady=10)
        updatebtn=Button(btn_frame,text="Update",width=10 ,command=self.update_data).grid(row=0,column=1,padx=10,pady=10)
        deletebtn=Button(btn_frame,text="Delete",width=10,command=self.delete_data).grid(row=0,column=2,padx=10,pady=10)
        clearbtn=Button(btn_frame,text="Clear",width=10,command=self.clear).grid(row=0,column=3,padx=10,pady=10)



    #-------detail frame---------

        detail_frame=Frame(self.root,bd=2,relief=RIDGE,bg="cyan")
        detail_frame.place(x=435,y=55,width=820,height=530)

        lbl_search=Label(detail_frame,text="Search By:",bg="cyan",font=("times new roman",15,"bold"))
        lbl_search.grid(row=0,column=0,pady=10,padx=20,sticky="W")
        combo_search=ttk.Combobox(detail_frame,textvariable=self.search_by, width=15,font=("times new roman",10,"bold"),state='readonly')
        combo_search['values']=("Roll_No","Name","contact")
        combo_search.grid(row=0,column=1,padx=20,pady=10)


        txt_search=Entry(detail_frame, textvariable=self.search_txt, width=20,font=("times new roman",10,"bold"),bd=2,relief=GROOVE)
        txt_search.grid(row=0,column=2,pady=10,padx=20,sticky="W")
        searchbtn=Button(detail_frame,text="Search",command=self.search_data, width=12,pady=4,padx=3).grid(row=0,column=3,padx=10,pady=10)
        showallbtn=Button(detail_frame,text="Showall", command=self.fetch_data, width=12,pady=4,padx=3).grid(row=0,column=4,padx=10,pady=10)

    #---------Table frame----------------
        table_frame=Frame(detail_frame,bd=2,relief=RIDGE,bg="cyan")
        table_frame.place(x=10,y=60,width=790,height=450)

        scroll_x=Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(table_frame,orient=VERTICAL)
        self.student_table=ttk.Treeview(table_frame,columns=("Roll","Name","Email","Gender","contact","DOB","ADD"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        self.student_table.heading("Roll",text="Roll No.")
        self.student_table.heading("Name",text="Name")
        self.student_table.heading("Email",text="Email")
        self.student_table.heading("Gender",text="Gender")
        self.student_table.heading("contact",text="Contact")
        self.student_table.heading("DOB",text="D.O.B")
        self.student_table.heading("ADD",text="Address")
        
        self.student_table['show']='headings'
        self.student_table.column("Roll",width=120)
        self.student_table.column("Name",width=120)
        self.student_table.column("Email",width=120)
        self.student_table.column("Gender",width=100)
        self.student_table.column("contact",width=100)
        self.student_table.column("DOB",width=100)
        self.student_table.column("ADD",width=130)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease-1>",self.get_curser)
        self.fetch_data()


    def add_students(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="sms")
        cur=con.cursor()
        cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s) ",(self.Roll_No_var.get(),
                                                                          self.Name_var.get(),  
                                                                          self.Email_var.get(),
                                                                          self.Gender_var.get(),
                                                                          self.contact_var.get(),
                                                                          self.DOB_var.get(),
                                                                          self.txt_add.get('1.0',END)
                                                                         ))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()
    def fetch_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="sms")
        cur=con.cursor()
        cur.execute("select * from students")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('',END,value=row)
            con.commit()

        con.close()
    def clear(self):
        self.Roll_No_var.set("")
        self.Name_var.set("")
        self.Email_var.set("")
        self.Gender_var.set("")
        self.contact_var.set("")
        self.DOB_var.set("")
        self.txt_add.delete("1.0",END)
    
    def get_curser(self,ev):
        curser_row=self.student_table.focus()
        contents=self.student_table.item(curser_row)
        row=contents['values']
        self.Roll_No_var.set(row[0])
        self.Name_var.set(row[1])
        self.Email_var.set(row[2])
        self.Gender_var.set(row[3])
        self.contact_var.set(row[4])
        self.DOB_var.set(row[5])
        self.txt_add.delete("1.0",END)
        self.txt_add.insert(END,row[6])

    def update_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="sms")
        cur=con.cursor()
        cur.execute("update students set name=%s,email=%s,gender=%s,contact=%s,dob=%s,add=%s where roll_no=%s;",(
                                                                                                                 self.Name_var.get(),  
                                                                                                                 self.Email_var.get(),
                                                                                                                 self.Gender_var.get(),
                                                                                                                 self.contact_var.get(),
                                                                                                                 self.DOB_var.get(),
                                                                                                                 self.txt_add.get('1.0',END),
                                                                                                                 self.Roll_No_var.get()
                                                                                                                ))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()
    def delete_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="sms")
        cur=con.cursor()
        cur.execute("delete from students where roll_no=%s",self.Roll_No_var.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()
    def search_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="sms")
        cur=con.cursor()
        cur.execute("select * from students where "+str(self.search_by.get())+"="+str(self.search_txt.get()))
        rows=cur.fetchall()
        if len(rows)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('',END,value=row)
            con.commit()

        con.close()




    




root=Tk()
ob=student(root)
root.mainloop()