from image_utils.vision import get_vin_number

image_path = 'vin_number.jpg'

num = get_vin_number(image_path)
print(num)