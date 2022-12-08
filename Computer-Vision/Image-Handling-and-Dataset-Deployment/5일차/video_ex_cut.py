import cv2
import os
video_file_path = "./video01.mp4"

# 동영상 캡처 객체 생성
# r
cap = cv2.VideoCapture(video_file_path)

fps = cap.get(cv2.CAP_PROP_FPS) # 필요한 fps를 가져올 수 있다.
print("fps >>", fps)
count = 0
if cap.isOpened():
    while True:
        ret, frame = cap.read()  # while문을 돌면서 사진을 한장한장 가져온다.
        if ret:
            if (int(cap.get(1)) % fps == 0): # fps 값을 사용하여 1초마다 추출, 나머지가 없을 때, 저장을 해준다.
                os.makedirs("./frame_image_save", exist_ok=True) # <- 이거는 알아두면 좋다 많이 사용한다. exist_ok를 True로 하게 되면 생성되어 있으면 무시하라는 것이다.
                cv2.imwrite("./frame_image_save/" + "frame%d.jpg" % count, frame) # 맨 마지막 이미지를 저장하지 않게 해준다.
                print("save frame number >> ",str(int(cap.get(1))))
                count += 1
        else:
            break # 아니라면 break를 시켜줌
else : print("비디오 열기 실패")
cap.release()
cv2.destroyAllWindows()