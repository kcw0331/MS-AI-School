# pip install petastorm
import os
import glob
import cv2
from torch.utils.data import Dataset
import time
from PIL import Image

class customDataset(Dataset):
    def __init__(self, path, transform=None):
        self.image_path = glob.glob(os.path.join(path, "*", "*.jpg"))
        self.transform = transform
        self.label_dict = {}

        for i, (category) in enumerate(os.listdir(".\\data\\train\\")):
            self.label_dict[category] = int(i)

        # self.image_list = []
        # for img_path in self.image_path:
        #     image = cv2.imread(img_path)
        #     image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        #     self.image_list.append(image)
        #
        # self.label_list = []
        # for i in self.image_path:
        #     folder_name = i.split("\\")[-2]
        #     label = self.label_dict[folder_name]
        #     self.label_list.append(label)
        # print(self.label_dic)

    def __getitem__(self, item):
        # image = self.image_list[item]
        # label = self.label_list[item]
        image_path = self.image_path[item]
        image = cv2.imread(image_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        label = image_path.split("\\")[-2]
        label = self.label_dict[label]

        if self.transform is not None:
            image = self.transform(image=image)["image"]

        return image, label

    def __len__(self):
        return len(self.image_path)

# if __name__ == "__main__":
#     # customDataset(".\\data\\train\\")
#     test = customDataset(".\\data\\train\\", transform=None)
#     for i in test:
#         pass
# 이렇게 하면 실행되는 시간을 알 수 있다.
# start = time.time()
# end = time.time()
# print(end - start)