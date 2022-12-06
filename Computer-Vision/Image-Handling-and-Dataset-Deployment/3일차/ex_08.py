import cv2
import numpy as np
from utils import image_show

image_path = "./test01.png"
image_read = cv2.imread(image_path)
image_gray = cv2.cvtColor(image_read, cv2.COLOR_BGR2GRAY)

# 감지할 모서리 개수
corners_to_detect = 4 # 몇개의 모서리를 감지할지 정해준다.(직사각형이라서 4개를 감지해준다.)
minimum_quality_score = 0.05
minimum_distance = 25

# 모서리 감지
corners = cv2.goodFeaturesToTrack(
    image_gray, corners_to_detect, minimum_quality_score, minimum_distance)
# print(corners)

for corner in corners:
    x, y = corner[0]
    cv2.circle(image_read, (int(x), int(y)), 10, (0, 255, 0), -1) 
    # 여기에서는 항상 integer로 변경해주어야 한다.

image_gray_temp = cv2.cvtColor(image_read, cv2.COLOR_BGR2GRAY)
image_show(image_gray_temp)