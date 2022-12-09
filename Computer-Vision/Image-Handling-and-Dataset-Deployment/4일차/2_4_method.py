'''
Gradient : detect edge (dilation - erosion)을 빼주는 방법
Tophat : original - opening -> 밝기 값이 변환하는 영역을 강조하는 것
Blackhat : closing - original -> 어두운 곳을 강조해준다.
opening : dilation * erosion -> 노이즈를 제거해준다.
closing : erosion * dilation -> 객체의 바운더리를 잘 생성해준다.
'''

import cv2
import matplotlib.pyplot as plt
import numpy as np
img = cv2.imread('./Billiards.png', cv2.IMREAD_GRAYSCALE)

_, mask = cv2.threshold(img, 230, 255, cv2.THRESH_BINARY_INV)

op_idx = {
    'gradient' : cv2.MORPH_GRADIENT,
    'tophat' : cv2.MORPH_TOPHAT,
    'blackhat' : cv2.MORPH_BLACKHAT
}

def onChange(k, op_name):
    if k == 0:
        cv2.imshow(op_name, mask)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (k, k))
    dst = cv2.morphologyEx(mask, op_idx[op_name], kernel)
    cv2.imshow(op_name, dst)

cv2.imshow('origin', img)
cv2.imshow('gradient', mask)
cv2.imshow('tophat', mask)
cv2.imshow('blackhat', mask)

cv2.createTrackbar('k', 'gradient', 0, 300, lambda x:onChange(k=x, op_name='gradient'))
cv2.createTrackbar('k', 'tophat', 0, 300, lambda x:onChange(k=x, op_name='tophat'))
cv2.createTrackbar('k', 'blackhat', 0, 300, lambda x:onChange(k=x, op_name='blackhat'))

cv2.waitKey(0)
cv2.destroyAllWindows()