from PIL import ImageEnhance
import numpy as np
import math

ASCII_CHARS = "@.'`^\",:;Il!i~+_-?][}{1)(|\\/*tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B$"
print("len of ascii: ", len(ASCII_CHARS))

def image_to_ascii(image, new_width=100):
    image = image.convert("L")
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(1.3)
    
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(aspect_ratio * new_width * 0.7)

    image = image.resize((new_width, new_height))
    pixels = np.array(image)

    ascii_str = ""

    for row in pixels:
        for pixel in row:
            index = math.ceil(pixel * (len(ASCII_CHARS) - 1) / 255)
            ascii_str += ASCII_CHARS[index]
        ascii_str += "\n"

    return ascii_str
