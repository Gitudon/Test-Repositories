from PIL import Image
import numpy as np


def image_to_array(image_path):
    with Image.open(image_path) as img:
        return np.array(img)


image_path = "test.jpg"
print(image_to_array(image_path))
