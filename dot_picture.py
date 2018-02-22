from PIL import Image

DOT_AREA_ONE_SIDE = 10

def open_RGBA_image(image_path):
    """Open a image in 'RGBA' mode

    Args:
        image_path: str
            image file path

    Returns:
        Image Object
            always 'RGBA' mode
    """
    im = Image.open(image_path)
    if im.mode != 'RGBA':
        print('convert to RGBA from {0}: {1}'.format(im.mode, image_path))
        return im.convert('RGBA')
    else:
        return im

icon_im = open_RGBA_image('my_icon.png')
icon_im_width, icon_im_height = icon_im.size
dot_icon_im = icon_im.copy()

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
        average_color_im = Image.new('RGBA',
                                     (DOT_AREA_ONE_SIDE, DOT_AREA_ONE_SIDE),
                                     (red, green, blue, 255)) # a=0だと透明で何も見えない
        dot_icon_im.paste(average_color_im, (left, top))

dot_icon_im.save('my_icon_dot.png')
