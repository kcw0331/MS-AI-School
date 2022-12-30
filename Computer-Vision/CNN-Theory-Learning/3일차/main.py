import copy
import os
import torch
import torch.optim as optim
import torch.nn as nn
import torchvision.models as models
import albumentations as A
from albumentations.pytorch import ToTensorV2
import matplotlib.pyplot as plt
from torch.utils.data import DataLoader
from customdataset import customDataset # 우리가 만든 데이터셋을 가져온다.
import argparse
from timm.loss import LabelSmoothingCrossEntropy # Loss를 이걸 사용해준다. 이게 성능이 좀더 잘 나온다고 하심.
from adamp import AdamP # 이 아담을 사용한다.
from utils import train

def main(opt):

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    # main에서는 augmentaion, dataset, dataloader를 만들어야 되겠다하고 생각하고 만들면 될거 같다.
    # augmentaion
    train_transform = A.Compose([
        A.SmallestMaxSize(max_size=160),
        A.ShiftScaleRotate(shift_limit=0.05, scale_limit=0.05, rotate_limit=15, p=0.8),
        A.RGBShift(r_shift_limit=15, g_shift_limit=15, b_shift_limit=15, p=0.7),
        A.RandomBrightnessContrast(p=0.5),
        # A.Normalize(mean=(0.5, 0.5, 0.5), std=(0.2, 0.2, 0.2)), # <- 귀찮으면 이렇게 하면된다.
        A.RandomShadow(p=0.5),
        A.Normalize(mean=(0.485, 0.456, 0.406), std=(0.229, 0.224, 0.225)),
        ToTensorV2()  # <- 항상 마지막에는 이걸 넣어준다.
    ])

    # val에는 랜덤하지 않은 것만 넣어줄 수 있다.
    # 왜냐하면 테스트일 때는 랜덤 확률을 빼주어야 한다.
    val_transform = A.Compose([
        A.SmallestMaxSize(max_size=160),
        A.Normalize(mean=(0.485, 0.456, 0.406), std=(0.229, 0.224, 0.225)),
        ToTensorV2()
    ])

    # dataset
    # 테스트 데이터 셋 같은 경우 val하고 똑같기 때문에 만들어 둔 val_transform을 사용하면된다.
    train_dataset = customDataset(img_path=opt.train_path, transform=train_transform)
    val_dataset = customDataset(img_path=opt.val_path, transform=val_transform)

    # dataloader
    # 데이터로더는 인자 값으로 train_dataset을 넣어도 동작은 한다.
    train_loader = DataLoader(train_dataset, batch_size=opt.batch_size, shuffle=True)
    val_loader = DataLoader(val_dataset, batch_size=opt.batch_size, shuffle=False)

    # model call
    # train -> label -> 53
    net = models.__dict__["resnet50"](pretrained=True)
    net.fc = nn.Linear(512, 53) # 우리가 학습할거는 53개, 우리껄로 라벨을 지정해주어야 한다.
    net.to(device)
    print(net)

    # loss
    criterion = LabelSmoothingCrossEntropy().to(device)
    # optimizer
    # pip install adamp을 사용해준다.
    optimizer = AdamP(net.parameters(), lr=opt.lr, weight_decay=1e-2) # optimizer는 끝
    # scheduler
    scheduler = optim.lr_scheduler.MultiStepLR(optimizer, milestones=[60, 90], gamma=0.1) # 60번대하고 90번대에 떨어진다. 그리고 gamma를 줘서 떨어뜨린다.
    # scheduler = optim.lr_scheduler.StepLR(optimizer, step_size=20, gamma=0.1) # 애는 20, 40, 60, 80, ... 이렇게 떨어진다.

    # model.pt save dir
    save_dir = opt.save_path
    os.makedirs("./weights/", exist_ok=True)
    # train(num_epoch, model, train_loader, val_loader, criterion, optimizer, scheduler, save_dir, device):
    #
    train(opt.epoch, net, train_loader, val_loader, criterion, optimizer, scheduler, save_dir, device)

# ArgumentParser를 사용하면 나중에 값을 고칠 때 편하다.
def parse_opt():
    parser = argparse.ArgumentParser()
    parser.add_argument("--train-path", type=str, default="C:\\Users\\labadmin\\Downloads\\dataset\\train",
                        help="train data path")
    parser.add_argument("--val-path", type=str, default="C:\\Users\\labadmin\\Downloads\\dataset\\valid",
                        help="val data path")
    parser.add_argument("--batch-size", type=int, default=32,
                        help="batch size")
    parser.add_argument("--epoch", type=int, default=100,
                        help="epoch number")
    parser.add_argument("--lr", type=float, default=0.001,
                        help="lr number")
    parser.add_argument("--save-path", type=str, default="./weights",
                        help="save mode path")
    opt = parser.parse_args()

    return opt

if __name__ =="__main__":
    opt = parse_opt()
    main(opt)