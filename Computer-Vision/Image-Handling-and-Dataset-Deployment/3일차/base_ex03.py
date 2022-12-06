import cv2
import numpy as np
from utils import image_show

image = cv2.imread('./car.png')

# Creating out charpening filter
filter = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])

sharpen_img = cv2.filter2D(image, -1, filter) # 영상의 같은 depth를 해준다.
# cv2.imshow("org image", image)
# cv2.waitKey(0)
# 바로 위에 주석 처리 한것은 원본이미지와 
# 필터된 이미지를 비교하기 위해 작성한것이다.
image_show(sharpen_img)