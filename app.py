import tkinter as tk
from tkinter import *
from PIL import Image
from tkinter.filedialog import *

class App:
    ####colori#####
    co0 = "#000000"  # black
    co1 = "#cc1d4e"  # red
    co2 = "#feffff"  # white
    co3 = "#0074eb"  # blue
    co4 = "#435e5a"  # dark green
    co5 = "#59b356"  # green
    co6 = "#d9d9d9"  # grey
    
    def __init__(self, root):
        self.root = root
        self.root.title("Image Size Converter")
        self.root.geometry("440x350")
        self.root.configure(bg=self.co2, relief="flat", borderwidth=0)
        self.root.resizable(False, False)
        
        #Frame
        self.frame = tk.Frame(self.root, width=440, height=200, bg=self.co2, relief="flat")
        self.frame.grid(row=0, column=0, sticky="nsew")
        
        #Label Title
        self.labelTitle = tk.Label(self.frame, 
                              text="Image Size Converter", 
                              font=("Courier", 22, "bold"), 
                              bg=self.co2, 
                              fg=self.co0, 
                              width=24, 
                              height=1,
                              anchor="center",
                              relief="flat")
        self.labelTitle.grid(row=0, column=0, sticky="nsew", columnspan=2, pady=10, padx=10)
        
        #Button New Image
        self.button_new_image = tk.Button(self.frame, 
                                          text="New Image", 
                                          font=("Arial", 12), 
                                          bg=self.co3, 
                                          fg=self.co2, 
                                          width=15, 
                                          height=1,
                                          relief="raised",
                                          anchor="center",
                                          command=self.new_image)
        self.button_new_image.grid(row=1, column=0, columnspan=2, sticky="nsew", pady=1)
        
        #Label Image Info
        self.labelImgInfo = tk.Label(self.frame, 
                              text="", 
                              font=("Arial", 20), 
                              bg=self.co2, 
                              fg=self.co2, 
                              width=24, 
                              height=1,
                              anchor="center",
                              relief="flat")
        self.labelImgInfo.grid(row=2, column=0, sticky="nsew", columnspan=2, pady=10, padx=10)
        
        #Button Convert Image
        self.button_convert_image = tk.Button(self.frame, 
                                              text="Convert Image", 
                                              font=("Arial", 12), 
                                              bg=self.co5, 
                                              fg=self.co2, 
                                              width=15, 
                                              height=1,
                                              relief="raised",
                                              anchor="center",
                                              command=self.convert_image)
        self.button_convert_image.grid(row=5, column=0,columnspan=2, sticky="nsew", pady=15)
    
    #Upload Image   
    def new_image(self):
        self.img_file = askopenfilename()
        self.img = Image.open(self.img_file)
        self.img_width, self.img_height = self.img.size
        self.labelImgInfo["bg"] = self.co1
        self.labelImgInfo["text"] = f"Image Size Info: {self.img_width} x {self.img_height} px"
        #Label Image Info Update
        self.labelImgInfoUpdate = tk.Label(self.frame, 
                              text="Insert New Image Size: ",
                              font=("Arial", 20), 
                              bg=self.co4, 
                              fg=self.co5, 
                              width=24, 
                              height=1,
                              anchor="center",
                              relief="flat")
        self.labelImgInfoUpdate.grid(row=3, column=0, sticky="nsew", columnspan=2, pady=10, padx=10)
        
        #Entry per altezza e larghezza
        self.entry_width = tk.Entry(self.frame, 
                                    font=("Arial", 20), 
                                    bg=self.co6, 
                                    fg=self.co1, 
                                    width=8, 
                                    relief="solid",
                                    justify="center")
        self.entry_width.insert(0, "Width")
        self.entry_width.grid(row=4, column=0, sticky="nsew", pady=10, padx=10)
        
        #svuota entry
        self.entry_width.bind("<Button-1>", lambda event: self.entry_width.delete(0, "end"))
        
        self.entry_height = tk.Entry(self.frame,
                                    font=("Arial", 20), 
                                    bg=self.co6, 
                                    fg=self.co1, 
                                    width=8, 
                                    relief="solid",
                                    justify="center")
        self.entry_height.insert(0, "Height")
        self.entry_height.grid(row=4, column=1, sticky="nsew", pady=10, padx=10)
        
        #svuota entry
        self.entry_height.bind("<Button-1>", lambda event: self.entry_height.delete(0, "end"))
    
    #Convert Image    
    def convert_image(self):
        self.new_width = int(self.entry_width.get())
        self.new_height = int(self.entry_height.get())
        self.img_resized = self.img.resize((self.new_width, self.new_height))
        #self.img.show()
        self.img_resized_save = asksaveasfilename()        
        self.img_resized.save(self.img_resized_save+".png")
        