import csv
import datetime
import sys

from PIL import Image

from mosaic_art import args_validation
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
    args = sys.argv
    if args_validation.validate(args):
        create_mosaic_art(args[1], args[2], args[3])
    else:
        sys.exit('Terminate without creating mosaic art due to argument error')

def create_mosaic_art(target_im,
                      target_representation, material_representation):
    """Creates mosaic art from target image
    with specified representation colors about target and material

    Args:
        target_im: path of target image file (:str)
            example: 'foo/bar.png'
        target_representation: str
            assumed to be `average`, `median` or `mode`
        material_representation: str
            assumed to be `average`, `median` or `mode`
    """
    color_data_file = material_color_file_name(material_representation)
    color_data = materials_list_from_file(color_data_file)

    icon_im = image_process.open_image_RGB(target_im)
    icon_im_width, icon_im_height = icon_im.size
    mosaic_icon_im = Image.new('RGBA', (1600, 1600))
    calculation_method = color_calculate_method(target_representation)

    for left in range(0, icon_im_width, DOT_AREA_ONE_SIDE):
        for top in range(0, icon_im_height, DOT_AREA_ONE_SIDE):
            average_color = calculation_method(icon_im, left, top,
                                left+DOT_AREA_ONE_SIDE, top+DOT_AREA_ONE_SIDE)
            if len(average_color) != 3:
                continue

            filename = similar_color_filename(average_color, color_data)
            # 距離最小のファイルを1600×1600の画像に貼り付け
            area_im = Image.open('material/euph_part_icon/'+filename)
            mosaic_icon_im.paste(area_im, (left//DOT_AREA_ONE_SIDE * THUMBNAIL_ONE_SIDE,
                                           top//DOT_AREA_ONE_SIDE * THUMBNAIL_ONE_SIDE))

    saved_file = mosaic_art_file_name(target_im,
                    target_representation, material_representation)
    save_file_path = 'product/{}'.format(saved_file)
    print('Mosaic art created at', save_file_path)
    mosaic_icon_im.save(save_file_path)

def mosaic_art_file_name(target_im,
                         target_representation, material_representation):
    """Returns a file name from target image name

    Args:
        target_im: path of target image file (:str)
            example: 'foo/bar.png'
        target_representation: str
            assumed to be `average`, `median` or `mode`
        material_representation: str
            assumed to be `average`, `median` or `mode`

    Returns:
        str
            example: 'bar_mosaic_average_median_20180331121251.png'
                target_representation: 'average'
                material_representation: 'median'
    """
    representation_variation = ['average', 'median', 'mode']
    if not target_representation in representation_variation:
        sys.exit('Not assumed args `target_representation` '
                 'at function `mosaic_art_file_name`: {}'
                 .format(target_representation))
    elif not material_representation in representation_variation:
        sys.exit('Not assumed args `material_representation` '
                 'at function `mosaic_art_file_name`: {}'
                 .format(material_representation))
    target_file_name = extract_file_name(target_im)
    now_dt = now_datetime()
    return '{0}_mosaic_{1}_{2}_{3}.png'.format(
                target_file_name, target_representation,
                material_representation, now_dt)

def extract_file_name(file_path):
    """Extracts file name from file path (not including extension)

    Args:
        file_path: str
            example: 'foo/bar.png'

    Returns:
        str
            example: 'bar'

    """
    # ファイルパスからファイル名(拡張子含む)を取り出す
    file_name = file_path.split('/')[-1]
    # 拡張子を取り除く
    return file_name.split('.')[0]

def now_datetime():
    """Returns current time as '%Y%m%d%H%M%S' string

    Returns:
        str
            example: '20180331121251'
                current time 2018/3/31 12:12:51
    """
    now = datetime.datetime.now()
    return now.strftime('%Y%m%d%H%M%S')

def material_color_file_name(representative_color):
    """Returns file name corresponding to specified representative color

    Args:
        representative_color: str
            assumed to be `average`, `median` or `mode`

    Returns:
        str
    """
    representation_variation = ['average', 'median', 'mode']
    if not representative_color in representation_variation:
        sys.exit('Not assumed args at function `material_color_file_name`: {}'
                 .format(representative_color))
    return '{}_color.csv'.format(representative_color)

def color_calculate_method(representative_color):
    """Returns a method for color calculation of target image
    corresponding to specified representative color

    Args:
        representative_color: str
            assumed to be `average`, `median` or `mode`

    Returns:
        function
    """
    if representative_color == 'average':
        return calc.average_color_in_range
    elif representative_color == 'median':
        return calc.median_color_in_range
    elif representative_color == 'mode':
        return calc.mode_color_in_range
    else:
        sys.exit('Not assumed args at function `color_calculate_method`: {}'
                 .format(representative_color))

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
