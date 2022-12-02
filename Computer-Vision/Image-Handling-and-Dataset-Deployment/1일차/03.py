# 선형적으로 구분되지 않는 데이터차원 축소
from sklearn.decomposition import KernelPCA
from sklearn.datasets import make_circles

# 선형적으로 구분되지 않는 데이터를 만듭니다.
features, _ = make_circles(n_samples=1000, random_state=1, noise=0.1, factor=0.1)
print(features) 

# 기저함수를 사용해서 커널 pca를 사용한다.
# 방사 기저 함수(radius basis function, RBF)를 사용해서 커널 PCA 적용
kpca = KernelPCA(kernel="rbf", gamma=15, n_components=1)
features_kpca = kpca.fit_transform(features)

print('원본 특성 개수 :', features.shape[1])
print('줄어든 특성 개수 :', features_kpca.shape[1])
# 원본 특성 개수와 줄어든 특성 개수를 출력을 해보았을 때 아래와 같이 된다.
# 원본 특성 개수 : 2
# 줄어든 특성 개수 : 1