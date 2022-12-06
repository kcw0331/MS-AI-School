import cv2
from utils import image_show

# 이미지 경로
image_path = "./cat.png"

# 이미지 이진화
image_gray = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
max_output_value = 255
neighborhood_size = 99
subtract_from_mean = 10 # 자신이 원하는 수치값으로 변경해준다.
# 평균값을 높이기 되면, 흰색의 값을 죽인다.
image_binary = cv2.adaptiveThreshold(image_gray, max_output_value,
                            cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,
                            neighborhood_size, subtract_from_mean) 
# 이진화 할때 많이 사용하는 함수이다.
image_show(image_binary)