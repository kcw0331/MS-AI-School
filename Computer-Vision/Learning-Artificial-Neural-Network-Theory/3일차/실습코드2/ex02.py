# w값이 변화에 따른 경사도 변화
import numpy as np
import matplotlib.pyplot as plt

def sigmoid(t):
    return 1 / (1+ np.exp(-t))

x = np.arange(-5.0, 5.0, 0.1)
y1 = sigmoid(0.5 * x)
y2 = sigmoid(x) # 기본 x를 넣어준다.
y3 = sigmoid(2*x)

print("y1: ", y1)
print("y2: ", y2)
print("y3: ", y2)
# 선형회귀에서는 w가 기울기를 뜻했는데, 
# 여기에서는 w가 경사도라는 것을 알 수 있다.
# w값에 따라서 경사도가 어떻게 변하는지를 보려고하는 것이다.
# 이제 알아야 할 것은 b값에 따라 위, 아래가 변하는지를 본다.

plt.plot(x, y1, 'r', linestyle='--') # w의 값이 0.5인 경우
plt.plot(x, y2, 'g') # w의 값이 1인 경우
plt.plot(x, y3, 'b', linestyle='--') # w의 값이 2인 경우
plt.plot([0, 0], [1.0, 0.0], ':') # 가운데 점선 추가
plt.title('sigmoid Function')
plt.show()