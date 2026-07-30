import pyvips as pv
from pathlib import Path
import shutil

types = (".avif",".tif",".jpeg",".jpg",".png",".webp",)

while True:
    input_dir = input("Directory of Images: ")
    dir_main = Path(input_dir)

    if dir_main.exists() and dir_main.is_dir():
        break

    print("Directory not found.")
Path("compressed").mkdir(exist_ok=True)
size169 = bool(int(input("Do you want to resize of images to 16:9? (1/0): ")))
for img in Path(dir_main).iterdir():
    try:
        if (img.suffix).lower() in types:
            img2 = pv.Image.new_from_file(img)
            output = Path("compressed") / f"{img.stem}.avif"
            if size169:
                if abs((img2.width / img2.height) - (16 / 9)) < 0.01 or\
                abs((img2.width / img2.height) - (9 / 16)) < 0.01:
                    while True:
                        try:
                            value = float(input(f"{img.name} is reduced in size,\
 choose the reduction percentage (1-0.01): "))
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
