import cv2
# 동영상의 속성 정보를 가지고 온다.
##### 동영상 속성 확인 #####

# OpenCV 비디오 속성 예시
cap = cv2.VideoCapture("./video01.mp4")
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
fps = cap.get(cv2.CAP_PROP_FPS)

print("width:", width,"height:", height)
# width: 1280.0 height: 720.0 # <- 출력을 하였을 때 이러한 값이 나오는 것을 알 수 있다.
print("fps:", fps)
print("frame_count:", frame_count)
"""
width: 1280.0 height: 720.0
fps: 25.0
frame_count: 323.0
"""
##### 동영상 파일 읽기 #####
if cap.isOpened(): # 캡쳐 객체 초기화 확인
    while True:
        ret, frame = cap.read()
        if ret : # 얘가 true일 경우
            cv2.imshow("video file show", frame)
            cv2.waitKey(25) # 25세컨드로 읽어온다.
        else:
            break
else:
    print("비디오 파일 읽기 실패")

cap.release()
cv2.destroyAllWindows() # 전부 반환하게 된다.