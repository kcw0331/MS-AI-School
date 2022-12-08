# 같은 크기의 이미지 블렌딩 실험
import cv2
import matplotlib.pyplot as plt
import numpy as np

large_img = cv2.imread("./ex_image.png")
watermakr = cv2.imread("./ex_image_logo.png")

# print("large_image size >>", large_img.shape)
# print("watermakr size >>", watermakr.shape)

# cv2.imshow("image show", large_img)
# cv2.imshow("water show", watermakr)
# cv2.waitKey(0)

img1 = cv2.resize(large_img, (800, 600))
img2 = cv2.resize(watermakr, (800, 600))

# print("img1 size >>", img1.shape)
# print("img2 size >>", img2.shape)
"""
large_image size >> (683, 1024, 3)
watermakr size >> (480, 640, 3)
img1 size >> (600, 800, 3)
img2 size >> (600, 800, 3)
"""

## 혼합 진행
# 베이스 5 :5
# blended = cv2.addWeighted(img1, 0.5, img2, 0.5, 0) # 비율을 5:5로 본다.
# 어떠한 이미지를 좀더 강조해서 보여줄지를 비율로 설정할 수 있다.

# 9:1
# blended = cv2.addWeighted(img1, 0.9, img2, 0.1, 0) # 비율을 5:5로 본다.

# 1로 설정 
blended = cv2.addWeighted(img1, 1, img2, 1, 0) 
# 어떠한 이미지를 좀더 강조해서 보여줄지를 비율로 설정할 수 있다.
cv2.imshow("image show", blended)
cv2.waitKey(0)
# cv2.imshow("image show", img1)
# cv2.imshow("water show", img2)
# cv2.waitKey(0)