from PIL import Image
import numpy as np

def random_img(output, width, height):

    array = np.random.randint(0,255, (height,width))  
    array = np.array(array, dtype=np.uint8)
    img = Image.fromarray(array, 'L')
    img.save(output)
    print(array)


random_img('random.png', 4, 4)