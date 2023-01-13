# 얼굴을 분류하는 데이터를 만들었다.
# 이 부분에서는 이미지와 라벨을 만들어 주었다.
from torch.utils.data import Dataset
import os
import glob
import cv2


class customDataset(Dataset):
    def __init__(self, path, transform=None):
        ## path -> ./dataset/train
        self.all_image_path = glob.glob(os.path.join(path, "*", "*.png"))
        self.transform = transform

        ## label dict
        self.category_dict = {}
        for index, label_name in enumerate(sorted(glob.glob(os.path.join(path, "*")))):
            # sorted(os.listdir(path))를 사용해도 된다.
            self.category_dict[label_name.split("\\")[-1]] = int(index)

    def __getitem__(self, item):
        # 1. Reading image
        image_path = self.all_image_path[item]
        image = cv2.imread(image_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # 2. class label
        folder_name = image_path.split("\\")
        folder_name = folder_name[-2]
        label = self.category_dict[folder_name]

        # 3. Applying transforms on image
        if self.transform is not None:
            image = self.transform(image=image)["image"]

        return image, label  # 다른 정보를 사용할 때, image, label과 다른 메타정보도 가지고 올 수 있다.

    def __len__(self):
        return len(self.all_image_path)  # 전체 길이가 반환되도록 해준다.

# my_dataset("D:\\dataset\\train\\")

# test = customDataset("D:\\dataset\\train\\", transform=None)
# for i in test:
#     pass

# if __name_ == "__main__":
#     test = my_dataset("D:\\dataset\\train\\", transform=None)
#     for i in test:
#         pass