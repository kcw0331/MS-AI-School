# 1. 얼굴 및 눈 감지를 위해 OpenCV Haar캐스케이스 구성을 사용한다.
import cv2
import numpy as np
# haarcascade의 정명 얼굴 감지 및 눈 감지 모듈을 사용한다.
# 얼굴과 눈이 감지된 것을 저장해준다.
face_cascade = cv2.CascadeClassifier("./haarcascade_frontalface_default.xml" )
eye_cascade = cv2.CascadeClassifier("./haarcascade_eye.xml")

#-------------------------------------------------------------------------------------------------------------------------------------------------------------#
# 2. 얼굴 이미지 데이터를 읽어온다.
img = cv2.imread("./face.png")

# 원본 얼굴 이미지 출력
# print(img.shape)
# cv2.imshow("image show", img)
# cv2.waitKey(0)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------#
# 3. 얼굴 이미지 바운딩 박스
# 케스케이드 경우는 그레이 스케일 이미지에서만 작동
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.1, 4) # <- 그레이 이미지에서 얼굴을 인식

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3) # 3은 얼굴영역에 표시하는 선의 굵기 조정

# 얼굴의 영역을 출력
# cv2.imshow("face", img)
# cv2.waitKey(0)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------#
# 4. 눈과 얼굴 이미지 바운딩 박스
# 눈을 감지할 회색조 이미지 첫번쨰 영역이 필요하고 두번째 영역은 사각형을 그릴 컬러 이미지가 필요
roi_gray = gray[y:(y+h), x:(x+w)] # <- 회색조 이미지의 얼굴영역을 잡아준다.
roi_color = img[y:(y+h), x:(x+w)] # <- 컬러 이미지의 얼굴영역을 잡아준다.

eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 4) # <- 그레이 이미지의 얼굴영역에서 눈을 인식, 그리고 eyes에 왼쪽눈과 오른쪽눈의 영역이 리스트로 되어있음.
'''
[[ 41 82 45 45]
 [112 48 52 52]]
'''
index = 0

# for 루프문을 만들어서 첫 번째 눈과 두 번째 눈의 좌표를 eye_1와 eye_2에 저장
for (ex, ey, ew, eh) in eyes: # 눈의 좌표를 ex, xy, ew, eh로 만들어서 for루프를 돌려준다.
    if index == 0:
        eye_1 = (ex, ey, ew, eh) # 왼쪽눈의 영역
    elif index == 1:
        eye_2 = (ex, ey, ew, eh) # 오른쪽눈의 영역
    cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 0, 255), 3)
    index = index + 1 # index를 사용해서 왼쪽눈과 오른쪽눈의 영역을 저장해주었다.

# 눈과 얼굴의 영역을 출력
# cv2.imshow("face", img)
# cv2.waitKey(0)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------#
# 5. 두 눈의 중심점 사이에 선을 그어본다.
if eye_1[0] < eye_2[0]: # eye_1의 x축이 eye_2의 x축보다 작으면 왼쪽눈 아니면 오른쪽눈
    left_eye = eye_1
    right_eye = eye_2
else:                  # 반대의 경우는 오른쪽눈 아니면 왼쪽눈
    left_eye = eye_2
    right_eye = eye_1

"""(41, 82, 45, 45)
(112, 48, 52, 52)"""

# 사각형의 중심점의 조정된 부분을 계산해준다.
# 왼쪽눈의 중심을 찾아준다.
left_eye_center = (int(left_eye[0] + (left_eye[2] / 2)), int(left_eye[1] + (left_eye[3] / 2)))
left_eye_center_x = left_eye_center[0]
left_eye_center_y = left_eye_center[1]
# 오른쪽눈의 중심을 찾아준다.
right_eye_center = (int(right_eye[0] + (right_eye[2] / 2)), int(right_eye[1] + (right_eye[3] / 2)))
right_eye_center_x = right_eye_center[0]
right_eye_center_y = right_eye_center[1]
# 0번째 인덱스: x 좌표, 1번째 인덱스: y좌표, 3번째 인덱스: 사각형의 너비, 4번째 인덱스: 사각형의 높이
cv2.circle(roi_color, left_eye_center, 5, (255, 0, 0), -1) # left_eye_center는 튜플이다. 그리고 -1로 하면 안채워진다.
cv2.circle(roi_color, right_eye_center, 5, (255, 0, 0), -1)
cv2.line(roi_color, right_eye_center, left_eye_center, (0, 200, 200), 3) # <- 왼쪽눈의 중심과 오른쪽눈의 중심을 노란색선으로 연결

# cv2.imshow("face", img) # cv2로 읽어 왔기 때문에 img에 적용을 시켜주지 않아도 적용이 되는 건가?
# cv2.waitKey(0)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------#
# 6. 수평선을 그리고 그 선과 눈의 중심점을 연결하는 선 사이의 각도를 계산
# 최종 목적 -> 각도를 기준으로 이미지를 회전
if left_eye_center_y > right_eye_center_y:
    A = (right_eye_center_x, left_eye_center_y)
    # 정수 -1은 이미지가 시계방향으로 회전하는 것을 나타낸다.
    direction = -1
else:
    A = (left_eye_center_x, right_eye_center_y)
    # 정수 1은 이미지가 반시계방향으로 회전하는 것을 나타낸다.
    direction = 1

cv2.circle(roi_color, A, 5, (255, 0, 0), -1)

cv2.line(roi_color, right_eye_center, left_eye_center, (0, 200, 200), 3)
cv2.line(roi_color, left_eye_center, A, (0, 200, 200), 3)
cv2.line(roi_color, right_eye_center, A, (0, 200, 200), 3)

# cv2.imshow("face", img)
# cv2.waitKey(0)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------#
# 7. 직각 삼각형의 두 변의 길이를 찾아준다.
# 각도 구하기
# np.arctan = 함수 단위는 라디안 단위
# 라디안 단위 -> 각도 : (theta * 180) / np.pi

delta_x = right_eye_center_x - left_eye_center_x
delta_y = right_eye_center_y - left_eye_center_y
angle = np.arctan(delta_y / delta_x) # <- 라디안 단위로 나오게 된다.
angle = (angle * 180) / np.pi # <- 180을 곱하고 파이를 나누게 되면 각도가 나오게 된다.
print(angle)
# 결과 -21.80140948635181도
# cv2.imshow('face', img)
# cv2.waitKey(0)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------#
# 8. 이미지를 각도 만큼 회전
# 약을 식별하는 이미지를 정렬할 때, 사용하기도 한다.
h, w = img.shape[:2] # 슬라이싱을 사용해서 두개만 사용한다.
center = (w // 2, h // 2)
M = cv2.getRotationMatrix2D(center, (angle), 1.0)
rotated = cv2.warpAffine(img, M, (w, h))
cv2.imshow("face", rotated)
cv2.waitKey(0)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------#