import os
import json
import cv2
import xml.etree.ElementTree as ET
import pandas as pd

# json 파일 읽기
json_path = "./annotations/instances_default.json"

with open(json_path, "r") as f :
    coco_info = json.load(f) # json의 경로와 leard r을 읽겠다

# print(coco_info)

assert len(coco_info) > 0, "파일 읽기 실패"  # 0보다 작으면 데이터에 문제가 있기 때문에 파일 일기 실패를 해준다.

# 카테고리 정보 수집
categories = dict()
for category in coco_info['categories']:
    # print(category) # {'id': 1, 'name': 'kiwi', 'supercategory': ''} 키위가 하나라서 하나의 정보만 나온다.
    categories[category["id"]] = category["name"] 

# print("categories info >> ", categories) # categories info >>  {1: 'kiwi'} 1번이 키위라는 것을 알 수 있다. 
# 0번은 백그라운드라서 기록이 안되고 1번 부터 기록이 된다.

# annotation 정보 수집
ann_info = dict() # 중요한 점은 지금 사용하는 코드는 coco데이터에만 맞는 거다
for annotation in coco_info['annotations']: 
    # print(annotation) # 각 annotations별로 필요한 정보들이 나오게 된다
    image_id = annotation["image_id"]
    bbox = annotation["bbox"]
    category_id = annotation["category_id"]
    # print(f"image_id : {image_id}, category_id : {category_id}, bbox : {bbox}")

    if image_id not in ann_info:
        ann_info[image_id] = {
            "boxes" : [bbox], "categories" : [category_id]
        }
    else:
        ann_info[image_id]["boxes"].append(bbox)
        ann_info[image_id]["categories"].append(categories[category_id])

# print("ann_info >> ", ann_info)

# import xml.etree.ElementTree as ET
tree = ET.ElementTree()
root = ET.Element("annotations")

"""bbbox_filename = []
ccount = 1"""

for i, image_info in enumerate(coco_info['images']):
    # print(image_info)

    # xml file save folder
    os.makedirs("./xml_folder", exist_ok=True)
    xml_save_path = "./xml_folder/test.xml"

    filename = image_info['file_name']
    width = image_info['width']
    height = image_info['height']
    img_id = image_info['id']
    # print(filename, width, height, img_id)
    xml_frame = ET.SubElement(root, "image", id=str(i), name=filename, width="%d" % width, height = "%d" % height) # 0, 1, 2, 3 , ...해주기 위해 enumerate를 사용함

    # 이미지를 가져오기 위한 처리
    file_path = os.path.join("./images", filename)   # <- 여기서 이걸로 filename으로 저장을 하고
    # print("file_path = ", file_path)
    img = cv2.imread(file_path)
    # cv2.imshow("show", img)
    # cv2.waitKey(0)
    try:
        annotation = ann_info[img_id]
    except KeyError:
        continue

    # print(annotation)

    ## box category

    # 만약 라벨링 여러개라면 label_list = {1: 'kiwi, 2 : 'apply'} 해준다.

    for bbox, category in zip(annotation['boxes'], annotation['categories']):
        # print(bbox, category)
        x1, y1, w, h = bbox
        print(x1, y1, w, h) # 해당하는 바운딩 박스의 정보를 얻을 수 있다. # <- 바운딩 박스로 csv파일로 저장을 할 수 있다.
        
        """bbbox_filename.append([os.path.basename(file_path), f'{ccount}',x1, y1, w, h])
        ccount += 1"""
        
        ET.SubElement(xml_frame, "box", label="kiwi", occlude="0", source="manual", x1 =str(x1), y1=str(y1), w =str(w), h =str(h), z_order ="0")
        rec_img = cv2.rectangle(img, (int(x1), int(y1)), (int(x1+w), int(y1+h)), (225, 0, 255), 2) # 해당하는 이미지를 넣어준다. 그럼 rectangle이 완성이 된다.

"""print(bbbox_filename)
col_name = ['file_name', 'image_id', 'x1', 'y1', 'w', 'h']
df_list = pd.DataFrame(bbbox_filename, columns = col_name)
print(df_list)
os.makedirs('./과제/', exist_ok=True)
df_list.to_csv('./과제/bbox_coordinate.csv')"""
    # cv2.imwrite(f"./{filename}", rec_img)
    # cv2.imshow("test", rec_img)
    # cv2.waitKey(0)

    # tree._setroot(root)
    # tree.write(xml_save_path, encoding='utf-8')
    # print("xml ok")
