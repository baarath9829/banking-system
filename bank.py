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
        Label(frame , text="Menu" ,fg="red").grid(row=0 , column=4)
        signup = Button(frame ,text = "sign up")
        signup.bind("<Button-1>", self.showsignup)
        signup.grid(row = 2, column=4)

        signin = Button(frame ,text = "sign in",command=lambda: self.showsignin())
        #signin.bind("<Button-1>", self.showsignin)
        signin.grid(row = 3, column=4)

        admin = Button(frame ,text = "admin sign in ")
        admin.bind("<Button-1>", self.showadmin)
        admin.grid(row = 4, column=4)

        Quit = Button(frame ,text = "Quit",command=self.Window.destroy)
        #Quit.bind("<Button-1>", self.Quitwindow)
        Quit.grid(row = 5, column=4)

        self.Frames["main"] = frame

    def signinframe(self):
        frame = Frame(self.Window, width=768, height=576 , bg="ivory")
        frame.grid(row=0,column=0)
        frame.grid_propagate(0)
        Label(frame , text="Login" ,fg="red").grid(row=0 , column=1)
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
        Label(frame , text="signup" ,fg="red").grid(row=0 , column=1)
        Label(frame , text="Name of Accountholder").grid(row=2, column=0)
        Label(frame ,text="age").grid(row =3, column=0)
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
        submit.grid(row = 9, column=1)

        self.Frames["signup"] = frame

    def adminframe(self): 
        frame = Frame(self.Window, width=768, height=576 , bg="ivory")
        frame.grid(row=0,column=0)
        frame.grid_propagate(0)
        Label(frame , text="Login" ,fg="red").grid(row=0 , column=1)
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

    def displaystatement(self, acctno, name, age, address, TOA, balance):
         #window creation
        frame = Frame(self.Window, width=768, height=576 , bg="ivory")
        frame.grid(row=0,column=0)
        frame.grid_propagate(0)
        Label(frame , text="account details" ,fg="red").grid(row=0 , column=1)
        
        Label(frame , text="Account Number :").grid(row=2, column=0)
        Label(frame , text="Accountholder Name :").grid(row=3, column=0)
        Label(frame ,text="Age :").grid(row =4, column=0)
        Label(frame , text="Address :").grid(row=5, column=0)
        Label(frame , text="Type Of Account :").grid(row=6, column=0)
        Label(frame , text="Balance :").grid(row=7, column=0)
        
        Label(frame , text=str(acctno)).grid(row=2, column=2)
        Label(frame , text=str(name)).grid(row=3, column=2)
        Label(frame ,text=str(age)).grid(row =4, column=2)
        Label(frame , text=str(address)).grid(row=5, column=2)
        Label(frame , text=str(TOA)).grid(row=6, column=2)
        Label(frame , text=str(balance)).grid(row=7, column=2)
        
        back = Button(frame ,text = "back", command= lambda: self.showsubmenu())
        back.grid(row = 8, column=1)

        self.Frames["display"] = frame

    def admindisplay(self, record):
        frame = Frame(self.Window, width=768, height=576 , bg="ivory")
        frame.grid(row=0,column=0)
        frame.grid_propagate(0)
        Label(frame , text="closed account details" ,fg="red").grid(row=0 , column=1)
        
        Label(frame , text="Account Number :").grid(row=2, column=0)
        i=2
        for acctno in record:
            i = i+1
            Label(frame , text=str(acctno)).grid(row=i, column=0)

        back = Button(frame ,text = "back")
        back.bind("<Button-1>", self.showadmin)
        back.grid(row = 3, column=2)

        self.Frames["closed"] = frame
        
    def showsignup(self,event):
        self.Frames["signup"].tkraise()

    def showsignin(self):
        self.Frames["signin"].tkraise()

    def showadmin(self,event):
        self.Frames["admin"].tkraise()

    def showsubmenu(self):
        self.Frames["submenu"].tkraise()

    def showdisplay(self):
        self.Frames["dislay"].tkraise()

    def showclosedacct(self):
        self.Frames["closed"].tkraise()

    def loginto(self,username,password):
        db = DB()
        self.accountno = db.login(username,password)
        if (self.accountno > 0):
            self.showsubmenu()
        else:
            print ("login failed")
        
    def adminlogin(self , username , password):
        if ((username == "system") and (password == "root")):
            db = DB()
            record = db.closedaccount()
            print (record)
            self.admindisplay(record[0])
            self.showclosedacct()
            

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
        statement = db.display(self.accountno)
        print (statement[0])
        actno  = statement[0][0]
        name = statement[0][1]
        age = statement[0][2]
        address = statement[0][3]
        TOA = statement[0][6]
        balance =  statement[0][7]
        self.displaystatement(actno, name, age, address, TOA, balance)
        self.showdisplay()
       

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
    con = None
    accountno = 1500
    def __init__(self):
        self.con = cx_Oracle.connect("bank/root@XE")
        self.cursor = self.con.cursor()

    def createaccount(self,name,age,address,username,password,TOA):
        print (name)
        print (age)
        print (address)
        print (username)
        print (password)
        print (TOA)
        self.accountno = self.accountno + 1
        balance = 0
        sql="insert into customer values(:accountno,:name,:age,:address,:username, :password ,:TOA ,:balance)"
        self.cursor.execute(sql,{'accountno':self.accountno,'name':name,'age':age,'address':address,'username':username,'password':password,'TOA':TOA,'balance': balance})
        self.con.commit()
        
    def deposit(self,amount,accountno):
        self.cursor.execute("select balance from customer where accountno = :accountno",{'accountno':accountno})
        balance = self.cursor.fetchall()
        self.cursor.execute("update customer set balance = :balance where accountno = :accountno",{'balance':balance+amount,'accountno':accountno})
        self.con.commit()

    def withdraw(self,amount,accountno):
        self.cursor.execute("select balance from customer where accountno = :accountno",{'accountno':accountno})
        balance = self.cursor.fetchall()
        self.cursor.execute("update customer set balance = :balance where accountno = :accountno",{'balance':balance-amount,'accountno':accountno})
        self.con.commit()
        
    def login(self,username ,password):
        self.cursor.execute("select username from customer")
        users = self.cursor.fetchall()
        if (username in users[0]):
            self.cursor.execute("select password from customer where username = :username",{'username':username})
            passwrd = self.cursor.fetchall()
            print (passwrd)
            if (passwrd[0][0] == password):
                self.cursor.execute("select accountno from customer where username = :username",{'username':username})
                accountno = self.cursor.fetchall()
                print (accountno[0][0])
                return accountno[0][0]
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
        self.con.commit()
    def close(self,accountno):
        self.cursor.execute("insert into closeaccount values(:accountno)",{'accountno':accountno})
        self.con.commit()
    def closedaccount(self):
        self.cursor.execute("select * from closeaccount")
        record = self.cursor.fetchall()
        return record
            
obj = UI()
