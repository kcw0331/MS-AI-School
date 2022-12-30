import os
import glob
import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from custom_dataset import custom_dataset
from torchvision import models # 토치비전에 모델에 해당하는게 있다.
# pip instal timm <- 이 모델을 다운 받음
import timm
from timm.loss import LabelSmoothingCrossEntropy
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# dataset
train_data = custom_dataset("D:\\MSAISchool_File\\data\\train")
test_data = custom_dataset("D:\\MSAISchool_File\\data\\test")

# for i in train_data:
#     print(i)

# dataloader
train_loader = DataLoader(train_data, batch_size=32, shuffle=True)
test_loader = DataLoader(test_data, batch_size=32, shuffle=False)

# model call
net = models.__dict__["resnet18"](pretrained=True)
net.fc = nn.Linear(512, 10) # 이부분에서 수정을 해줘야한다.
net.to(device)

# loss function
criterion = LabelSmoothingCrossEntropy()
criterion = criterion.to(device)
# this is better than nn.CrossEntropyLoss

# optimizer
optimizer = torch.optim.AdamW(net.parameters(), lr=0.001)

net.train()
total_step = len(train_loader)
curr_lr = 0.001
best_score = 0
num_epochs = 100
for epoch in range(num_epochs+1):
    total_loss = 0
    for i, (images, labels) in enumerate(train_loader):
        images = images.to(device)
        labels = labels.to(device)
        output = net(images)
        loss = criterion(output, labels)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        total_loss += loss.item()

        if (i+1) % 100 == 0:
            print("{} / {} ".formate(32*(i+1), train_data.__len__()))

    net.eval() # 트레인 돌고나서 평가를 해준다.
    score = 0
    total = 0
    for i, (images, labels) in enumerate(test_loader):
        images = images.to(device)
        labels = labels.to(device)
        output = net(images)

        total += images.size(0)
        _, argmax = torch.max(output, 1)
        score += (labels == argmax).sum().item()
    print("Epoch : {}, Loss : {:.4f}".format(
        epoch+1, total_loss / total_step
    ))

    avg = (score / total * 100)
    print("Accuracy : {:.2f}\n".format(avg))
    net.train()

    if best_score < avg:
        best_score = avg
        torch.save(net.state_dict(), "./best.pt")