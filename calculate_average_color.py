import os
import csv

from PIL import Image


data_list = []
for image_name in os.listdir('image/euph_part_icon'):
    if not image_name.endswith('.png'):
        continue
    im = Image.open('image/euph_part_icon/'+image_name)
    im_width, im_height = im.size
    red = 0
    green = 0
    blue = 0
    for x in range(0, im_width):
        for y in range(0, im_height):
            rgba = im.getpixel((x, y))
            red   += rgba[0]
            green += rgba[1]
            blue  += rgba[2]
    red   = round(red   / (im_width*im_height))
    green = round(green / (im_width*im_height))
    blue  = round(blue  / (im_width*im_height))
    data_list.append([image_name, red, green, blue])

with open('average_color.csv', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerows(data_list)
