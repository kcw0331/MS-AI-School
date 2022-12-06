import cv2
from utils import image_show

iamge_path = './cat.png'
image_gray = cv2.imread(iamge_path, cv2.IMREAD_GRAYSCALE)
# imread하면서 그레이 이미지로 변경을 해주었다.

image_10x10 = cv2.resize(image_gray, (10, 10)) 
image_10x10.flatten() # 이미지 데이터를 1차원 벡터로 변환을 해준다.
image_show(image_10x10)