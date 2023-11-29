import sys
import os
from PIL import Image

folder = sys.argv[1]
new_folder = sys.argv[2]

if not os.path.exists(new_folder):
    os.makedirs(new_folder)

for items in os.listdir(folder):
    im = Image.open(f'{folder}{items}')
    clean_name = os.path.splitext(items)[0]
    im.save(f'{new_folder}{clean_name}.png', 'png')
    print('all done!')
