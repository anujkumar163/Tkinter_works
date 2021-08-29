def searchstudent():
        def serch():
            id=idval.get()
            name=nameval.get()
            mobile=mobileval.get()
            email=emailval.get()
            address=addressval.get()
            gender=genderval.get()
            dob=dobval.get()
            e = datetime.datetime.now()
            a=e.strftime("%d/%m/%Y")
            mydb = pymysql.connect(host="localhost",port=3306,user="root",passwd="",database="studentmanagementsystem")
            if(id!=''):
                    strr='select * from studentdata where id=%s'
                    mycursor.execute(strr,(id))
                    datas=mycursor.fetchall()
                    studenttable.delete(* studenttable.get_children())
                    for i in datas:
                            vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                            studenttable.insert('',END,values=vv )
                            
            elif(name!=''):
                    strr='select * from studentdata where NAME=%s'
                    mycursor.execute(strr,(name))
                    datas=mycursor.fetchall()
                    studenttable.delete(* studenttable.get_children())
                    for i in datas:
                            vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                            studenttable.insert('',END,values=vv )

            elif(mobile!=''):
                    strr='select * from studentdata where mobile=%s'
                    mycursor.execute(strr,(mobile))
                    datas=mycursor.fetchall()
                    studenttable.delete(* studenttable.get_children())
                    for i in datas:
                            vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                            studenttable.insert('',END,values=vv )
            elif(email!=''):
                    strr='select * from studentdata where email=%s'
                    mycursor.execute(strr,(email))
                    datas=mycursor.fetchall()
                    studenttable.delete(* studenttable.get_children())
                    for i in datas:
                            vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                            studenttable.insert('',END,values=vv )
            elif(address!=''):
                    strr='select * from studentdata where address=%s'
                    mycursor.execute(strr,(address))
                    datas=mycursor.fetchall()
                    studenttable.delete(* studenttable.get_children())
                    for i in datas:
                            vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                            studenttable.insert('',END,values=vv )
            elif(gender!=''):
                    strr='select * from studentdata where gender=%s'
                    mycursor.execute(strr,(gender))
                    datas=mycursor.fetchall()
                    studenttable.delete(* studenttable.get_children())
                    for i in datas:
                            vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                            studenttable.insert('',END,values=vv )
            elif(dob!=''):
                    strr='select * from studentdata where dob=%s'
                    mycursor.execute(strr,(dob))
                    datas=mycursor.fetchall()
                    studenttable.delete(* studenttable.get_children())
                    for i in datas:
                            vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                            studenttable.insert('',END,values=vv )
            elif(a!=''):
                    strr='select * from studentdata where date=%s'
                    mycursor.execute(strr,(a))
                    datas=mycursor.fetchall()
                    #mydb.commit()
                    studenttable.delete(* studenttable.get_children())
                    for i in datas:
                            vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                            studenttable.insert('',END,values=vv )
                            
        searchroot=Toplevel(master=DataEntryFrame)
        searchroot.grab_set()
        searchroot.geometry('470x540+220+200')
        searchroot.title("studentManagement System")
        searchroot.config(bg='blue')
        searchroot.resizable(False,False)
        #-----add student label
        idlabel=Label(searchroot,text='Enter id:',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
        idlabel.place(x=10,y=10)

        namelabel=Label(searchroot,text='Enter Name:',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
        namelabel.place(x=10,y=70)

        mobilelabel=Label(searchroot,text='Enter Mobile:',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
        mobilelabel.place(x=10,y=130)

        emaillabel=Label(searchroot,text='Enter Email:',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
        emaillabel.place(x=10,y=190)

        addresslabel=Label(searchroot,text='Enter Address:',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
        addresslabel.place(x=10,y=250)

        genderlabel=Label(searchroot,text='Enter Gender:',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
        genderlabel.place(x=10,y=310)

        doblabel=Label(searchroot,text='Enter D.O.B:',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
        doblabel.place(x=10,y=370)

        datelabel=Label(searchroot,text='Enter Date:',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
        datelabel.place(x=10,y=430)
        #-----add student entry
        idval = StringVar()
        nameval = StringVar()
        mobileval = StringVar()
        emailval = StringVar()
        addressval = StringVar()
        genderval = StringVar()
        dobval = StringVar()
        dateval = StringVar()
        identry = Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=idval)
        identry.place(x=250,y=10)
    
        nameentry = Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=nameval)
        nameentry.place(x=250,y=70)
        mobileentry = Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=mobileval)
        mobileentry.place(x=250,y=130)
        emailentry = Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=emailval)
        emailentry.place(x=250,y=190)
        addressentry = Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=addressval)
        addressentry.place(x=250,y=250)
        genderentry = Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=genderval)
        genderentry.place(x=250,y=310)
        dobentry = Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=dobval)
        dobentry.place(x=250,y=370)
        dateentry = Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=dateval)
        dateentry.place(x=250,y=430)
        ##----addbutton
        serchbtn=Button(searchroot,text="serch",font=('roman',15,'bold'),width=20,bd=5,activebackground='blue',activeforeground='white',bg='red',command=serch)
        serchbtn.place(x=150,y=480)
        
        searchroot.mainloop()


def addstudent():
    def submitadd():
        print('hello')
        id=idval.get()
        name=nameval.get()
        mobile=mobileval.get()
        email=emailval.get()
        address=addressval.get()
        gender=genderval.get()
        dob=dobval.get()
        #addedtime=time.strftime("%H:%M:%S")
        #addeddate=time.strftime("%d/%m/%Y")
        e = datetime.datetime.now()
        a=e.strftime("%d/%m/%Y")
        b=e.strftime("%I:%M:%S %p")
        try:
                strr='insert into studentdata values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                mycursor.execute(strr,(id,name,mobile,email,address,gender,dob,a,b))
                mydb.commit()
                res=messagebox.askyesnocancel('Notification','id{} Name{} Added sucessfullyand want to cleane the form?',format(id,name),parent=addroot)
                if(res==True):
                        idval.set("")
                        nameval.set("")
                        mobileval.set("")
                        emailval.set("")
                        addressval.set("")
                        genderval.set("")
                        dobval.set("")
                        
                        
        except:
                res=messagebox.showerror('Notification',' data entered',parent=addroot)
        strr='select * from studentdata'
        mycursor.execute(strr)
        datas=mycursor.fetchall()
        studenttable.delete(* studenttable.get_children())
        for i in datas:
                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                studenttable.insert('',END,values=vv )      
        
        
        
        
        
    addroot=Toplevel(master=DataEntryFrame)
    addroot.grab_set()
    addroot.geometry('470x470+220+200')
    addroot.title("studentManagement System")
    addroot.config(bg='blue')
    addroot.resizable(False,False)
    #-----add student label
    idlabel=Label(addroot,text='Enter id:',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    idlabel.place(x=10,y=10)

    namelabel=Label(addroot,text='Enter Name:',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    namelabel.place(x=10,y=70)

    mobilelabel=Label(addroot,text='Enter Mobile:',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    mobilelabel.place(x=10,y=130)

    emaillabel=Label(addroot,text='Enter Email:',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    emaillabel.place(x=10,y=190)

    addresslabel=Label(addroot,text='Enter Address:',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    addresslabel.place(x=10,y=250)

    genderlabel=Label(addroot,text='Enter Gender:',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    genderlabel.place(x=10,y=310)

    doblabel=Label(addroot,text='Enter D.O.B:',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    doblabel.place(x=10,y=370)
#-----add student entry
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()
    identry = Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=idval)
    identry.place(x=250,y=10)
    
    nameentry = Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=nameval)
    nameentry.place(x=250,y=70)
    mobileentry = Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=mobileval)
    mobileentry.place(x=250,y=130)
    emailentry = Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=emailval)
    emailentry.place(x=250,y=190)
    addressentry = Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=addressval)
    addressentry.place(x=250,y=250)
    genderentry = Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=genderval)
    genderentry.place(x=250,y=310)
    dobentry = Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=dobval)
    dobentry.place(x=250,y=370)
    ##----addbutton
    submitbtn=Button(addroot,text="submit",font=('roman',15,'bold'),width=20,bd=5,activebackground='blue',activeforeground='white',bg='red',command=submitadd)
    submitbtn.place(x=150,y=420)
    
    addroot.mainloop()

def deletestudent():
    cc=studenttable.focus()
    content=studenttable.item(cc)
    pp=content['values'][0]
    strr='delete from studentdata where id=%s'
    mycursor.execute(strr,(pp))
    mydb.commit()
    messagebox.showinfo('Notifications','Id{} deleted sucessfully'.format(pp))
    strr='select * from studentdata'
    mycursor.execute(strr)
    datas=mycursor.fetchall()
    studenttable.delete(* studenttable.get_children())
    for i in datas:
            vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
            studenttable.insert('',END,values=vv )

    
def updatestudent():
    def update():
        print('hello')
        id=idval.get()
        name=nameval.get()
        mobile=mobileval.get()
        email=emailval.get()
        address=addressval.get()
        gender=genderval.get()
        dob=dobval.get()
        aa=a.get()
        bb=b.get()
        #addedtime=time.strftime("%H:%M:%S")
        #addeddate=time.strftime("%d/%m/%Y")
        #e = datetime.datetime.now()
        #a=e.strftime("%d/%m/%Y")
        #b=e.strftime("%I:%M:%S %p")

        strr='update studentdata set NAME=%s,mobile=%s,email=%s,address=%s,gender=%s,dob=%s,DATE=%s,TIME=%s where id=%s'
        mycursor.execute(strr,(name,mobile,email,address,gender,dob,aa,bb,id))
        mydb.commit()
        messagebox.showinfo('Notifications','Id{} modified  deleted sucessfully'.format(id),parent=updateroot)
        strr='select * from studentdata'
        mycursor.execute(strr)
        datas=mycursor.fetchall()
        studenttable.delete(* studenttable.get_children())
        for i in datas:
                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                studenttable.insert('',END,values=vv )


    updateroot=Toplevel(master=DataEntryFrame)
    updateroot.grab_set()
    updateroot.geometry('470x650+220+160')
    updateroot.title("studentManagement System")
    updateroot.config(bg='blue')
    updateroot.resizable(False,False)
    #-----add student label
    idlabel=Label(updateroot,text='Enter id:',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    idlabel.place(x=10,y=10)

    namelabel=Label(updateroot,text='Enter Name:',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    namelabel.place(x=10,y=70)

    mobilelabel=Label(updateroot,text='Enter Mobile:',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    mobilelabel.place(x=10,y=130)

    emaillabel=Label(updateroot,text='Enter Email:',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    emaillabel.place(x=10,y=190)

    addresslabel=Label(updateroot,text='Enter Address:',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    addresslabel.place(x=10,y=250)

    genderlabel=Label(updateroot,text='Enter Gender:',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    genderlabel.place(x=10,y=310)

    doblabel=Label(updateroot,text='Enter D.O.B:',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    doblabel.place(x=10,y=370)

    datelabel=Label(updateroot,text='Enter Date:',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    datelabel.place(x=10,y=430)
    
    timelabel=Label(updateroot,text='Enter Date:',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    timelabel.place(x=10,y=490)
    #-----add student entry
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()
    a = StringVar()
    b = StringVar()
    #e = datetime.datetime.now()
    #a=e.strftime("%d/%m/%Y")
    #b=e.strftime("%I:%M:%S %p")
    
    identry = Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=idval)
    identry.place(x=250,y=10)
    
    nameentry = Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=nameval)
    nameentry.place(x=250,y=70)
    mobileentry = Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=mobileval)
    mobileentry.place(x=250,y=130)
    emailentry = Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=emailval)
    emailentry.place(x=250,y=190)
    addressentry = Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=addressval)
    addressentry.place(x=250,y=250)
    genderentry = Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=genderval)
    genderentry.place(x=250,y=310)
    dobentry = Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=dobval)
    dobentry.place(x=250,y=370)
    dateentry = Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=a)
    dateentry.place(x=250,y=430)
    timeentry = Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=b)
    timeentry.place(x=250,y=490)
    ##----addbutton
    serchbtn=Button(updateroot,text="serch",font=('roman',15,'bold'),width=20,bd=5,activebackground='blue',activeforeground='white',bg='red',command=update)
    serchbtn.place(x=150,y=550)
    cc=studenttable.focus()
    content=studenttable.item(cc)
    pp=content['values']
    if(len(pp) != 0):
            idval.set(pp[0])
            nameval.set(pp[1])
            mobileval.set(pp[2])
            emailval.set(pp[3])
            addressval.set(pp[4])
            genderval.set(pp[5])
            dobval.set(pp[6])
            a.set(pp[7])
            b.set(pp[8])
    
        
    updateroot.mainloop()


    
    
    print('student update')
def showstudent():
    print('student show')
    strr='select * from studentdata'
    mycursor.execute(strr)
    datas=mycursor.fetchall()
    studenttable.delete(* studenttable.get_children())
    for i in datas:
            vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
            studenttable.insert('',END,values=vv )
    
def exportstudent():
    print('student export')
    ff=filedialog.asksaveasfilename()
    gg=studenttable.get_children()
    id,name,mobile,email,address,gender,dob,date,time=[],[],[],[],[],[],[],[],[]
    for i in gg:
            content=studenttable.item(i)
            pp=content['values']
            id.append(pp[0]),name.append(pp[1]),mobile.append(pp[2]),email.append(pp[3]),address.append(pp[4]),gender.append(pp[5]),dob.append(pp[6]),date.append(pp[7]),time.append(pp[8]) 
    dd=['Id','Name','Mobile','Email','Address','Gender','D.O.B','Date','Time']
    df=pandas.DataFrame(list(zip(id,name,mobile,email,address,gender,dob,date,time)),columns=dd)
    paths=r'{}.csv'.format(ff)
    df.to_csv(paths,index=False)
    messagebox.showinfo('Notifications','student data is save {}'.format(paths))
    
            
def exitstudent():
    res=messagebox.askyesnocancel('Notification','Do you want to exit?')
    if(res==True):
        root.destroy()
        


    
def connectdb():
    def submitdb():
        global mydb,mycursor
        host = hostval.get()
        user = userval.get()
        passwordd = passwordval.get()
        try:
            #mydb = pymysql.connect(host=host,user=user,password="")//uncomment this in your pc
            #mycursor = mydb.cursor()//uncomment this in your pc
            mydb = pymysql.connect(host="localhost",port=3306,user="root",passwd="",database="8pm_sample")#autoconnect for me,anujpc not for you,comment it.
            mycursor = mydb.cursor()#autoconnect for me,anujpc not for you,comment it
            messagebox.showerror('Notifications','connected')
        except:
            messagebox.showerror('Notifications','Data is incorrect')
            return
        try:
                strr='create database studentmanagementsystem'
                mycursor.execute(strr)
                strr='use studentmanagementsystem'
                mycursor.execute(strr)
                strr='create table studentdata(id INT(10),NAME VARCHAR(50), mobile VARCHAR(50),email VARCHAR(50),address VARCHAR(50),gender VARCHAR(50),dob VARCHAR(50),DATE VARCHAR(50),TIME VARCHAR(50))'
                mycursor.execute(strr)
                messagebox.showinfo('Notification','Now database is created and connected in your pc babu',parent=dbroot)
                
                
        except:
                pass
                strr='use studentmanagementsystem'
                mycursor.execute(strr)
                messagebox.showinfo('Notification','Now you are connected',parent=dbroot)
                '''strr='alter table studentdata modify column id int not null'
                mycursor.execute(strr)
                strr='alter table studentdata modify column id int primary key'
                mycursor.execute(strr)'''
                
                
      #-----check data connection  37.01
    dbroot = Toplevel()
    dbroot.grab_set()
    dbroot.geometry('470x250+800+230')
    #dbroot.iconbitmap('Camera.ico')
    dbroot.resizable(False,False)
    dbroot.config(bg='pink')
    #######dblabel
    hostlabel =Label(dbroot,text='Enter Host:',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    hostlabel.place(x=10,y=10)

    userlabel =Label(dbroot,text='Enter User:',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    userlabel.place(x=10,y=70)

    passwordlabel =Label(dbroot,text='Password:',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    passwordlabel.place(x=10,y=130)

    hostval = StringVar()
    userval = StringVar()
    passwordval = StringVar()


    
    
    hostentry = Entry(dbroot,font=('roman',15,'bold'),bd=5,textvariable=hostval)
    hostentry.place(x=250,y=10)

    userentry = Entry(dbroot,font=('roman',15,'bold'),bd=5,textvariable=userval)
    userentry.place(x=250,y=70)

    passwordentry = Entry(dbroot,font=('roman',15,'bold'),bd=5,textvariable=passwordval)
    passwordentry.place(x=250,y=130)

    submitbutton= Button(dbroot,text="submit",font=('roman',15,'bold'),bg='red',bd=5 ,width=20,activebackground='blue',activeforeground='white',command=submitdb)
    submitbutton.place(x=150,y=190)
    
    dbroot.mainloop()

def tick():
    e = datetime.datetime.now()
    a=e.strftime("%d/%m/%Y")
    b=e.strftime("%I:%M:%S %p")
    clock.config(text='Date:'+a+"\n"+"Time:"+b)
    clock.after(200,tick)
import random    
color=['red','green','blue','pink']

def introLabelColorTick():
    fg=random.choice(color)
    sliderLabel.config(fg=fg)
    sliderLabel.after(20,introLabelColorTick)
    
def introLabelTick():
    global count,text
    if(count>=len(ss)):
        count = 0
        text=''
        sliderLabel.config(text=text)
    else:
        text = text+ss[count]
        sliderLabel.config(text=text)
        count += 1
    sliderLabel.after(200,introLabelTick)    
        
##################################

import random
import pymysql
#mydb = pymysql.connect(host="localhost",port=3306,user="root",passwd="",database="StudentManagementSystem")
#mycursor = mydb.cursor()
from tkinter import Toplevel,messagebox,filedialog
from tkinter import *
import pandas
#####################



###############

from tkinter.ttk import Treeview
from tkinter import ttk
import datetime 
from datetime import date
root = Tk()
root.title("student Management system")
root.config(bg="green")
root.geometry('1174x700+100+50')
root.resizable(False,False)





################################data entry frame

DataEntryFrame = Frame(root,bg="red",relief=GROOVE,borderwidth=5)
DataEntryFrame.place(x=10,y=80,width=500,height=600)

frontlabel=Label(DataEntryFrame,text='----Welcom bhau---',width=30,font=('arial',22,'italic bold'),bg='gold')
frontlabel.pack(side=TOP,expand=True)
addbtn=Button(DataEntryFrame,text='1. Add Student',width=25,font=('chiller',20,'bold'),bd=6,activebackground='gold',relief=RIDGE,activeforeground='white',command=addstudent)
addbtn.pack(side=TOP,expand=True)

serchbtn=Button(DataEntryFrame,text='1. serch Student',width=25,font=('chiller',20,'bold'),bd=6,activebackground='gold',relief=RIDGE,activeforeground='white',command=searchstudent)
serchbtn.pack(side=TOP,expand=True)

deletebtn=Button(DataEntryFrame,text='1. Delete Student',width=25,font=('chiller',20,'bold'),bd=6,activebackground='gold',relief=RIDGE,activeforeground='white',command=deletestudent)
deletebtn.pack(side=TOP,expand=True)

updatebtn=Button(DataEntryFrame,text='1. Update Student',width=25,font=('chiller',20,'bold'),bd=6,activebackground='gold',relief=RIDGE,activeforeground='white',command=updatestudent)
updatebtn.pack(side=TOP,expand=True)

showallbtn=Button(DataEntryFrame,text='1. Show All',width=25,font=('chiller',20,'bold'),bd=6,activebackground='gold',relief=RIDGE,activeforeground='white',command=showstudent)
showallbtn.pack(side=TOP,expand=True)

exportbtn=Button(DataEntryFrame,text='1. Export Data',width=25,font=('chiller',20,'bold'),bd=6,activebackground='gold',relief=RIDGE,activeforeground='white',command=exportstudent)
exportbtn.pack(side=TOP,expand=True)

exitbtn=Button(DataEntryFrame,text='1. Exit',width=25,font=('chiller',20,'bold'),bd=6,activebackground='gold',relief=RIDGE,activeforeground='white',command=exitstudent)
exitbtn.pack(side=TOP,expand=True)

################### show data frame

ShowDataFrame = Frame(root,bg="red",relief=GROOVE,borderwidth=5)
ShowDataFrame.place(x=550,y=80,width=620,height=600)
#---------showdataframe

style = ttk.Style()
style.configure('Treeview.Heading',font=('chiller',20,'bold'),foreground='blue')
style.configure('Treeview',font=('times',15,'bold'),foreground='black',background='cyan')
scroll_x=Scrollbar(ShowDataFrame,orient=HORIZONTAL)
scroll_y=Scrollbar(ShowDataFrame,orient=VERTICAL)
studenttable = Treeview(ShowDataFrame,yscrollcommand=scroll_y.set,xscrollcommand=scroll_x.set,columns=('Id','Name','Mobile No','Email','Address','Gender','D.O.B','Added Date','Added Time'))
scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_x.config(command=studenttable.xview)
scroll_y.config(command=studenttable.yview)
studenttable.heading('Id',text='Id')
studenttable.heading('Name',text='Name')
studenttable.heading('Mobile No',text='Mobile No')
studenttable.heading('Email',text='Email')
studenttable.heading('Address',text='Address')
studenttable.heading('Gender',text='Gender')
studenttable.heading('D.O.B',text='D.O.B')
studenttable.heading('Added Date',text='Added Date')
studenttable.heading('Added Time',text='Added Time')
studenttable['show']='headings'
studenttable.pack(fill=BOTH,expand=1)



####################################slider
ss="welcom to student Management system"
count=0
text=''
sliderLabel = Label(root,text=ss,font=('chiller',30,'italic bold'),relief=RIDGE,borderwidth=5,width=35,bg='cyan')
sliderLabel.place(x=260, y=0)
introLabelTick()
introLabelColorTick()
##################################clock
clock= Label(root,font=('times',14,'bold'),relief=RIDGE,borderwidth=4,width=15,bg='lawn green')
clock.place(x=0,y=0)
tick()
######################databasebutton
connectbutton=Button(root,activebackground='blue',activeforeground='white',font=('chiller',19,'italic bold'),relief=RIDGE,borderwidth=5,bg='cyan',text="connect to database",width=23,command=connectdb)
connectbutton.place(x=930,y=0)


root.mainloop()
