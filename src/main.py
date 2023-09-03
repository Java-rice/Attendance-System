import tkinter as tk
import customtkinter
from views import Homepage, Login, Admin
from PIL import Image, ImageTk
from database import createtable

class mainframe(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        #clip on the center
        width = 1200
        height = 700
        s_width = self.winfo_screenwidth()
        s_height = self.winfo_screenheight()
        x = (s_width/2) - (width/2)
        y = (s_height/2) - (height/2)
        
        #window
        self.wm_title("Attendance System")
        self.geometry("%dx%d+%d+%d" % (width, height, x, y))
        self.resizable(0,0)
    
        self.discUserInfo = {}
        #create windows
        self.frames = {}
        
        # Main content container
        container = customtkinter.CTkFrame(self)
        container.place(relx=.5, rely=.5, anchor="center")
        
        # we'll create the frames themselves later but let's add the components to the dictionary.
        for F in (Homepage.Homepage, Login.Login, Admin.admin):
            frame = F(container, self)
            # the windows class acts as the root window for the frames.
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            
        self.show_frame(Homepage.Homepage)
        
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
        # raises the curent frame to the top
    
    def get_page(self, page_class):
        return self.frames[page_class]
    
if __name__ == "__main__":
    
    #creates database table
    createtable.startdb()
    
    App = mainframe()
    App.mainloop()