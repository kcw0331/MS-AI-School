# 가우시안 블러
# 야간에 사용하는 것은 별로
import cv2
from utils import image_show # 이미지를 보기 위해 image_show를 불러온다.

image_path = "./cat.png"
#이미지 읽기
image = cv2.imread(image_path)

image_g_blur = cv2.GaussianBlur(image, (15, 15), 0) # 시그마는 0으로 지정한다.
image_show(image_g_blur)