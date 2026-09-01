import pyvips as pv
from pathlib import Path
import shutil
from utils import is_169, is_supported, put_percentage
import customtkinter as ctk

app = ctk.CTk()
size169 = ctk.BooleanVar(app,value=False)

def compress(dir_main:str):
    outpath = Path(f"{dir_main}\compressed")
    outpath.mkdir(exist_ok=True)
    for img in Path(dir_main).iterdir():
        try:
            if is_supported(img.name):
                img2 = pv.Image.new_from_file(img)
                output = outpath / f"{img.stem}.avif"
                if size169.get():
                    if is_169(img2.width,img2.height):
                        while True:
                            try:
                                value = put_percentage(img.name) / 100
                                if 0.01 <= value <= 1.00:
                                    break
                            except ValueError:
                                pass
                            print("Invalid value")
                        img2 = img2.resize(value)
                img2.write_to_file(
                    str(output),
                    Q=1,
                    lossless=False,
                    effort=7,
                    bitdepth=8,
                    compression='av1',
                    encoder='x265'
                )
        except Exception as x:
            print(f"Error en {img.name}: {x}")

