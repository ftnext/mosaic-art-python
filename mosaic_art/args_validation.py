import os.path


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
