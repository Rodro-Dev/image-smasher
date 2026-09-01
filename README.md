# Image Smasher

A strong Python tool to convert and do a massive compress images to AVIF.
It is useful for those who need to compress textures or photos EXTREMELY for a smaller file size.

> **Note:** The final format always will be AVIF (This may change in future updates).

## Features

- Convert multiple image formats to AVIF
- Compress images using pyvips
- Optional resize for 16:9 and 9:16 images
- Automatic output folder
- Error handling for unsupported or corrupted images

## Supported formats

- PNG
- JPG / JPEG
- WEBP
- TIFF
- AVIF

## Requirements

- Python 3.x
- pyvips
- libvips

Install pyvips:

```bash
pip install pyvips
```

> **Note:** On Windows, libvips must also be installed and added to the PATH.
            On Android, libvips must also be installed with Termux. 

## Usage

Run the program:

```bash
python main_gui.py
```

Then enter the folder containing your images and follow the prompts.

## License

MIT