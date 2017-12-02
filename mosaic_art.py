import csv

from PIL import Image


DOT_AREA_ONE_SIDE = 10
THUMBNAIL_ONE_SIDE = 40

color_data = []
with open('average_color.csv' ,'r', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        color_data.append(row)

icon_im = Image.open('my_icon.png')
icon_im_width, icon_im_height = icon_im.size
mosaic_icon_im = Image.new('RGBA', (1600, 1600))

for left in range(0, icon_im_width, DOT_AREA_ONE_SIDE):
    for top in range(0, icon_im_height, DOT_AREA_ONE_SIDE):
        red = 0
        green = 0
        blue = 0
        #平均色の計算
        for x in range(left, left+DOT_AREA_ONE_SIDE):
            for y in range(top, top+DOT_AREA_ONE_SIDE):
                rgba = icon_im.getpixel((x, y))
                red   += rgba[0]
                green += rgba[1]
                blue  += rgba[2]
        red   = int(red   / (DOT_AREA_ONE_SIDE*DOT_AREA_ONE_SIDE))
        green = int(green / (DOT_AREA_ONE_SIDE*DOT_AREA_ONE_SIDE))
        blue  = int(blue  / (DOT_AREA_ONE_SIDE*DOT_AREA_ONE_SIDE))

        distance = 255**2 * 3 # 最大の距離
        filename = ''
        # 色の差が最小になるファイルを決定(距離に見立てている)
        for color in color_data:
            d = (red-int(color[1]))**2 + (green-int(color[2]))**2 + (blue-int(color[3]))**2
            if d < distance:
                distance = d
                filename = color[0]
        # 距離最小のファイルを縮小して1600×1600の画像に貼り付け
        area_im = Image.open('image/euph_part_icon/'+filename)
        area_im.thumbnail((THUMBNAIL_ONE_SIDE, THUMBNAIL_ONE_SIDE))
        mosaic_icon_im.paste(area_im, (left//10 * THUMBNAIL_ONE_SIDE, top//10 * THUMBNAIL_ONE_SIDE))

mosaic_icon_im.save('product/my_icon_mosaic.png')
