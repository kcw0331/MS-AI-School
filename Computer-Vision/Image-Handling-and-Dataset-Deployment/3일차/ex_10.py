import cv2
from utils import image_show
import numpy as np

iamge_path = './cat.png'
image = cv2.imread(iamge_path)
# image 10x10 픽셀 크기로 변환
image_color_10x10 = cv2.resize(image, (10, 10))
image_color_10x10.flatten()
# print("image_shpae_info", image_shpae_info)

image_show(image_color_10x10)

# image 255x255 픽셀 크기로 변환
image_color_255x255 = cv2.resize(image, (255, 255))
image_color_255x255.flatten()
image_show(image_color_255x255)

#-----------------------------------------------------------------
# flatten에 대해 이해하기 위해 간단한 예제를 돌려본다.
x = np.array([[51, 20], [14, 19], [10, 7]])
x = x.flatten()
# [51, 40, 14, 19, 10, 7]
print(x)
'''
결과 [51 20 14 19 10  7]
'''