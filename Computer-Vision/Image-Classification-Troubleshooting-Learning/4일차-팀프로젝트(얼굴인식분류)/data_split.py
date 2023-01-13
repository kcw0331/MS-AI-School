import os
import glob
import cv2
import random
import shutil
# C드라이브의 용량이 부족하여 날릴 것을 고려하면 D 드라이브에 생성함
"""
# 꼭 사진 폴더 안에 .db파일 제거 
os.makedirs("D:/dataset/" + "m70", exist_ok=True) # <- 여기 에서 나이를 변경
os.makedirs("D:/dataset/" + "w70", exist_ok=True) # <- 여기 에서 나이를 변경

folder_name_m = "D:/dataset/" + "m70" # <- 여기 에서 나이를 변경
folder_name_w = "D:/dataset/" + "w70" # <- 여기 에서 나이를 변경

age20 = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
age30 = [30, 31, 32, 33, 34, 35, 36, 37, 38, 39]
age40 = [40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
age50 = [50, 51, 52, 53, 54, 55, 56, 57, 58, 59]
age60 = [60, 61, 62, 63, 64, 65, 66, 67, 68, 69]
age70 = [70, 71, 72, 73, 74, 75]

for i in age70: # <- 여기 에서 나이를 변경
    i = str(i)
    path_man = '.\\AFAD-Full\\'+ "{}".format(i) +'\\111'
    path_woman = '.\\AFAD-Full\\' + "{}".format(i) + '\\112'

    for index1, path1 in enumerate(glob.glob(os.path.join(path_man,"*"))):
        image_name1 = path1.split("\\")[-1]
        image_name1 = image_name1.split(".")[0]
        img1 = cv2.imread(path1)
        cv2.imwrite(os.path.join(folder_name_m, image_name1 + ".png"), img1)
    print("남자 끝")
    for index2, path2 in enumerate(glob.glob(os.path.join(path_woman,"*"))):
        image_name2 = path2.split("\\")[-1]
        image_name2 = image_name2.split(".")[0]
        img2 = cv2.imread(path2)
        cv2.imwrite(os.path.join(folder_name_w, image_name2 + ".png"), img2)
    print("여자 끝")
"""

# 위에서는 폴더 이름 dataset이라고 해 놓았는데, 아래 꺼 실행하려면 데이터 폴더 이름을 data라고 해야함.
# 위에꺼 주석 처리 후 아래 꺼 실행해야 함.
def create_train_val_split_folder(path):
    all_categories = os.listdir(path)
    # print("all categories >>", all_categories)
    # 빈 폴더를 생성해준다.
    os.makedirs("D:/dataset/train", exist_ok=True)
    os.makedirs("D:/dataset/val", exist_ok=True)

    # train 데이터 생성후 이미지 이동
    for category in sorted(all_categories):  # 카테고리를 정렬하면서 for문 실행
        os.makedirs(f"D:/dataset/train/{category}", exist_ok=True)  # 해당하는 카테고리로 빈 폴더생성
        all_image = os.listdir(f"D:/data/{category}/")  # 해당 카테고리의 모든 이미지 추출(리스트로 되어있음)
        # print("all_image >>", all_image)
        for image in random.sample(all_image, int(0.875 * len(all_image))):  # train에 랜덤으로 90% 이미지 추출
            # origin dataset, new dataset
            shutil.move(f"D:/data/{category}/{image}", f"D:/dataset/train/{category}/")  # move를 사용하여 이전 폴더에서 새로운 폴더로 이동

    # val 데이터 생성 후 이미지 이동 (train에서 하던거 반복)
    for category in sorted(all_categories):
        os.makedirs(f"D:/dataset/val/{category}", exist_ok=True)
        all_image = os.listdir((f"D:/data/{category}"))
        for image in all_image:  # train으로 이미 이미지 이동하여 random없이 이미지 이동
            shutil.move(f"D:/data/{category}/{image}", f"D:/dataset/val/{category}/")

#
# if __name__ == "__main__":
#     path = "D:/data/"
#     # image_size(path)
#     create_train_val_split_folder(path)