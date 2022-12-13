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
# 1. 데이터 셋
training_data = datasets.FashionMNIST(
    root='data',
    train=True,
    download=True, # 다운로드가 True로 되어있지만 이미 설치가 되어있으면 다시 다운로드 되지 않음
    transform=ToTensor()
)

test_data = datasets.FashionMNIST(
    root='data',
    train=False,
    download=True,
    transform=ToTensor()
)

# 2. 데이터 시각화
img_size = 28
num_images = 5
with open('./data/FashionMNIST/raw/t10k-images-idx3-ubyte', 'rb') as f: # rb는 읽어 온다. 쓰는 것도 사용하려면 a를 써준다.
    a = f.read(16) # 헤더에 대한 정보여서 17바이트 부터 이미지에 대한 정보가 들어 있다.
    buf = f.read(img_size*img_size*num_images) # 28x28의 이미지를 가지고 옴.
    data = np.frombuffer(buf, dtype=np.uint8).astype(float) # 버퍼를 통해서 uint8을 가지고 와서 float으로 데이터 형태를 바꾸어준다.
    data = data.reshape(num_images, img_size, img_size, 1) # 채널의 수는 단일 채널로 가져옴
    import matplotlib.pyplot as plt
    image = np.asarray(data[1]).squeeze() # squeeze는 하나를 보고 싶어서 차원 하나를 줄여준다.
    # plt.imshow(image, 'gray')
    # plt.show()

# 3. 실제로 생성되는 데이터 확인
with open('./data/FashionMNIST/raw/train-labels-idx1-ubyte', 'rb') as f:
    _ = f.read(8)
    buf = f.read(num_images)
    labels = np.frombuffer(buf, dtype=np.uint8).astype(np.int64)
    print(labels[1])
    # 출력을 해보았을 때, 0번째 데이터라는 것을 알 수 있다.
plt.title(f'{labels[1]}') # 몇 번째 라벨인지 확인해본 결과 0번째 라벨이며 티셔츠라는 것을 알 수 있다.
# plt.imshow(image, 'gray')
# plt.show()

# 4.torchvision에서 생성된 데이터로 시각화
labels_map = {
    0: 'T-Shirt',
    1: 'Trouser',
    2: 'Pullover',
    3: 'Dress',
    4: 'Coat',
    5: 'Sandal',
    6: 'Shirt',
    7: 'Sneaker',
    8: 'Bag',
    9: 'Ankle Boot',
}
figure = plt.figure(figsize=(8, 8))
cols, rows = 3, 3
for i in range(1, cols * rows + 1):
    sample_idx = torch.randint(len(training_data), size = (1,)).item()
    img, label = training_data[sample_idx]
    figure.add_subplot(rows, cols, i)
    plt.title(labels_map[label])
    plt.axis("off")
    plt.imshow(img.squeeze(), cmap="gray")
plt.show()

# header
imgf = open('./data/FashionMNIST/raw/train-images-idx3-ubyte', 'rb')
imgd = imgf.read(16)
lblf = open('./data/FashionMNIST/raw/train-labels-idx1-ubyte', 'rb')
lbuf = lblf.read(8)
df_dict = {
    'file_name': [],
    'label': []
}
idx = 0
os.makedirs('./data/FashionMNIST/imgs.', exist_ok=True)
while True:
    imgd = imgf.read(img_size*img_size)
    if not imgd:
        break
    data = np.frombuffer(imgd, dtype=np.uint8).astype(float)
    data = data.reshape(1,img_size, img_size, 1)
    image = np.asarray(data).squeeze()
    lbld = lblf.read(1)
    labels = np.frombuffer(lbld, dtype=np.uint8).astype(np.int64)
    file_name = f'{idx}.png'
    cv2.imwrite(f'./data/FashionMNIST/imgs/{file_name}', image)
    df_dict['label'].append(labels[0])
    df_dict['file_name'].append(file_name)
    idx += 1
# print(df_dict)
import pandas as pd
df = pd.DataFrame(df_dict)
print(df)
df.to_csv('./data/FashionMNIST/annotations.csv')

# 파일이 저장이 잘 되어쓴지를 판단해준다.
# img_dir = './data/FashionMNIST/imgs/'
# for i in range(5):
#     file_name, label = mnist_data.iloc[i]

#----------------------------------------------------------------------------------------------------#

# train_test.py에 만들어 두었다.
"""epochs = 10
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
train_loader = torch.utils.data.dataloader(dataset, batch_size=64, shuffle=True)
test_loader = torch.utils.data.dataloader(dataset, batch_size=test_batch_size, shuffle=True, **kwargs)

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
                100. * batch_idx / len(train_loader), loss.item()))"""