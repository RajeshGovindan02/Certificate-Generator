from PIL import Image, ImageFont, ImageDraw
import tkinter as tk
from tkinter import filedialog
from tkinter import colorchooser
from tkinter import messagebox
import shutil


def make_certificates(name):
    FONT_COLOR = color_label['bg']

    image_source = Image.open(image_path_entry.get("1.0", "end-1c"))
    x=int(posx.get())
    y=int(posy.get())
    position = (x,y)

    fontsize = int(font_size.get())

    draw = ImageDraw.Draw(image_source)

    font = ImageFont.truetype(font_path_entry.get("1.0", "end-1c"), fontsize)
    draw.text(position, name, fill=FONT_COLOR, font=font)

    # Separate the file name from the full name
    file_name = name.split(",")[0]

    # Open the file dialog
    file_path = folder_path_entry.get("1.0", "end-1c")

    # Saving the certificates in a different directory.
    image_source.save(f"{file_path}/" + file_name + ".png")
    #print('Saving Certificate of:', file_name)
    #list1=file_name
    #for namelist in list1:
    list_entry.insert(tk.END, f'Saving {file_name}\n' )
    list_entry.config(fg='#011c87')



def generate_certificates():
    names = name_entry.get("1.0", "end-1c").split("\n")
    if not names:
        messagebox.showinfo("Error", "Empty input detected!")

    for name in names:
        make_certificates(name)

    #print(len(names), "certificates done.")
    list_entry.insert(tk.END, f"{len(names)} certificates done.")


def browse_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")],title="Select image")
    image_path_entry.delete("1.0", "end")
    image_path_entry.insert("end", file_path)

def browse_font():
    file_path = filedialog.askopenfilename(filetypes=[("Font Files", "*.ttf")],title="Select Font file")
    font_path_entry.delete("1.0", "end")
    font_path_entry.insert("end", file_path)

def choose_color():
    color = colorchooser.askcolor(title="Choose a color")
    if color[1]:  # Check if a color was chosen
        chosen_color = color[1]
        color_label.config(text=chosen_color, bg=chosen_color,width=10)
    else:
        color_label.config(text="No color chosen", bg="white")

def select_folder():
    folder_path = filedialog.askdirectory(title="Select the Path")
    folder_path_entry.delete("1.0", "end")
    folder_path_entry.insert("end", folder_path)

# Create Tkinter window
window = tk.Tk()
window.geometry("782x655+300+20")
window.title("Certificate Generator")
window.wm_iconbitmap("./extrafiles/icon.ico")
window.resizable(False, False)

canvas = tk.Canvas(
    window,
    bg = "#ffffff",
    height = 655,
    width = 782,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = tk.PhotoImage(file = f"./extrafiles/background.png")
background = canvas.create_image(
    365, 355,
    image=background_img)

# Image Selection
image_path_entry = tk.Text(window, height=1, width=35,border=0)
image_path_entry.place(x=127,y=125)
image1 = tk.PhotoImage(file=f"./extrafiles/Button-2.png")
image_browse_button = tk.Button(window, image=image1, command=browse_image,width=30,border=0,bg='#333333',fg='white',font=('arial bold',10))
image_browse_button.place(x=50,y=118)

# Font Selection
font_path_entry = tk.Text(window, height=1, width=35,border=0)
font_path_entry.place(x=127,y=172)
image2 = tk.PhotoImage(file="./extrafiles/Button-3.png")
font_browse_button = tk.Button(window, image=image2, command=browse_font,width=30,border=0,bg='#333333',fg='white',font=('arial bold',10))
font_browse_button.place(x=50,y=165)

#font size
font_size = tk.Entry(window,width=9,border=0)
font_size.place(x=357,y=336)

#Path
image3 = tk.PhotoImage(file="./extrafiles/Button-4.png")
select_button = tk.Button(window, image=image3, command=select_folder,width=35,border=0,bg='#333333',fg='white',font=('arial bold',10))
select_button.place(x=50,y=214)

folder_path_entry = tk.Text(window, height=1, width=31,border=0)
folder_path_entry.place(x=127,y=220)



#position
posx = tk.Entry(window,width=4,border=0)
posx.place(x=345,y=393)
posy=tk.Entry(window,width=4,border=0)
posy.place(x=400,y=393)

# Create a button to choose a color
image4 = tk.PhotoImage(file="./extrafiles/Button.png")
button = tk.Button(window, image=image4, command=choose_color,border=0,bg='#333333',fg='white',font=('arial bold',10))
button.place(x=261,y=445)

# Create a label to display the chosen color
color_label = tk.Label(window, text="No color chosen", bg="white",font=('arial',7))
color_label.place(x=350,y=447)

# Names Input
name_entry = tk.Text(window, height=18, width=23,border=0)
name_entry.place(x=49,y=313)

#List
list_entry = tk.Text(window, height=15, width=28,border=0,font=("arial",8,"bold italic"))
list_entry.place(x=517,y=332)

# Generate Certificates Button
image5 = tk.PhotoImage(file="./extrafiles/Button-1.png")
generate_button = tk.Button(window, image=image5, command=generate_certificates,border=0,bg='#333333',fg='white',font=('arial bold',10))
generate_button.place(x=305,y=509)

# Start the Tkinter event loop
window.mainloop()
