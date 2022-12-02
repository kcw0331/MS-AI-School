# 딕셔너리 특성 행렬로 변환
from sklearn.feature_extraction import DictVectorizer
import pandas as pd
data_dict = [{"Red" :2 , "Blue" : 4},
              {"Red" : 4, "Blue" : 4},
              {"Red" : 1, "Yellow" : 2},
              {"Red" : 2, "Yellow" : 2}]
# print(data_dict)
# [{'Red': 2, 'Blue': 4, 'Yellow': 2}]

dictvectorizer = DictVectorizer(sparse=False) # 밀집한 벡터로 만들어서 날라간것 같다.
# 0아닌 원소만 저장하는 회소 행렬을 반환

# 딕셔너리를 특성 행렬로 변환
features = dictvectorizer.fit_transform(data_dict)
# features를 출력해주었다.
#   (0, 0)        4.0
#   (0, 1)        2.0
#   (0, 2)        2.0

features_names = dictvectorizer.get_feature_names() # 특성 이름 획득 가능
# print(features_names)
# features의 이름을 출력해주었다.
# ['Blue', 'Red', 'Yellow']

dict_data = pd.DataFrame(features, columns=features_names)
print(dict_data)
# 비어있는 값을 0으로 채워두었다.
#    Blue  Red  Yellow
# 0   4.0  2.0     0.0
# 1   4.0  4.0     0.0
# 2   0.0  1.0     2.0
# 3   0.0  2.0     2.0

## 행렬 형태
# 단어 카운트 딕셔너리 만들기
doc_1_word_count = {"Red" : 2, "Blue" : 4}
doc_2_word_count = {"Red" : 4, "Blue" : 4}
doc_3_word_count = {"Red" : 1, "Yellow" : 2}
doc_4_word_count = {"Red" : 2, "Yellow" : 2}
doc_word_counts = [doc_1_word_count, doc_2_word_count, 
                    doc_3_word_count, doc_4_word_count]
# print(doc_word_counts)

#    Blue  Red  Yellow
# 0   4.0  2.0     0.0
# 1   4.0  4.0     0.0
# 2   0.0  1.0     2.0
# 3   0.0  2.0     2.0
# [{'Red': 2, 'Blue': 4}, {'Red': 4, 'Blue': 4}, {'Red': 1, 'Yellow': 2}, {'Red': 2, 'Yellow': 2}]

data_array = dictvectorizer.fit_transform(doc_word_counts)
print(data_array)

# 행렬로 만들어 지는 것을 볼 수 있다.
# [[4. 2. 0.]
#  [4. 4. 0.]
#  [0. 1. 2.]
#  [0. 2. 2.]]