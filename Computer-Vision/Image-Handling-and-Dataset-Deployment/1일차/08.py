# 순서가 있는 범주형 특성 인코딩
import pandas as pd

data = {"Score" : [ "Low", "Low", "Medium", "Medium", "High", 
                    "Berely More Than Medium"]} # 특성데이터 생성

dataframe = pd.DataFrame(data)
print(dataframe)
# 아래와 같이 데이터프레임이 만들어진다.
#     Score
# 0     Low
# 1     Low
# 2  Medium
# 3    High

# 매핑 딕셔너리 생성
scale_mapper = {"Low" : 1, "Medium" : 2, "Berely More Than Medium" : 3,"High" : 4}
dataframe = dataframe["Score"].replace(scale_mapper) # 매핑이 된다.
print(dataframe)