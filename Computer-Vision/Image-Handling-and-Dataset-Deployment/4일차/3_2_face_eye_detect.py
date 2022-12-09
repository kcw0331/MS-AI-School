import cv2
import numpy as np

face_casacade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')
eye_casacade = cv2.CascadeClassifier('./haarcascade_eye.xml')

face_img = cv2.imread('./face.png')

face_gray = cv2.cvtColor(face_img, cv2.COLOR_BGR2GRAY)

faces = face_casacade.detectMultiScale(face_gray, 1.1, 4)

for (x, y, w, h) in faces:
    cv2.rectangle(face_img, (x, y), (x+w, y+h), (0, 255, 0), 3)

    roi_img = face_img[y:y+h, x:x+w].copy()
    roi_gray = face_gray[y:y+h, x:x+w].copy()
    # cv2.imshow('roi', roi_img)
    # cv2.waitKey(0)


eyes = eye_casacade.detectMultiScale(roi_gray, 1.1, 4)
# print(eyes)
'''
eyes_list = []
for roi in roi_img:
    eyes_list = eye_casacade.detectMultiScale(roi, 1.1, 4)
'''
for (x, y, w, h) in eyes:
    cv2.rectangle(roi_img, (x, y), (x+w, y+h), (0, 0, 255), 3)
cv2.imshow('eyes box', roi_img)
cv2.waitKey(0)
'''
눈을 기준으로 각도를 구해야 한다.
get eyes cor -> cal degree -> make affine metrix -> image affine transfrom
'''
cv2.imshow('face box', face_img)
cv2.waitKey(0)