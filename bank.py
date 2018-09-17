from Tkinter import *
import cx_Oracle
class UI:
    Frames = {}
    Window = None
    def __init__(self):
        self.Window = Tk()
        self.mainframe()
        self.signinframe()
        self.signupframe()
        self.adminframe()

        self.Frames["main"].tkraise()
        self.Window.mainloop()
        
    def mainframe(self):
        frame = Frame(self.Window, width=768, height=576 , bg="red")
        frame.grid(row=0,column=0)
        Label(frame , text="Menu" ,fg="red").grid(row=0 , column=2)
        signup = Button(frame ,text = "sign up")
        signup.bind("<Button-1>", self.showsignup)
        signup.grid(row = 2, column=2)

        signin = Button(frame ,text = "sign in")
        signin.bind("<Button-1>", self.showsignin)
        signin.grid(row = 3, column=2)

        admin = Button(frame ,text = "admin sign in ")
        admin.bind("<Button-1>", self.showadmin)
        admin.grid(row = 4, column=2)

        Quit = Button(frame ,text = "Quit")
        Quit.bind("<Button-1>", self.Quitwindow)
        Quit.grid(row = 5, column=2)

        self.Frames["main"] = frame

    def signinframe(self):
        frame = Frame(self.Window, width=768, height=576 , bg="red")
        frame.grid(row=0,column=0)
        Label(frame , text="Login" ,fg="red").grid(row=0 , column=2)
        Label(frame , text="username").grid(row=2, column=0)
        Label(frame ,text="password").grid(row =3, column=0)
        username = Entry(frame, width=20)
        password = Entry(frame , width=20)
        username.grid(row=2, column=1)
        password.grid(row=3, column=1)

        login = Button(frame ,text = "login")
        login.bind("<Button-1>", self.loginto)
        login.grid(row = 4, column=1)

        self.Frames["signin"] = frame

    def signupframe(self):
        
        frame = Frame(self.Window, width=768, height=576 , bg="red" ,bd=5)
        frame.grid(row=0,column=0)
        Label(frame , text="signup" ,fg="red").grid(row=0 , column=2)
        Label(frame , text="username").grid(row=2, column=0)
        Label(frame ,text="Date of birth").grid(row =3, column=0)
        Label(frame ,text="password").grid(row =4, column=0)
        username = Entry(frame, width=20)
        dob = Entry(frame , width=20)
        password = Entry(frame , width=20)
        username.grid(row=2, column=1)
        dob.grid(row=3, column=1)
        password.grid(row=3, column=1)

        submit = Button(frame ,text = "submit")
        submit.bind("<Button-1>", self.showsignin)
        submit.grid(row = 4, column=1)

        self.Frames["signup"] = frame

    def adminframe(self): 
        frame = Frame(self.Window, width=768, height=576 , bg="red")
        frame.grid(row=0,column=0)
        Label(frame , text="Login" ,fg="red").grid(row=0 , column=2)
        Label(frame , text="username").grid(row=2, column=0)
        Label(frame ,text="password").grid(row =3, column=0)
        username = Entry(frame, width=20)
        password = Entry(frame , width=20)
        username.grid(row=2, column=1)
        password.grid(row=3, column=1)

        login = Button(frame ,text = "login")
        login.bind("<Button-1>", self.adminlogin)
        login.grid(row = 4, column=1)

        self.Frames["admin"] = frame

    def showsignup(self,event):
        self.Frames["signup"].tkraise()

    def showsignin(self,event):
        self.Frames["signin"].tkraise()

    def showadmin(self,event):
        self.Frames["admin"].tkraise()

    def Quitwindow(self,event):
        self.Window.destory()

    def loginto(self,event):
        print ("checkdb")
        #checkdb()
    def adminlogin(self , event):
        print ("admin login")

class db:
    cursor = None
    def __init__(self):
        con = cx_Oracle.connect("VIDHU/Yazhini@XE")
        self.cursor = con.cursor()

    def createaccount(self,username,dob,password):
        self.cursor.execute("insert into customer values(:username, :dob, :password)",{'username':username,'dob':dob,'password':password})

    def deposit(self,amount,accountno):
        self.cursor.execute("select balance from customer where accountno = :accountno",{'accountno':accountno})
        balance = self.cursor.fetchall()
        self.cursor.execute("update customer set balance = :balance where accountno = :accountno",{'balance':balance+amount,'accountno':accountno})

    def withdraw(self,amount,accountno):
        self.cursor.execute("select balance from customer where accountno = :accountno",{'accountno':accountno})
        balance = self.cursor.fetchall()
        self.cursor.execute("update customer set balance = :balance where accountno = :accountno",{'balance':balance-amount,'accountno':accountno})

    def login(self,username ,password):
        users = []
        self.cursor.execute("select username from customer")
        users = self.cursor.fetchall()
        if username in users:
            self.cursor.execute("select password from customer where username = :username",{'username':username})
            passwrd = self.cursor.fetchall()
            if (passwrd == password):
                return True
            else:
                return False
        else:
            return False
