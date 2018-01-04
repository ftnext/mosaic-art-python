import os

from PIL import Image


THUMBNAIL_ONE_SIDE = 40

for image_name in os.listdir('image/euph_part_icon'):
    if not image_name.endswith('.png'):
        continue
    im = Image.open('image/euph_part_icon/'+image_name)
    im.thumbnail((THUMBNAIL_ONE_SIDE, THUMBNAIL_ONE_SIDE))
    im.save('material/euph_part_icon/'+image_name)
