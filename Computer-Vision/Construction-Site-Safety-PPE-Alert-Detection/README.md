# PPE Detection for Construction Site Safety using YoloV5

## Introduction

- There are many safety accidents without wearing safety equipment (safety helmets, seat belts, safety shoes, etc.) at the construction site until 2023, and a pilot company has been selected and implemented since February 2022. 
<center><img src="./result/reference2.jpg"  width="700" height="300"/></center>

- It was seen that an employee who did not wear safety equipment at the construction site was notified to the construction site manager when he was found not wearing it for a certain period of time on CCTV. 
- Therefore, we are working on the project with the goal of making the current Object Detection class and practice similar to the actual practice.

- references:

    - [reference_1](http://news.kmib.co.kr/article/view.asp?arcid=0016070557&code=61121111&cp=nv),
    [reference_2](https://newsis.com/view/?id=NISX20230127_0002172017),
    [reference_3](https://www.hankyung.com/society/article/202302032530Y)

---

- Number of participants: 5 people

- Technology Stack: Python, ,Pytorch(ObjectDetection), Pyqt5, Yolov5, Yolov7, Deepsort, MMdetection

- My Role: Data Collection and Purification (Labeling and Bounding Box using CVAT), Data Segmentation, Model Training, GUI Implementation using Pyqt5 and Tracking Connection using Deepsort.

---

- There are 7 classes to detect from the dataset:
    
    <center><img src="./result/reference1.png"  width="300" height="200"/></center>
    
    - 'Safety_Belt', 'No_Safety_Belt', 'Safety_Shoes', 'No_Safety_shoes', 'Safety_helmet', 'No_Safety_helmet', 'Person'

## Results

### 1. Yolov5
The training of Yolov5n model was done for 100 epochs and wa completed in about 5 hours. After training, we get the following results:

<details><summary>VM Environment</summary>
GPU : Tesla V100, Memory : 112GB, CPU : Intel(R) Xeon(R) CPU E5-2690 v4 @ 2.60GHz 
</details>  

### Data set
|Type|Images|
|----|----|
|Train|11,495|
|Valid|1,437|

- Train image data is 11,495 and Valid image data is 1,437.

### Annotation Information
|Label|Train|Valid|
|----|----|----|
|Safety_Belt|7,841|1,006|
|No_Safety_Belt|14,820|2,111|
|Safety_Shoes|8,979|1,156|
|No_Safety_Shoes|6,607|881|
|Safety_Helmet|13,747|2,480|
|No_Safety_Helmet|6,474|811|
|Person|25,855|3,235|
|Total|84,323|11,680|

- When determining the number of bounding boxes, 84,323 bounding boxes for Train and 11,680 bounding boxes for Valid.

### Yolov5 & Yolov7 result Table
|Model|Hyperparameter|Batch_size|Epochs|optimizer|mAP0.5|mAP0.5-0.95|
|--|--|--|--|--|--|--|
|Yolov5n|Hyp.scratch-low|16|100|SGD|0.83782|0.49619|
|Yolov5s|Hyp.scratch-high|84|100|SGD|0.86399|0.53363|
|Yolov5l|Hyp.scratch-high|16|30|SGD|0.8715|0.55632|
|Yolov5m|Hyp.scratch-low|32|100|SGD|0.88586|0.5667|
|Yolov5x|Hyp.scratch-med|16|100|Adam|0.88726|0.57239|
|Yolov7|Hyp.scratch.p5|16|200|SGD|0.933|0.598|

- When we looked at Yolov5's model with n, s, l, m, x, and Yolov7, we found that mAP 0.5~0.95 did not have more than 0.6 values.

### Yolov5 of confusion_matrix result(Yolov5x):
<center><img src="./result/confusion_matrix.png"  width="400" height="300"/></center>

### Yolov5 of Val_batch_label result(Yolov5x):
<center><img src="./result/val_batch0_labels.jpg"  width="400" height="300"/></center>

- This is the image when I trained with Train and printed out the image of Validation.

### Yolov5 of result(Yolov5x):
<center><img src="./result/results.png"  width="700" height="400"/></center>

- In mAP 0.5 it has a value of more than 0.8, but in mAP 0.5 to 0.95, when 100 epochs were turned, it was found to converge from 0.55 to 0.6.
- So even when we turned Yolov7 200 epochs, we could see that it converges below 0.6. I've only watched 1-Stage, so I'm trying to see if I get different results when I watch 2-Stage on MMdetection. We're also figuring out if the data is weird.

### Yolov5 of Output(Yolov5x):

<center><img src="./result/result_GUI.png"  width="800" height="500"/></center>

- The Yolov5 pt file and the bounding box tracked people with Deepsort are implemented by calculating IOU, wearing a safety helmet, seat belt, and safety shoes using the GUI to indicate whether it is safe or not, and sending an e-mail to the manager for a certain period of time. 
<center><img src="./result/result_email_memo.png"  width="500" height="300"/></center>

<center><img src="./result/result_email_image.png"  width="700" height="400"/></center>

<!-- ### 2. Yolov7 -->