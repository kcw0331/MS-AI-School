import cv2

# 이미지 경로
image_path ="./cat.png"

# 이미지 읽기
image = cv2.imread(image_path)

"""img90 = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE) # 시계 방향으로 90도 회전
img180 = cv2.rotate(image, cv2.ROTATE_180) # 180도 회전
img270 = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE) 
# 반시계 방향으로 90도 회전 = 270도 회전

cv2.imshow("Original image", image)
cv2.imshow("Rotate90 image", img90)
cv2.imshow("Rotate180 image", img180)
cv2.imshow("Rotate270 image", img270)

cv2.waitKey(0)"""

# 이미지 좌우 및 상하 반전
# 1은 좌우 반전, 0은 상하 반전
dst_temp1 = cv2.flip(image, 1)
dst_temp2 = cv2.flip(image, 0)

cv2.imshow("dst_temp1", dst_temp1)
cv2.imshow("dst_temp2", dst_temp2)
cv2.waitKey(0)