import cv2
import numpy as np
import matplotlib.pyplot as plt

img_gray = cv2.imread('./pocket.png', cv2.IMREAD_GRAYSCALE)
_, mask = cv2.threshold(img_gray, 230, 255, cv2.THRESH_BINARY_INV) 

kernel = np.ones((3, 3), np.uint8)
dilation = cv2.dilate(mask, kernel, iterations = 10)

titles = ['image', 'mask', 'dilation'] # 3개의 타이틀을 본다.
images = [img_gray, mask, dilation]

for i in range(3):
    plt.subplot(1, 3, i + 1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i]) 
    plt.xticks([]) # x, y축을 없앤 것이다.
    plt.yticks([])
plt.show()
