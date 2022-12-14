from utils import image_file, expand2squre
import os
from PIL import Image

train_image_path = "./dataset/train_image"
train_data = image_file(train_image_path)
print(len(train_data))
# train data 갯수 : 568개

test_image_path = "./dataset/test_image"
test_data = image_file(test_image_path)
print(len(test_data))
# test data 갯수 : 310개
train_image_resize = False # train했는데, test를 또하면 안되니깐 그걸 방지하기 위해 if문을 쓴다.
if train_image_resize == True:
    for i in train_data:
        f_name = i.split("/")[-1]
        f_name = f_name.split("\\")
        # f_name_temp = f_name[-1]
        # print(f_name_temp)
        f_name = f_name[-2]
        # print(type(f_name))
        if f_name == "0":
            img = Image.open(i)
            img_new = expand2squre(img, (0, 0, 0)).resize((400, 400))
            # 저장
            file_name = os.path.basename(i)
            file_name = file_name.split('.')
            file_name = file_name[0]
            # print(file_name)
            os.makedirs("./data/train/0/", exist_ok=True) # 이안에다가 이미지를 저장해준다.
            img_new.save(f"./data/train/0/{file_name}.png")
            # print(img_new)
        elif f_name == "1":
            img = Image.open(i)
            img_new = expand2squre(img, (0, 0, 0)).resize((400, 400))
            # 저장
            file_name = os.path.basename(i)
            file_name = file_name.split('.')
            file_name = file_name[0]
            # print(file_name)
            os.makedirs("./data/train/1/", exist_ok=True) 
            img_new.save(f"./data/train/1/{file_name}.png")
        elif f_name == "2":
            img = Image.open(i)
            img_new = expand2squre(img, (0, 0, 0)).resize((400, 400))
            # 저장
            file_name = os.path.basename(i)
            file_name = file_name.split('.')
            file_name = file_name[0]
            # print(file_name)
            os.makedirs("./data/train/2/", exist_ok=True) 
            img_new.save(f"./data/train/2/{file_name}.png")
        elif f_name == "3":
            img = Image.open(i)
            img_new = expand2squre(img, (0, 0, 0)).resize((400, 400))
            # 저장
            file_name = os.path.basename(i)
            file_name = file_name.split('.')
            file_name = file_name[0]
            # print(file_name)
            os.makedirs("./data/train/3/", exist_ok=True) 
            img_new.save(f"./data/train/3/{file_name}.png")
        elif f_name == "4":
            img = Image.open(i)
            img_new = expand2squre(img, (0, 0, 0)).resize((400, 400))
            # 저장
            file_name = os.path.basename(i)
            file_name = file_name.split('.')
            file_name = file_name[0]
            # print(file_name)
            os.makedirs("./data/train/4/", exist_ok=True) 
            img_new.save(f"./data/train/4/{file_name}.png")
        elif f_name == "5":
            img = Image.open(i)
            img_new = expand2squre(img, (0, 0, 0)).resize((400, 400))
            # 저장
            file_name = os.path.basename(i)
            file_name = file_name.split('.')
            file_name = file_name[0]
            # print(file_name)
            os.makedirs("./data/train/5/", exist_ok=True) 
            img_new.save(f"./data/train/5/{file_name}.png")
        elif f_name == "6":
            img = Image.open(i)
            img_new = expand2squre(img, (0, 0, 0)).resize((400, 400))
            # 저장
            file_name = os.path.basename(i)
            file_name = file_name.split('.')
            file_name = file_name[0]
            # print(file_name)
            os.makedirs("./data/train/6/", exist_ok=True) 
            img_new.save(f"./data/train/6/{file_name}.png")
        elif f_name == "7":
            img = Image.open(i)
            img_new = expand2squre(img, (0, 0, 0)).resize((400, 400))
            # 저장
            file_name = os.path.basename(i)
            file_name = file_name.split('.')
            file_name = file_name[0]
            # print(file_name)
            os.makedirs("./data/train/7/", exist_ok=True) 
            img_new.save(f"./data/train/7/{file_name}.png")
        elif f_name == "8":
            img = Image.open(i)
            img_new = expand2squre(img, (0, 0, 0)).resize((400, 400))
            # 저장
            file_name = os.path.basename(i)
            file_name = file_name.split('.')
            file_name = file_name[0]
            # print(file_name)
            os.makedirs("./data/train/8/", exist_ok=True) 
            img_new.save(f"./data/train/8/{file_name}.png")
        elif f_name == "9":
            img = Image.open(i)
            img_new = expand2squre(img, (0, 0, 0)).resize((400, 400))
            # 저장
            file_name = os.path.basename(i)
            file_name = file_name.split('.')
            file_name = file_name[0]
            # print(file_name)
            os.makedirs("./data/train/9/", exist_ok=True) 
            img_new.save(f"./data/train/9/{file_name}.png")

########################################################################################

test_image_resize = True # train했는데, test를 또하면 안되니깐 그걸 방지하기 위해 if문을 쓴다.
if test_image_resize == True:
    for i in test_data:
        f_name = i.split("/")[-1]
        f_name = f_name.split("\\")
        f_name = f_name[-2]
        # print(f_name)
        if f_name == "0":
            img = Image.open(i)
            img_new = expand2squre(img, (0, 0, 0)).resize((400, 400))
            # 저장
            file_name = os.path.basename(i)
            file_name = file_name.split('.')
            file_name = file_name[0]
            # print(file_name)
            os.makedirs("./data/test/0/", exist_ok=True) # 이안에다가 이미지를 저장해준다.
            img_new.save(f"./data/test/0/{file_name}.png")
            # print(img_new)
        if f_name == "1":
            img = Image.open(i)
            img_new = expand2squre(img, (0, 0, 0)).resize((400, 400))
            # 저장
            file_name = os.path.basename(i)
            file_name = file_name.split('.')
            file_name = file_name[0]
            # print(file_name)
            os.makedirs("./data/test/1/", exist_ok=True) # 이안에다가 이미지를 저장해준다.
            img_new.save(f"./data/test/1/{file_name}.png")
            # print(img_new)
        if f_name == "2":
            img = Image.open(i)
            img_new = expand2squre(img, (0, 0, 0)).resize((400, 400))
            # 저장
            file_name = os.path.basename(i)
            file_name = file_name.split('.')
            file_name = file_name[0]
            # print(file_name)
            os.makedirs("./data/test/2/", exist_ok=True) # 이안에다가 이미지를 저장해준다.
            img_new.save(f"./data/test/2/{file_name}.png")
            # print(img_new)
        if f_name == "3":
            img = Image.open(i)
            img_new = expand2squre(img, (0, 0, 0)).resize((400, 400))
            # 저장
            file_name = os.path.basename(i)
            file_name = file_name.split('.')
            file_name = file_name[0]
            # print(file_name)
            os.makedirs("./data/test/3/", exist_ok=True) # 이안에다가 이미지를 저장해준다.
            img_new.save(f"./data/test/3/{file_name}.png")
            # print(img_new)
        if f_name == "4":
            img = Image.open(i)
            img_new = expand2squre(img, (0, 0, 0)).resize((400, 400))
            # 저장
            file_name = os.path.basename(i)
            file_name = file_name.split('.')
            file_name = file_name[0]
            # print(file_name)
            os.makedirs("./data/test/4/", exist_ok=True) # 이안에다가 이미지를 저장해준다.
            img_new.save(f"./data/test/4/{file_name}.png")
            # print(img_new)
        if f_name == "5":
            img = Image.open(i)
            img_new = expand2squre(img, (0, 0, 0)).resize((400, 400))
            # 저장
            file_name = os.path.basename(i)
            file_name = file_name.split('.')
            file_name = file_name[0]
            # print(file_name)
            os.makedirs("./data/test/5/", exist_ok=True) # 이안에다가 이미지를 저장해준다.
            img_new.save(f"./data/test/5/{file_name}.png")
            # print(img_new)
        if f_name == "6":
            img = Image.open(i)
            img_new = expand2squre(img, (0, 0, 0)).resize((400, 400))
            # 저장
            file_name = os.path.basename(i)
            file_name = file_name.split('.')
            file_name = file_name[0]
            # print(file_name)
            os.makedirs("./data/test/6/", exist_ok=True) # 이안에다가 이미지를 저장해준다.
            img_new.save(f"./data/test/6/{file_name}.png")
            # print(img_new)
        if f_name == "7":
            img = Image.open(i)
            img_new = expand2squre(img, (0, 0, 0)).resize((400, 400))
            # 저장
            file_name = os.path.basename(i)
            file_name = file_name.split('.')
            file_name = file_name[0]
            # print(file_name)
            os.makedirs("./data/test/7/", exist_ok=True) # 이안에다가 이미지를 저장해준다.
            img_new.save(f"./data/test/7/{file_name}.png")
            # print(img_new)
        if f_name == "8":
            img = Image.open(i)
            img_new = expand2squre(img, (0, 0, 0)).resize((400, 400))
            # 저장
            file_name = os.path.basename(i)
            file_name = file_name.split('.')
            file_name = file_name[0]
            # print(file_name)
            os.makedirs("./data/test/8/", exist_ok=True) # 이안에다가 이미지를 저장해준다.
            img_new.save(f"./data/test/8/{file_name}.png")
            # print(img_new)
        if f_name == "9":
            img = Image.open(i)
            img_new = expand2squre(img, (0, 0, 0)).resize((400, 400))
            # 저장
            file_name = os.path.basename(i)
            file_name = file_name.split('.')
            file_name = file_name[0]
            # print(file_name)
            os.makedirs("./data/test/9/", exist_ok=True) # 이안에다가 이미지를 저장해준다.
            img_new.save(f"./data/test/9/{file_name}.png")
            # print(img_new)