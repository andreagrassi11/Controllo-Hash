from tkinter import *
import customtkinter
from tkinter import filedialog

class App(customtkinter.CTk):

    # costruttore
    def __init__(self):
        super().__init__()

        self.__filename = None

        # configure window
        self.title("Control Download")
        self.geometry(f"{1100}x{580}")  # {1100}x{580}
        customtkinter.set_appearance_mode("Dark")
        customtkinter.set_default_color_theme("dark-blue")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=2)
        self.grid_columnconfigure(3, weight=1)
        self.grid_rowconfigure((0, 1, 2, 3), weight=1)

        # -------------------- create sidebar frame with widgets --------------------------
        # sidebar frame
        self.top_bar = customtkinter.CTkFrame(self, corner_radius=15,fg_color= '#EEEEDA')
        self.top_bar.grid(row=0, column=0, columnspan=4, rowspan=2, sticky="NSew")

        self.file_dialog = customtkinter.CTkButton(self.top_bar, text="Scegli file", command=self.open_file, fg_color='#144D5F', width=500)
        self.file_dialog.grid(row=0, column=0, ipadx=5, ipady=5, padx=10, pady=10)

        self.input_hash_correct = customtkinter.CTkEntry(self.top_bar, placeholder_text="Hash corretto", width=500)
        self.input_hash_correct.grid(row=0, column=1,ipadx=5, ipady=5, padx=10, pady=10)

        self.submit_control = customtkinter.CTkButton(self.top_bar, text="Controlla", fg_color='#CB292C')
        self.submit_control.grid(row=2, column=1, columnspan=2)
    
    # Open file
    def open_file(self):
        self.__filename = filedialog.askopenfilename()
        if(self.__filename != None and self.__filename != ''):
            self.file_dialog.configure(fg_color='green')
            
            self.file_path = customtkinter.CTkLabel(self.top_bar, text=self.__filename, text_color='black')
            self.file_path.grid(row=1, column=0)

    # Get filename
    def get_filename(self):
        return self.__filename



