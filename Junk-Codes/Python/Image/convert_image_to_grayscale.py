# https://x.com/clcoding/status/1993373827699818723

from PIL import Image

img = Image.open(input("Enter image file path: "))
gray_img = img.convert("L")
gray_img.save(input("Enter output grayscale image file path: "))
