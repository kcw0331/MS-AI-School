from torch.utils.data.dataset import Dataset
import pandas as pd
import torch

class MyCustomDataset(Dataset):
    def __init__(self, csv_path):
        df = pd.read_csv(csv_path)
        # print(df.shape)
        self.bbox = df.iloc[:, 3:].values
        self.filename = df.iloc[:,1].values
        # print(self.bbox)
        # print(self.filename)  

    def __getitem__(self, index) :
        bbox = self.bbox[index]
        filename = self.filename[index].split('.')[0]
        return filename, bbox

    def __len__(self) :
        return len(self.bbox, self.filename)

temp = MyCustomDataset("./bbox_coordinate.csv")

for i, j in temp:
    print(i, j)