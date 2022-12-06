import cv2 
import  matplotlib.pyplot as plt # 두개의 변경된 이미지를 보기 위해서 matplot을 본다.

image_path = "./cat.png"

"""# 흑백 이미지 대비 높이기 page 114
image_gray = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE) # 이미지가 그레이로 변한다.
image_enhanced = cv2.equalizeHist(image_gray)

# plot
fig, ax = plt.subplots(1, 2, figsize = (10, 5))
ax[0].imshow(image_gray, cmap='gray')
ax[0].set_title("Original Image")
ax[1].imshow(image_enhanced, cmap='gray')
ax[1].set_title("Enhanced Image")
plt.show()
# 흑백 이미지 대비 높이기"""

#------------------------------------------------------------------------------------

# 컬러 이미지 대비 높이기
# 방법 : RGB -> YUV 컬러 포맷으로 변환 -> equalizeHist() -> RGB
# BGR <- matplot으로 하게 되면 BGR로 되어 있는 경우가 많다.
image_bar = cv2.imread(image_path)

# RGB
image_rgb = cv2.cvtColor(image_bar, cv2.COLOR_BGR2RGB)

# YUV
image_yuv = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2YUV)

# 히스토그램 평활화 적용
image_yuv[:, :, 0] = cv2.equalizeHist(image_yuv[:, :, 0])

# RGB 변경
image_rgb_temp = cv2.cvtColor(image_yuv, cv2.COLOR_YUV2RGB)

# plot
fig, ax = plt.subplots(1, 2, figsize=(12, 8))
ax[0].imshow(image_rgb)
ax[0].set_title("Original Image")
ax[1].imshow(image_rgb_temp)
ax[1].set_title("Enhanced Image")
plt.show()