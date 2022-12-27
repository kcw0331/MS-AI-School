# 다중 퍼셉트론을 이용한 XOR_gate 구현
import numpy as np

def and_gate(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7

    temp = np.sum(w*x)+b
    if temp <= 0: 
        return 0
    else:
        return 1

def nand_gate(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7

    temp = np.sum(x*w) +b

    if temp <= 0:
        return 0
    else:
        return 1

def or_gate(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2
    temp = np.sum(x*w) + b

    if temp <= 0:
        return 0
    else:
        return 1

def xor_gate(x1, x2):
    s1 = nand_gate(x1, x2)
    s2 = or_gate(x1, x2)
    y = and_gate(s1, s2)

    return y

print(xor_gate(1, 1))