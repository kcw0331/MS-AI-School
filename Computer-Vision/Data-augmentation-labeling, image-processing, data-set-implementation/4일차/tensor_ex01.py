import torch
import numpy as np

"""data = [[1, 2,], [3, 4]]
x_data = torch.tensor(data)
# print(x_data)
# print(x_data.shape)

# numpy 배열로부터 생성
# np_array = np.array(data).reshape
# x_np = torch.from_numpy(np_array)
# print(x_np)

# 1의 값으로 값이 채워지는 것을 볼 수 있다.
x_ones = torch.ones_like(x_data)
# print(f"Ones Tensor >> \n", x_ones)

# 랜덤한 숫자로 like하게 된다. (2x2행렬에다가)
x_rand = torch.rand_like(x_data, dtype=torch.float32)
# print(x_rand)

# 무작위(random) 또는 상수(constant) 값을 사용하기
shape = (3, 3)
randn_tensor = torch.rand(shape)
ones_tensor = torch.ones(shape)
zeros_tensor = torch.zeros(shape)

print(f"Random Tensor >> \n {randn_tensor} \n")
print(f"ones Tensor >> \n {ones_tensor} \n")
print(f"zeros Tensor >> \n {zeros_tensor} \n")"""

"""tensor = torch.rand(3,4)
print(f"shape of tensor: {tensor.shape}") # 크기가 나오게 된다.
print(f"data type of tensor: {tensor.dtype}") # 데이터의 타입이 나온다.(기본으로 float32를 쓴다.) 
# 속도를 올리고 싶으면 float16, float8을 사용한다. 
print(f"Device tensor is stored on : {tensor.device}") # 디바이스의 정보가 나오게 된다."""

"""tensor = torch.rand(3,4)

if torch.cuda.is_available() :
    tensor = tensor.to("cuda")
else:
    tensor = tensor.to("cpu")
print(f"Device tensor is sorted on : {tensor.device}") # 우리는 GPU가 없기 때문에 CPU가 나오게 된다."""

tensor = torch.ones(4,4)
"""tensor[:,1] = 3
print(tensor)"""
# 3으로 바뀐 것을 알 수 있다.
# tensor([[1., 3., 1., 1.], 
#         [1., 3., 1., 1.], 
#         [1., 3., 1., 1.], 
#         [1., 3., 1., 1.]])

"""t1 = torch.cat([tensor, tensor, tensor], dim = 1) # cat은 합치는 기능이다.
print(t1)

print(tensor*tensor)"""

"""print(tensor) # 이 행렬을 가지고 아래와 같이 텐서간의 행렬곱을 만들어 냈다.
print(tensor.matmul(tensor.T)) # 텐서간의 행렬곱이다.
print(tensor @ tensor.T) # 텐서간의 행렬곲이다."""

"""
바꿔치기(in-place)
tensor.add_(5)
print(tensor) # 1로 되어 있던 것들이 6으로 바뀌게 되었다.
"""

"""
### 텐서 numpy 배열 변환
t = torch.ones(5)
print("tensor -> ", t)
n = t.numpy()
print("numpy ->", n)
"""

"""
# tensor를 numpy로 형변환 할 수 있다.
t = torch.ones(5)
t.add_(1)
n = t.numpy()
print(t) # 주소가 공유가 될 수 있어서 numpy와 tensor를 혼용하지 않는다.
print(n)

# numpy를 tensor로 형변환 할 수 있다.
n = np.ones(5)
t = torch.from_numpy(n)

print(n)
print(t)
np.add(n, 1, out=n)
print(n)
print(t) # 서로 주소를 공유하고 있기 때문에 값을 바꾸게 되면 둘다 바뀐다.
"""

"""
# view
t = np.array([[[0, 1, 2], [3, 4, 5]], [[6, 7, 8], [9, 10, 11]]])
ft = torch.FloatTensor(t)
print(ft.shape) 
print(ft)
"""

"""
t = np.array([[[0, 1, 2], [3, 4, 5]], [[6, 7, 8], [9, 10, 11]]])
print(t.shape)
ft = torch.FloatTensor(t)
print(ft.view([-1, 3])) # ft tensor (?, 3) size changed
print(ft.view([-1, 3]).shape)
"""

"""
t = np.array([[[0, 1, 2], [3, 4, 5]], [[6, 7, 8], [9, 10, 11]]])
ft = torch.FloatTensor(t)
print(ft.view([-1, 1, 3]))
print(ft.view([-1, 1, 3]).shape)
"""
"""
# squeeze
# 3x1
ft = torch.FloatTensor([[0], [1], [2]])
print(ft)
print(ft.shape)
print(ft.squeeze())
print(ft.squeeze().shape) # 차원을 날려줄 수 있다.
"""

"""
# unsqueeze
ft = torch.FloatTensor([0, 1, 2])
print(ft)
print(ft.shape) # 이것에 대해서 unsqueeze를 해준다.

print(ft.unsqueeze(0))
print(ft.unsqueeze(0).shape)
"""

ft = torch.FloatTensor([0, 1, 2])
print(ft.view(1, -1))
print(ft.view(1, -1).shape)