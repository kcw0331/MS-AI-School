'''
opening : erosion -> dilation (to delete dot noise)
점을 없애는 데 사용한다.
'''

import cv2
import matplotlib.pyplot as plt
import numpy as np
img = cv2.imread('./Billiards.png', cv2.IMREAD_GRAYSCALE)

_, mask = cv2.threshold(img, 230, 255, cv2.THRESH_BINARY_INV)

# datatype : int, float
# 파이썬에서는 int와 float는 제한이 없다.
kernel = np.ones((3, 3), np.uint8) 
# 넘파이 내부에 데이터 타입이 있다.(unit8은 음의 값이 없는 것이다.)

N = 5
idx = 1
for i in range(1, N):
    erosion = cv2.erode(mask, kernel, iterations = i)
    opening = cv2.dilate(erosion, kernel, iterations = i)
    f_opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations = i)
    plt.subplot(N, 2, idx)
    idx += 1
    plt.imshow(opening, 'gray')
    plt.title(f'{i}manual opening')


    plt.subplot(N, 2, idx)
    plt.imshow(f_opening, 'gray')
    plt.title(f'{i}functions opening')
    idx += 1
plt.tight_layout()
plt.show()