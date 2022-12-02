import numpy as np
from sklearn.preprocessing import OrdinalEncoder
features = np.array([["Low", 10],["High", 50],["Medium", 3]])
ordinal_encoding = OrdinalEncoder()
ordinal_encoding.fit_transform(features)
ordinal_encoding_data = ordinal_encoding.categories_

print("ordinal_encoding.categories_", ordinal_encoding_data)
# 출력을 해보았을 때 아래와 같은 값이 나오게 된다.
# ordinal_encoding.categories_ [array(['High', 'Low', 'Medium'], dtype='<U11'), array(['10', '3', '50'], dtype='<U11')]