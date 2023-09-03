import tkinter as tk 
import customtkinter
from PIL import Image, ImageTk
import customtkinter
from views import Login

#font
font1 = ('Montserrat', 48, 'bold')
font2 = ('Montserrat', 17)
font3 = ('Montserrat', 16, 'bold')
font4 = ('Montserrat', 16, 'bold', 'underline')
font5 = ('Montserrat', 14)

class admin(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        # Background image frame
        self.background_frame = tk.Frame(self, width=1200, height=700)
        self.background_frame.pack()
        
        # Background image
        self.pil_image = Image.open("Assets/adminlogin_bg.png")
        self.background_image = ImageTk.PhotoImage(self.pil_image)
        self.background_label = tk.Label(self.background_frame, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)  # Adjust placement
        
        #loginform container
        self.adminloginform = customtkinter.CTkFrame(self.background_frame, height=700, width=600, fg_color="#235D84", bg_color="#235D84")
        self.adminloginform.place(relx = 0.5, rely = 0.5, anchor = "w")
        
        #loginlabel
        self.adminloginlabel = customtkinter.CTkLabel(self.adminloginform, text="Admin Login", font=font1, text_color="#D5FFD0")
        self.adminloginlabel.place(relx = 0.5, rely = 0.2, anchor = "center")
        
        #admin input
        self.adminID = customtkinter.CTkEntry(self.adminloginform,border_width=0, font=font2,text_color="#D5FFD0", corner_radius=0, fg_color="transparent", placeholder_text_color="#D5FFD0", placeholder_text="Employee ID", width=400, height=64)
        self.adminID.place(relx = 0.5, rely = 0.4, anchor = "center")
        self.idlinebreak = customtkinter.CTkFrame(self.adminloginform, height=4, width=400, fg_color="#D5FFD0")
        self.idlinebreak.place(relx = 0.5, rely = 0.43, anchor = "center")
        self.error_empID = customtkinter.CTkLabel(self.adminloginform, text="", font=font5, text_color="#FF6349")
        self.error_empID.place(relx = 0.5, rely = 0.46, anchor = "center")
        
        #password input
        self.adminPASS = customtkinter.CTkEntry(self.adminloginform,border_width=0, font=font2, show="*", text_color="#D5FFD0",  corner_radius=0, fg_color="transparent", placeholder_text_color="#D5FFD0", placeholder_text="Password", width=400, height=64)
        self.adminPASS.place(relx = 0.5, rely = 0.53, anchor = "center")
        self.passlinebreak = customtkinter.CTkFrame(self.adminloginform, height=4, width=400, fg_color="#D5FFD0")
        self.passlinebreak.place(relx = 0.5, rely = 0.56, anchor = "center")
        self.error_password = customtkinter.CTkLabel(self.adminloginform, text="", font=font5, text_color="#FF6349")
        self.error_password.place(relx = 0.5, rely = 0.59, anchor = "center")
        self.showpass = 0
        self.passwordshow = Image.open("Assets/show.png")
        self.passwordhidden = Image.open("Assets/hidden.png")
        self.passwordshow_image = customtkinter.CTkImage(self.passwordshow)
        self.passwordhidden_image = customtkinter.CTkImage(self.passwordhidden)
        self.passwordbutton = customtkinter.CTkButton(self.adminloginform, text = "", hover_color="#235D84",  width=0, image=self.passwordshow_image, bg_color="transparent", fg_color="transparent", command= self.showpassword)
        self.passwordbutton.place(relx = 0.8, rely = 0.53, anchor = "center")

        #adminlogin
        self.buttoncontainer = customtkinter.CTkFrame(self.adminloginform, bg_color="transparent", fg_color="transparent")
        self.buttoncontainer.place(relx = 0.5, rely = 0.8, anchor="center")
        self.returnemp = customtkinter.CTkButton(self.buttoncontainer, corner_radius=50, height=40, width=200, font= font3, hover_color="#D5FFD0", text_color = "#235D84", fg_color="#D5FFD0", bg_color="transparent", text="Return",cursor="hand2", command=self.returnemployee)
        self.returnemp.pack(side="left", padx=10)
        self.adminlogin = customtkinter.CTkButton(self.buttoncontainer, corner_radius=50, height=40, width=200, font= font3, hover_color="#D5FFD0", text_color = "#235D84", fg_color="#D5FFD0", bg_color="transparent", text="Login",cursor="hand2", command= self.adm_login)
        self.adminlogin.pack(side="left", padx=10)
    
    # see and hide password
    def showpassword(self):
        if self.showpass == 0:
            self.passwordbutton["image"] = self.passwordhidden_image
            self.adminPASS.configure(show="")
            self.showpass = 1
        else:
            self.passwordbutton["image"] = self.passwordshow_image
            if self.adminPASS.get() != "":
                self.adminPASS.configure(show="*")
                self.showpass = 0
                
    # login as employee
    def returnemployee(self):
        self.adminID.delete(0, "end")
        self.adminPASS.delete(0, "end")
        Login.Login.noerror(Login.Login)
        self.controller.show_frame(Login.Login)
    
    def adm_login(self):
        admID = self.adminID.get()
        admPASS = self.adminID.get()
        
        # checking empty entries
        if admID == "" and admPASS == "":
            self.error_password.configure(text="This field is required!")
            self.error_empID.configure(text="This field is required!")
            self.passlinebreak.configure(fg_color="#FF5349")
            self.idlinebreak.configure(fg_color="#FF5349")
        elif admID == "":
            self.error_password.configure(text="")
            self.error_empID.configure(text="This field is required!")
            self.passlinebreak.configure(fg_color="#D5FFD0")
            self.idlinebreak.configure(fg_color="#FF5349")
            
        elif admPASS == "":
            self.error_password.configure(text="This field is required!")
            self.error_empID.configure(text="")
            self.passlinebreak.configure(fg_color="#FF5349")
            self.idlinebreak.configure(fg_color="#D5FFD0")
        else:
            self.error_password.configure(text="")
            self.error_empID.configure(text="")
            self.passlinebreak.configure(fg_color="#D5FFD0")
            self.idlinebreak.configure(fg_color="#D5FFD0")
            self.clear()
            
    def clear(self):
        self.adminID.delete(0, "end")
        self.adminPASS.delete(0,"end")
    