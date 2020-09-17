import sys
import os
from PIL import Image, ImageFilter
existing_folder = sys.argv[1] #grabs arguments from terminal
new_folder = sys.argv[2]
if not os.path.exists(new_folder):
    os.mkdir(new_folder)
jpgs = os.listdir(existing_folder)
for image in jpgs:
    im = Image.open(f'{existing_folder}{image}')
    clean_name = os.path.splitext(image)[0] #splits file name into the name the file type e.g. .jpg or .docx
    gray_im = im.convert('L')
    gray_im.save(f'{new_folder}{clean_name}.png', 'png') 