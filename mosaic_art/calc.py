import statistics as st

from PIL import ImageStat


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
    im_crop = icon_im.crop((left, top, right, bottom))
    mean_color = ImageStat.Stat(im_crop).mean
    red   = round(mean_color[0])
    green = round(mean_color[1])
    blue  = round(mean_color[2])
    return (red, green, blue)

def mode_color_in_range(icon_im, left, top, right, bottom):
    """Returns the mode color of pixels in a given region

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
    red_values   = []
    green_values = []
    blue_values  = []
    color_values = []
    for x in range(left, right):
        for y in range(top, bottom):
            rgba = icon_im.getpixel((x, y))
            color_str = str(rgba[0]).zfill(3)+str(rgba[1]).zfill(3)+str(rgba[2]).zfill(3)
            color_values.append(color_str)
    try:
        mode_color = st.mode(color_values)
    except st.StatisticsError:
        # 複数の最頻値がある場合、平均値を返す
        im_crop = icon_im.crop((left, top, right, bottom))
        mean_color = ImageStat.Stat(im_crop).mean
        red   = round(mean_color[0])
        green = round(mean_color[1])
        blue  = round(mean_color[2])
    else:
        red   = int(mode_color[0:3])
        green = int(mode_color[3:6])
        blue  = int(mode_color[6:9])
    return (red, green, blue)

def median_color_in_range(icon_im, left, top, right, bottom):
    """Returns the median color of pixels in a given region

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
    im_crop = icon_im.crop((left, top, right, bottom))
    median_color = ImageStat.Stat(im_crop).median
    red   = median_color[0]
    green = median_color[1]
    blue  = median_color[2]
    return (red, green, blue)
