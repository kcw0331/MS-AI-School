# 금요일에 WebCam을 잘 다루지 못한 팀이 있어서 2023년1월9일에 다루어보았다.
import cv2
from torchvision import models
from torchvision import transforms
import torch.nn as nn
import torch

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

webcam = cv2.VideoCapture(1)
webcam.set(cv2.CAP_PROP_FRAME_WIDTH, 640) # 가로
webcam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480) # 세로

# model
# 순서는 아키텍처가 먼저이고 그 다음 우리가 학습한 데이터를 가져온다.
net = models.resnet18(pretrained=True)
# net.fc = nn.Linear(in_features=512, out_features="클래스의개수")

# 학습한 모델 불러오기
# 학습한게 없기 때문에 아래 두줄은 주석을 처리한다.
# models_loader_path = "./weight/resnet.pt"
# net.load_state_dict(torch.load(models_loader_path, map_location=device))
net.to(device)
# exit()

val_transforms = transforms.Compose([
    transforms.Resize((224,224)),
    transforms.ToTensor(),
    transforms.Normalize([0.485,0.456,0.406],[0.229,0.224,0.225])
])

def preprocess(image, device):
    from PIL import Image
    image = Image.fromarray(image)
    image = val_transforms(image)
    image = image.float()
    image = image.to(device)
    image = image.unsqueeze(0) # 차원을 하나 줄여준다.
    print(image.size())

    return image

if not webcam.isOpened():
    print("카메라 열기 실패 !!!")
    exit()

while webcam.isOpened():
    status, frame = webcam.read()
    frame = cv2.flip(frame, 1) # 좌우 대칭
    net.eval()
    with torch.no_grad():
    if status:
        image = preprocess(frame, device=device)
        output = net(frame)
        _, argmax = torch.max(output, 1)
        print("output", output)
        cv2.imshow("test", frame)

    if status:
        cv2.imshow("test", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
webcam.release()
cv2.destoryAllwindows()