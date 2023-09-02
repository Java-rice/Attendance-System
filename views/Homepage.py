import tkinter as tk
from PIL import Image, ImageTk
import customtkinter
from views import Login

font1 = ('Montserrat', 16, 'bold') 

class Homepage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        # Background image frame
        self.background_frame = tk.Frame(self, width=1200, height=700)
        self.background_frame.pack()
        
        # Background image
        self.pil_image = Image.open("Assets/background.png")
        self.background_image = ImageTk.PhotoImage(self.pil_image)
        self.background_label = tk.Label(self.background_frame, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)  # Adjust placement
        
        self.homebutton = customtkinter.CTkButton(self.background_frame, corner_radius=20, height=40, width=200, font= font1, text_color = "#F5F5F5", fg_color="#0C356A", bg_color="#D5FFD0", text="Proceed",cursor="hand2", command=lambda: controller.show_frame(Login.Login))
        self.homebutton.place(relx = 0.5, rely = 0.8, anchor = "center")
        