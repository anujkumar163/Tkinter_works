from tkinter import *
import sqlite3
from tkinter import messagebox as mb
import json


window=Tk()
window.geometry("500x500")

def login():
	def login_database():
		conn=sqlite3.connect("1.db")
		cur=conn.cursor()
		cur.execute("SELECT * FROM test WHERE email=? AND password=?",(e1.get(),e2.get()))
		row=cur.fetchall()
		conn.close()
		print(row)
		if row!=[]:
			user_name=row[0][1]
			l3.config(text="user name found with name: "+user_name )
                        
		else:
			l3.config(text="user not found ")



	window.destroy()
	login_window=Tk()
	login_window.geometry("500x500")
	
	l1=Label(login_window,text="email",font="times 20")
	l1.grid(row=1,column=1)
	l2=Label(login_window,text="password",font="times 20")
	l2.grid(row=2,column=1)
	l3=Label(login_window,font="times 20")
	l3.grid(row=5,column=2)

	email_text=StringVar()
	e1=Entry(login_window,textvariable=email_text)
	e1.grid(row=1,column=2)
	password_text=StringVar()
	e2=Entry(login_window,textvariable=password_text)
	e2.grid(row=2,column=2)


	b1=Button(login_window,text="login",width=20,command=login_database)
	b1.grid(row=4,column=2)
	b2=Button(login_window,text="quiz",width=20,command=login_window.destroy)
	b2.grid(row=8,column=2)

	login_window.mainloop()
	




def signup():


	def signup_database():
		conn=sqlite3.connect("1.db")
		cur=conn.cursor()
		cur.execute("CREATE TABLE IF NOT EXISTS test(id INTEGER PRIMARY KEY,name text,email text, password text)")
		cur.execute("INSERT INTO test Values(Null,?,?,?)",(e1.get(),e2.get(),e3.get()))
		l4=Label(signup_window,text="account created",font="times 15")
		l4.grid(row=6,column=2)
		conn.commit()
		conn.close()





	#window.destroy()
	signup_window=Tk()
	signup_window.geometry("500x500")
	l1=Label(signup_window,text="user name",font="times 20")
	l1.grid(row=1,column=1)
	l2=Label(signup_window,text="user email",font="times 20")
	l2.grid(row=2,column=1)
	l3=Label(signup_window,text="user password",font="times 20")
	l3.grid(row=3,column=1)


	name_text=StringVar()
	e1=Entry(signup_window,textvariable=name_text)
	e1.grid(row=1,column=2)
	email_text=StringVar()
	e2=Entry(signup_window,textvariable=email_text)
	e2.grid(row=2,column=2)
	password_text=StringVar()
	e3=Entry(signup_window,textvariable=password_text)
	e3.grid(row=3,column=2)

	b1=Button(signup_window,text="Registered",width=20,command=signup_database)
	b1.grid(row=4,column=2)
	b2=Button(signup_window,text="login",width=20,command=login)
	b2.grid(row=5,column=2)
	b3=Button(signup_window,text="exit",width=20,command=signup_window.destroy)
	b3.grid(row=8,column=2)
import pymysql
mydb = pymysql.connect(host="localhost",port=3306,user="root",passwd="",database="anuj")
mycursor = mydb.cursor()	

def func():
    mycursor.execute("select * from tk")
    i = 0
    for student in mycursor:
        for j in range(len(student)):
            e=Entry(f,width=30,fg='blue',bg='pink')
            e.grid(row=i,column=j)
            e.insert(END, student[j])
        i=i+1



l1=Label(window,text="what do you want to do",font="times 20")
l1.grid(row=1,column=2,columnspan=2)

b1=Button(window,text="login",width=20,command=login)
b1.grid(row=2,column=2)

b2=Button(window,text="signup",width=20,command=signup)
b2.grid(row=2,column=3)
window.mainloop()

        
class Quize:
    def __init__(self):
        self.q_no=0
        self.display_title()
        self.display_question()
        self.opt_selected=IntVar()
        self.opts=self.radio_buttons()
        self.display_options()
        self.buttons()
        self.data_size=len(question)
        self.correct=0

    def display_result(self):
        wrong_count = self.data_size - self.correct
        correct = f"Correct: {self.correct}"
        wrong = f"Wrong: {wrong_count}"
        score = int(self.correct/self.data_size*100)
        result = f"Score: {score}%"
        mb.showinfo("Result", f"{result}\n{correct}\n{wrong}")
        
    def check_ans(self, q_no):
        if self.opt_selected.get() == answer[q_no]:
            return True

    def next_btn(self):
        if self.check_ans(self.q_no):
            self.correct += 1
        self.q_no += 1
        if self.q_no==self.data_size:
            self.display_result()
            gui.destroy()
        else:
            self.display_question()
            self.display_options()
        
    def buttons(self):
        next_button=Button(gui, text="Next",command=self.next_btn,width=10,bg="blue",fg="white",font=("ariel",16,"bold"))
        next_button.place(x=350,y=380)

        quit_button=Button(gui,text="show student detail",command=gui.destroy,width=20,bg="black",fg="white",font=("arriel",16,"bold"))
        quit_button.place(x=35,y=50)
    
    def display_options(self):
        val=0
        self.opt_selected.set(0)
        for option in options[self.q_no]:
            self.opts[val]['text']=option
            val+=1

    def display_question(self):
        q_no=Label(gui,text=question[self.q_no], width=60, font=('ariel',16,'bold'),anchor='w')
        q_no.place(x=70, y=100)

    def display_title(self):
        title=Label(gui,text="made by Anuj",width=50, bg="green",fg="white", font=("ariel",20,"bold"))
        title.place(x=0, y=2)
    


    def radio_buttons(self):
        q_list=[]
        y_pos=150
        while len(q_list)< 4:
            radio_btn=Radiobutton(gui,text=" ",variable=self.opt_selected, value=len(q_list)+1, font=("ariel",14))
            q_list.append(radio_btn)
            radio_btn.place(x=100,y=y_pos)
            y_pos += 40
        return q_list

gui=Tk()
gui.geometry("800x450")
gui.title("Quize")
with open('data.json') as f:
        data = json.load(f)

question = (data['question'])
options = (data['options'])
answer = (data['answer'])
quiz = Quize()
gui.mainloop()

from tkinter import *
import tksheet
import pymysql
mydb = pymysql.connect(host="localhost",port=3306,user="root",passwd="",database="anuj")
mycursor = mydb.cursor()
r = Tk()
r.geometry('600x500')

def save():
    id = a.get()
    nm = b.get()
    sal = c.get()
    mycursor.execute("insert into tk values ({},'{}',{})".format(id,nm,sal))
    mydb.commit()
    
    l4 = Label(r, text="Data Inserted!")
    l4.pack()
    
def query():
    mycursor.execute("select * from tk")
    rows = mycursor.fetchall()
    for i in rows:
        print(i)
        
def func():
    mycursor.execute("select * from tk")
    i = 0
    for student in mycursor:
        for j in range(len(student)):
            e=Entry(f,width=30,fg='blue',bg='pink')
            e.grid(row=i,column=j)
            e.insert(END, student[j])
        i=i+1

a = StringVar()
b = StringVar()
c = StringVar()

l1 = Label(r, text="Enter ID: ")
l1.pack()
e1 = Entry(r, textvariable=a)
e1.pack()

l2 = Label(r, text="Enter name: ")
l2.pack()
e2 = Entry(r, textvariable=b)
e2.pack()

l3 = Label(r, text="Enter Salary: ")
l3.pack()
e3 = Entry(r, textvariable=c)
e3.pack()

b1 = Button(r, text="Submit", command=save)
b1.pack()
b2 = Button(r, text="Show Records", command=query)
b2.pack()
b3 = Button(r, text="Show", command=func)
b3.pack()

f = Frame(r,  width=200, height=300)
f.pack()


r.mainloop()

