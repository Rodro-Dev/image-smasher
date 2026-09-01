import pyvips as pv
from pathlib import Path
import utils
import customtkinter as ctk

app = ctk.CTk()
size169 = ctk.BooleanVar(app,value=False)

def compress(dir_main:str):
    outpath = Path(f"{dir_main}\compressed")
    outpath.mkdir(exist_ok=True)
    for img in Path(dir_main).iterdir():
        try:
            if utils.is_supported(img.name):
                iformat = utils.selected_format
                img2 = pv.Image.new_from_file(img)
                output = f"{outpath}\{img.stem}{iformat}"
                if size169.get():
                    if utils.is_169(img2.width,img2.height):
                        while True:
                            try:
                                value = utils.put_percentage(img.name) / 100
                                if 0.01 <= value <= 1.00:
                                    break
                            except ValueError:
                                pass
                            print("Invalid value")
                        img2 = img2.resize(value)
                match iformat:
                    case ".avif":
                        img2.write_to_file(
                            str(output),
                            Q=1,
                            lossless=False,
                            effort=9,
                            bitdepth=8,
                            subsample_mode='on',
                            compression='av1',
                            encoder='aom',
                            strip=True
                        )
                    case ".png":
                        img2.write_to_file(
                            str(output),
                            compression=9,
                            filter='all',
                            palette=True,
                            bitdepth=8
                        )
                    case ".jpg":
                        img2.write_to_file(
                            str(output),
                            Q=1,
                            optimize_coding=True,
                            interlace=True,
                            strip=True,
                            background=[0,0,0]
                        )
        except Exception as x:
            print(f"Error en {img.name}: {x}")

