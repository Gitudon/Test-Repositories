from PIL import Image

original_image = input("Input original image's path: ")
image = Image.open(original_image)

mirrored_image = image.transpose(Image.FLIP_LEFT_RIGHT)
mirrored_image_path = "mirrored_image.jpg"
mirrored_image.save(mirrored_image_path)
Image.open(mirrored_image_path)
