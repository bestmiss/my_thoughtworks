import unittest
import requests
from PIL import Image
from io import BytesIO
import matplotlib.pyplot


class SimpleImageDownloaderTest(unittest.TestCase):

    def test_download_image(self):

        response = requests.get('https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png')

        image = Image.open(BytesIO(response.content))

        matplotlib.pyplot.imshow(image)
     

if __name__ == '__main__':

    unittest.main()