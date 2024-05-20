from image_utils.check import create_edited_mask

import os

images_folder = 'edited_test_photos'
images = os.listdir(images_folder)

out_images_folder = 'out_photos'

for img in images:
    create_edited_mask(os.path.join(images_folder, img),
                       os.path.join(out_images_folder, img))
    print(img, 'processed')