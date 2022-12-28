# 가져온 이미지 파일의 폴더의 파일을 서치 하는 함수와 이미지를 정사각형으로 만드는 것에 대해 함수로 만듦
import os
import glob
from PIL import Image
IMAGE_FORMATS = [".jpg", ".png", ".jpeg", ".PNG", ".JPG",".PNG", ".JPEG"]

# 이미지 리사이즈 정사각형 만들기
def expand2squre(pil_image, background_color):
    width, height = pil_image.size
    if width == height:
        return pil_image
    elif width > height:
        result = Image.new(pil_image.mode, (width, width), background_color)
        result.paste(pil_image, (0, (width - height) // 2))
        return result
    else:
        result = Image.new(pil_image.mode, (height, height), background_color)
        result.paste(pil_image, (0, (height - width) // 2))
        return result

def image_file(image_folder_path):
    # 폴더에서 파일 서치 하는 함수
    all_root = []
    for (path, dir, files) in os.walk(image_folder_path):
        for filename in files:
            ext = os.path.splitext(filename)[-1]
            if ext in IMAGE_FORMATS: # 리스트 안에 있을 경우 파일 이름을 찍어와라
                root = os.path.join(path, filename)
                # print(root)
                all_root.append(root)
            else:
                print("no image file...")
                continue
            # print(ext.lower())
            # jpg jpeg png PNG JPG JPEG
    return all_root
# image_file("./dataset/train_image")