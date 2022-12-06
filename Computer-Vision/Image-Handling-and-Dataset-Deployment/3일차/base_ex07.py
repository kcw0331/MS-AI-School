import cv2
import numpy as np
from utils import image_show

image_path = './car.png'
img = cv2.imread(image_path)

# 엠보싱 효과
# 엠보싱 필터 1과 엠보싱 필터2이다.
filter1 = np.array([[0, 1, 0], [0, 0, 0], [0, -1, 0]])
filter2 = np.array([[-1, -1, 0], [-1, 0, 1], [0, 1, 1]])
# 엠보싱에 대해서 2D필터에 적용해준다.
emboss_img = cv2.filter2D(img, -1, filter2)
emboss_img += 128 # 128을 사용해서 회색으로 만들어 준다.
image_show(emboss_img)