from pathlib import Path
import customtkinter as ctk

types = (".avif",".tif",".jpeg",".jpg",".png",".webp",)
not_supported = []

def dir_correct(path:str):
    if bool(path):
        dm = Path(path)
        if dm.exists() and dm.is_dir():
            return True
        return False

def is_169(width:int,height:int):
    if abs((width / height) - (16 / 9)) < 0.01:
        return True
    elif abs((width / height) - (9 / 16)) < 0.01:
        return True
    else:
        return False

def get_if_169():
    return

def is_supported(img_name:str):
    if Path(img_name).suffix in types:
        return True
    not_supported.append(img_name)
    return False

def get_unsuported_files():
    return not_supported

def put_percentage(file_name:str):
    while True:
        dialog = ctk.CTkInputDialog(
            text="Enter a % from 1-100:", 
            title=f"{file_name} will be resized"
        )
        entered_value = dialog.get_input()
        
        if entered_value is None:
            print("Canceled operation by user.")
            return 100
            
        try:
            num = int(entered_value)
            if 1 <= num <= 100:
                return num
            else:
                print("Error: Only 1-100 numbers.")
        except ValueError:
            print("Error: Please, put a valid number.")