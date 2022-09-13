import os
from PIL import Image

def shrink_imgs(images=os.listdir('atlas_images/')):
    for image in images:

        img = Image.open('atlas_images/' + image)
        img.thumbnail(size=(300,300))

        # We would run the command below to save the images:
        img.save('atlas_images/resized'+image, optimize=True)

if __name__ == "__main__":
    IMAGES = '/home/blondbeard/projects/1017/atlas_images'
    shrink_imgs()