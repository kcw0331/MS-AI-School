import glob
import os
import torch
import cv2
from torch.utils.data import Dataset
from albumentations.pytorch import ToTensorV2
import albumentations as A # 이미지를 회전시킬 것을 가져온다.
import numpy as np
# from torchvision.transforms import transforms
# pip install albumentations==1.2.1

# 시드를 고정시켜주는 방법
# random_seed =44444
# torch.manual_seed(random_seed)
# torch.cuda.manual_seed(random_seed)
# torch.cuda.manual_seed_all(random_seed) # if use multi-GPU
# torch.backends.cudnn.deterministic = True
# torch.backends.cudnn.benchmark = False
# np.random.seed(random_seed)
# random.seed(random_seed)

class customDataset(Dataset):
    def __init__(self, img_path, transform=None):
        # dataset / train / * / *.jpg
        self.all_img_path = glob.glob(os.path.join(img_path, "*", "*.jpg"))
        self.class_names = os.listdir(img_path) # 디렉토리에 있는 모든 파일을 리스트로 만든다.
        self.class_names.sort() # 리스트로 만든 것을 정렬
        self.transform = transform
        self.all_img_path.sort() # 이미지들을 정령
        self.labels = [] # label값을 넣어준기 위해 list 생성

        for path in self.all_img_path:
            self.labels.append(self.class_names.index(path.split("\\")[-2])) # 카드 이름의 폴더의 이름을 가져옴
        self.labels = np.array(self.labels) # 가져온 카드 이름을 labels 리스트에 append
        # print(self.labels)

    def __getitem__(self, item):
        image_path = self.all_img_path[item]
        image = cv2.imread(image_path)
        label = self.labels[item]
        label = torch.tensor(label) # 라벨을 tensor로 변환(라벨은 숫자 형태여야 한다.)
        if self.transform is not None:
            image = self.transform(image=image)["image"]

        return image, label

        # print(image_path, label)

    def __len__(self):
        return len(self.all_img_path)

# test = customDataset("C:\\Users\\labadmin\\Downloads\\dataset\\train", transform=None)
#
# for i in test:
#     pass