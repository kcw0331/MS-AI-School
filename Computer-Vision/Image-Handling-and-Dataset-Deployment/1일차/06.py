# MultiLabelBinarizer
import numpy as np
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import MultiLabelBinarizer

multiclass_feature = [("Texas", "Florida"),
                        ("California", "Alabama"),
                        ("Texas", "Florida"),
                        ("Delware", "Florida"),
                        ("Texas", "Florida")]
print(multiclass_feature) # 특성 데이터 생성

one_hot_multiclass = MultiLabelBinarizer() # 다중 클래스 원-핫 인코더 객체 생성
one_hot_multiclass.fit_transform(multiclass_feature) # 다중 클래스 특성을 원-핫 인코더 실행

one_hot_multiclass = one_hot_multiclass.classes_
print("one_hot_multiclass >>", one_hot_multiclass)
# 클래스일 때는 중복이 되지만 데이터를 flatten하게되면 중복을 제거하지 않고 일렬로 나열만 해준다.