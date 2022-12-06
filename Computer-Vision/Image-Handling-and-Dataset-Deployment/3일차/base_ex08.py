import cv2
import matplotlib.pyplot as plt

# image loading and input image -> gray
img = cv2.imread('./pocket.png', cv2.IMREAD_GRAYSCALE)

# 임계값 연산자의 출력을 마스크라는 변수에 저장
# 230보다 작으면 모든 값은 흰색으로 처리
# 230보다 큰면 모든 값은 검은색이 됩니다.
_, mask = cv2.threshold(img, 230, 255, cv2.THRESH_BINARY_INV) 
# 필요없는 변수는 _라고 표현해넣음

titles = ['image', 'mask'] # 이미지 바로 위에 있는 title이다.
images = [img, mask] # 이미지와 마스크 이미지를 두개 다 띄울 수 있다.

for i in range(2):
    plt.subplot(1,2, i+1),
    plt.imshow(images[i], 'gray'),
    plt.title(titles[i]),
    plt.xticks([]),
    plt.yticks([]),
plt.show()