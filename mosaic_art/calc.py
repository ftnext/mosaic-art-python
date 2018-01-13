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
    red_values   = []
    green_values = []
    blue_values  = []
    for x in range(left, right):
        for y in range(top, bottom):
            rgba = icon_im.getpixel((x, y))
            red_values.append(rgba[0])
            green_values.append(rgba[1])
            blue_values.append(rgba[2])
    red   = round(st.mean(red_values))
    green = round(st.mean(green_values))
    blue  = round(st.mean(blue_values))
    return (red, green, blue)
