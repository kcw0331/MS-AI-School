from torch.utils.data.dataset import Dataset
from torchvision import transfroms
label_dic = {"cat" : 0, "dog" : 1}

# 클래스를 만들고 상속을 받아준다.
class MyCustomDataset(Dataset):
    def __init__(self, path, transfroms = None):
        # data path
        self.all_data_path = "./image/*.jpg"
        # pass # 에러 안나게 하려고 pass를 써준다.

    def __getitem__(self, index) : # getitem에서는 return해줘야한다.
        image_path = self.all_data_path[index] # index를 랜덤하게 뽑는다.
        # "image01.pnd, image02.png, image03.png, ..."
        label_temp = image_path.split("\\")
        label_temp = label_temp[2]
        label_temp = label_temp.replace(".jpg","")
        label = label_dic[label_temp]
        # cat -> 0
        # [. , image , cat.jpg]
        # image read
        image = cv2.imread(image_path) # read된 이미지가 return된다.
        
        if self.transforms is not None:
            image = self.transforms(image)

        # augmentation
        # image, label = 0
        # return filename, bbox # <- 이렇게 해서 만들고 위에도 지금은 이미지인데 뼈대도 바꾸어야 한다.
        return image, label

    def __len__(self) :
        return len(self.all_data_path) # 마지막에 몇개인지 출력해주었다.

temp = MyCustomDataset("./dataset")

for i in temp: # 어제 했던 csv파일로 출력을 해서 스크린 샷을 찍으면된다.
    print(i)
    # image01 x y w h 이렇게 출력이된다.


