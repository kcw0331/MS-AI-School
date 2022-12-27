# 파이토치로 다층 퍼셉트론 구현
import torch
import torch.nn as nn
from tqdm.notebook import tqdm

# GPU 사용가능 여부 파악
device = "cuda" if torch.cuda.is_available() else "cpu"
print(device)

# xor 문제를 풀기 위한 입력과 출력 정의
x = [[0, 0], [0, 1], [1, 0], [1, 1]]
y = [[0], [1], [1], [0]]

x = torch.tensor(x, dtype=torch.float32).to(device)
y = torch.tensor(y, dtype=torch.float32).to(device)

# 참고
# CrossEntropy 경우에는 마지막 레이어 노드수가 2개 이상이여야 한다.
# 만약 마지막 층에 1개 ouput이라면 BCELoss를 사용할때가 있다.
# BCELoss 함수를 사용할 경우에는 먼저 마지막 레이어의 값이 0~1로 조정을 해줘야한다.
# model
# 입력층, 은닉층 1, 은닉층 2, 은닉층 3, 출력층
model = nn.Sequential(
    nn.Linear(2, 10, bias=True),    # iput_layer = 2, hidden_layer = 1 -> 10
    nn.Sigmoid(),
    nn.Linear(10, 10),              # hidden_layer1 = 10 hidden_layer2 = 10
    nn.Sigmoid(),
    nn.Linear(10, 10, bias=True),   # hidden_layer2 = 10, hidden_layer3 = 10
    nn.Sigmoid(),
    nn.Linear(10, 1, bias=True),    # hidden_layer3 = 10, output_layer = 1
    nn.Sigmoid()                    # 우리가 사용할 Loss BCELoss 이므로 마지막 레이어를 시그모이드 함수 적용
).to(device)

# BCELoss는 0과 1로만 나오기 때문에 1을 쓰게 된다.
# BCELoss를 사용할 때, 마지막에는 Sigmoid를 사용해준다. 마지막을 0, 1로 조정을 해준다.

print(model)
"""
Sequential(
  (0): Linear(in_features=2, out_features=10, bias=True)
  (1): Sigmoid()
  (2): Linear(in_features=10, out_features=10, bias=True)
  (3): Sigmoid()
  (4): Linear(in_features=10, out_features=10, bias=True)
  (5): Sigmoid()
  (6): Linear(in_features=10, out_features=1, bias=True)
  (7): Sigmoid()
)
"""
criterion = torch.nn.BCELoss().to(device)
optimizer = torch.optim.SGD(model.parameters(), lr=0.1)

# 10000번  에포크를 수행 하겠습니다.
epoch_number = 100000
for epoch in range(epoch_number + 1):
    output = model(x) # 모델에 넣어준다.

    loss = criterion(output, y) # 예측과 정답지를 준다 그래야 loss를 나타낸다.
    optimizer.zero_grad()
    loss.backward()
    optimizer.step() # 갱신을 해준다.

    # 100의 배수에 해당되는 에포크 마다 loss print
    if epoch % 100 == 0:
        print(f"Epoch : {epoch} loss : {loss.item()}")

# 모델을 save 하지 않았기 때문에 인퍼런스 코드를 작성해야 한다.
# 인퍼런스 코드
with torch.no_grad(): # 미분하지 마라는 것이다.
    output = model(x)
    predicted = (output > 0.5).float()
    acc = (predicted == y).float().mean()
    print("모델의 출력값 output \n", output.detach().cpu().numpy()) # 넘파이로 바꾸어 줄려고 .cpu()로 바꾸어 준 것이다.
    print("모델의 예측값 output \n", output.detach().cpu().numpy())
    print("실제값 (Y) \n", y.cpu().numpy())
    print("정확도 -> ", acc.item())

"""
모델의 출력값 output 
 [[1.0587639e-04]
 [9.9987435e-01]
 [9.9988461e-01]
 [1.2620556e-04]]
모델의 예측값 output
 [[1.0587639e-04]
 [9.9987435e-01]
 [9.9988461e-01]
 [1.2620556e-04]]
실제값 (Y)
 [[0.]
 [1.]
 [1.]
 [0.]]
정확도 ->  1.0
"""