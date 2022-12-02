
import sklearn
from sklearn.preprocessing import *
import numpy as np
from numpy import *

# pip install sklearn

def normalization(data):
    data_mm = (data - data.min(axis = 0) / (data.max(axis = 0) - data.min(axis = 0)))
    return data_mm

def numpy_standardization(data):
    '''
    (각데이터 - 평균(각열)) / 표준편차(각열)
    '''
    std_data = (data - np.mean(data, axis = 0) / np.std(data, axis = 0)) # np.mean은 평균을 구해주는 것
    return std_data

def main():
    data = np.random.randint(30, size = (6, 5))
    #print(data)
    std_data_temp = numpy_standardization(data)
    print('정규화', std_data_temp)
    data_mm_temp = normalization(data)
    print('일반화', data_mm_temp)

if __name__ == '__main__':
    main()

# Normalization 와 정규화 Standardiztion을 한 결과이다.
# 정규화 
# [[12.30797184  6.2209175  17.79818385 16.68664863 10.75098588]
#  [20.30797184  8.2209175   1.79818385 18.68664863 18.75098588]
#  [19.30797184 14.2209175   5.79818385 24.68664863 16.75098588]
#  [ 4.30797184 14.2209175  16.79818385 12.68664863  1.75098588]
#  [ 0.30797184  7.2209175  17.79818385 10.68664863 26.75098588]
#  [26.30797184  6.2209175   9.79818385 12.68664863 23.75098588]]
# 일반화 
# [[13.92307692  8.75       19.75       19.92857143 12.84      ]
#  [21.92307692 10.75        3.75       21.92857143 20.84      ]
#  [20.92307692 16.75        7.75       27.92857143 18.84      ]
#  [ 5.92307692 16.75       18.75       15.92857143  3.84      ]
#  [ 1.92307692  9.75       19.75       13.92857143 28.84      ]
#  [27.92307692  8.75       11.75       15.92857143 25.84      ]]