from torch.utils.data import Dataset
from xml.etree.ElementTree import parse

def box_xyxy(image_metas):
    list_box = []
    for img_meta in image_metas:
        box_metas = img_meta['box']
        for box_meta in box_metas:
            box_label = box_meta.attrib['label']
            box = [int(float(box_meta.attrib['xtl'])),
                   int(float(box_meta.attrib['ytl'])),
                   int(float(box_meta.attrib['xbr'])),
                   int(float(box_meta.attrib['ybr']))]
            list_box.append(box)
        return list_box

class CustomDataset(Dataset):

    def __init__(self, dataset_path, xml_path):
        self.dataset_path = dataset_path
        self.xml_path = xml_path

    def __getitem__(self, index):
        # 왠만하면 get에서 처리하는게 좋다.
        image_path = self.dataset_path[index]
        xml_path = self.xml_path[index]
        tree = parse(xml_path)
        root = tree.getroot()
        image_metas = root.findall("image") # 해당하는 박스를 찾는다.
        box_mates = root.findall('box')
        box = box_xyxy(box_mates)
        print(box)

        # return image, box, label <- 로 해서 뽑아올 수 있다.
        # 추가 aug 밝기 조절 및 그림자 추가
        # 추가적인 augmentation은 get에 다가 추가하는게 좋다.
        # image = or_s()

        # aug

    def __len__(self):
        return len(self.dataset_path)

image_path = ["./01.png"]
xml_path = ["./annotations.xml"]
test = CustomDataset(image_path, xml_path)

for i in test:
    pass

# 내가 받고 싶은 데이터를 만들고 싶어서 커스텀 데이터를 만드는 것이다.