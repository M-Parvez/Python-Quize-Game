from tkinter import *
from tkinter import messagebox
import mysql.connector as msc
import random
class AdminLogin:
    def __init__(self):
        self.root=Tk()
        self.root.geometry("300x300")
        self.root.title("Admin-Login")
        self.l1=Label(self.root, text="Enter id :")
        self.l2=Label(self.root, text="Enter Password :")
        self.t1=Entry(self.root,width=21)
        self.t2=Entry(self.root,width=21)
        self.b1=Button(self.root,text="Login",command=self.login,width=17)
        self.l1.place(x=20,y=30)
        self.l2.place(x=20,y=60)
        self.t1.place(x=110,y=30)
        self.t2.place(x=110,y=60)
        self.b1.place(x=110,y=90)
        self.root.mainloop()
    def login(self):
        self.conn=msc.connect(host="localhost",user="root",password="Parvez@123",database="qe")
        self.cur=self.conn.cursor()
        self.cur.execute("select* from adminuser where Name='{}' and Password='{}'".format(self.t1.get(),self.t2.get()))
        self.user=self.cur.fetchone()
        if self.user==None:
            messagebox.showinfo("sorry","invalid User")
        else:
            messagebox.showinfo("Welcome")
            w=WelcomeAdmin()  #Object -- call Welcome admin 
            self.conn.close()

class WelcomeAdmin:
    def __init__(self):
        self.root=Tk()
        self.root.geometry("300x300")
        self.root.title("Welcome-Admin")
        self.l1=Label(self.root,text="Hii..,  PLEASE select Your choice.")
        self.b1=Button(self.root,text="Add QUESTIONS",command=self.addq,width=17)
        self.b2=Button(self.root,text="Add NEW.ADMIN",command=self.newadmin,width=17)
        self.l1.place(x=20,y=20)
        self.b1.place(x=20,y=50)
        self.b2.place(x=20,y=80)
        self.root.mainloop()
    def addq(self):
        a=AddQuestion()
    def newadmin(self):
        a=NewAdmin()

class AddQuestion:
    def __init__(self):
        self.root=Tk()
        self.root.geometry("300x300")
        self.root.title("Adding-Questions")
        self.l1=Label(self.root,text="Q.")
        self.l2=Label(self.root,text="1:")
        self.l3=Label(self.root,text="2:")
        self.l4=Label(self.root,text="3:")
        self.l5=Label(self.root,text="4:")
        self.l6=Label(self.root,text="ANS:")
        
        self.t1=Entry(self.root,width=35)
        self.t2=Entry(self.root,width=35)
        self.t3=Entry(self.root,width=35)
        self.t4=Entry(self.root,width=35)
        self.t5=Entry(self.root,width=35)
        self.t6=Entry(self.root,width=35)
        self.b1=Button(self.root,text="Save",command=self.save,width=17)
        
        self.l1.place(x=20,y=30)
        self.l2.place(x=20,y=60)
        self.l3.place(x=20,y=90)
        self.l4.place(x=20,y=120)
        self.l5.place(x=20,y=150)
        self.l6.place(x=2,y=180)
        
        self.t1.place(x=40,y=30)
        self.t2.place(x=40,y=60)
        self.t3.place(x=40,y=90)
        self.t4.place(x=40,y=120)
        self.t5.place(x=40,y=150)
        self.t6.place(x=40,y=180)
        self.b1.place(x=40,y=210)
        self.root.mainloop()
    def save(self):
        self.conn=msc.connect(host="localhost",user="root",password="Parvez@123",database="qe")
        self.cur=self.conn.cursor()
        self.cur.execute("insert into Questions(question,op1,op2,op3,op4,Ans)values('{}','{}','{}','{}','{}','{}')".format(self.t1.get(),self.t2.get(),self.t3.get(),self.t4.get(),self.t5.get(),self.t6.get()))
        self.conn.commit()
        self.conn.close()
        messagebox.showinfo("saved Succesfully")
        self.t1.delete(0,"end")
        self.t2.delete(0,"end")
        self.t3.delete(0,"end")
        self.t4.delete(0,"end")
        self.t5.delete(0,"end")
        self.t6.delete(0,"end")

class NewAdmin:
    def __init__(self):
        self.root=Tk()
        self.root.geometry("300x300")
        self.root.title("Add-Admin")
        self.l1=Label(self.root,text="Enter ID :")
        self.t1=Entry(self.root,width=20)
        self.l2=Label(self.root,text="Enter PASS :")
        self.t2=Entry(self.root,width=20)
        self.b1=Button(self.root,text="Save",command=self.save,width=16)
        self.l1.place(x=20,y=30)
        self.t1.place(x=100,y=30)
        self.l2.place(x=20,y=80)
        self.t2.place(x=100,y=80)
        self.b1.place(x=100,y=120)
        self.root.mainloop()
    def save(self):
        self.conn=msc.connect(host="localhost",user="root",password="Parvez@123",database="qe")
        self.cur=self.conn.cursor()
        self.cur.execute("insert into adminuser values('{}','{}')".format(self.t1.get(),self.t2.get()))
        self.conn.commit()
        self.conn.close()
        messagebox.showinfo("saved Succesfully")
        self.t1.delete(0,"end")
        self.t2.delete(0,"end") 

  #--------------------------------------End Of ADMIN SECTION  
class StudentLogin:
    def __init__(self):
        self.root=Tk()
        self.root.geometry("300x300")
        self.root.title("Student-Login")
        self.l1=Label(self.root,text="Username:")
        self.l2=Label(self.root,text="Password:")

        
        self.t1=Entry(self.root,width=21)
        self.t2=Entry(self.root,width=21)
        self.b1=Button(self.root,text="Login",command=self.login,width=12)
        self.l1.place(x=20,y=30)
        self.l2.place(x=20,y=60)

        self.l3=Label(self.root,text="Are You New here,Please CLICK on SIGNUP Button ")
        self.b3=Button(self.root,text="SIGNUP",command=self.signup,width=12)
        self.l3.place(x=20,y=150)
        self.b3.place(x=110,y=170)
        
        self.t1.place(x=100,y=30)
        self.t2.place(x=100,y=60)
        self.b1.place(x=110,y=90)
        self.root.mainloop()
    def login(self):
        self.conn=msc.connect(host="localhost",user="root",password="Parvez@123",database="qe")
        self.cur=self.conn.cursor()
        self.cur.execute("select* from studentuser where id='{}' and Password='{}'".format(self.t1.get(),self.t2.get()))
        self.user=self.cur.fetchone()
        if self.user==None:
            messagebox.showinfo("sorry","invalid User")
        else:
            messagebox.showinfo("Welcome")
            w=WelcomeStudent()
    def signup(self):
        a=Signup()


class Signup:
    def __init__(self):
        self.root=Tk()
        self.root.geometry("300x300")
        self.root.title("Signup-Student")
        self.l1=Label(self.root,text="Enter ID :")
        self.t1=Entry(self.root,width=20)
        self.l2=Label(self.root,text="Enter PASS :")
        self.t2=Entry(self.root,width=20)
        self.b1=Button(self.root,text="Save",command=self.save,width=16)
        self.l1.place(x=20,y=30)
        self.t1.place(x=100,y=30)
        self.l2.place(x=20,y=80)
        self.t2.place(x=100,y=80)
        self.b1.place(x=100,y=120)
        self.root.mainloop()
    def save(self):
        self.conn=msc.connect(host="localhost",user="root",password="Parvez@123",database="qe")
        self.cur=self.conn.cursor()
        self.cur.execute("insert into studentuser values('{}','{}')".format(self.t1.get(),self.t2.get()))
        self.conn.commit()
        self.conn.close()
        messagebox.showinfo("saved Succesfully")
        self.t1.delete(0,"end")
        self.t2.delete(0,"end")                           

class WelcomeStudent:
    def __init__(self):
        self.root=Tk()
        self.root.geometry("300x300")
        self.root.title("Game-Start")
        self.b1=Button(self.root,text="START Qiuz",command=self.Quiz,bg="Blue")
        self.l1=Label(self.root,text="Are YO Ready For Quiz ??")
        self.b1.place(x=160,y=20)
        self.l1.place(x=20,y=20)
        self.root.mainloop()            
#-------------------------------------------------------------XXXX------

    def Quiz(self):
        self.aq=[]
        while True:
            self.qid=random.randint(1,5)
            if self.qid not in self.aq:
                self.aq.append(self.qid)
                break
        self.conn=msc.connect(host="localhost",user="root",password="Parvez@123",database="qe")     #connection established
        self.cur=self.conn.cursor()
        self.cur.execute("select* from Questions")
        self.records=self.cur.fetchall()
        self.r=self.records[self.qid]
        self.root=Tk()
        self.root.geometry("400x400")
        self.s=IntVar()
        self.l1=Label(self.root,text=self.r[1])
        self.r2=Radiobutton(self.root,text=self.r[2],value=2,variable=self.s)
        self.r3=Radiobutton(self.root,text=self.r[3],value=3,variable=self.s)
        self.r4=Radiobutton(self.root,text=self.r[4],value=4,variable=self.s)
        self.r5=Radiobutton(self.root,text=self.r[5],value=5,variable=self.s)
        self.b1=Button(self.root,text="NEXT",command=self.Next,width=17)
            
        self.l1.place(x=20,y=30)
        self.r2.place(x=20,y=60)
        self.r3.place(x=20,y=90)
        self.r4.place(x=20,y=120)
        self.r5.place(x=20,y=150)
        self.b1.place(x=40,y=180)
        self.root.mainloop()
            
    def Next(self):
        print(self.s.get(),"*",self.r[6])
        self.score=0
        if self.s.get()==self.r[6]:
            self.score=self.score+1
            messagebox.showinfo("score","yr score is "+str(self.score))            
        while True:
            self.qid=random.randint(1,5) #Enter qid
            if self.qid not in self.aq:
                self.aq.append(self.qid)
                break
                self.r=self.records[self.qid]
        print(self.r)
        self.l1["text"]=self.r[1]
        self.r2["text"]=self.r[2]
        self.r3["text"]=self.r[3]
        self.r4["text"]=self.r[4]
        self.r5["text"]=self.r[5]                      
#------------------------------------------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-------------------------------------

def adminlogin():
    a=AdminLogin()
def studentlogin():
    a=StudentLogin()
root=Tk()
root.geometry("300x300")
root.title("Quiz Game")
l1=Label(root,text="Please Login To Play The QUIZ",font=('Helvetica',10,'bold'))
l2=Label(root,text="If You Are a Student, Click on STUDENT LOGIN ",font=('Helvetica',8))
l3=Label(root,text="If You Are a ADMIN, Click on ADMIN LOGIN",font=('Helvetica',8,))
b3=Button(root,text="ADMIN Login",command=AdminLogin,width=15)
b2=Button(root,text="STUDENT Login",command=StudentLogin,width=15)
l5=Label(root,text="Developed by:- MOHAMMAD PARVEZ ",font=('Helvetica',7))
l1.place(x=40,y=20)
l2.place(x=30,y=70)
b2.place(x=80,y=95)
l3.place(x=40,y=140)
b3.place(x=80,y=165)
l5.place(x=55,y=270)
root.mainloop()
