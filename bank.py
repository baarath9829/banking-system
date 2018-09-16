from Tkinter import *
class UI:
    Frames = []
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

        self.Frames.append(frame)

    def signinframe(self):
        
