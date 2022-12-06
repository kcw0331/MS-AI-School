import cv2
import numpy as np
import matplotlib.pyplot as plt

# 그레이 스케일로 바꾸어 주어야 한다.
img_gray = cv2.imread('./pocket.png', cv2.IMREAD_GRAYSCALE)
_, mask = cv2.threshold(img_gray, 230, 255, cv2.THRESH_BINARY_INV) 

# 3x3 Kernel
kernel = np.ones((3, 3), np.uint8) # 부호없는 정수로 uint8을 해준다.
# print(kernel)
'''
이 행렬을 이용해준다.
[[1 1 1]
 [1 1 1]
 [1 1 1]]
'''
dilation = cv2.dilate(mask, kernel)
titles = ['image', 'mask', 'dilation']
images = [img_gray, mask, dilation]
for i in range(3):
    plt.subplot(1, 3, i + 1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])
plt.show()