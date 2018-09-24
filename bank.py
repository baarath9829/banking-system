from Tkinter import *
import cx_Oracle
class UI:
    Frames = {}
    Window = None
    accountno = 0
    def __init__(self):
        self.Window = Tk()
        self.Window.geometry("300x200")
        self.mainframe()
        self.signinframe()
        self.signupframe()
        self.adminframe()
        self.submenuframe()

        self.Frames["main"].tkraise()
        self.Window.mainloop()
        
    def mainframe(self):
        frame = Frame(self.Window, width=768, height=576 , bg="ivory")
        frame.grid(row=0,column=0)
        frame.grid_propagate(0)
        Label(frame , text="Menu" ,fg="red").grid(row=0 , column=2)
        signup = Button(frame ,text = "sign up")
        signup.bind("<Button-1>", self.showsignup)
        signup.grid(row = 2, column=2)

        signin = Button(frame ,text = "sign in",command=lambda: self.showsignin())
        #signin.bind("<Button-1>", self.showsignin)
        signin.grid(row = 3, column=2)

        admin = Button(frame ,text = "admin sign in ")
        admin.bind("<Button-1>", self.showadmin)
        admin.grid(row = 4, column=2)

        Quit = Button(frame ,text = "Quit",command=self.Window.destroy)
        #Quit.bind("<Button-1>", self.Quitwindow)
        Quit.grid(row = 5, column=2)

        self.Frames["main"] = frame

    def signinframe(self):
        frame = Frame(self.Window, width=768, height=576 , bg="ivory")
        frame.grid(row=0,column=0)
        frame.grid_propagate(0)
        Label(frame , text="Login" ,fg="red").grid(row=0 , column=2)
        Label(frame , text="username").grid(row=2, column=0)
        Label(frame ,text="password").grid(row =3, column=0)
        username = Entry(frame, width=20)
        password = Entry(frame , width=20)
        username.grid(row=2, column=1)
        password.grid(row=3, column=1)

        login = Button(frame ,text = "login",command=lambda: self.loginto(username.get(),password.get()))
        #login.bind("<Button-1>", self.loginto)
        login.grid(row = 4, column=1)

        self.Frames["signin"] = frame

    def signupframe(self):
        
        frame = Frame(self.Window, width=768, height=576 , bg="ivory" ,bd=5)
        frame.grid(row=0,column=0)
        frame.grid_propagate(0)
        Label(frame , text="signup" ,fg="red").grid(row=0 , column=2)
        Label(frame , text="Name of Accountholder").grid(row=2, column=0)
        Label(frame ,text="Date of birth").grid(row =3, column=0)
        Label(frame , text="address").grid(row=4, column=0)
        Label(frame , text="Type Of Account").grid(row=5, column=0)
        Label(frame , text="username").grid(row=6, column=0)
        Label(frame ,text="password").grid(row =7, column=0)
        name = Entry(frame, width=20)
        age = Entry(frame , width=20)
        address = Entry(frame , width=20)
        TOA = Entry(frame , width=20)
        username = Entry(frame, width=20)
        password = Entry(frame , width=20)
        name.grid(row=2, column=1)
        age.grid(row=3, column=1)
        address.grid(row=4, column=1)
        TOA.grid(row=5, column=1)
        username.grid(row=6, column=1)
        password.grid(row=7, column=1)

        submit = Button(frame ,text = "submit",command=lambda: self.signup(name.get(),age.get(),address.get(),username.get(),password.get(),TOA.get()))
        #submit.bind("<Button-1>", self.showsignin)
        submit.grid(row = 4, column=1)

        self.Frames["signup"] = frame

    def adminframe(self): 
        frame = Frame(self.Window, width=768, height=576 , bg="ivory")
        frame.grid(row=0,column=0)
        frame.grid_propagate(0)
        Label(frame , text="Login" ,fg="red").grid(row=0 , column=2)
        Label(frame , text="username").grid(row=2, column=0)
        Label(frame ,text="password").grid(row =3, column=0)
        username = Entry(frame, width=20)
        password = Entry(frame , width=20)
        username.grid(row=2, column=1)
        password.grid(row=3, column=1)

        login = Button(frame ,text = "login",command=lambda: self.adminlogin(username.get(), password.get()))
        #login.bind("<Button-1>", self.adminlogin(username, password))
        login.grid(row = 4, column=1)

        self.Frames["admin"] = frame

    def submenuframe(self):
        frame = Frame(self.Window, width=768, height=576 , bg="ivory")
        frame.grid(row=0,column=0)
        frame.grid_propagate(0)
        Label(frame , text="SubMenu" ,fg="red").grid(row=0 , column=2)

        addresschange = Button(frame ,text = "Address Change", command= lambda: self.changeaddress())
        addresschange.grid(row = 2, column=2)

        deposit = Button(frame ,text = "Money Deposit", command= lambda: self.deposit())
        deposit.grid(row = 3, column=2)

        withdraw = Button(frame ,text = "Money Withdrawal", command= lambda: self.withdraw())
        withdraw.grid(row = 4, column=2)

        statement = Button(frame ,text = "Print Statement", command= lambda: self.printstatement())
        statement.grid(row = 5, column=2)

        transfer = Button(frame ,text = "Transfer Money", command= lambda: self.transfer())
        transfer.grid(row = 6, column=2)

        accountclose = Button(frame ,text = "Account Closure", command= lambda: self.accountclose())
        accountclose.grid(row = 7, column=2)

        logout = Button(frame ,text = "Customer Logout", command= lambda: self.logout())
        logout.grid(row = 8, column=2)

        self.Frames["submenu"] = frame


    def showsignup(self,event):
        self.Frames["signup"].tkraise()

    def showsignin(self):
        self.Frames["signin"].tkraise()

    def showadmin(self,event):
        self.Frames["admin"].tkraise()

    def showsubmenu(self):
        self.Frames["submenu"].tkraise()

    def loginto(self,username,password):
        db = DB()
        self.accountno = db.login(username,password)
        if (self.accountno > 0):
            self.showsubmenu()
        else:
            print ("login failed")
        
    def adminlogin(self , username , password):
        if ((username == "system") and (password == "root")):
            print ("closed account")
            db = DB()
            db.close(self.accountno)

    def changeaddress(self):
        address = input("enter the address")
        db = DB()
        db.updateaddress(address,self.accountno)

    def deposit(self):
        amount = input("enter the amount")
        db = DB()
        db.deposit(amount,self.accountno)

    def withdraw(self):
        amount = input("enter the amount")
        db = DB()
        db.withdraw(amount,self.accountno)

    def printstatement(self):
        record = []
        db = DB()
        record = db.display(self.accountno)
        for statement in record:
            print (statement)

    def transfer(self):
        amount = input("enter the amount")
        actno = input("enter the accountno of reciever account")
        db = DB()
        db.withdraw(amount,self.accountno)
        db.deposit(amount,actno)

    def accountclose(self):
        db = DB()
        db.close(self.accountno)

    def logout(self):
        self.accountno = 0
        self.showsignin()

    def signup(self,name,age,address,username,password,TOA):
        db = DB()
        db.createaccount(name,age,address,username,password,TOA)
        self.showsignin()
        

class DB:
    cursor = None
    accountno = 1500
    def __init__(self):
        con = cx_Oracle.connect("bank/root@XE")
        self.cursor = con.cursor()

    def createaccount(self,name,age,address,username,password,TOA):
        print (name)
        print (age)
        print (address)
        print (username)
        print (password)
        print (TOA)
        self.accountno = self.accountno + 1
        balance = 0
        self.cursor.execute("insert into customer values(:accountno,:name,:age,:address,:username, :password ,:TOA ,:balance)",{'accountno':self.accountno,'name':name,'age':age,'address':address,'username':username,'password':password,'TOA':TOA,'balance': balance})

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
                self.cursor.execute("select accountno from customer where username = :username",{'username':username})
                accountno = self.cursor.fetchall()
                return accountno
            else:
                return 0
        else:
            return 0
    def display(self,accountno):
        record = []
        self.cursor.execute("select *  from customer")
        record = self.cursor.fetchall()
        return (record)
    def updateaddress(self,address,accountno):
        self.cursor.execute("update customer set address = :address where accountno = :accountno",{'address':address,'accountno':accountno})
    def close(self,accountno):
        self.cursor.execute("insert into closeaccount values(:accountno",{'accountno':accountno})
