import os
import csv
import statistics as st

from PIL import Image


data_list = []
for image_name in os.listdir('image/euph_part_icon'):
    if not image_name.endswith('.png'):
        continue
    im = Image.open('image/euph_part_icon/'+image_name)
    im_width, im_height = im.size
    red_values   = []
    green_values = []
    blue_values  = []
    for x in range(0, im_width):
        for y in range(0, im_height):
            rgba = im.getpixel((x, y))
            red_values.append(rgba[0])
            green_values.append(rgba[1])
            blue_values.append(rgba[2])
    red   = round(st.mean(red_values))
    green = round(st.mean(green_values))
    blue  = round(st.mean(blue_values))
    data_list.append([image_name, red, green, blue])

with open('average_color.csv', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerows(data_list)
