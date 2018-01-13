import os
import csv

from PIL import Image

from mosaic_art import calc


data_list = []
for image_name in os.listdir('image/euph_part_icon'):
    if not image_name.endswith('.png'):
        continue
    im = Image.open('image/euph_part_icon/'+image_name)
    im_width, im_height = im.size
    red, green, blue = calc.median_color_in_range(im, 0, 0, im_width, im_height)
    data_list.append([image_name, red, green, blue])

with open('median_color.csv', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerows(data_list)
