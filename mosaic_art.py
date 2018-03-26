import csv
import os.path

from PIL import Image

from mosaic_art import calc
from mosaic_art import image_process


DOT_AREA_ONE_SIDE = 10
THUMBNAIL_ONE_SIDE = 40
# 2つの色(R,G,B)の間の最大の距離
MAX_COLOR_DISTANCE = 255**2 * 3
# CSVファイル中のカラムの意味づけ
POS_NAME  = 0
POS_RED   = 1
POS_GREEN = 2
POS_BLUE  = 3

def main():
def validate(args):
    """Validates arguments

    Args:
        args: list of arguments
    """
    if len(args) > 2:
        print('Too Many arguments:', args)
        show_usage()
        return False
    elif len(args) == 1:
        print('Missing arguments')
        show_usage()
        return False
    if not validate_image_format(args[1]):
        print('image file is not PNG or JPEG:', args[1])
        show_usage()
        return False
    if not exists_file(args[1]):
        print('image file does not exist:', args[1])
        show_usage()
        return False
    return True

def validate_image_format(image):
    """Verify that the image file path is PNG or JPEG

    Args:
        image: target image file path (:str)
    """
    return image.endswith('png') or image.endswith('jpg')

def exists_file(file):
    """Verify that the file exists

    Args:
        file: target file path (:str)
    """
    return os.path.exists(file)

def show_usage():
    """Displays usage along with error message
    """
    print('[Usage] python mosaic_art.py target/image/path')

def create_mosaic_art(target_im):
    """Creates mosaic art from target image

    Args:
        target_im: path of target image file (:str)
            example: 'foo/bar.png'
    """
    color_data = materials_list_from_file('average_color.csv')

    icon_im = image_process.open_image_RGB(target_im)
    icon_im_width, icon_im_height = icon_im.size
    mosaic_icon_im = Image.new('RGBA', (1600, 1600))

    for left in range(0, icon_im_width, DOT_AREA_ONE_SIDE):
        for top in range(0, icon_im_height, DOT_AREA_ONE_SIDE):
            average_color = calc.average_color_in_range(icon_im, left, top,
                                left+DOT_AREA_ONE_SIDE, top+DOT_AREA_ONE_SIDE)
            if len(average_color) != 3:
                continue

            filename = similar_color_filename(average_color, color_data)
            # 距離最小のファイルを1600×1600の画像に貼り付け
            area_im = Image.open('material/euph_part_icon/'+filename)
            mosaic_icon_im.paste(area_im, (left//DOT_AREA_ONE_SIDE * THUMBNAIL_ONE_SIDE,
                                           top//DOT_AREA_ONE_SIDE * THUMBNAIL_ONE_SIDE))

    mosaic_icon_im.save('product/my_icon_mosaic.png')

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

def color_distance(RGB1, RGB2):
    """Returns color distance

    Considering the distance between two points
    (x1, y1, z1) and (x2, y2, z2) in three dimensions

    Args:
        RGB1: A tuple which means (R, G, B)
        RGB2: A tuple which means (R, G, B)

    Returns:
        color distance(:int)

    """
    d2_r = (RGB1[0] - RGB2[0]) ** 2
    d2_g = (RGB1[1] - RGB2[1]) ** 2
    d2_b = (RGB1[2] - RGB2[2]) ** 2
    return d2_r + d2_g + d2_b

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
    distance = MAX_COLOR_DISTANCE
    filename = ''
    # 色の差が最小になるファイルを決定(距離に見立てている)
    for color in color_data:
        sample_color = (color[POS_RED], color[POS_GREEN], color[POS_BLUE])
        d = color_distance(average_color, sample_color)
        if d < distance:
            distance = d
            filename = color[POS_NAME]
    return filename

if __name__ == '__main__':
    main()
