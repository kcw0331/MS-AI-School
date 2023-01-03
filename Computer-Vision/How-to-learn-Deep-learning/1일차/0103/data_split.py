import matplotlib.pyplot as plt
import glob
import os
from sklearn.model_selection import train_test_split
import cv2
# 처음 보는 데이터라서 데이터의 분포가 어떻게 되는지 보아야 한다.
# data_dir = "./dataset"

# 함수로 만들어 보았다.
def data_size_show(data_dir):
    x_plt = []
    y_plt = []

    for directory in os.listdir(data_dir):
        # print(directory)
        x_plt.append(directory) # x축에는 폴더 명이 들어간다.
        y_plt.append(len(os.listdir(os.path.join(data_dir, directory)))) # y축은 해당하는 폴더의 이미지 개수

    # creating the bar plot
    flg, ax = plt.subplots(figsize = (16, 16))
    plt.barh(x_plt, y_plt, color="maroon")

    # remove x, y Ticks
    ax.xaxis.set_ticks_position("none") # 눈끔선을 없앤다.
    ax.yaxis.set_ticks_position("none")

    # add padding between axes and labels
    ax.xaxis.set_tick_params(pad = 5)
    ax.yaxis.set_tick_params(pad = 10)

    # show to values
    ax.invert_yaxis()

    plt.ylabel('Bark Type')
    plt.xlabel('No. of images')
    plt.title("Bark Texture Dataset")
    plt.show()

# data_dir = "./dataset"
# data_size_show(data_dir)

"""
데이터를 나누는 작업을 진행한다.
8 : 1 : 1
data
    train
        - label folder
            - image.png
    val
        - label folder
            - image.png
    test
        - label folder
            - image.png
"""
def data_split(name):
    image_path = f".\\dataset\\{name}"
    image = glob.glob(os.path.join(image_path, "*.JPG"))

    train_list, val_list = train_test_split(image, test_size=0.2, random_state=777)
    val_data, test_data = train_test_split(val_list, test_size=0.5, random_state=777)
    # print(len(acacia_train_list), len(acacia_val_data), len(acacia_test_data))

    return train_list, val_data, test_data

def data_save(data, mode):
    for path in data:
        # 0. 폴더명 구하기
        folder_name = path.split("\\")[2]

        # 1. 폴더 구성
        folder_path = f".\\data\\{mode}\\{folder_name}"
        os.makedirs(folder_path, exist_ok=True)

        # 2. 이미지 이름 구하기
        image_name = path.split("\\")[-1]
        image_name = image_name.split(".")[0]

        # 4. 이미지 읽기
        img = cv2.imread(path)

        # 5. 이미지 저장
        # print(os.path.join(folder_path, image_name + ".jpg"))
        cv2.imwrite(os.path.join(folder_path, image_name + ".jpg"), img)
        # print(folder_name)
    print("작성 완료")

list = []
data = glob.glob(os.path.join(".\\dataset\\", "*"))
for path in data:
    list.append(os.path.basename(path))
print(list)

for i in list:
    train_list, val_data, test_data = data_split(name=i)

    print(i,"의 개수", "train 개수=", len(train_list), "val 개수=", len(val_data), "test 개수=", len(test_data))
    print()
    print(f"{i} 첫번째 실행")
    data_save(train_list, mode = "train")
    print()
    print(f"{i} 두번째 실행")
    data_save(val_data, mode = "val")
    print()
    print(f"{i }세번째 실행")
    data_save(test_data, mode = "test")
    print()