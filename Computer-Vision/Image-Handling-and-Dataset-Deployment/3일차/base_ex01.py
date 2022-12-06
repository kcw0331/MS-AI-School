# 기본적인 이미지 처리 기술을 이용한 이미지 선명화 -1
import cv2
import numpy as np

img = cv2.imread('./car.png', 0) # 흑백으로 이미지를 가져와 준다.
# print(img.shape) # -> (640, 960)

blurred_1 = np.hstack([
    cv2.blur(img, (3, 3)),
    cv2.blur(img, (5, 5)),
    cv2.blur(img, (9, 9))])
cv2.imshow("show", blurred_1)
cv2.imwrite("./blur.png", blurred_1) # 저장을 해준다. 가우시안 블러랑 어떠한 차이가 있는지 보려고
cv2.waitKey(0)