import numpy as np

class SGD:
    # 확률적 경사 하강방법
    # 러닝레이트를 받아준다.
    def __init__(self, lr=0.01):
        self.lr = lr

    def update(self, params, grads):
        # SGD 논문에 있는 공식을 그대로 사용한 것이다.
        for key in params.keys():
            params[key] -= self.lr * grads[key]

# 실질적으로 가져다 쓰는데 어떻게 만들어졌는지 구해보는 것이다.
class Momentum:
    # 모멘텀 SGD
    def __init__(self, lr=0.01, momentum=0.9):
        # 초기화를 해준다.
        self.lr = lr
        self.momentum = momentum
        self.v = None
    def update(self, params, grads):
        if self.v is None:
            self.v = {}
            for key, val in params.items():
                self.v[key] = np.zeros_like(val)

        for key in params.keys():
            self.v[key] = self.momentum*self.v[key] - self.lr*grads[key]
            params[key] += self.v[key]

class AdaGrad:
    """Ada Grad"""
    def __init__(self, lr=0.01):
        self.lr = lr
        self.h = None

    def update(self, params, grads):
        if self.h is None:
            self.h = {}
            for key, val in params.items():
                self.h[key] = np.zeros_like(val)

        for key in params.keys():
            self.h[key] += grads[key] * grads[key]
            #                                      여기는 자연값을 더하는 부분이다.
            params[key] -= self.lr * grads[key] / (np.sqrt(self.h[key]) + 1e-7)

class Adam:
    def __init__(self, lr=0.001, beta1=0.9, beta2=0.999):
        self.lr = lr
        self.beta1 = beta1
        self.beta2 = beta2
        self.iter = 0 # 초기값 0을 준다.
        self.m = None
        self.v = None
    
    def update(self, params, grads):
        # 인자 값을 주지 않는 이상 초기값은 None이다.
        if self.m is None:
            self.m, self.v = {}, {}
            for key, val in params.items():
                self.m[key] = np.zeros_like(val)
                self.v[key] = np.zeros_like(val)
        
        self.iter += 1
        lr_t = self.lr * np.sqrt(1.0 - self.beta2 ** self.iter) / (1.0 - self.beta1 ** self.iter)

        for key in params.keys():
            self.m[key] += (1 - self.beta1) * (grads[key] - self.m[key])
            self.v[key] += (1 - self.beta2) * (grads[key]**2 - self.v[key])
            params[key] -= lr_t * self.m[key] / (np.sqrt(self.v[key]) + 1e-7)
