import sys
import os
# if you have not already enter 'pip3 install Pillow' in the terminal
from PIL import Image

# 3 arguments entered in the terminal: the Python file, the origin folder, and the new folder respectively
folder = sys.argv[1]
new_folder = sys.argv[2]

# creates a new folder with the name you entered unless that name you entered is used
if not os.path.exists(new_folder):
    os.makedirs(new_folder)

# looping through origin folder, transferring files, converting them into .png
for items in os.listdir(folder):
    im = Image.open(f'{folder}{items}')
    clean_name = os.path.splitext(items)[0]
    im.save(f'{new_folder}{clean_name}.png', 'png')
    print('all done!')
