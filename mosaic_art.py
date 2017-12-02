import csv

from PIL import Image


DOT_AREA_ONE_SIDE = 10
THUMBNAIL_ONE_SIDE = 40
# 2つの色(R,G,B)の間の最大の距離
MAX_COLOR_DISTANCE = 255**2 * 3
# CSVファイル中のカラムの意味づけ
POS_NAME  = 0
POS_RED   = 1
POS_GREEN = 2
POS_BLUE  = 3

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
            image_info = (row[POS_NAME], int(row[POS_RED]),
                          int(row[POS_GREEN]), int(row[POS_BLUE]))
            color_data.append(image_info)
    return color_data

def average_color_in_range(icon_im, left, top, right, bottom):
    """Returns the average color of pixels in a given region

    Args:
        icon_im: Image object of Pillow
        left: X coordinate of the upper left point of the given region
        top:  Y coordinate of the upper left point of the given region
            NOTICE: (left, top) is included in the given region
        right:  X coordinate of the lower right point of the given area
        bottom: Y coordinate of the lower right point of the given area
            NOTICE: (right, bottom) is NOT included in the given region

    Returns:
        A tuple which means (R, G, B)
    """
    if left >= right: # 引数は left < right と想定
        print('left', left, '>= right', right)
        return ()
    if top >= bottom: # 引数は top < bottom と想定
        print('bottom', bottom, '>= top', top)
        return ()
    red   = 0
    green = 0
    blue  = 0
    for x in range(left, right):
        for y in range(top, bottom):
            rgba = icon_im.getpixel((x, y))
            red   += rgba[0]
            green += rgba[1]
            blue  += rgba[2]
    pixel_count = (right-left) * (bottom-top)
    red   = round(red   / pixel_count)
    green = round(green / pixel_count)
    blue  = round(blue  / pixel_count)
    return (red, green, blue)

def similar_color_filename(average_color, color_data):
    """Returns name of file similar to average color

    Find the image with average color closest to `average_color` from `color_data`

    Args:
        average_color: a tuple which means (R, G, B) of average color of a certain range
        color_data: A list of tuples
                    Tuple is like (image_name, red_average, green_average, blue_average)

    Returns:
        A name of file such as 'foo.png' (NOT path)
    """
    pass

color_data = materials_list_from_file('average_color.csv')

icon_im = Image.open('my_icon.png')
icon_im_width, icon_im_height = icon_im.size
mosaic_icon_im = Image.new('RGBA', (1600, 1600))

for left in range(0, icon_im_width, DOT_AREA_ONE_SIDE):
    for top in range(0, icon_im_height, DOT_AREA_ONE_SIDE):
        try:
            red, green, blue = average_color_in_range(icon_im, left, top,
                                   left+DOT_AREA_ONE_SIDE, top+DOT_AREA_ONE_SIDE)
        except ValueError:
            continue

        distance = MAX_COLOR_DISTANCE
        filename = ''
        # 色の差が最小になるファイルを決定(距離に見立てている)
        for color in color_data:
            d = (red-color[POS_RED])**2 + (green-color[POS_GREEN])**2 + (blue-color[POS_BLUE])**2
            if d < distance:
                distance = d
                filename = color[POS_NAME]
        # 距離最小のファイルを縮小して1600×1600の画像に貼り付け
        area_im = Image.open('image/euph_part_icon/'+filename)
        area_im.thumbnail((THUMBNAIL_ONE_SIDE, THUMBNAIL_ONE_SIDE))
        mosaic_icon_im.paste(area_im, (left//DOT_AREA_ONE_SIDE * THUMBNAIL_ONE_SIDE,
                                       top//DOT_AREA_ONE_SIDE * THUMBNAIL_ONE_SIDE))

mosaic_icon_im.save('product/my_icon_mosaic.png')
