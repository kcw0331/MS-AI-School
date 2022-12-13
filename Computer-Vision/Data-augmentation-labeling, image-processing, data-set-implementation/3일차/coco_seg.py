import os
import json
import cv2

json_path = "./annotations/instances_default.json"

with open(json_path, "r") as f:
    coco_info = json.load(f)

# print(coco_info)

# 파일 읽기 실패
assert len(coco_info) > 0, "파일 읽기 실패"

# 카테고리 수집과 annotation 수집을 해본다
# 카테고리 수집 
categories = dict() 
for category in coco_info['categories']:
    categories[category["id"]] = category["name"]

# print(categories)

# annotation 정보
ann_info = dict()
for annotation in coco_info['annotations']:
    image_id = annotation["image_id"]
    bbox = annotation["bbox"]
    category_id = annotation["category_id"]
    segmentation = annotation["segmentation"]

    # print(image_id, bbox, category_id, segmentation)
    if image_id not in ann_info: # 여기서는 박스랑 세그멘테이션이 두개가 들어간다.
        ann_info[image_id] = {
            "boxes" : [bbox], "segmentation" : [segmentation],
            "categories" : [category_id] 
        }
    else:
        ann_info[image_id]["boxes"].append(bbox)
        ann_info[image_id]["segmentation"].append(segmentation)
        ann_info[image_id]["categories"].append(categories[category_id])

for image_info in coco_info['images']:
    # print(image_info)
    filename = image_info['file_name']
    width = image_info['width']
    height = image_info['height']
    img_id = image_info['id']

    file_path = os.path.join("./images", filename)
    img = cv2.imread(file_path)

    try:
        annotation = ann_info[img_id]
    except KeyError :
        continue
    for bbox, segmentation, category in zip(annotation['boxes'], 
                                            annotation['segmentation'], annotation['categories']):
        x1, y1, w, h = bbox
        import numpy as np
        for seg in segmentation: # 이렇게 해주어야 폴리건이 뽑힌다.
            # print(seg)
            poly = np.array(seg, np.int32).reshape((int(len(seg)/2), 2)) 
            # print(poly)
            poly_img = cv2.polylines(img, [poly], True, (255, 0, 0), 2)
    cv2.imwrite(f"./{filename}", poly_img)
    # cv2.imshow("test", poly_img)
    # cv2.waitKey(0)