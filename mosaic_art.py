import csv

from PIL import Image


def materials_list_from_file(filename):
    """Returns a list which contains material image information.

    Args:
        filename: File name such as "foo.csv"
            The file contains information on average color of image.
            (Average color maens the average of the values of R of all pixels,
             the average of the values of G of all pixels,
             and the average of the values of B of all pixels)
            A row is as follows:
                image_name, R_average, G_average, B_average

    Returns:
        A list of tuples
        Tuple is like (
            image_name   : str (such as "bar.png"),
            red_average  : int,
            green_average: int,
            blue_average : int
            )
    """
    color_data = []
    with open(filename, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            image_info = (row[0], int(row[1]), int(row[2]), int(row[3]))
            color_data.append(image_info)
    return color_data

DOT_AREA_ONE_SIDE = 10
THUMBNAIL_ONE_SIDE = 40

color_data = materials_list_from_file('average_color.csv')

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
        red   = round(red   / (DOT_AREA_ONE_SIDE*DOT_AREA_ONE_SIDE))
        green = round(green / (DOT_AREA_ONE_SIDE*DOT_AREA_ONE_SIDE))
        blue  = round(blue  / (DOT_AREA_ONE_SIDE*DOT_AREA_ONE_SIDE))

        distance = 255**2 * 3 # 最大の距離
        filename = ''
        # 色の差が最小になるファイルを決定(距離に見立てている)
        for color in color_data:
            d = (red-color[1])**2 + (green-color[2])**2 + (blue-color[3])**2
            if d < distance:
                distance = d
                filename = color[0]
        # 距離最小のファイルを縮小して1600×1600の画像に貼り付け
        area_im = Image.open('image/euph_part_icon/'+filename)
        area_im.thumbnail((THUMBNAIL_ONE_SIDE, THUMBNAIL_ONE_SIDE))
        mosaic_icon_im.paste(area_im, (left//10 * THUMBNAIL_ONE_SIDE, top//10 * THUMBNAIL_ONE_SIDE))

mosaic_icon_im.save('product/my_icon_mosaic.png')
