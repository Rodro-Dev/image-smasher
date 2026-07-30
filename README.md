# python-super-image-compressor
# Python Super Image Compressor

A simple Python tool to convert and compress images to AVIF.

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

## Usage

Run the program:

```bash
python image_smasher.py
```

Then enter the folder containing your images and follow the prompts.

## License

MIT