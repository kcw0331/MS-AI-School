# 파이토치의 nn.Linear와 nn.Sigmoid로 로지스틱 회귀를 구현하기
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

# train data -> Tensor
x_data = [[1, 2], [2, 3], [3, 1],[4, 3], [5, 3], [6, 2]]
y_data = [[0], [0], [0], [1], [1], [1]]

# Tensor
x_train = torch.FloatTensor(x_data)
y_train = torch.FloatTensor(y_data)
# x데이터 넘파이를 텐서로 변환을 하였다.

# 신경망 층을 쌓을 때, nn.Sequential을 사용해준다.
# nn.Sequential()은 Wx+b와 같은 수식과 시그모이드 함수 등과 같은 여러 함수들을 연결해주는 역할을 합니다.
model = nn.Sequential(
    nn.Linear(2, 1), # input dim = 2 output dim = 1
    nn.Sigmoid()     # 출력은 시그모이드 함수를 거칩니다.
)

optimizer = optim.SGD(model.parameters(), lr=0.1)
epochs_num = 1000

for epoch in range(epochs_num + 1):
    output = model(x_train)

    # loss
    # binary로 하면 이진분류로 된다.
    loss = F.binary_cross_entropy(output, y_train)
    # 두개의 차이가 로스로 해서 구해진다.

    # loss H(x) 개선
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if epoch % 10 == 0:
        prediction = output >= torch.FloatTensor([0.5]) # 예측값이 0.5 넘으면 True 간주
        # 0.5이상은 다 Ture, 미만은 False로 해준다.
        correct_prediction = prediction.float() == y_train # 실제값과 일치하는 경우만 True
        acc = correct_prediction.sum().item() / len(correct_prediction) # 정확도 계산
        print("Epoch : {:4d}/{} loss : {:.6f} acc : {:.2f}%".format(
            epoch, epochs_num, loss.item(), acc * 100 
        ))

print(model(x_train))

"""
0.5를 기준으로 보았을 때, 0.5이상은 True, 미만은 False인 것을 볼 수 있다.
tensor([[0.0294],
        [0.1570],
        [0.2983],
        [0.7844],
        [0.9415],
        [0.9808]], grad_fn=<SigmoidBackward0>)

        y_data = [[0], [0], [0], [1], [1], [1]]
"""