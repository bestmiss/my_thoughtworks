from PIL import Image
import numpy as np
#读取彩色图片
image = Image.open('image.jpg')
image.show()
image_array = np.array(image)
#灰度图
image1 = Image.fromarray(image_array)
image1.show()

