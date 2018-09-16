from Tkinter import *
class UI:
    Frames = {}
    Window = None
    def __init__(self):
        Window = Tk()
        self.mainframe()
        self.signinframe()
        self.signupframe()
        self.AdminSignInFrame()
        self.firstframe()
        Window.mainloop()
        
    def mainframe(self):
        frame = Frame(Window)
        frame.grid(row=0,column=0)
        Label(frame , text="Menu" ,fg="red").grid(row=0 , column=2)
        signup = Button(frame ,text = "sign up")
        signup.bind("<Button-1>", showsignup)
        signup.grid(row = 2, column=2)

        signin = Button(frame ,text = "sign in")
        signin.bind("<Button-1>", showsignin)
        signin.grid(row = 3, column=2)

        admin = Button(frame ,text = "admin sign in ")
        admin.bind("<Button-1>", showadmin)
        admin.grid(row = 4, column=2)

        Quit = Button(frame ,text = "Quit")
        Quit.bind("<Button-1>", Quitwindow)
        Quit.grid(row = 5, column=2)

        self.Frames["main"] = frame

    def signinframe(self):
        frame = Frame(Window)
        frame.grid(row=0,column=0)
        Label(frame , text="Login" ,fg="red").grid(row=0 , column=2)
        Label(frame , text="username").grid(row=2, column=0)
        Label(frame ,text="password").grid(row =3, column=0)
        username = Entry(frame, width=20)
        password = Entry(frame , width=20)
        username.grid(row=2, column=1)
        passowrd.grid(row=3, column=1)

        login = Button(frame ,text = "login")
        login.bind("<Button-1>", loginto)
        login.grid(row = 4, column=1)

        self.Frames["signin"] = frame

    def signupframe(self):
        frame = Frame(Window)
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
        passowrd.grid(row=3, column=1)

        submit = Button(frame ,text = "submit")
        submit.bind("<Button-1>", showsignin)
        submit.grid(row = 4, column=1)

        self.Frames["signup"] = frame

     def adminframe(self):
        frame = Frame(Window)
        frame.grid(row=0,column=0)
        Label(frame , text="Login" ,fg="red").grid(row=0 , column=2)
        Label(frame , text="username").grid(row=2, column=0)
        Label(frame ,text="password").grid(row =3, column=0)
        username = Entry(frame, width=20)
        password = Entry(frame , width=20)
        username.grid(row=2, column=1)
        passowrd.grid(row=3, column=1)

        login = Button(frame ,text = "login")
        login.bind("<Button-1>", showsubmenu)
        login.grid(row = 4, column=1)

        self.Frames["admin"] = frame

    def showsignup(event):
        self.Frame["signup"].tkraise()

    def showsignin(event):
        self.Frame["signin"].tkraise()

    def showadmin(event):
        self.Frame["admin"].tkraise()

    def Quitwindow(event):
        window.destory()

    def loginto(event):
        checkdb()
