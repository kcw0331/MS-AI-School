import os
import glob
import cv2
from torch.utils.data import Dataset
from torchvision import datasets

class customdata(Dataset):
    def __init__(self, path, transform=None):
        self.all_path = glob.glob(os.path.join(path, "*", "*.png"))
        self.transform = transform

        # label
        self.label_dict = {}

        # window
        # for i, (label) in enumerate(os.listdir(("dataset\\train\\"))):
        #     label_dict[label] = int(i)

        # mac
        for i, (label) in enumerate(os.listdir("./dataset/train/")):
            self.label_dict[label] = int(i)
        print(self.label_dict)

    def __getitem__(self, item):
        # image_path
        image_path = self.all_path[item]
        # image_read
        image = cv2.imread(image_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # label
        label_temp = image_path.split("\\")[1] # --> window
        # label_temp = image_path.split("/")[3] # --> mac
        label = self.label_dict[label_temp]
        # transform
        if self.transform is not None:
            image = self.transform(image=image)["image"]
        print(image, label)
        # return image, label

    def __len__(self):
        return len(self.all_path)

test = customdata("./dataset/train/", transform=None)
for i in test:
    pass