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
img_size = 28
num_images = 5
with open('./data/FashionMNIST/raw/t10k-images-idx3-ubyte', 'rb') as f: # rb는 읽어 온다. 쓰는 것도 사용하려면 a를 써준다.
    a = f.read(16) # 헤더에 대한 정보여서 17바이트 부터 이미지에 대한 정보가 들어 있다.
    buf = f.read(img_size*img_size*num_images) # 28x28의 이미지를 가지고 옴.
    data = np.frombuffer(buf, dtype=np.uint8).astype(float) # 버퍼를 통해서 uint8을 가지고 와서 float으로 데이터 형태를 바꾸어준다.
    data = data.reshape(num_images, img_size, img_size, 1) # 채널의 수는 단일 채널로 가져옴
    import matplotlib.pyplot as plt
    image = np.asarray(data[1]).squeeze() # squeeze는 하나를 보고 싶어서 차원 하나를 줄여준다.


imgf = open('./data/FashionMNIST/raw/t10k-images-idx3-ubyte', 'rb')
imgd = imgf.read(16)
lblf = open('./data/FashionMNIST/raw/t10k-labels-idx1-ubyte', 'rb')
lbuf = lblf.read(8)
df_dict = {
    'file_name': [],
    'label': []
}
idx = 0 
os.makedirs('./data/FashionMNIST/test_image.', exist_ok=True)
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
    cv2.imwrite(f'./data/FashionMNIST/test_image/{file_name}', image)
    df_dict['label'].append(labels[0])
    df_dict['file_name'].append(file_name)
    idx += 1
# print(df_dict)
import pandas as pd
df = pd.DataFrame(df_dict)
print(df)
df.to_csv('./data/FashionMNIST/test.csv')