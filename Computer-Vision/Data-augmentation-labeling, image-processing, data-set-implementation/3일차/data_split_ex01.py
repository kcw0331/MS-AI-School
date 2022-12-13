# image data get -> train 80 val 10 test 10

# image -> cats get
# image -> dogs get
import os
import glob
import natsort # 낫소트를 사용하면 좋다.(문자와 숫자가 섞여있는 경우)
from sklearn.model_selection import train_test_split
import cv2

cat_image_path = "./image1/cats/"
dog_image_path = "./image1/dogs/"

# cat_0324

# cat 4000장
cat_image_full_path = natsort.natsorted(glob.glob(os.path.join(f"{cat_image_path}/*.jpg")))
print("cat imgae size >> ", len(cat_image_full_path)) # 숫자는 sorted를 쓰면 되는데, 문자와 숫자가 섞여있는 경우 natsort를 사용하면 좋다.

# dog 4005장 (5장 중복)
dog_image_full_path = natsort.natsorted(glob.glob(os.path.join(f"{dog_image_path}/*.jpg")))
print("dog image size >> ", len(dog_image_full_path))

# trian 80, val 20 -> val 10, test 10을 쪼개 준다
cat_train_data, cat_val_data = train_test_split(cat_image_full_path, test_size= 0.2, random_state=7777)
cat_val, cat_test = train_test_split(cat_val_data, test_size= 0.5, random_state=7777)

print(f"cat train data : {len(cat_train_data)}, cat val data : {len(cat_val)}, cat test data : {len(cat_test)}")
# cat train data : 3200, cat val data : 400, cat test data : 400

# train 80 val 20 -> val 10 test 10
dog_train_data, dog_val_data = train_test_split(dog_image_full_path, test_size=0.2, random_state=7777)
dog_val, dog_test = train_test_split(dog_val_data, test_size=0.5, random_state=7777)
print(f"dog train data : {len(dog_train_data)}, dog val data : {len(dog_val)}, dog test data : {len(dog_test)}")

# dog data save
for dog_train_path in dog_train_data:
    dog_train_img = cv2.imread(dog_train_path)
    dog_train_file_name = os.path.basename(dog_train_path)
    os.makedirs("./dataset/train/dog/", exist_ok=True)
    cv2.imwrite(f"./dataset/train/dog/{dog_train_file_name}", dog_train_img)

for dog_val_path, dog_test_path in zip(dog_val, dog_test):
    dog_val_img = cv2.imread(dog_val_path) # 각각의 이미지와 이름을 가지고 왔다.
    dog_test_img = cv2.imread(dog_test_path)
    dog_val_name = os.path.basename(dog_val_path)
    dog_test_name = os.path.basename(dog_test_path)
    os.makedirs("./dataset/val/dog/", exist_ok=True)
    os.makedirs("./dataset/test/dog/", exist_ok=True)
    cv2.imwrite(f"./dataset/val/dog/{dog_val_name}", dog_val_name)
    cv2.imwrite(f"./dataset/test/dog/{dog_test_name}", dog_test_name)

# image cv2 imread -> 저장 하는 방법 <- 우리는 이 저장하는 방식으로 해본다.
# mv copy

# if문으로 통해 flog를 사용해서 할 수 있다.
flog = False
if flog == True:
    for cat_train_data_path in cat_train_data:
        print(cat_train_data_path)
        img = cv2.imread(cat_train_data_path) # cv2를 사용해서 분할한 이미지를 저장시켜준다.
        os.makedirs("./dataset/train/cat/", exist_ok=True) # 파일이 만약에 있으면 무시를 해준다.
        file_name = os.path.basename(cat_train_data_path)
        cv2.imwrite(f"./dataset/train/cat/{file_name}", img)
        # print(file_name)

    for cat_val_path, cat_test_path in zip(cat_val, cat_test): # 크기가 동일해서 zip을 사용해준다.
        img_val = cv2.imread(cat_val_path)
        img_test = cv2.imread(cat_test_path)
        file_name_val = os.path.basename(cat_val_path)
        file_name_test = os.path.basename(cat_test_path)
        os.makedirs("./dataset/val/cat/", exist_ok=True)
        os.makedirs("./dataset/test/cat/", exist_ok=True)
        cv2.imwrite(f"./dataset/val/cat/{file_name_val}", img_val)
        cv2.imwrite(f"./dataset/test/cat/{file_name_test}", img_test)


