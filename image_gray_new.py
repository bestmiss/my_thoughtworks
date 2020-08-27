from PIL import Image
import numpy as np
#读取彩色图片
image = Image.open('image.jpg') 
#image.show() 
image_ar = np.array(image)
image_array=np.mean(image_ar, axis=2)
#灰度图
image_gray = Image.fromarray(image_array)
image_gray.show()
if image_gray.mode == "F":
    image_gray = image_gray.convert('RGB') 
image_gray.save('image_gray.jpg')