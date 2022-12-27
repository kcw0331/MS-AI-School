# 다중 퍼셉트론으로 손글씨 분류
# 사이킷런에 있는 제공한 이미지를 이용한다.
import matplotlib.pyplot as plt
import torch
import torch.nn as nn
from torch import optim
from sklearn.datasets import load_digits

digits = load_digits()

# 첫번째 샘플을 출력 .images[인덱스] 8x8 사이즈이다.
# print(digits.images[0])

"""
[[ 0.  0.  5. 13.  9.  1.  0.  0.]
 [ 0.  0. 13. 15. 10. 15.  5.  0.]
 [ 0.  3. 15.  2.  0. 11.  8.  0.]
 [ 0.  4. 12.  0.  0.  8.  8.  0.]
 [ 0.  5.  8.  0.  0.  9.  8.  0.]
 [ 0.  4. 11.  0.  1. 12.  7.  0.]
 [ 0.  2. 14.  5. 10. 12.  0.  0.]
 [ 0.  0.  6. 13. 10.  0.  0.  0.]]
 """

 # 실제 레이블도 숫자 0인지 첫번째 샘플 레이어 확인 target[인덱스]
# print(digits.target[0])

# 전체 이미지 개수
print("전체 이미지 수 : ", len(digits.images)) # 해당하는 전체 이미지의 수가 나오게 된다.
# 전체 이미지 수 :  1797

# 상위 5개만 샘플이미지를 확인
# zip() enumerate()
"""
zip은 두개 묶을 리스트의 개수가 동일한지를 보아야 한다.
iamge = [1,2,3,4]
label = [사과, 바나나, 자몽, 수박]
1 사과 2 바나나 3 자몽 4 수박
"""
image_and_label_list = list(zip(digits.images, digits.target))

for index, (image, label) in enumerate(image_and_label_list[:4]): # 묶은 거에서 4개의 샘플만 본다.
    plt.subplot(2, 5, index + 1)
    plt.axis('off')
    plt.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
    plt.title('sample : %i' % label)
plt.show()

# 상위 레이블5개 확인
for i in range(5):
    print(i, "번 index sample label : ", digits.target[i]) # 상위의 5가지에 대해 알 수 있다.

"""
0 번 index sample label :  0
1 번 index sample label :  1
2 번 index sample label :  2
3 번 index sample label :  3
4 번 index sample label :  4
"""

# train data and label
x = digits.data # 이미지 데이터
y = digits.target # 각 이미지 레이블
# print(y)
# [[ 0.  0.  5. ...  0.  0.  0.]
#  [ 0.  0.  0. ... 10.  0.  0.]
#  [ 0.  0.  0. ... 16.  9.  0.]
#  ...
#  [ 0.  0.  1. ...  6.  0.  0.]
#  [ 0.  0.  2. ... 12.  0.  0.]
#  [ 0.  0. 10. ... 12.  1.  0.]]

# y의 값 출력
# [0 1 2 ... 8 9 8]

# 64개의 차원이다.
model = nn.Sequential(
    nn.Linear(64, 32), # input_layer = 64 hidden_layer_1 = 32
    nn.ReLU(),
    nn.Linear(32, 16), # input_layer = 32 hidden_layer_2 = 16
    nn.ReLU(),
    nn.Linear(16, 10) # input_layer = 32 output_layer = 10
    # CrossEntropyLoss() output layer = 2인 이상인 경우
)
print(model)
"""
Sequential(
  (0): Linear(in_features=64, out_features=32, bias=True)
  (1): ReLU()
  (2): Linear(in_features=32, out_features=16, bias=True)
  (3): ReLU()
  (4): Linear(in_features=16, out_features=10, bias=True)
)
"""
# 데이터에 대해서 텐서로 만들어 주었다.
x = torch.tensor(x, dtype=torch.float32)
y = torch.tensor(y, dtype=torch.int64)

loss_fun = nn.CrossEntropyLoss() # 소프트 맥스 함수를 포함!
optimizer = optim.Adam(model.parameters())

losses = [] # loss 그래프 확인, # 로스의 값을 여기에 저장을 해준다.
epoch_number = 100

for epoch in range(epoch_number+1):
    output = model(x)
    loss = loss_fun(output, y)
    
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if epoch % 10 == 0:
        print("Epoch : [{:4d}/{}] loss : {:.6f}".format(epoch, epoch_number, loss.item()))

    # append (append는 많이 사용된다.)
    losses.append(loss.item())

plt.title("loss")
plt.plot(losses)
plt.show()

# 트레인 로스만 보았다.