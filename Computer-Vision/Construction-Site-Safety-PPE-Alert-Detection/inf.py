# 2023년 2월 8일(수)
import torch.cuda
import os
import glob
import cv2

# device setting
DEVICE = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Model call
model = torch.hub.load('ultralytics/yolov5', 'custom', path=".\\runs\\train\\exp_0209\\weights\\best.pt")
# model = custom(path_or_model='.\\runs\\train\\exp3\\weights\\best.pt')
model.conf = 0.5  # NMS confidence threshold
model.iou = 0.45 # NMS IoU threshold
model.to(DEVICE)

# image path list
# jpg파일을 가져옴
image_path_list = glob.glob(os.path.join(".\\dataset\\test\\images", "*.jpg"))

# 하나하나의 이미지 추출
for i in image_path_list:
    image_path = i
    # cv2 image read
    image = cv2.imread(image_path)
    # label_dict = {   0 : 'safety_belt_used', 1 : 'safety_belt_unused', 2 : 'safety_shoes_used', 3 : 'safety_shoes_unused',
    #                 4 : 'safety_helmet_used', 5 : 'safety_helmet_unused'}
    label_dict = {0: 'belt', 1: 'no_belt', 2: 'shoes', 3: 'no_shoes', 4: 'helmet', 5: 'no_helmet', 6 : 'person'}
    # model input
    # 모델에 이미지를 넣어준다.
    output = model(image, size = 640)
    # print(output.print())
    bbox_info = output.xyxy[0] # bounding box의 결과를 추출
    # for문을 들어가서 우리가 원하는 결과를 뽑는다.

    person = []
    # score = bbox[4].item()
    # label_number = int(bbox[5].item())
    for bbox in bbox_info:
        if bbox[5] == 6:
            person.append(bbox[:4])
    for bbox2 in bbox_info:
        for i in person:
            if bbox2[5] in [1, 3, 5]:
                x1 = int(bbox2[0].item())
                y1 = int(bbox2[1].item())
                x2 = int(bbox2[2].item())
                y2 = int(bbox2[3].item())
                np_x, np_y = (x2 + x1) / 2, (y2 + y1) / 2

                if int(i[0]) <= x1 and int(i[2]) >= x2 and int(i[1]) <= y1 and int(i[3]) >= y2:
                    if bbox2[5] == 1 or bbox2[5] == 3 or bbox2[5] == 5:
                        cv2.putText(image, 'False', (int(x1), int(y1 - 5)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        #     else:
        #         x1 = int(bbox[0].item())
        #         y1 = int(bbox[1].item())
        #         x2 = int(bbox[2].item())
        #         y2 = int(bbox[3].item())
        #         np_x, np_y = (x2 + x1) / 2, (y2 + y1) / 2
        #         if i[0] <= x1 and i[2] >= x2 and i[1] <= y1 and i[3] >= y2:
        #             if label_number == 0 and label_number == 4:
        #                 cv2.putText(image, 'True', (int(x1), int(y1 - 5)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        # print(x1, y1, x2, y2, score, label_number) # 298 706 437 728 0.8252878785133362 7의 결과가 나오는 것을 볼 수 있다
        # cv2.rectangle(image, (x1, y1), (x2, y2),(0, 255, 0), 2)
        # cv2.putText(image, label_dict[label_number], (int(x1), int(y1 - 5)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        # cv2.putText(image, str(round(score, 4)), (int(x1), int(y1 - 25)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    cv2.imshow("test", image)
    cv2.waitKey(0) # 1초 정도마다 이미지가 나오고 닫힌다.