# 클래스 분리를 최대화함으로써 특성 축소(실습4)
# 사용할 패키지를 선언해준다.
from sklearn import datasets
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

# iris 붓꽃 데이터를 사용해본다.
iris = datasets.load_iris() # 붓꽃 데이터셋을 로드
features = iris.data
target = iris.target
# print(target) # 데이터가 어떻게 생겼는지 확인을 해준다.
# print(features)

# LAD 객체를 만들고 실행하여 특성을 반환합니다.
# lda = LinearDiscriminantAnalysis(n_components=1)
# features_lad = lda.fit(features, target).transform(features) # fit이라고 써서 알아서 학습하도록해준다.

# print('원본 특성 개수 :', features.shape[1])
# print('줄어든 특성 개수 :', features_lad.shape[1])

# 4개의 특성이 1개로 줄어들었다고 볼 수 있다.
# 줄어든거에 대해서는 사람이 알 수 없다고 말씀하심.
# 원본 특성 개수 : 4
# 줄어든 특성 개수 : 1


###########################################################################################
# 클래스 분리를 최대화함으로써 특성 축소

# 설명된 분산의 비율이 담긴 배열을 저장
lda = LinearDiscriminantAnalysis(n_components=None)
features_lad = lda.fit(features, target)

lda_var_ratios = lda.explained_variance_ratio_
print(lda_var_ratios)

def select_n_components(var_ratio, goal_var: float) -> int:
    total_variances = 0.0 # 설명된 분산의 초기값을 지정
    n_components = 0 # 특성 개수의 초기값을 지정

    for explained_variacne in var_ratio: # 각 특성의 설명된 분산을 순회하는 Loop
        total_variances += explained_variacne # 설명된 분산 값을 누적
        n_components += 1 # 성분 개수를 카운트
        if total_variances >= goal_var: # 설명된 분산이 목표치에 도달하면 반복을 종료
            break
    return n_components # 성분 개수를 반환

temp = select_n_components(lda_var_ratios, 0.95)
print("temp = ", temp)

# 출력을 하였을 때, 아래와 같은 결과가 나오게 된다.
# [0.9912126 0.0087874]
# temp =  1