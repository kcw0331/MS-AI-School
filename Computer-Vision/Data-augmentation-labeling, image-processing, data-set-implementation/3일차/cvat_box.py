import os
import glob
import cv2
from xml.etree.ElementTree import parse

# xml 파일 찾을 수 있는 함수 제작
def find_xml_file(xml_folder_path):
    all_root = []
    # print(",,", xml_folder_path)
    for (path, dir, files) in os.walk(xml_folder_path): # walk로 하게 되면, path, dir, files로 읽어온다.
        # print("...", path, dir, files)
        for filename in files:
            # image.png -> .png 이렇게 나오게 된다.
            # image.xml -> .xml
            ext = os.path.splitext(filename)[-1]
            # print(filename)
            if ext == ".xml":
                root = os.path.join(path, filename)
                # ./cavt_annotations/annotations.xml
                all_root.append(root) # 여기에 저장을 해준다.
            else:
                print("no xml file..")
                break # 이렇게 해야 all root를 빠져 나가게 된다.
    return all_root

xml_dirs = find_xml_file("./cvat_annotations/")
# print(xml_dirs)
# ['./cvat_annotations/annotations.xml']

# xml에서 정보를 가져와준다.
for xml_dir in xml_dirs:
    tree = parse(xml_dir)
    root = tree.getroot()
    img_metas = root.findall("image")
    for img_meta in img_metas:
        # xml에 기록된 이미지 이름
        image_name = img_meta.attrib['name']
        print(image_name)

        image_path = os.path.join("./images", image_name)
        #./images/aaa.png

        # image read
        image = cv2.imread(image_path)
        
        # image size info 
        img_width = int(img_meta.attrib['width']) # 너비와 높이의 정보를 가져온다.
        img_height = int(img_meta.attrib['height'])

        print(img_width, img_height)

        # box meta info 박스의 메타 정보를 가져온다.
        box_metas = img_meta.findall("box")

        for box_meta in box_metas:
            box_label = box_meta.attrib['label']
            box = [
                int(float(box_meta.attrib['xtl'])),
                int(float(box_meta.attrib['ytl'])),
                int(float(box_meta.attrib['xbr'])),
                int(float(box_meta.attrib['ybr'])),
            ]
            print(box[0], box[1], box[2], box[3])

            rect_img = cv2.rectangle(image, (box[0], box[1]), (box[2], box[3]), (0, 255, 255), 2)
        # cv2.namedWindow("aaaa")
        # cv2.moveWindow("aaaa", 40, 30) # 창의 크기를 조절하는 방법
        cv2.imwrite(f"./{image_name}", rect_img)
        # cv2.imshow("test", rect_img)
        # cv2.waitKey(0)