from PIL import Image


def open_image_RGB(image_path):
    """Open a image in a mode that can provide RGB values.
    If RGB values cannot be acquired from a image,
    convert the image to 'RGBA' mode.

    Args:
        image_path: str
            image file path

    Returns:
        Image Object
            'RGBA' or 'RGB' mode
    """
    im = Image.open(image_path)
    if not im.mode in ['RGBA', 'RGB']:
        print('convert to RGBA from {0}: {1}'.format(im.mode, image_path))
        return im.convert('RGBA')
    else:
        return im
