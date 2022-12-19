from dataset_temp import custom_dataset
import albumentations as A
from albumentations.pytorch import ToTensorV2
from torch.utils.data import DataLoader
import torch

# device
# 윈도우 기반 그래픽 카드 엔비디아 사용하고 계신경우
device = torch.device("cuda" if torch.cuda.is_available else "cpu")
# m1 m2 칩셋 사용하는 경우
device = torch.device("mps:0" if torch.backends.mps.is_available() else "cpu")
# train aug
train_transform = A.Compose([ # Compose는 여러개를 묶어서 해준다.
    A.Resize(height=224, width=224),
    ToTensorV2()
])

# val aug
val_transform = A.Compose([
    A.Resize(height=224, width=224),
    ToTensorV2()
])

# dataset
train_dataset = custom_dataset("./data/train", transform=train_transform)
val_dataset = custom_dataset("./data/val", transform=val_transform)

# dataloader
train_loader = DataLoader(train_dataset, batch_size=24, shuffle=True)
val_loader = DataLoader(val_dataset, batch_size=24, shuffle=False)
# 데이터의 양에 따라서 batch_size를 정해준다.

