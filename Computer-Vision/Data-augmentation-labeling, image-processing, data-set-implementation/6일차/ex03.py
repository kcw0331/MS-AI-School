import cv2
import random
import albumentations as A

# Define a function to visualize an image

def visualize(image): # 이미지가 필요할 때 마다 가지고 올 수 있게 함수를 만들어 준다.
    cv2.imshow("visualization", image)
    cv2.waitKey(0)

# Load the image from the disk
image = cv2.imread('./weather.png')

# visualize the original image
# visualize(image)

# RandomRain
transform = A.Compose([
    # A.RandomRain(brightness_coefficient=0.7, drop_width=1, blur_value=5, p=1)
    # A.RandomSnow(brightness_coeff=2.5, snow_point_lower=0.3, snow_point_upper=0.4, p=1)
    # A.RandomSunFlare(flare_roi=(0, 0, 1, 0.5), angle_lower=0.3, p=1)
    # A.RandomShadow(num_shadows_lower=1, num_shadows_upper=1, shadow_dimension=5, shadow_roi=(0, 0.5, 1, 1) , p=1)
    A.RandomFog(fog_coef_lower=0.3, fog_coef_upper=0.8, alpha_coef=0.08, p=1)
]) # drop_width는 비의 굵기를 바꾸는 것이다.
transformed = transform(image=image)
visualize(transformed["image"])