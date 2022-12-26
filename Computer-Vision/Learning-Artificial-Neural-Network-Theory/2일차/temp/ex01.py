import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

# 랜덤 시드 설정
torch.manual_seed(1)

# 실습을 위한 기본셋팅 훈련데이터 x_train, y_train을 선언
x_train = torch.FloatTensor(([1], [2], [3]))
y_train = torch.FloatTensor(([2], [4], [6]))

# x_train와 shape 출력
print(x_train, x_train.shape) # shape or size
print(y_train, y_train.shape) # shape or size
"""
tensor([1.],
       [2.],
       [3.]) torch.Size([3, 1])
tensor([2.],
       [4.],
       [6.]) torch.Size([3, 1])
"""

# 가중치와 편향의 초기화 -> w and b
# requires_grad = Treu -> 학습을 통해 계속 값이 변경되는 변수
w = torch.zeros(1, requires_grad=True)
# 학습을 통해서 requires_grad 값을 변경시켜주는 애이다.
print(w)
b = torch.zeros(1, requires_grad=True)

# 가설 세우기
# 직선의 방정식
hypothesis = x_train* w + b
print(hypothesis)
# loss fn 선언 하기
# 평균 제곱 오차 선언
loss = torch.mean((hypothesis - y_train) ** 2)
print(loss)

# 경사하강법 구현 하기
optimizer = optim.SGD([w, b], lr=0.01)

# 기울기 0으로 초기화
optimizer.zero_grad()
loss.backward() # 백워드를 해서 미분해서 내려가준다.

# 학습 진행
epoch_num = 2000

# epoch : 전체 훈련 데이터가 학습에 한번 사용된 주기
# train loop
for epoch in range(epoch_num + 1):

    # 1. 가설을 세워준다. -> 우리가 알고있는 model
    hypothesis = x_train * w + b

    # loss를 계산해준다.
    loss = torch.mean((hypothesis - y_train) ** 2)

    # loss H(x) 개선
    optimizer.zero_grad()
    loss.backward()
    optimizer.step() # 옵티마이저도 갱신이 필요하다. 그래야 랜덤되서 들어간다.

    # 100번 마다 프린트를 해준다.
    if epoch % 100 == 0:
        print("Epoch {:4d}/{} W : {:.3f} b : {:.3f} loss : {:.6f}".format(
            epoch, epoch_num, w.item(), b.item(), loss.item()
        ) )