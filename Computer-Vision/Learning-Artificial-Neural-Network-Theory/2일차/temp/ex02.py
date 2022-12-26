import torch 
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

# 다중 선형 회귀 실습
# 앞서 배운 x가 1개인 선형 회귀 -> 단순 선형이라고 합니다.
# 다수 x 로부터 y를 예측하는 다중 선형 회귀

# 다수의 x를 만들어 준다.
x1_train = torch.FloatTensor([[73], [93], [83], [96], [73]])
x2_train = torch.FloatTensor([[80], [88], [91], [98], [66]])
x3_train = torch.FloatTensor([[75], [93], [90], [100], [70]])

# 정답지인 y를 만들어준다.
y_train = torch.FloatTensor([[152], [185], [180], [196], [142]])

# 가중치 w와 편향 b를 선언 필요하고 w -> 3개가 필요, b -> 1개가 필요
w1 = torch.zeros(1, requires_grad=True)
w2 = torch.zeros(1, requires_grad=True)
w3 = torch.zeros(1, requires_grad=True)
b = torch.zeros(1, requires_grad=True)

# optimizer
optimizer = optim.SGD([w1, w2, w3, b], lr=1e-9) # 파라메터들을 설정해준다.

# 학습 몇번 진행할래 ?
epoch_num = 10000

for epoch in range(epoch_num + 1): # 1부터 시작하기 위해서 1을 더해준다. 

    # 가설 xw + xw + ... + b <- 마지막에는 편향 b가 붙어줘야한다.
    hypothesis = (x1_train * w1) + (x2_train * w2) + (x3_train * w3) + b
    
    # loss
    loss = torch.mean((hypothesis - y_train) ** 2)

    # loss H(x) 개선
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    
    if epoch % 100 == 0:
        # 텐서에서 item()으로 사용하면 정수로 뽑아낼 수 있다.
        print("Epoch {:4d}/{} w1 {:.3f} w2 {:.3f} w3 {:.3f} loss {:.6f}".format(
            epoch, epoch_num, w1.item(), w2.item(), w3.item(), b.item(), loss))