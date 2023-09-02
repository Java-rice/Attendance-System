import tkinter as tk 
import customtkinter
from PIL import Image, ImageTk
import customtkinter
from views import Admin

font1 = ('Montserrat', 48, 'bold')
font2 = ('Montserrat', 17)
font3 = ('Montserrat', 16, 'bold')
font4 = ('Montserrat', 16, 'bold', 'underline')
font5 = ('Montserrat', 14)

class Login(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        # Background image frame
        self.background_frame = tk.Frame(self, width=1200, height=700)
        self.background_frame.pack()
        
        # Background image
        self.pil_image = Image.open("Assets/login_bg.png")
        self.background_image = ImageTk.PhotoImage(self.pil_image)
        self.background_label = tk.Label(self.background_frame, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)  # Adjust placement
        
        #loginform container
        self.loginform = customtkinter.CTkFrame(self.background_frame, height=700, width=600, fg_color="#235D84", bg_color="#235D84")
        self.loginform.place(relx = 0.5, rely = 0.5, anchor = "w")
        
        #loginlabel
        self.loginlabel = customtkinter.CTkLabel(self.loginform, text="Employee\nLogin", font=font1, text_color="#D5FFD0")
        self.loginlabel.place(relx = 0.5, rely = 0.2, anchor = "center")
        
        #userID input
        self.employeeID = customtkinter.CTkEntry(self.loginform,border_width=0, font=font2,text_color="#D5FFD0",  corner_radius=0, fg_color="transparent", placeholder_text_color="#D5FFD0", placeholder_text="Employee ID", width=400, height=64)
        self.employeeID.place(relx = 0.5, rely = 0.4, anchor = "center")
        self.idlinebreak = customtkinter.CTkFrame(self.loginform, height=4, width=400, fg_color="#D5FFD0")
        self.idlinebreak.place(relx = 0.5, rely = 0.43, anchor = "center")
        self.error_empID = customtkinter.CTkLabel(self.loginform, text="", font=font5, text_color="#FF6349")
        self.error_empID.place(relx = 0.5, rely = 0.46, anchor = "center")
        
        #password input
        self.employeePASS = customtkinter.CTkEntry(self.loginform,border_width=0,show="*", font=font2, text_color="#D5FFD0",  corner_radius=0, fg_color="transparent", placeholder_text_color="#D5FFD0", placeholder_text="Password", width=400, height=64)
        self.employeePASS.place(relx = 0.5, rely = 0.53, anchor = "center")
        self.passlinebreak = customtkinter.CTkFrame(self.loginform, height=4, width=400, fg_color="#D5FFD0")
        self.passlinebreak.place(relx = 0.5, rely = 0.56, anchor = "center")
        self.error_password = customtkinter.CTkLabel(self.loginform, text="", font=font5, text_color="#FF6349")
        self.error_password.place(relx = 0.5, rely = 0.59, anchor = "center")
        self.showpass = 0
        self.passwordshow = Image.open("Assets/show.png")
        self.passwordhidden = Image.open("Assets/hidden.png")
        self.passwordshow_image = customtkinter.CTkImage(self.passwordshow)
        self.passwordhidden_image = customtkinter.CTkImage(self.passwordhidden)
        self.passwordbutton = customtkinter.CTkButton(self.loginform, text = "", hover_color="#235D84",  width=0, image=self.passwordshow_image, command=self.showpassword, bg_color="transparent", fg_color="transparent")
        self.passwordbutton.place(relx = 0.8, rely = 0.53, anchor = "center")
        
        #button
        self.emploginbutton = customtkinter.CTkButton(self.loginform, corner_radius=50, height=40, width=200, font= font3, hover_color="#D5FFD0", text_color = "#235D84", fg_color="#D5FFD0", bg_color="transparent", text="Login",cursor="hand2", command= self.emp_login)
        self.emploginbutton.place(relx = 0.5, rely = 0.7, anchor = "center")
        
        #adminlogin
        self.admincontainer = customtkinter.CTkFrame(self.loginform, bg_color="transparent", fg_color="transparent")
        self.admincontainer.place(relx = 0.5, rely = 0.8, anchor="center")
        self.ruadmin = customtkinter.CTkLabel(self.admincontainer, text="Are you an admin?", text_color="#D5FFD0", font = font2, fg_color="transparent", bg_color="transparent")
        self.ruadmin.pack(side="left")
        self.adminbutton = customtkinter.CTkButton(self.admincontainer, font= font4, hover_color="#235D84", text_color = "#D5FFD0", width=0, fg_color="transparent", bg_color="transparent", text="Login Here",cursor="hand2", command=self.loginadmin)
        self.adminbutton.pack(side="left")
    
    # see and hide password
    def showpassword(self):
        if self.showpass == 0:
            self.passwordbutton["image"] = self.passwordhidden_image
            self.employeePASS.configure(show="")
            self.showpass = 1
        else:
            self.passwordbutton["image"] = self.passwordshow_image
            if self.employeePASS.get() != "":
                self.employeePASS.configure(show="*")
                self.showpass = 0    
    
    # login as admin
    def loginadmin(self):
        self.clear()
        self.controller.show_frame(Admin.admin)
    
    def emp_login(self):
        empID = self.employeeID.get()
        empPASS = self.employeePASS.get()
        
        # checking empty entries
        if empID == "" and empPASS == "":
            self.error_password.configure(text="This field is required!")
            self.error_empID.configure(text="This field is required!")
            self.passlinebreak.configure(fg_color="#FF5349")
            self.idlinebreak.configure(fg_color="#FF5349")
        elif empID == "":
            self.error_password.configure(text="")
            self.error_empID.configure(text="This field is required!")
            self.passlinebreak.configure(fg_color="#D5FFD0")
            self.idlinebreak.configure(fg_color="#FF5349")
            
        elif empPASS == "":
            self.error_password.configure(text="This field is required!")
            self.error_empID.configure(text="")
            self.passlinebreak.configure(fg_color="#FF5349")
            self.idlinebreak.configure(fg_color="#D5FFD0")
        else:
            self.noerror()
            self.clear()
        
    def clear(self):
        self.employeePASS.delete(0, "end")
        self.employeeID.delete(0,"end")
    
    def noerror(self):
        self.error_password.configure(text="")
        self.error_empID.configure(text="")
        self.passlinebreak.configure(fg_color="#D5FFD0")
        self.idlinebreak.configure(fg_color="#D5FFD0")
    