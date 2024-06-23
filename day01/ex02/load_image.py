import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image
import numpy as np

def ft_load(path: str)-> list:
    with Image.open(path) as img:
        image_rgb = img.convert('RGB')
        image_array = np.array(image_rgb)
    image = mpimg.imread(path)
    # plt.imshow(image)
    # plt.axis('off') 
    # plt.show()
    print(f'The shape of image is: {image.shape}')
    print(f"{image_array}")
    return image








