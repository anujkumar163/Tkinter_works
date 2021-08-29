from tkinter import *
import pymysql
import tkinter.messagebox as m
#from oparator import itemgetter

mainwindow = Tk()
mainwindow.title("Login & Register")
mainwindow.geometry("400x400")

bigText = Label(text="Login and redister", font="Vardana 20 bold")
bigText.place(x=30,y=30)

def Register():
    print("register")
    registerwindow = Tk()
    registerwindow.title("Register")
    registerwindow.geometry("400x400")

    
    mydb = pymysql.connect(host="localhost",port=3306,user="root",passwd="",database="anuj")
    mycursor = mydb.cursor()

    
    bigText = Label(text="redister", font="Vardana 20 bold")
    bigText.place(x=100,y=30)

    name = Label(registerwindow, text="Name")
    name.place(x=90, y=100)
    email = Label(registerwindow, text="email")
    email.place(x=90, y=140)
    password = Label(registerwindow, text="password")
    password.place(x=90, y=180)
    repassword = Label(registerwindow, text="repassword")
    repassword.place(x=90, y=220)
    l3=Label(login_window,font="times 20")
    l3.place(x=110,y=250)

    e1=Entry(registerwindow)
    e1.place(x=180,y=100)
    e2=Entry(registerwindow)
    e2.place(x=180,y=140)
    e3=Entry(registerwindow,show="*")
    e3.place(x=180,y=180)
    e4=Entry(registerwindow,show="*")
    e4.place(x=180,y=220)


    def clearEntryBox():
        e1.delete(first=0,last=100)
        e2.delete(first=0,last=100)
        e3.delete(first=0,last=100)
        e4.delete(first=0,last=100)

    def error():
        m.showerror(title="error",message="password not same")

    def insert():
        insert=("insert into register(name,email,password,repassword) values(%s,%s,%s,%s)")
        values=[e1.get(),e2.get(),e3.get(),e4.get()]
        mycursor.execute(insert,values)
        if e3.get()==e4.get():
            mydb.commit()
            clearEntryBox()
            m.showinfo(title="Done",message="Account created")
        else:
            error()
            
    register=Button(registerwindow, text="Register",fg="green",command=insert )
    register.place(x=175,y=350)
    btnExit=Button(registerwindow,text="Exit",bg="red",command=registerwindow.destroy)
    btnExit.place(x=350,y=350)

    #mainwindow.destroy()
    #registerwindow.mainloop()
    #mainwindow.destroy()


    
    

    

def Login():
    print("hello")
    loginwindow = Tk()
    loginwindow.title("Login")
    loginwindow.geometry("400x400")

    
    mydb = pymysql.connect(host="localhost",port=3306,user="root",passwd="",database="anuj")
    mycursor = mydb.cursor()

    mydb1 = pymysql.connect(host="localhost",port=3306,user="root",passwd="",database="anuj")
    mycursor1 = mydb1.cursor()

    
    bigText = Label(text="Login", font="Vardana 20 bold")
    bigText.place(x=140,y=30)

    
    email = Label(loginwindow, text="email")
    email.place(x=100, y=150)
    password = Label(loginwindow, text="password")
    password.place(x=100, y=180)
   

    e1=Entry(loginwindow)
    e1.place(x=160,y=150)
    e2=Entry(loginwindow,show="*")
    e2.place(x=160,y=180)

    def check():
        
        
        mycursor.execute("SELECT * FROM register WHERE email=? AND password=?",(e1.get(),e2.get()))
        row=mycursor.fetchall()
        print(row)
        if row!=[]:
            email=row[0][1]
            password=row[0][2]
            l3.config(text="email found with name: "+email)
            l3.config(text="password found:")
        else:
            l3.config(text="not matched ")


        sqlcommand1="select email from register"
        sqlcommand2="select password from register"

        mycursor.execute(sqlcommand1)
        mycursor1.execute(sqlcommand2)
        email=e1.get()
        password=e2.get()
        e=[]
        p=[]
        
        for i in mycursor:
            e.append(i)
        for j in mycursor1:
            p.append(j)
        
        a = set(e)  
        b = set(p)  
  
        if a == email and b == password:
            m.showinfo(title="Deo",message="Login is Done")
            print("The list1 and list2 are equal")
        
        else:
            m.showinfo(title="error",message="some thing went wrong")
            print("The list1 and list2 are not equal")      
            

    login=Button(loginwindow, text="Register",fg="green",command=check )
    login.place(x=160,y=260)
    btnExit=Button(loginwindow,text="Exit",bg="red",command=loginwindow.destroy)
    btnExit.place(x=350,y=350)
    #mainwindow.destroy()
    loginwindow.mainloop()

    











    

goToLogin=Button(mainwindow, text="login",fg="green",font="Vardana 10 bold",command=Login)
goToLogin.place(x=120, y=200)

goToRegister=Button(mainwindow, text="register",fg="green",font="Vardana 10 bold",command=Register)
goToRegister.place(x=180, y=200)

btnExit=Button(mainwindow, text="Exit",fg="green",font="Vardana 10 bold",command=mainwindow.destroy)
btnExit.place(x=350, y=350)

mainwindow.mainloop()    
