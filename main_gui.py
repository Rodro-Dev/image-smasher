import customtkinter as ctk
from image_smasher import compress, size169
import utils
import os
import sys

if getattr(sys, "frozen", False):
    BASE_DIR = sys._MEIPASS
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

LIBVIPS_BIN = os.path.join(BASE_DIR, "libvips", "bin")

if os.path.isdir(LIBVIPS_BIN):
    os.environ["PATH"] = LIBVIPS_BIN + os.pathsep + os.environ.get("PATH", "")

    if hasattr(os, "add_dll_directory"):
        os.add_dll_directory(LIBVIPS_BIN)

import pyvips

def resource_path(relative_path):
    if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))

    return os.path.join(base_path, relative_path)

main = ctk.CTk()

main.title("Image Smasher")
main.geometry("800x600")
icon_path = "assets/icon.ico"
main.iconbitmap(resource_path(icon_path))

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme("dark-blue")

label1 = ctk.CTkLabel(main,text_color="white",
                      border_color="white",
                      text="Smash the images of your directory",
                      font=("Arial",16,"bold"))
label1.pack(pady=10)

path_entry = ctk.CTkEntry(main,220, placeholder_text="Put here the path")
path_entry.pack(pady=18)

label1 = ctk.CTkLabel(main,text_color="white",
                      border_color="white",
                      text="Select output format:",
                      font=("Arial",14,"bold"))
label1.place(x=580,y=80)
out_format = ctk.CTkOptionMenu(main,values=[".AVIF",".PNG",".JPG"])
out_format.place(x=585,y=120)

verify_b = ctk.CTkButton(main, text="Verify Path", command=lambda: verify())
verify_b.pack(pady=20)

switch169 = ctk.CTkSwitch(main, text="Ask for resize 16:9 images", variable=size169)
switch169.pack()

luf= []
def do_compress(path:str):
    utils.selected_format = out_format.get().lower()
    compress(path)
    yi = 80
    for f in utils.get_unsuported_files():
        if f != "compressed":
            lbl = ctk.CTkLabel(main, text=f,height=0, font=("Arial", 14))
            lbl.place(y=yi, x=15, anchor="w")
            yi += 15
            luf.append(lbl)
    lbus = ctk.CTkLabel(main,text_color="red",
                        text="UNSUPPORTED FILES:",
                        font=("Times New Roman", 16, "bold")
                        )
    if len(luf) != 0:
        lbus.place(x=10, y=50, anchor="w")

lb_error_path = ctk.CTkLabel(main,
                             text="ERROR: Path not found",
                             text_color="red",
                             font=("Times New Roman", 12, "bold")
                             )
def hide_lbep():
    lb_error_path.pack_forget()
compress_b = None
def verify():
    global compress_b

    if utils.dir_correct(path_entry.get()):
        if compress_b is None:
            compress_b = ctk.CTkButton(
                main,
                text="Compress",
                command=lambda: do_compress(path_entry.get())
            )
            compress_b.pack(pady=8)
    else:
        path_entry.delete(0, "end")
        lb_error_path.pack()
        main.after(3000, hide_lbep)

def close_app():
    main.destroy()
    sys.exit()
main.protocol("WM_DELETE_WINDOW", close_app)

main.mainloop()