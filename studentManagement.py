#Import Modules
from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox
#Student Management System with database connectivity ..and add table in database
#and correct .gridin button

class Password:

    def __init__(self,root):

        self.root = root
        self.root.title("CPP Secrets Student Management System")
        self.root.geometry("1350x700+0+0")

        title = Label(self.root,text="CPP Secrets Student Management System",bd = 10,
                relief=GROOVE,font=("Arial",43,"bold"),bg="#00A1E4",fg="#FFFCF9")
        title.pack(side=TOP,fill=X)

        
        #Variables
        self.username = StringVar()
        self.old_password = StringVar()
        self.new_password = StringVar()


        #DashBoard Frame
        Dash_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="#F0EDEE")
        Dash_Frame.place(x=2,y=95,width=98,height=600)

        manage_student_btn = Button(Dash_Frame,bg="#00A1E4",text="Student",fg="#F0EDEE",
        font=("Arial",9,"bold"),relief=GROOVE,width=11,pady=20,command=self.student_btn).
        grid(row=0,column=0,padx=2,pady=0,sticky="w")

        manage_employee_btn = Button(Dash_Frame,bg="#00A1E4",fg="#F0EDEE",text="Employee",
        font=("Arial",9,"bold"),relief=GROOVE,width=11,pady=20,command=self.employee_btn).
        grid(row=1,column=0,padx=2,pady=2,sticky="w")

        department_btn = Button(Dash_Frame,text="Department",bg="#00A1E4",fg="#F0EDEE",
        font=("Arial",9,"bold"),relief=GROOVE,width=11,pady=20,command=self.dept_btn).
        grid(row=2,column=0,padx=2,pady=2,sticky="w")

        password_btn = Button(Dash_Frame,text="Password",bg="#00A1E4",fg="#F0EDEE",
        font=("Arial",9,"bold"),relief=GROOVE,width=11,pady=20).
        grid(row=3,column=0,padx=2,pady=2,sticky="w")

        exit_btn = Button(Dash_Frame,text="Exit",bg="#00A1E4",fg="#F0EDEE",
        font=("Arial",9,"bold"),relief=GROOVE,width=11,pady=20,command=self.logout).
        grid(row=4,column=0,padx=2,pady=2,sticky="w")

                           

        #Manage Frame
        Manage_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="#F0EDEE")
        Manage_Frame.place(x=100,y=95,width=1250,height=600)

               
        m_title = Label(Manage_Frame,text="Change Password",bg="#F0EDEE",fg="#0A090C",
        font=("Arial",30,"bold","italic"))

        m_title.grid(row = 0,columnspan=2,pady=20,padx=450)

        
        lbl_username = Label(Manage_Frame,text="Username -",bg="#F0EDEE",fg="#0A090C",
        font=("Arial",15,"bold"))
        lbl_username.grid(row = 1,column=0,pady=10,padx=500)

    

        txt_dept_id = Entry(Manage_Frame,textvariable=self.username,
        font=("Arial",15,"bold"),bd=5,relief=GROOVE)
        txt_dept_id.grid(row = 2,column=0,pady=10,padx=500)

        

        lbl_name = Label(Manage_Frame,text="Old Password -",bg="#F0EDEE",fg="#0A090C",
        font=("Arial",15,"bold"))
        lbl_name.grid(row = 3,column=0,pady=10,padx=500)

    

        txt_name = Entry(Manage_Frame,show="*",textvariable=self.old_password,
        font=("Arial",15,"bold"),bd=5,relief=GROOVE)
        txt_name.grid(row = 4,column=0,pady=10,padx=500)

        

        lbl_name = Label(Manage_Frame,text="New Password -",bg="#F0EDEE",fg="#0A090C",
        font=("Arial",15,"bold"))
        lbl_name.grid(row = 5,column=0,pady=10,padx=500)

    

        txt_name = Entry(Manage_Frame,show="*",textvariable=self.new_password,
        font=("Arial",15,"bold"),bd=5,relief=GROOVE)
        txt_name.grid(row = 6,column=0,pady=10,padx=500)
        

        #Button Frame
        btn_frame = Frame(Manage_Frame,bg="#F0EDEE")
        btn_frame.place(x=400,y=420,width=410) 

        
        chg_btn = Button(btn_frame,text="Change Password",bg="#00A1E4",fg="#FFFCF9",
        font=("Arial",10,"bold"),relief=GROOVE,width=30,command=self.change_pass)
        .grid(row=0,column=0,padx=90,pady=10,ipady=4)

       
                         

    def change_pass(self):

        if self.username.get() == "" or self.old_password.get() == "" 
                                                 or self.new_password.get() == "":
            messagebox.showerror("Error","Fields Missing")

        else:
            connect = pymysql.connect("localhost","root","","Student Management")
            curr = connect.cursor()

            
            curr.execute("SELECT * from admin")
            rows = curr.fetchall()

            
            for row in rows:
                if row[1] == self.username.get() and row[2] == self.old_password.get():
                    connect = pymysql.connect("localhost","root","","Student Management")  
                    curr = connect.cursor()

                    

                    curr.execute("UPDATE ADMIN SET password=%s where username=%s",
                    (self.new_password.get(),self.username.get()))

                    connect.commit()
                    connect.close()
                    messagebox.showinfo("Success","Password Updated Successsfully")
                else:
                    messagebox.showerror("Error","Please Make Sure That the Details 
                                                                         are Correct")

         

    def logout(self):

        self.root.destroy() 
        st_root = Tk()
        st = Login(st_root)
        st_root.mainloop()

       
    def student_btn(self):
        self.root.destroy() 
        st_root = Tk()
        st = Student(st_root)
        st_root.mainloop()

       
    def employee_btn(self):
        self.root.destroy() 
        st_root = Tk()
        st = Employee(st_root)
        st_root.mainloop()

      
    def dept_btn(self):
        self.root.destroy()
        st_root = Tk()
        st = Department(st_root)
        st_root.mainloop()

class Department:

    def __init__(self,root):
        self.root = root
        self.root.title("CPP Secrets Student Management System")
        self.root.geometry("1350x700+0+0")

       
        title = Label(self.root,text="CPP Secrets Student Management System",bd = 10,
        relief=GROOVE,font=("Arial",43,"bold"),bg="#00A1E4",fg="#FFFCF9")
        title.pack(side=TOP,fill=X)

        

        #Variables
        self.dept_id = StringVar()
        self.dept_name = StringVar()


        #DashBoard Frame
        Dash_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="#F0EDEE")
        Dash_Frame.place(x=2,y=95,width=98,height=600)

       
        manage_student_btn = Button(Dash_Frame,bg="#00A1E4",text="Student",fg="#F0EDEE",
        font=("Arial",9,"bold"),relief=GROOVE,width=11,pady=20,command=self.student_btn)
        .grid(row=0,column=0,padx=2,pady=0,sticky="w")

        manage_employee_btn = Button(Dash_Frame,bg="#00A1E4",fg="#F0EDEE",text="Employee",
        font=("Arial",9,"bold"),relief=GROOVE,width=11,pady=20,command=self.employee_btn)
        .grid(row=1,column=0,padx=2,pady=2,sticky="w")

        department_btn = Button(Dash_Frame,text="Department",bg="#00A1E4",fg="#F0EDEE",
        font=("Arial",9,"bold"),relief=GROOVE,width=11,pady=20)
        .grid(row=2,column=0,padx=2,pady=2,sticky="w")

        password_btn = Button(Dash_Frame,text="Password",bg="#00A1E4",fg="#F0EDEE",
        font=("Arial",9,"bold"),relief=GROOVE,width=11,pady=20,command=self.pass_btn)
        .grid(row=3,column=0,padx=2,pady=2,sticky="w")

        exit_btn = Button(Dash_Frame,text="Exit",bg="#00A1E4",fg="#F0EDEE",
        font=("Arial",9,"bold"),relief=GROOVE,width=11,pady=20,command=self.logout)
        .grid(row=4,column=0,padx=2,pady=2,sticky="w")

                           

        #Manage Frame
        Manage_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="#F0EDEE")
        Manage_Frame.place(x=100,y=95,width=450,height=600)

                

        m_title = Label(Manage_Frame,text="Manage Department",bg="#F0EDEE",fg="#0A090C",
        font=("Arial",30,"bold","italic"))
        m_title.grid(row = 0,columnspan=2,pady=20)

        

        lbl_dept_id = Label(Manage_Frame,text="Department ID -",bg="#F0EDEE",fg="#0A090C",
        font=("Arial",15,"bold"))
        lbl_dept_id.grid(row = 1,column=0,pady=30,padx=100)

    

        txt_dept_id = Entry(Manage_Frame,textvariable=self.dept_id,
        font=("Arial",15,"bold"),bd=5,relief=GROOVE)
        txt_dept_id.grid(row = 2,column=0,pady=10,padx=100)

        

        lbl_name = Label(Manage_Frame,text="Department Name -",bg="#F0EDEE",fg="#0A090C",
        font=("Arial",15,"bold"))
        lbl_name.grid(row = 3,column=0,pady=30,padx=100)

    
        txt_name = Entry(Manage_Frame,textvariable=self.dept_name,
        font=("Arial",15,"bold"),bd=5,relief=GROOVE)
        txt_name.grid(row = 4,column=0,pady=10,padx=100)

        
        #Button Frame
        btn_frame = Frame(Manage_Frame,bg="#F0EDEE")
        btn_frame.place(x=12,y=420,width=410) 

        

        add_btn = Button(btn_frame,text="Add",width=10,bg="#00A1E4",fg="#FFFCF9",
        font=("Arial",10,"bold"),command=self.add_department)
        .grid(row=0,column=0,padx=5,pady=10)

        update_btn = Button(btn_frame,text="Update",width=10,bg="#00A1E4",fg="#FFFCF9",
        font=("Arial",10,"bold"),command=self.update).grid(row=0,column=1,padx=5,pady=10)

        delete_btn = Button(btn_frame,text="Delete",width=10,bg="#00A1E4",fg="#FFFCF9",
        font=("Arial",10,"bold"),command=self.delete).grid(row=0,column=2,padx=5,pady=10)

        clear_btn = Button(btn_frame,text="Clear",width=10,bg="#00A1E4",fg="#FFFCF9",     
        font=("Arial",10,"bold"),command=self.clear_field)
        .grid(row=0,column=3,padx=5,pady=10)

        
        #Detail Frame
        Detail_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="#FFFCF9")
        Detail_Frame.place(x=550,y=95,width=800,height=600)

       
        logout_btn = Button(Detail_Frame,text="Log Out",bg="#00A1E4",fg="#FFFCF9",
        font=("Arial",10,"bold"),relief=GROOVE,width=10,pady=5,command=self.logout)
        .grid(row=0,column=7,padx=690,pady=10)

        

        #Table Frame
        Table_Frame = Frame(Detail_Frame,bg="#0A090C")
        Table_Frame.place(x=10,y=60,width=760,height=505)

        

        X_scroll = Scrollbar(Table_Frame,orient=HORIZONTAL)

        Y_scroll = Scrollbar(Table_Frame,orient=VERTICAL)

        self.Table = ttk.Treeview(Table_Frame,columns=("DEPT-ID","Department Name")
        ,xscrollcommand=X_scroll.set,yscrollcommand=Y_scroll.set)

        X_scroll.pack(side=BOTTOM,fill=X)

        Y_scroll.pack(side=RIGHT,fill=Y)

        X_scroll.config(command=self.Table.xview)

        Y_scroll.config(command=self.Table.yview)

        self.Table.heading("DEPT-ID",text="DEPT-ID")

        self.Table.heading("Department Name",text="Department Name")

            

        

        self.Table['show']="headings"

        self.Table.column("DEPT-ID",width=100)

        self.Table.column("Department Name",width=100)



        self.Table.pack(fill=BOTH,expand=1)

        self.Table.bind('<ButtonRelease 1>',self.get_fields)

        self.show_data()

        

    def add_department(self):
        if self.dept_id.get() == "" or self.dept_name.get() == "":
            messagebox.showerror("Error","All Fields are Required")
        else:
            connect = pymysql.connect("localhost","root","","Student Management")
            curr = connect.cursor()

 
            curr.execute("INSERT INTO DEPARTMENT VALUES(%s,%s)",(self.dept_id.get(),

                                                                 self.dept_name.get(),

                                                                ))

            connect.commit()
            self.show_data()
            self.clear_field()
            connect.close()
            messagebox.showinfo("Success","Record Successfully Added")

        

    def show_data(self):
        connect = pymysql.connect("localhost","root","","Student Management")
        curr = connect.cursor()

        

        curr.execute("SELECT * from department")
        rows = curr.fetchall()

        if(len(rows)!=0):
            self.Table.delete(*self.Table.get_children())
            for row in rows:
                self.Table.insert('',END,values=row)
            connect.commit()
        connect.close()

        

    def clear_field(self):

        if self.dept_id.get() == "" or self.dept_name.get() == "":
            messagebox.showerror("Error","All Fields are Required")
        else:
            self.dept_id.set("")
            self.dept_name.set("")


    def get_fields(self,event):

        cursor_row = self.Table.focus()
        content = self.Table.item(cursor_row)
        row = content['values']

        self.dept_id.set(row[0])
        self.dept_name.set(row[1])
   

    def update(self):

        if self.dept_id.get() == "" or self.dept_name.get() == "":
            messagebox.showerror("Error","All Fields are Required")
        else:
            connect = pymysql.connect("localhost","root","","Student Management")
            curr = connect.cursor()

            

            curr.execute("UPDATE Department SET name=%s where dept_id=%s",
            (self.dept_name.get(),self.dept_id.get()))

            connect.commit()
            self.show_data()
            self.clear_field()
            connect.close()
            messagebox.showinfo("Succes","Record Successfully Updated")

        
    def delete(self):

        if self.dept_id.get() == "" or self.dept_name.get() == "":
            messagebox.showerror("Error","All Fields are Required")
        else:
            connect = pymysql.connect("localhost","root","","Student Management")
            curr = connect.cursor()

            

            curr.execute("DELETE from DEPARTMENT where dept_id=%s",(self.dept_id.get()))


            connect.commit()
            self.show_data()
            self.clear_field()
            connect.close()
            messagebox.showinfo("Succes","Record Successfully Deleted")
      

    def logout(self):

        self.root.destroy() 
        st_root = Tk()
        st = Login(st_root)
        st_root.mainloop()

        

    def student_btn(self):

        self.root.destroy() 
        st_root = Tk()
        st = Student(st_root)
        st_root.mainloop()
   

    def employee_btn(self):

        self.root.destroy() 
        st_root = Tk()
        st = Employee(st_root)
        st_root.mainloop()

        

    def pass_btn(self):

        self.root.destroy() 
        st_root = Tk()
        st = Password(st_root)
        st_root.mainloop()

class Employee:

    def __init__(self,root):
        self.root = root
        self.root.title("CPP Secrets Student Management System")
        self.root.geometry("1350x700+0+0")

        

        title = Label(self.root,text="CPP Secrets Student Management System",bd = 10,
        relief=GROOVE,font=("Arial",43,"bold"),bg="#00A1E4",fg="#FFFCF9")
        title.pack(side=TOP,fill=X)

      
        #Variables
        self.emp_id = StringVar()
        self.dept_id = StringVar()
        self.ename = StringVar()
        self.email_id = StringVar()
        self.contact = StringVar()
        self.dept = StringVar()
        self.address = StringVar()
        self.position = StringVar()

        

        self.search_combo = StringVar()
        self.search_field = StringVar()

        

        #DashBoard Frame
        Dash_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="#F0EDEE")
        Dash_Frame.place(x=2,y=95,width=98,height=600)

        

        manage_student_btn = Button(Dash_Frame,bg="#00A1E4",text="Student",fg="#F0EDEE",
        font=("Arial",9,"bold"),relief=GROOVE,width=11,pady=20,command=self.student_btn)
        .grid(row=0,column=0,padx=2,pady=0,sticky="w")

        manage_employee_btn = Button(Dash_Frame,bg="#00A1E4",fg="#F0EDEE",text="Employee",
        font=("Arial",9,"bold"),relief=GROOVE,width=11,pady=20)
        .grid(row=1,column=0,padx=2,pady=2,sticky="w")

        department_btn = Button(Dash_Frame,text="Department",bg="#00A1E4",fg="#F0EDEE",
        font=("Arial",9,"bold"),relief=GROOVE,width=11,pady=20,command=self.dept_btn)
        .grid(row=2,column=0,padx=2,pady=2,sticky="w")

        password_btn = Button(Dash_Frame,text="Password",bg="#00A1E4",fg="#F0EDEE",
        font=("Arial",9,"bold"),relief=GROOVE,width=11,pady=20,command=self.pass_btn)
        .grid(row=3,column=0,padx=2,pady=2,sticky="w")

        exit_btn = Button(Dash_Frame,text="Exit",bg="#00A1E4",fg="#F0EDEE",
        font=("Arial",9,"bold"),relief=GROOVE,width=11,pady=20,command=self.logout)
        .grid(row=4,column=0,padx=2,pady=2,sticky="w")

                           

        #Manage Frame
        Manage_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="#F0EDEE")
        Manage_Frame.place(x=100,y=95,width=450,height=600)

                

        m_title = Label(Manage_Frame,text="Manage Employees",bg="#F0EDEE",fg="#0A090C",
        font=("Arial",30,"bold","italic"))
        m_title.grid(row = 0,columnspan=2,pady=20)

        

        lbl_roll = Label(Manage_Frame,text="Emp ID.",bg="#F0EDEE",fg="black",
        font=("Arial",15,"bold"))
        lbl_roll.grid(row = 1,column=0,pady=10,padx=20,sticky="w")

    

        txt_Roll = Entry(Manage_Frame,textvariable=self.emp_id,font=("Arial",15,"bold"),
        bd=5,relief=GROOVE)
        txt_Roll.grid(row = 1,column=1,pady=10,padx=20,sticky="w")

        

        lbl_name = Label(Manage_Frame,text="Name.",bg="#F0EDEE",fg="black",
        font=("Arial",15,"bold"))
        lbl_name.grid(row = 2,column=0,pady=10,padx=20,sticky="w")

    

        txt_name = Entry(Manage_Frame,textvariable=self.ename,font=("Arial",15,"bold")
        ,bd=5,relief=GROOVE)
        txt_name.grid(row = 2,column=1,pady=10,padx=20,sticky="w")

        

        lbl_email = Label(Manage_Frame,text="Email-ID.",bg="#F0EDEE",fg="black",
        font=("Arial",15,"bold"))
        lbl_email.grid(row = 3,column=0,pady=10,padx=20,sticky="w")

    

        txt_email = Entry(Manage_Frame,textvariable=self.email_id,
        font=("Arial",15,"bold"),bd=5,relief=GROOVE)
        txt_email.grid(row = 3,column=1,pady=10,padx=20,sticky="w")

        

        lbl_contact = Label(Manage_Frame,text="Contact",bg="#F0EDEE",fg="black",
        font=("Arial",15,"bold"))
        lbl_contact.grid(row = 4,column=0,pady=10,padx=20,sticky="w")

    

        txt_contact = Entry(Manage_Frame,textvariable=self.contact,
        font=("Arial",15,"bold"),bd=5,relief=GROOVE)
        txt_contact.grid(row = 4,column=1,pady=10,padx=20,sticky="w")

        

        lbl_Dept = Label(Manage_Frame,text="Dept No",bg="#F0EDEE",fg="black", 
        font=("Arial",15,"bold"))
        lbl_Dept.grid(row = 5,column=0,pady=10,padx=20,sticky="w")

    

        txt_dept = Entry(Manage_Frame,textvariable=self.dept,font=("Arial",15,"bold")
        ,bd=5,relief=GROOVE)
        txt_dept.grid(row = 5,column=1,pady=10,padx=20,sticky="w")


        lbl_position = Label(Manage_Frame,text="Position",bg="#F0EDEE",fg="black",
        font=("Arial",15,"bold"))
        lbl_position.grid(row = 6,column=0,pady=10,padx=20,sticky="w")

    

        txt_dept = Entry(Manage_Frame,textvariable=self.position,
        font=("Arial",15,"bold"),bd=5,relief=GROOVE)
        txt_dept.grid(row = 6,column=1,pady=10,padx=20,sticky="w")        

        

        lbl_address = Label(Manage_Frame,text="Address",bg="#F0EDEE",fg="black",
        font=("Arial",15,"bold"))
        lbl_address.grid(row = 7,column=0,pady=10,padx=20,sticky="w")

    

        self.txt_address = Text(Manage_Frame,bd=2,relief=RIDGE,width =30,height=4)
        self.txt_address.grid(row = 7,column=1,pady=10,padx=20,sticky="w")

        

        #Button Frame
        btn_frame = Frame(Manage_Frame,bg="#F0EDEE")
        btn_frame.place(x=12,y=520,width=410) 

        

        add_btn = Button(btn_frame,text="Add",width=10,bg="#00A1E4",fg="#FFFCF9",
        font=("Arial",10,"bold"),command=self.add_employee)
        .grid(row=0,column=0,padx=5,pady=10)

        update_btn = Button(btn_frame,text="Update",width=10,bg="#00A1E4",fg="#FFFCF9",
        font=("Arial",10,"bold"),command=self.update)
        .grid(row=0,column=1,padx=5,pady=10)

        delete_btn = Button(btn_frame,text="Delete",width=10,bg="#00A1E4",fg="#FFFCF9",
        font=("Arial",10,"bold"),command=self.delete)
        .grid(row=0,column=2,padx=5,pady=10)

        clear_btn = Button(btn_frame,text="Clear",width=10,bg="#00A1E4",fg="#FFFCF9",
        font=("Arial",10,"bold"),command=self.clear_field)
        .grid(row=0,column=3,padx=5,pady=10)

        

        

        #Detail Frame
        Detail_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="#FFFCF9")
        Detail_Frame.place(x=550,y=95,width=800,height=600)

        

        lbl_search = Label(Detail_Frame,text="Search-",bg="#FFFCF9",fg="#0A090C",
        font=("Arial",18,"bold"))
        lbl_search.grid(row = 0,column=0,pady=10,padx=15,sticky="w")

        

        search_box = ttk.Combobox(Detail_Frame,width=10,textvariable=self.search_combo,
        font=("Arial",13,"bold"),state="readonly")

        search_box['values'] = ("Emp_ID","Dept_ID","Position","Email_ID")
        search_box.grid(row=0,column=1,pady=10,padx=10,ipady=4,sticky="w")

        

        

        txt_search = Entry(Detail_Frame,width=20,textvariable=self.search_field,
        font=("Arial",10,"bold"),bd=5,relief=GROOVE)
        txt_search.grid(row = 0,column=2,pady=10,padx=20,ipady=4,sticky="w")

        

        search_btn = Button(Detail_Frame,text="Search",bg="#00A1E4",fg="#FFFCF9",
        font=("Arial",10,"bold"),relief=GROOVE,width=10,pady=5,command=self.search_data)
        .grid(row=0,column=5,padx=10,pady=10)

        show_all_btn = Button(Detail_Frame,text="Show All",bg="#00A1E4",fg="#FFFCF9",
        font=("Arial",10,"bold"),relief=GROOVE,width=10,pady=5,command=self.show_data)
        .grid(row=0,column=6,padx=10,pady=10)

        logout_btn = Button(Detail_Frame,text="Log Out",bg="#00A1E4",fg="#FFFCF9",
        font=("Arial",10,"bold"),relief=GROOVE,width=10,pady=5,command=self.logout)
        .grid(row=0,column=7,padx=10,pady=10)

        

        #Table Frame
        Table_Frame = Frame(Detail_Frame,bg="#0A090C")
        Table_Frame.place(x=10,y=60,width=760,height=505)

        

        X_scroll = Scrollbar(Table_Frame,orient=HORIZONTAL)

        Y_scroll = Scrollbar(Table_Frame,orient=VERTICAL)

        self.Table = ttk.Treeview(Table_Frame,columns=("Emp-ID","Department","Name",
        "Email-ID","Address","Contact No","Position"),xscrollcommand=X_scroll.set,
         yscrollcommand=Y_scroll.set)


        X_scroll.pack(side=BOTTOM,fill=X)
        Y_scroll.pack(side=RIGHT,fill=Y)
        X_scroll.config(command=self.Table.xview)
        Y_scroll.config(command=self.Table.yview)
        self.Table.heading("Emp-ID",text="Emp-ID")
        self.Table.heading("Department",text="Dept")
        self.Table.heading("Name",text="Name")
        self.Table.heading("Email-ID",text="Email-ID")
        self.Table.heading("Address",text="Address")
        self.Table.heading("Contact No",text="Contact")
        self.Table.heading("Position",text="Position")

            

        
        self.Table['show']="headings"
        self.Table.column("Emp-ID",width=100)
        self.Table.column("Department",width=100)
        self.Table.column("Name",width=100)
        self.Table.column("Email-ID",width=100)
        self.Table.column("Address",width=150)
        self.Table.column("Contact No",width=100)
        self.Table.column("Position",width=100)

       
        self.Table.pack(fill=BOTH,expand=1)
        self.Table.bind('<ButtonRelease 1>',self.get_fields)
        self.show_data()

        

    def add_employee(self):

        if self.emp_id.get() == "" or self.ename.get() == "" or self.email_id.get() == ""
        or self.position.get()== "" or self.dept.get()== ""or self.contact.get() == ""
        or self.txt_address.get('1.0',END) == "":

            messagebox.showerror("Error","All Fields are Required")

        else:
            connect = pymysql.connect("localhost","root","","Student Management")
            curr = connect.cursor()

            

            curr.execute("INSERT INTO EMPLOYEE VALUES(%s,%s,%s,%s,%s,%s,%s)",
            (self.emp_id.get(), self.dept.get(), self.ename.get(), self.email_id.get(), 
             self.txt_address.get('1.0',END), self.contact.get(), self.position.get() ))

            connect.commit()
            self.show_data()
            self.clear_field()
            connect.close()

            messagebox.showinfo("Success","Record Successfully Added")

        

    def show_data(self):

        connect = pymysql.connect("localhost","root","","Student Management")
        curr = connect.cursor()

        
        curr.execute("SELECT * from employee")
        rows = curr.fetchall()

        if(len(rows)!=0):

            self.Table.delete(*self.Table.get_children())
            for row in rows:

                self.Table.insert('',END,values=row)

            connect.commit()
        connect.close()

        

    def clear_field(self):

        if self.emp_id.get() == "" or self.ename.get() == "" or self.email_id.get() == ""
        or self.position.get()== "" or self.dept.get()== ""or self.contact.get() == "" 
        or self.txt_address.get('1.0',END) == "":

            messagebox.showerror("Error","All Fields are Required")

        else:

            self.emp_id.set("")
            self.dept.set("")
            self.email_id.set("")
            self.ename.set("")
            self.contact.set("")
            self.position.set("")
            self.txt_address.delete("1.0",END)

        

    def get_fields(self,event):

        cursor_row = self.Table.focus()
        content = self.Table.item(cursor_row)
        row = content['values']

        

        self.emp_id.set(row[0])
        self.dept.set(row[1])
        self.ename.set(row[2])
        self.email_id.set(row[3])
        self.txt_address.delete("1.0",END)
        self.txt_address.insert(END,row[4])
        self.contact.set(row[5])
        self.position.set(row[6])


        

    def update(self):

        if self.emp_id.get() == "" or self.ename.get() == "" or self.email_id.get() == ""
        or self.position.get()== "" or self.dept.get()== ""or self.contact.get() == "" 
        or self.txt_address.get('1.0',END) == "":

            messagebox.showerror("Error","All Fields are Required")

        else:
            connect = pymysql.connect("localhost","root","","Student Management")
            curr = connect.cursor()

            
            curr.execute("UPDATE EMPLOYEE SET dept_id=%s,ename=%s,email_id=%s,address=%s,
contact_no=%s,position=%s where emp_id=%s",(
self.dept.get(), self.ename.get(),
self.email_id.get(), self.txt_address.get('1.0',END), self.contact.get(),
self.position.get(),  self.emp_id.get()                                                                                                                           ))

            connect.commit()
            self.show_data()
            self.clear_field()
            connect.close()

            messagebox.showinfo("Succes","Record Successfully Updated")

        

    def delete(self):

        if self.emp_id.get() == "" or self.ename.get() == "" or self.email_id.get() == ""
        or self.position.get()== "" or self.dept.get()== ""or self.contact.get() == "" 
        or self.txt_address.get('1.0',END) == "":

            messagebox.showerror("Error","All Fields are Required")

        else:
            connect = pymysql.connect("localhost","root","","Student Management")
            curr = connect.cursor()

           
            curr.execute("DELETE from EMPLOYEE where emp_id=%s",(self.emp_id.get()))

                                                                           
            connect.commit()
            self.show_data()
            self.clear_field()
            connect.close()
            messagebox.showinfo("Succes","Record Successfully Deleted")

        

    def search_data(self):

        if self.search_combo.get() == "" or self.search_field.get() == "":
            messagebox.showerror("Error","Some Fields might be Empty")

        else:
            connect = pymysql.connect("localhost","root","","Student Management")
            curr = connect.cursor()

            

            curr.execute("SELECT * from employee where "+str(self.search_combo.get())+
                         " LIKE '%"+str(self.search_field.get())+"%'")

            rows = curr.fetchall()
            if(len(rows)!=0):

                self.Table.delete(*self.Table.get_children())
                for row in rows:

                    self.Table.insert('',END,values=row)

                connect.commit()
            connect.close()

            

    def logout(self):

        self.root.destroy() 
        st_root = Tk()
        st = Login(st_root)
        st_root.mainloop()

        

    def student_btn(self):

        self.root.destroy() 
        st_root = Tk()
        st = Student(st_root)
        st_root.mainloop()

        

    def dept_btn(self):

        self.root.destroy()
        em_root = Tk()
        em = Department(em_root)
        em_root.mainloop()

        

    def pass_btn(self):

        self.root.destroy() 
        ps_root = Tk()
        ps = Password(ps_root)
        ps_root.mainloop()

class Student:

    def __init__(self,root):
        self.root = root
        self.root.title("CPP Secrets Student Management System")
        self.root.geometry("1350x700+0+0")

        

        title = Label(self.root,text="CPP Secrets Student Management System"
        ,bd = 10,relief=GROOVE,font=("Arial",43,"bold"),bg="#00A1E4",fg="#FFFCF9")

        title.pack(side=TOP,fill=X)

        

        #Variables
        self.roll_no = StringVar()
        self.name = StringVar()
        self.email_id = StringVar()
        self.gender = StringVar()
        self.contact = StringVar()
        self.dob = StringVar()
        self.address = StringVar()

        

        self.search_combo = StringVar()
        self.search_field = StringVar()

        
        #DashBoard Frame
        Dash_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="#F0EDEE")
        Dash_Frame.place(x=2,y=95,width=98,height=600)

        

        manage_student_btn = Button(Dash_Frame,bg="#00A1E4",text="Student",fg="#F0EDEE",
        font=("Arial",9,"bold"),relief=GROOVE,width=11,pady=20)
        .grid(row=0,column=0,padx=2,pady=0,sticky="w")

        manage_employee_btn = Button(Dash_Frame,bg="#00A1E4",fg="#F0EDEE",text="Employee",
        font=("Arial",9,"bold"),relief=GROOVE,width=11,pady=20,command=self.employee_btn)
        .grid(row=1,column=0,padx=2,pady=2,sticky="w")

        department_btn = Button(Dash_Frame,text="Department",bg="#00A1E4",fg="#F0EDEE",
        font=("Arial",9,"bold"),relief=GROOVE,width=11,pady=20,command=self.dept_btn)
        .grid(row=2,column=0,padx=2,pady=2,sticky="w")

        password_btn = Button(Dash_Frame,text="Password",bg="#00A1E4",fg="#F0EDEE",
        font=("Arial",9,"bold"),relief=GROOVE,width=11,pady=20,command=self.pass_btn)
        .grid(row=3,column=0,padx=2,pady=2,sticky="w")

        exit_btn = Button(Dash_Frame,text="Exit",bg="#00A1E4",fg="#F0EDEE",
        font=("Arial",9,"bold"),relief=GROOVE,width=11,pady=20,command=self.logout)
        .grid(row=4,column=0,padx=2,pady=2,sticky="w")

                           

        #Manage Frame

        Manage_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="#F0EDEE")
        Manage_Frame.place(x=100,y=95,width=450,height=600)

                

        m_title = Label(Manage_Frame,text="Manage Student",bg="#F0EDEE",fg="#0A090C",
        font=("Arial",30,"bold","italic"))
        m_title.grid(row = 0,columnspan=2,pady=20)

        

        lbl_roll = Label(Manage_Frame,text="Roll No.",bg="#F0EDEE",fg="black",
        font=("Arial",15,"bold"))
        lbl_roll.grid(row = 1,column=0,pady=10,padx=20,sticky="w")

    

        txt_Roll = Entry(Manage_Frame,textvariable=self.roll_no,font=("Arial",15,"bold"),
        bd=5,relief=GROOVE)
        txt_Roll.grid(row = 1,column=1,pady=10,padx=20,sticky="w")

        

        lbl_name = Label(Manage_Frame,text="Name.",bg="#F0EDEE",fg="black",
        font=("Arial",15,"bold"))
        lbl_name.grid(row = 2,column=0,pady=10,padx=20,sticky="w")

    

        txt_name = Entry(Manage_Frame,textvariable=self.name,font=("Arial",15,"bold"),
        bd=5,relief=GROOVE)
        txt_name.grid(row = 2,column=1,pady=10,padx=20,sticky="w")

        

        lbl_email = Label(Manage_Frame,text="Email-ID.",bg="#F0EDEE",fg="black",
        font=("Arial",15,"bold"))
        lbl_email.grid(row = 3,column=0,pady=10,padx=20,sticky="w")

    

        txt_email = Entry(Manage_Frame,textvariable=self.email_id,
        font=("Arial",15,"bold"),bd=5,relief=GROOVE)
        txt_email.grid(row = 3,column=1,pady=10,padx=20,sticky="w")

        

        lbl_gender = Label(Manage_Frame,text="Gender",bg="#F0EDEE",fg="black",
        font=("Arial",15,"bold"))
        lbl_gender.grid(row = 4,column=0,pady=10,padx=20,sticky="w")

        

        gender_box = ttk.Combobox(Manage_Frame,textvariable=self.gender,
        font=("Arial",13,"bold"),state="readonly")

        gender_box['values'] = ("Male","Female","Other")
        gender_box.grid(row=4,column=1,pady=10,padx=20,sticky="w")

        

        lbl_contact = Label(Manage_Frame,text="Contact",bg="#F0EDEE",fg="black", 
        font=("Arial",15,"bold"))
        lbl_contact.grid(row = 5,column=0,pady=10,padx=20,sticky="w")

    

        txt_contact = Entry(Manage_Frame,textvariable=self.contact,
        font=("Arial",15,"bold"),bd=5,relief=GROOVE)
        txt_contact.grid(row = 5,column=1,pady=10,padx=20,sticky="w")

        

        lbl_DOB = Label(Manage_Frame,text="D.O.B",bg="#F0EDEE",fg="black",
        font=("Arial",15,"bold"))
        lbl_DOB.grid(row = 6,column=0,pady=10,padx=20,sticky="w")

    

        self.txt_DOB = Entry(Manage_Frame,textvariable=self.dob,font=("Arial",15,"bold")
        ,bd=5,relief=GROOVE)
        self.txt_DOB.grid(row = 6,column=1,pady=10,padx=20,sticky="w")

        

        

        lbl_address = Label(Manage_Frame,text="Address",bg="#F0EDEE",fg="black",
        font=("Arial",15,"bold"))
        lbl_address.grid(row = 7,column=0,pady=10,padx=20,sticky="w")

    

        self.txt_address = Text(Manage_Frame,bd=2,relief=RIDGE,width =30,height=4)
        self.txt_address.grid(row = 7,column=1,pady=10,padx=20,sticky="w")

        

        #Button Frame
        btn_frame = Frame(Manage_Frame,bg="#F0EDEE")
        btn_frame.place(x=12,y=520,width=410) 

        

        add_btn = Button(btn_frame,text="Add",width=10,bg="#00A1E4",fg="#FFFCF9",
        font=("Arial",10,"bold"),command=self.add_student)
        .grid(row=0,column=0,padx=5,pady=10)

        update_btn = Button(btn_frame,text="Update",width=10,bg="#00A1E4",fg="#FFFCF9",
        font=("Arial",10,"bold"),command=self.update).grid(row=0,column=1,padx=5,pady=10)

        delete_btn = Button(btn_frame,text="Delete",width=10,bg="#00A1E4",fg="#FFFCF9",
        font=("Arial",10,"bold"),command=self.delete).grid(row=0,column=2,padx=5,pady=10)

        clear_btn = Button(btn_frame,text="Clear",width=10,bg="#00A1E4",fg="#FFFCF9",
        font=("Arial",10,"bold"),command=self.clear_field)
        .grid(row=0,column=3,padx=5,pady=10)

        

        

        #Detail Frame
        Detail_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="#FFFCF9")
        Detail_Frame.place(x=550,y=95,width=800,height=600)

        

        lbl_search = Label(Detail_Frame,text="Search-",bg="#FFFCF9",fg="#0A090C",
        font=("Arial",18,"bold"))
        lbl_search.grid(row = 0,column=0,pady=10,padx=15,sticky="w")

        

        search_box = ttk.Combobox(Detail_Frame,width=12,textvariable=self.search_combo,
        font=("Arial",13,"bold"),state="readonly")

        search_box['values'] = ("Roll_No","SName","Contact_No")
        search_box.grid(row=0,column=1,pady=10,padx=10,ipady=4,sticky="w")

        

        

        txt_search = Entry(Detail_Frame,width=20,textvariable=self.search_field,
        font=("Arial",10,"bold"),bd=5,relief=GROOVE)
        txt_search.grid(row = 0,column=2,pady=10,padx=20,ipady=4,sticky="w")

        

        search_btn = Button(Detail_Frame,text="Search",bg="#00A1E4",fg="#FFFCF9",
        font=("Arial",10,"bold"),relief=GROOVE,width=10,pady=5,command=self.search_data)
        .grid(row=0,column=5,padx=10,pady=10)

        show_all_btn = Button(Detail_Frame,text="Show All",bg="#00A1E4",fg="#FFFCF9",
        font=("Arial",10,"bold"),relief=GROOVE,width=10,pady=5,command=self.show_data)
        .grid(row=0,column=6,padx=10,pady=10)

        logout_btn = Button(Detail_Frame,text="Log Out",bg="#00A1E4",fg="#FFFCF9",
        font=("Arial",10,"bold"),relief=GROOVE,width=10,pady=5,command=self.logout)
        .grid(row=0,column=7,padx=10,pady=10)

        

        #Table Frame

        Table_Frame = Frame(Detail_Frame,bg="#0A090C")
        Table_Frame.place(x=10,y=60,width=760,height=505)

        

        X_scroll = Scrollbar(Table_Frame,orient=HORIZONTAL)
        Y_scroll = Scrollbar(Table_Frame,orient=VERTICAL)
        self.Table = ttk.Treeview(Table_Frame,columns=("Roll-No","Name","Email-ID",
        "Gender","D.O.B","Address","Contact No"),xscrollcommand=X_scroll.set,
        yscrollcommand=Y_scroll.set)

        X_scroll.pack(side=BOTTOM,fill=X)
        Y_scroll.pack(side=RIGHT,fill=Y)
        X_scroll.config(command=self.Table.xview)
        Y_scroll.config(command=self.Table.yview)

        self.Table.heading("Roll-No",text="Roll-No")
        self.Table.heading("Name",text="Name")
        self.Table.heading("Email-ID",text="Email-ID")
        self.Table.heading("Gender",text="Gender")
        self.Table.heading("Contact No",text="Contact No")
        self.Table.heading("D.O.B",text="D.O.B")
        self.Table.heading("Address",text="Address")

        

        self.Table['show']="headings"
        self.Table.column("Roll-No",width=100)
        self.Table.column("Name",width=100)
        self.Table.column("Email-ID",width=100)
        self.Table.column("Gender",width=100)
        self.Table.column("Contact No",width=100)
        self.Table.column("D.O.B",width=100)
        self.Table.column("Address",width=150)

        

        self.Table.pack(fill=BOTH,expand=1)
        self.Table.bind('<ButtonRelease 1>',self.get_fields)
        self.txt_DOB.bind("<FocusIn>", self.foc_in)
        self.txt_DOB.bind("<FocusOut>", self.foc_out)


        self.put_placeholder()
        self.show_data()

        

    def add_student(self):

        if self.roll_no.get() == "" or self.name.get() == "" or self.email_id.get() == ""
        or self.gender.get()== "" or self.dob.get()== ""or self.contact.get() == ""
        or self.txt_address.get('1.0',END) == "":

            messagebox.showerror("Error","All Fields are Required")

        else:
            connect = pymysql.connect("localhost","root","","Student Management")
            curr = connect.cursor()

            

            curr.execute("INSERT INTO STUDENT VALUES(%s,%s,%s,%s,%s,%s,%s)",
            (self.roll_no.get(), self.name.get(), self.email_id.get(), self.gender.get(),
             self.dob.get(), self.txt_address.get('1.0',END), self.contact.get() ))

            connect.commit()

            self.show_data()
            self.clear_field()
            connect.close()

            messagebox.showinfo("Succes","Record Successfully Added")

        

    def show_data(self):

        connect = pymysql.connect("localhost","root","","Student Management")
        curr = connect.cursor()

        

        curr.execute("SELECT * from student")
        rows = curr.fetchall()

        if(len(rows)!=0):

            self.Table.delete(*self.Table.get_children())
            for row in rows:

                self.Table.insert('',END,values=row)

            connect.commit()
        connect.close()

        

    def clear_field(self):

        if self.roll_no.get() == "" or self.name.get() == "" or self.email_id.get() == ""
        or self.gender.get()== "" or self.dob.get()== ""or self.contact.get() == "" 
        or self.txt_address.get('1.0',END) == "":

            messagebox.showerror("Error","Fields Empty")

        else:

            self.roll_no.set("")
            self.name.set("")
            self.email_id.set("")
            self.gender.set("")
            self.contact.set("")
            self.dob.set("")
            self.txt_address.delete("1.0",END)

        

    def get_fields(self,event):

        cursor_row = self.Table.focus()
        content = self.Table.item(cursor_row)
        row = content['values']

        

        self.roll_no.set(row[0])
        self.name.set(row[1])
        self.email_id.set(row[2])
        self.gender.set(row[3])
        self.contact.set(row[6])
        self.dob.set(row[4])

        self.txt_address.delete("1.0",END)
        self.txt_address.insert(END,row[5])

        

    def update(self):

        if self.roll_no.get() == "" or self.name.get() == "" or self.email_id.get() == ""
        or self.gender.get()== "" or self.dob.get()== ""or self.contact.get() == "" 
        or self.txt_address.get('1.0',END) == "":

            messagebox.showerror("Error","Fields are Empty")

        else:

            connect = pymysql.connect("localhost","root","","Student Management")
            curr = connect.cursor()

            

            curr.execute("UPDATE STUDENT SET Sname=%s,email_id=%s,gender=%s,dob=%s,
             address=%s,contact_no=%s where roll_no=%s",(self.name.get(),

                                                         self.email_id.get(),

                                                         self.gender.get(),

                                                         self.dob.get(),

                                                         self.txt_address.get('1.0',END),

                                                         self.contact.get(),

                                                         self.roll_no.get()

                                                        ))

            connect.commit()

            self.show_data()
            self.clear_field()
            connect.close()

            messagebox.showinfo("Succes","Record Successfully Updated")

        

    def delete(self):

        if self.roll_no.get() == "" or self.name.get() == "" or self.email_id.get() == ""
        or self.gender.get()== "" or self.dob.get()== ""or self.contact.get() == "" 
        or self.txt_address.get('1.0',END) == "":

            messagebox.showerror("Error","Fields are Empty")

        else:

            connect = pymysql.connect("localhost","root","","Student Management")
            curr = connect.cursor()

            

            curr.execute("DELETE from STUDENT where roll_no=%s",(self.roll_no.get()))

                                                                             

            

            connect.commit()

            self.show_data()
            self.clear_field()
            connect.close()

            messagebox.showinfo("Succes","Record Successfully Deleted")

        

    def search_data(self):

        if self.search_combo.get() == "" or self.search_field.get() == "":

            messagebox.showerror("Error","Some Fields might be Empty")

        else:

            connect = pymysql.connect("localhost","root","","Student Management")
            curr = connect.cursor()

            

            curr.execute("SELECT * from student where "+str(self.search_combo.get())+
                         " LIKE '%"+str(self.search_field.get())+"%'")

            rows = curr.fetchall()

            if(len(rows)!=0):

                self.Table.delete(*self.Table.get_children())

                for row in rows:

                    self.Table.insert('',END,values=row)

                connect.commit()
            connect.close()

            

    def put_placeholder(self):

        self.txt_DOB.insert(0,"DD-MM-YYYY")

        self.txt_DOB['fg'] = "grey"


    def foc_in(self,event):

        if self.txt_DOB['fg'] == "grey":

            self.txt_DOB.delete('0', 'end')
            self['fg'] = "grey"


    def foc_out(self, event):

        if not self.get():
            self.txt_DOB.put_placeholder()

            

    def logout(self):

        self.root.destroy() 

        st_root = Tk()
        st = Login(st_root)
        st_root.mainloop()        

        

    def employee_btn(self):

        self.root.destroy() 

        st_root = Tk()
        st = Employee(st_root)
        st_root.mainloop()

        

    def dept_btn(self):

        self.root.destroy()

        st_root = Tk()
        st = Department(st_root)
        st_root.mainloop()

        

    def pass_btn(self):

        self.root.destroy() 

        st_root = Tk()
        st = Password(st_root)
        st_root.mainloop()

        

class Login:

    def __init__(self,root):

        self.root = root
        self.root.title("Login")
        self.root.geometry("350x350+450+200")
        self.root.resizable(0,0)

        

        self.username = StringVar()
        self.password = StringVar()

        

        title = Label(self.root,text="Login",bd = 5,relief=GROOVE,
        font=("Arial",30,"bold"),bg="#FFFCF9",fg="#0A090C")

        title.pack(side=TOP,fill=X)

        

        Main_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="#F0EDEE")
        Main_Frame.place(x=0,y=60,width=350,height=290)

        

        lbl_username = Label(Main_Frame,text="Username :-",bg="#F0EDEE",fg="#0A090C",
        font=("Arial",10,"bold"))

        lbl_username.grid(row = 1,column=0,pady=45,padx=30,sticky="w")

    

        txt_username = Entry(Main_Frame,textvariable=self.username,width = 12,
        font=("Arial",15,"bold"),bd=5,relief=GROOVE)

        txt_username.grid(row = 1,column=1,pady=45,padx=5,sticky="w")

        

        lbl_password = Label(Main_Frame,text="Password :-",bg="#F0EDEE",fg="#0A090C"
        ,font=("Arial",10,"bold"))

        lbl_password.grid(row = 2,column=0,pady=5,padx=30,sticky="w")

    

        txt_password = Entry(Main_Frame,show="*",textvariable=self.password,width = 12,
        font=("Arial",15,"bold"),bd=5,relief=GROOVE)

        txt_password.grid(row = 2,column=1,pady=5,padx=5,sticky="w")

        

        btn_frame = Frame(Main_Frame,bg="#F0EDEE")

        btn_frame.place(x=100,y=200,width=170)

        

        login_btn = Button(btn_frame,text="Login",width=20,relief=GROOVE,bg="#00A1E4",
        font=("Arial",10,"bold"),command=self.validate_user)
        .grid(row=0,column=0,padx=0,pady=10)

        

    def validate_user(self):

        if self.username.get() == "" or self.password.get() == "":

            messagebox.showerror("Error","Fields Missing")

        else:

            connect = pymysql.connect("localhost","root","","Student Management")
            curr = connect.cursor()

            

            curr.execute("SELECT * from admin")
            rows = curr.fetchall()


            for row in rows:

                if row[1] == self.username.get() and row[2] == self.password.get():

                    self.root.destroy() 
                    st_root = Tk()
                    st = Student(st_root)
                    st_root.mainloop()  

                else:

                    messagebox.showerror("Error","Please Make Sure That the Details are
                                          Correct")

              

             

root = Tk()
st = Login(root)
root.mainloop()
