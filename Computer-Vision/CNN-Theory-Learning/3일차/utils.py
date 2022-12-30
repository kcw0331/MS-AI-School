import copy
import os
import albumentations as A
from albumentations.pytorch import ToTensorV2
import matplotlib.pyplot as plt
import torch

# main에 깔끔하게하기 위해서 utils.py에 저장해 놓았다.

# 우리가 augmentaion 한게 어떻게 적용이 되는지 시각화 해본다.
# 이렇게 시각화 해주는 방법은 albumentations방법을 사용해주었을 때, 사용해주는 방법이다.
def visualize_aug(dataset, idx=0, samples=10, cols=5):
    dataset = copy.deepcopy(dataset)
    dataset.transform = A.Compose([
        t for t in dataset.transform if not isinstance(t, (A.Normalize, ToTensorV2))
    ])
    rows = samples // cols
    figure, ax = plt.subplots(nrows=rows, ncols=cols, figsize=(12,6))

    for i in range(samples):
        image, _ = dataset[idx]
        ax.ravel()[i].imshow(image)
        ax.ravel()[i].set_axis_off()
    plt.tight_layout()
    plt.show()

# visualize_aug(train_dataset)

def train(num_epoch, model, train_loader, val_loader, criterion, optimizer, scheduler, save_dir, device):
    print("Start training............")
    running_loss = 0.0
    total = 0
    best_loss = 9999 # 초기 값을 잡아주기 위해서하는 거라서 000만 아니면 된다고 말씀하심.
    for epoch in range(num_epoch + 1): # 전체 한바퀴 돌릴거라서 num_epoch가 들어간다.
        for i, (imgs, labels) in enumerate(train_loader):
            img, label = imgs.to(device), labels.to(device)

            output = model(img) # 모델이 예측한 결과치
            loss = criterion(output, label)
            scheduler.step() # 이렇게 해줘야 적용이 된다.
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            running_loss += loss.item() # 턴서 갑일 테니깐, item()으로 값을 뽑아내었다.
            # loss 그래프를 그려주기 위해서 running_loss를 만들어 준 것이다.

            _, argmax = torch.max(output, 1) # argmax는 예측한 라벨이 나온다.
            acc = (label == argmax).float().mean()
            total += label.size(0)

            if (i + 1) % 10 == 0:
                print("Epoch [{}/{}], Step[{}/{}], Loss : {:.4f}, Acc : {:.2f}%".format(
                    epoch + 1, num_epoch, i + 1, len(train_loader), loss.item(),
                    acc.item() * 100 # 100을 해줘야 퍼센트로 나오게 된다.
                ))

        avrg_loss, val_acc = validation(model, val_loader, criterion, device)

        """
        나중에 사용하려면 사용하시라고 하심.
        if epoch % 10 == 0:
            save_mode(model, save_dir, file_name=f"{epoch}.pt") # 10번째 마다 에포크를 저장하는 것이다.
        """
        if avrg_loss < best_loss:
            print(f"Best save at epoch >> {epoch}")
            print("save model in ", save_dir) # 이 모델이 어디에 저장되어 있는지 만듦
            best_loss = avrg_loss
            save_model(model, save_dir)

    # 마지막 에포크가 끝날때 저장해준다.
    save_model(model, save_dir, file_name="last_resnet.pt")

def validation(model, val_loader, criterion, device): # epoch를 넘겨줄 필요가 없다.
    print("Start val")

    # 애는 학습이 되면 안되는 거니깐 미분하면 안된다.
    with torch.no_grad():
        model.eval() # 평가모드로 전환해준다.

        total = 0
        correct = 0
        total_loss = 0
        cnt = 0
        batch_loss = 0

        for i, (imgs, labels) in enumerate(val_loader):
            imgs, labels = imgs.to(device), labels.to(device)
            output = model(imgs)
            loss = criterion(output, labels)
            batch_loss += loss.item()

            total += imgs.size(0)
            _, argmax = torch.max(output, 1) # 가장 높은 예측이 하나가 나오게 된다.
            correct += (labels == argmax).sum().item()
            total_loss += loss
            cnt += 1

    avrg_loss = total_loss / cnt
    val_acc = (correct / total * 100) # 평균이 나오게 된다.
    print("val Acc : {:.2f}% avg_loss : {:.4f}".format(
        val_acc, avrg_loss
    ))
    model.train() # validation에서 평가 후 train으로 전환이 되서 들어가게 된다.

    return avrg_loss, val_acc

def save_model(model, save_dir, file_name="best_resnet.pt"):
    output_path = os.path.join(save_dir, file_name) # 전체 저장 경로가 만들어 진다.
    # 여기는 싱글 GPU이고 멀티 GPU이면 이거와 다르다.
    torch.save(model.state_dict(), output_path)