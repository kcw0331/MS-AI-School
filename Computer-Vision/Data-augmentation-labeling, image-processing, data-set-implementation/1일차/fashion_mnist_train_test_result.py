import cv2
import numpy as np
from torchvision import datasets
from torchvision.transforms import ToTensor
import torch
import os
from fashion_mnist_package import CustomImageDataset
import torch.nn.functional as F
import torch.optim as optim
import torch.utils.data.dataloader
from fashion_mnist_package import Net

epochs = 10
lr = 0.01 # 
momentum = 0.5 # 옵티마이저의 최적화 함수에 들어간다.
no_cuda = True # 
seed = 1
log_interval = 200

use_cuda = not no_cuda and torch.cuda.is_available()

torch.manual_seed(seed)

device = torch.device("cuda" if use_cuda else "cpu")

kwargs = {"num_workers": 1, 'pin_memory': True} if use_cuda else {} # kwargs는 아규먼트들이다.

print("set vars and device done")

#----------------------------------------------------------------------------------------------------#
batch_size = 64
test_batch_size = 1000

dataset = CustomImageDataset(
    annotations_file='./data/FashionMNIST/annotations.csv',
    img_dir='./data/FashionMNIST/imgs/'
)

dataset_test = CustomImageDataset(
    annotations_file='./data/FashionMNIST/test.csv',
    img_dir='./data/FashionMNIST/test_image/'
)
train_loader = torch.utils.data.DataLoader(dataset, batch_size=64, shuffle=True)
test_loader = torch.utils.data.DataLoader(dataset_test, batch_size=test_batch_size, shuffle=True, **kwargs)

model = Net().to(device)
optimizer = optim.SGD(model.parameters(), lr=lr, momentum=momentum)

def train(log_interval, model, device, train_loader, optimizer, epoch):
    model.train()
    for batch_idx, (data, target) in enumerate(train_loader):
        data, target = data.to(device), target.to(device)
        optimizer.zero_grad()
        output = model(data)
        loss = F.nll_loss(output, target)
        loss.backward()
        optimizer.step()
        if batch_idx % log_interval == 0:
            print('Train Epoch: {} [{}/{} ({:.0f}%)]\tLoss: {:.6f}'.format(
                epoch, batch_idx * len(data), len(train_loader.dataset),
                100. * batch_idx / len(train_loader), loss.item()))

def test(log_interval, model, device, test_loader):
    model.eval() # 데이터를 평가해준다.
    test_loss = 0
    correct = 0
    with torch.no_grad(): # grad를 연산하지 마라!하는 원천적으로 차단
        for data, target in test_loader:
            data, target = data.to(device), target.to(device) # 타깃하도 데이터를 똑같이 넣어준다.
            output = model(data)
            test_loss += F.nll_loss(output, target, reduction='sum').item()
            pred = output.argmax(dim=1, keepdim=True) # 아규먼트들 중에서 가장 큰 값을 가지고 오는 것
            correct += pred.eq(target.view_as(pred)).sum().item() # 정확도를 보여준다.
     
    test_loss /= len(test_loader.dataset)

    print('\nTest set: Average loss: {:.4f}, Accuracy: {}/{} ({:.0f}%)\n'.format
          (test_loss, correct, len(test_loader.dataset),
        100. * correct / len(test_loader.dataset)))

for epoch in range(1, 11):
    train(log_interval, model, device, train_loader, optimizer, epoch)
    test(log_interval, model, device, test_loader)
torch.save(model, './model.pt') # 테스트된 결과를 저장해둔다.